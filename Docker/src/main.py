import sys
from flask import Flask, render_template, send_file, abort
import os

app = Flask(__name__)

# define the root directory for browsing
root_dir = os.getcwd() + "/host"
title = sys.argv[1]


@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    if req_path != '':
        title = req_path.split('/')[-1]
    else:
        title = sys.argv[1]

    # Joining the base and the requested path
    abs_path = os.path.join(root_dir, req_path)
    description_path = os.path.join(abs_path, ".description")

    if os.path.exists(description_path):
        with open(description_path, "r") as f:
            description = f.read()
    else:
        description = ""

        # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path, as_attachment=True)

    # Show directory contents
    files = os.listdir(abs_path)

    final_files = []
    final_directories = []

    for file in files:
        current_dir = os.path.join(abs_path, file)

        if file.startswith("."):
            continue

        if os.path.isfile(current_dir):
            final_files.append(file)
        else:
            final_directories.append(file)

    return render_template('index.html', files=final_files, directories=final_directories, title=title, description=description)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
