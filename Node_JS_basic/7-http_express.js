const express = require('express');
const fs = require('fs');

const app = express();
const databasePath = process.argv[2];

function getStudentsReport(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(path, 'utf8', (error, content) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = content.split('\n').map((line) => line.trim()).filter((line) => line !== '');
      const students = lines.slice(1).map((line) => line.split(','));

      const fields = {};
      students.forEach((student) => {
        const firstName = student[0];
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      const report = [`Number of students: ${students.length}`];
      Object.keys(fields).forEach((field) => {
        const names = fields[field];
        report.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      });

      resolve(report.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  getStudentsReport(databasePath)
    .then((report) => {
      res.send(`This is the list of our students\n${report}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
