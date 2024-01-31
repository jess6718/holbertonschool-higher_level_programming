// Get the element with id "update_header"
let updateHeader = document.getElementById('update_header');

// Add an event listener
updateHeader.addEventListener('click', function() {

    // Get the header element
    let headerElement = document.querySelector('header');

    // Update the text content
    headerElement.textContent = 'New Header!!!';
});