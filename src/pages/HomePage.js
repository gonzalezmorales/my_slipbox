import React from "react";

const HomePage = () => (
  <>
    <h1>Hello! Welcome to my Slip Box</h1>
    <div className="full-width">
      <img
        src={require("../assets/kolar-io-lRoX0shwjUQ-unsplash_med.jpg")}
        alt=""
        width="100%"
      />
      <p>
        <a
          href="https://unsplash.com/photos/lRoX0shwjUQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Image from Unsplash
        </a>
      </p>
    </div>
  </>
);

export default HomePage;
