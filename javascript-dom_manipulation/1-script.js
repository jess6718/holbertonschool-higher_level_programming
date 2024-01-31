// Select the element with id
let redHeader = document.getElementById('red_header');

// Add an event listener
redHeader.addEventListener('click', function() {
    // Select the header element and change its color
    document.querySelector('header').style.color = '#FF0000';
});
