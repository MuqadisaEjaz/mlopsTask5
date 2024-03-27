document.getElementById('submitForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value
    };

    const response = await fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    });

    const result = await response.text();
    console.log(result);
});
