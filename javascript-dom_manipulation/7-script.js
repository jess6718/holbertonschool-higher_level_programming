// Use the Fetch API to get data
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Convert the response to JSON
    return response.json();
  })
  .then(data => {
    // Get the element with id
    let moviesListElement = document.getElementById('list_movies');

    // Loop through the movies in the fetched data and append
    data.results.forEach(movie => {
      let listItem = document.createElement('li');
      listItem.textContent = movie.title;
      moviesListElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });