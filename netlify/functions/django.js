const { spawn } = require('child_process');
const path = require('path');

exports.handler = async (event, context) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python', [
      path.join(process.cwd(), 'manage.py'),
      'runserver',
      '0.0.0.0:8000'
    ]);

    let responseData = '';

    pythonProcess.stdout.on('data', (data) => {
      responseData += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`Process exited with code ${code}`));
      } else {
        resolve({
          statusCode: 200,
          body: responseData
        });
      }
    });
  });
}; 