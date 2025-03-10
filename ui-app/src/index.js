const express = require('express');
const app = express();
const axios = require('axios');
const port = 3000;

// Middleware to parse JSON
app.use(express.json());

// Serve a simple HTML form
app.get('/', (req, res) => {
    res.send(`
        <h1>User Registration</h1>
        <form action="/register" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="subdomain">Subdomain:</label>
            <input type="text" id="subdomain" name="subdomain" required><br><br>
            <button type="submit">Register</button>
        </form>
    `);
});

// Handle form submission
app.post('/register', async (req, res) => {
    const { username, subdomain } = req.body;

    try {
        // Call the API Gateway to register the user
        const response = await axios.post('http://api-gateway:8000/register-user', {
            username,
            subdomain,
            schema_name: subdomain.replace('.', '_')
        });

        res.send(`<h1>Registration Successful!</h1><p>${response.data.message}</p>`);
    } catch (error) {
        res.status(500).send(`<h1>Registration Failed</h1><p>${error.response.data.detail}</p>`);
    }
});

app.listen(port, () => {
    console.log(`UI App running on http://localhost:${port}`);
});
