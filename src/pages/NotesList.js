import React from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";

const noteContent = require("../data/nodes.json");

const NotesList = () => (
  <>
    <h1>Notes</h1>
    {noteContent.map((note, key) => (
      <>
        <Link className="article-list-item" key={key} to={`/note/${note.id}`}>
          <h3>{note.name}</h3>
        </Link>
        <ReactMarkdown source={note.text_md} />

        <hr />
      </>
    ))}
  </>
);

export default NotesList;
