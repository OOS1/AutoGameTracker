// AGT/static/home.js

// Wait for the DOM to be ready
document.addEventListener("DOMContentLoaded", function () {
    // Select elements from the DOM
    const playerCard = document.querySelector(".player-card");
    const toggleButton = document.querySelector("#toggle-info");
  
    // Add event listener to toggle button
    toggleButton.addEventListener("click", function () {
      // Toggle the visibility of additional player info
      const additionalInfo = document.querySelector(".additional-info");
      additionalInfo.classList.toggle("hidden");
    });
  
    // Add event listener to player card for hover effect
    playerCard.addEventListener("mouseenter", function () {
      // Add a CSS class on hover
      playerCard.classList.add("hovered");
    });
  
    // Remove the CSS class when the mouse leaves
    playerCard.addEventListener("mouseleave", function () {
      playerCard.classList.remove("hovered");
    });
  });