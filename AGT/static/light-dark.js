// light-dark.js

// Check for saved theme preference in localStorage
const savedTheme = localStorage.getItem('theme');

// Apply the saved theme or default to 'light' if none is saved
document.body.classList.toggle('dark', savedTheme === 'dark');

// Function to toggle between light and dark mode
function toggleTheme() {
    const currentTheme = document.body.classList.contains('dark') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    // Toggle the class on the body to switch the theme
    document.body.classList.toggle('dark', newTheme === 'dark');

    // Save the theme preference to localStorage
    localStorage.setItem('theme', newTheme);
}

// Event listener for the light/dark mode button
document.getElementById('light-dark').addEventListener('click', toggleTheme);
