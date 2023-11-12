document.querySelector('#add_item')
	.addEventListener('click', () => {
		let list = document.querySelector('.my_list');
		let item = document.createelement('li');

		item.textContent = 'Item';
		list.appendChild(item);
	});

