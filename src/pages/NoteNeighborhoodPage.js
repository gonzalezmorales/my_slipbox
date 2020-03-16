import React from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";

const noteContent = require("../data/nodes.json");

const NoteNeighborhoodPage = ({ match }) => {
  const note_id = match.params.note_id;
  const note = noteContent.find(note => note.id === note_id);

  if (!note) return <h1>Note does not exist.</h1>;
  return (
    <>
      <h1>{note.name}</h1>
      <ReactMarkdown source={note.text_md} />
      <h2>Related notes:</h2>

      {note.links.map((link, key) => {
        const related_note = noteContent.find(note => note.id === link);

        return (
          <>
            <hr />
            <h3>
              <Link
                className="article-list-item"
                key={key}
                to={`/note/${link}`}
              >
                {related_note.name}
              </Link>
            </h3>
            <ReactMarkdown source={related_note.text_md} />
          </>
        );
      })}
    </>
  );
};

export default NoteNeighborhoodPage;
