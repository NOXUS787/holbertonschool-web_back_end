const fs = require('fs');

function countStudents(path) {
  let content;

  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const lines = content.split('\n').map((line) => line.trim()).filter((line) => line !== '');
  const students = lines.slice(1).map((line) => line.split(','));

  console.log(`Number of students: ${students.length}`);

  const fields = {};
  students.forEach((student) => {
    const firstName = student[0];
    const field = student[3];
    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  });

  Object.keys(fields).forEach((field) => {
    const names = fields[field];
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  });
}

module.exports = countStudents;
