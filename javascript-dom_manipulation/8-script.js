// Listen for the "DOMContentLoaded" event
document.addEventListener('DOMContentLoaded', function() {
  // Use the Fetch API to get data
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      // Convert the response to JSON
      return response.json();
    })
    .then(data => {
      // Get the element
      let helloElement = document.getElementById('hello');

      // Set the content of the div
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});