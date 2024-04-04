const link = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(link, function (data) {
	(data.results).forEach(element => {
		$('UL#list_movies').append(`<li>${element.title}</li>`);
	});
});
