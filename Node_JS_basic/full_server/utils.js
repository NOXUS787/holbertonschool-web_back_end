import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, content) => {
      if (error) {
        reject(error);
        return;
      }

      const lines = content.split('\n').map((line) => line.trim()).filter((line) => line !== '');
      const fields = {};

      lines.slice(1).forEach((line) => {
        const columns = line.split(',');
        const firstName = columns[0];
        const field = columns[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      resolve(fields);
    });
  });
}

export default readDatabase;
