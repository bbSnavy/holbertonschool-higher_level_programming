document.querySelector('#update_header')
	.addEventListener('click', () => {
		let header = document.querySelector('header');

		header.textContent = 'New Header!!!';
	});

