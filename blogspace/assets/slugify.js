const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = val => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-') //repalce &
    .replace(/[\s\W-]+/g, '-') // replace space and special char with dash
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});
