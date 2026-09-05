const express = require('express');
const app = express();
const port = 80;

// Endpoint de verificación de estado
app.get('/check', (req, res) => {
  res.status(200).send('OK');
});

// Endpoint de información
app.get('/info', (req, res) => {
  res.json({
    "Instancia": "Instancia-1 - API Javascript",
    "Curso": "Seminario de Sistemas 1 A",
    "Grupo": "Grupo 11"
  });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`API Node.js corriendo en el puerto ${port}`);
});
