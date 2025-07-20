document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const movieList = document.getElementById('list_movies');
        data.results.forEach(film => {
          const listItem = document.createElement('li');
          listItem.textContent = film.title;
          movieList.appendChild(listItem);
        });
      })
      .catch(error => console.error('Error fetching movies:', error));
  }); 
