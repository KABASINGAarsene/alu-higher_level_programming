// jQuery to handle click on #add_item and append a new <li> element to the list
$('#add_item').click(function() {
  $('ul.my_list').append('<li>Item</li>');
});
