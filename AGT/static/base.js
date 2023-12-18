// static/js/base.js

$(document).ready(function () {
    // Your custom JavaScript code goes here
// AGT/static/base.js

    // Example: Change the background color of the body
    $('body').css('background-color', '#f0f0f2');

    // Example: Add a click event to a button
    $('#myButton').click(function () {
        alert('Button clicked!');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener for a button that toggles dark mode
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
        });
    }
});


// static/base.js

document.addEventListener("DOMContentLoaded", function () {
    // This function runs when the DOM is ready

    // Example: Change the background color of the body
    document.body.style.backgroundColor = "#f0f0f0";

    // You can add more JavaScript code for your project here
});
