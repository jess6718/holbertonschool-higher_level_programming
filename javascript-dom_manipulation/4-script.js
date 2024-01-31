// Get the element with id
let addItem = document.getElementById('add_item');

// Add an event listener
addItem.addEventListener('click', function() {

    // Create a new list
    let newListItem = document.createElement('li');
    newListItem.textContent = 'Item';

    // Get the list with class
    let myList = document.querySelector('.my_list');

    // Append the new list item
    myList.appendChild(newListItem);
});