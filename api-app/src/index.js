const express = require('express');
const app = express();
const port = 4000;

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

app.listen(port, () => {
  console.log(`API App running on http://localhost:${port}`);
});
