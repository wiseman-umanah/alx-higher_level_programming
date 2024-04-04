const link = 'https://swapi.co/api/people/5/?format=json'
$.get(link, function (data) {
  $('#character').text(data.name);
});
