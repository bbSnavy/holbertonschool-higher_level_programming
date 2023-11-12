$(document).ready(() => {
	$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
		for (const movie of data.results) {
			$('ul#list_movies').append(`<li>${movie.title}</li>`);
		}
	});
});

