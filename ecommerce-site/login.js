document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Login failed');
        }
        return response.json();
    })
    .then(data => {
        localStorage.setItem('token', data.token);
        // Redirect or perform actions after successful login
        alert('Login successful');
        window.location.replace('/'); // Redirect to homepage or desired page
    })
    .catch(error => {
        console.error('Login failed:', error);
        alert('Login failed');
    });
});
