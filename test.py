const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    if (!email || !message) {
        alert('Please fill in all fields.');
        event.preventDefault();
    }
});