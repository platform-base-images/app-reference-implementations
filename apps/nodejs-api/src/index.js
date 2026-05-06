'use strict';

const express = require('express');

const app  = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: 'nodejs-api' });
});

app.get('/api/items', (_req, res) => {
  res.json([
    { id: 1, name: 'item-1', description: 'First item' },
    { id: 2, name: 'item-2', description: 'Second item' },
  ]);
});

app.get('/api/items/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  if (id < 1 || id > 2) {
    return res.status(404).json({ error: 'Item not found' });
  }
  res.json({ id, name: `item-${id}`, description: `Item ${id}` });
});

app.listen(PORT, () => {
  console.log(`nodejs-api listening on port ${PORT}`);
});
