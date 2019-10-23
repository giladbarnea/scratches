const Hamburger = document.getElementById('menu');
Hamburger.addEventListener('click', (event) => {
	console.log('menu.click');
	Hamburger.classList.toggle('open');

});

