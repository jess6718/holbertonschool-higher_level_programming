// Get the element with id
let toggleHeader= document.getElementById('toggle_header');

// Add an event listener
toggleHeader.addEventListener('click', function() {
    let headerElement = document.querySelector('header');

    // Check the current class and toggle
    if (headerElement.classList.contains('green')) {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    } else {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    }
});