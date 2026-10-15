import { readDatabase } from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    return readDatabase(process.argv[2])
      .then((fields) => {
        const lines = ['This is the list of our students'];

        Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
          .forEach((field) => {
            const names = fields[field];
            lines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
          });

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major parameter must be CS or SWE');
    }

    return readDatabase(process.argv[2])
      .then((fields) => {
        const names = fields[major] || [];
        response.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}
