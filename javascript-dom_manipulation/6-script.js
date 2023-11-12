let url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
	.then((response) => {
		if (response.status !== 200) {
			throw new Error('Unable to fetch character data');
		}

		return response.json();
	})
	.then((data) => {
		let element = document.querySelector('#character');

		element.textContent = data.name;
	})
	.catch((err) => {
		console.error('Error:', err);
	});

