import os
from flask import Flask, request

# Create a new Flask application instance
app = Flask(__name__)

# Define the GET route for the application
@app.route('/', defaults={'filename': 'file1.txt'})
@app.route('/<filename>')
def read_file(filename):
    # Set the default encoding to UTF-8 to support Chinese characters
    encoding = 'utf-8'

    # Get the absolute path of the file
    file_path = os.path.abspath(os.path.join('files', filename))

    # Check if the file exists
    if not os.path.isfile(file_path):
        # If the file doesn't exist, return a 404 error
        return "File not found", 404

    # Get the start and end line numbers from the query parameters
    start_line = int(request.args.get('start', 1))
    end_line = int(request.args.get('end', -1))

    # Open the file and read its contents
    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()

    # Check if the start and end line numbers are valid
    if start_line < 1 or end_line < 1 or start_line > end_line:
        # If the line numbers are invalid, return a 400 error
        return "Invalid start or end line number", 400

    # Get the lines between the start and end line numbers
    lines = lines[start_line-1:end_line]

    # Return the lines as a response
    return ''.join(lines), 200

# Run the Flask application
if __name__ == '__main__':
    # Set the debug mode to True to enable debugging
    app.run(debug=True)