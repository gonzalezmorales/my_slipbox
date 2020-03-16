import React from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";

const noteContent = require("../data/nodes.json");

const NotePage = ({ match }) => {
  const note_id = match.params.note_id;
  const note = noteContent.find(note => note.id === note_id);

  if (!note) return <h1>Note does not exist.</h1>;
  return (
    <>
      <h1>{note.name}</h1>
      <ReactMarkdown source={note.text_md} />
      <h5>Related notes:</h5>

      <ul>
        {note.links.map((link, key) => {
          const related_note = noteContent.find(note => note.id === link);

          return (
            <li>
              <Link key={key} to={`/note/${link}`}>
                {related_note.name}
              </Link>
            </li>
          );
        })}
      </ul>
    </>
  );
};

export default NotePage;
