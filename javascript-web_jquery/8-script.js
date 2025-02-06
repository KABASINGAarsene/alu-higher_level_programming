// jQuery to fetch movie data and list all titles in the #list_movies element
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  // Loop through the movies and append each title to the list
  data.results.forEach(function(movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
