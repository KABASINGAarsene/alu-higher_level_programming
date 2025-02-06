// jQuery to fetch data from the API and display the character name
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  // Display the character's name in the #character div
  $('#character').text(data.name);
});
