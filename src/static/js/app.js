// Loader
const loader = document.getElementById('loader');
const loaderAfter = document.querySelector('.loader-after');
window.addEventListener('DOMContentLoaded', () => {
	loader.style.animation = 'loaderFinished .3s';
	loaderAfter.style.opacity = '1';
	loader.addEventListener('animationend', () => loader.parentElement.remove());
});

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
	document.documentElement.classList.toggle('dark-theme');
	if (document.documentElement.classList.contains('dark-theme')) {
		localStorage.setItem('theme', 'dark');
	} else {
		localStorage.setItem('theme', 'light');
	}
});

// // Making the articles the same height
// const articles = document.querySelectorAll('#articlesView .article-card');
// let bigHeight = 0;
// articles.forEach((article) => (article.offsetHeight > bigHeight ? (bigHeight = article.offsetHeight) : null));
// articles.forEach((article) => (article.style.height = bigHeight + 'px'));

// Adding the relative position to article author
const articleAuthors = document.querySelectorAll('#articlesView .article-card .article-author');
articleAuthors.forEach((article) => (article.style.position = 'absolute'));

// Search Ahowing
const searchButton = document.getElementById('searchButton');
const searchParent = document.querySelector('.search-bg');
const closeButton = document.getElementById('closeButton');

searchButton.addEventListener('click', (e) => {
	e.preventDefault();
	searchParent.classList.add('open');
});
closeButton.addEventListener('click', (e) => {
	e.preventDefault();
	searchParent.classList.remove('open');
});
