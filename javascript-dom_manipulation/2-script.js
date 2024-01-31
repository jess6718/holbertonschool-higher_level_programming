// Select the element with id
let redHeader = document.getElementById('red_header');

// Add an event listener
redHeader.addEventListener('click', function() {
    // Select the header element and add the class
    document.querySelector('header').classList.add('red');
});