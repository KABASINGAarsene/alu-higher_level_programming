// jQuery to fetch the translation of "hello" and display it in the #hello div
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
  // Display the translated hello in the #hello div
  $('#hello').text(data.hello);
});
