let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

document.addEventListener('DOMContentLoaded', () => {
	fetch(url)
		.then((response) => {
			if (response.status !== 200) {
				throw new Error('Unable to fetch translation');
			}

			return response.json();
		})
		.then((data) => {
			let element = document.querySelector('#hello');

			element.textContent = data.hello;
		})
		.catch((err) => {
			console.error('Error:', err);
		});
});

