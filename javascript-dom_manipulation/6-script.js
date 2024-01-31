// Use the Fetch API to get data
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Convert the response to JSON
    return response.json();
  })
  .then(data => {
    // Get the element with id
    let characterElement = document.getElementById('character');

    // Update the text content
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });