// Runing the menu
const navbarToggler = document.querySelector('#navbar .toggler');
const navbarMenu = document.querySelector('#navbar .nav');
navbarToggler.addEventListener('click', () => {
	navbarMenu.classList.toggle('open');
});

// Changing the theme
const sunButton = document.getElementById('themeSun');
sunButton.addEventListener('click', (e) => {
	e.preventDefault();
	console.log(document.documentElement.style);
});
