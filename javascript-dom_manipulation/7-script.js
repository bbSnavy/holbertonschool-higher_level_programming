let url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
	.then((response) => {
		if (response.status !== 200) {
			throw new Error('Unable to fetch movie data');
		}

		return response.json();
	})
	.then((data) => {
		let element = document.querySelector('#list_movies');
		let movies = data.results;

		movies.forEach((movie) => {
			let item = document.createElement('li');

			item.textContent = movie.title;

			element.appendChild(item);
		});
	})
	.catch((err) => {
		console.error('Error:', err);
	});

