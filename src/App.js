import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import NotesList from "./pages/NotesList";
import NotePage from "./pages/NotePage";
import NoteNeighborhoodPage from "./pages/NoteNeighborhoodPage";
import GraphPage from "./pages/GraphPage";
import NavBar from "./NavBar";
import "./App.css";

function App() {
  return (
    <Router basename={`/my_slipbox`}>
      <div className="App">
        <NavBar />
        <div id="page-body">
          <Route path={`/`} component={HomePage} exact />
          <Route path={`/about`} component={AboutPage} />
          <Route path={`/notes-list`} component={NotesList} />
          <Route path={`/graph`} component={GraphPage} />
          <Route path={`/note/:note_id`} component={NotePage} />
          <Route path={`/note-group/:note_id`} component={NoteNeighborhoodPage} />
        </div>
      </div>
    </Router>
  );
}

export default App;
