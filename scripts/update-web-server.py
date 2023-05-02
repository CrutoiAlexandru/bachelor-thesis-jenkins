import os
import mysql.connector
from get_docker_images import get_versions


content = None
rds_host = os.environ['RDS_HOST']
rds_user = os.environ['RDS_USER']
rds_password = os.environ['RDS_PASSWORD']
rds_database = 'build_number'
rds_table = 'build_number'

cnx = mysql.connector.connect(user=rds_user, password=rds_password,
                              host=rds_host,
                              database=rds_database)

cursor = cnx.cursor()

repository = 'crutoialexandru/flask-file-hosting'
product_name = 'flaskfilehosting'
versions = get_versions(repository)
tags = {}

for version in versions:

    select_stmt = f"SELECT tag FROM {rds_table} WHERE product = '{product_name}' AND build_number = '{version}'"
    cursor.execute(select_stmt)

    tags[version] = cursor.fetchone()

# header
content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>FlaskFileHosting</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style>
      body {
        background-color: #f0f0f0;
      }
      .jumbotron {
        background-color: #00abe7;
        color: #ffffff;
      }
    </style>
  </head>
  <body>
"""

# body
content += """
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4">FlaskFileHosting</h1>
        <p class="lead">A file sharing Docker image application</p>
      </div>
    </div>

    <div class="container">
      <h2>Download</h2>
      <p>Here are the available versions and tags:</p>
      <table class="table table-hover">
        <thead>
          <tr>
            <th>Version</th>
            <th>Tag</th>
          </tr>
        </thead>
        <tbody>
"""

for version in versions:
    content += f"""
        <tr>
        <td>{version}</td>
        <td><a href="#">latest</a></td>
        </tr>
    <tr>
        <td>{version}</td>
        <td>{tags[version]}</td>
    </tr>
    """

content += """
        </tbody>
      </table>
    </div>
"""

# end
content += """
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
"""


with open('/server/index.html', 'w') as f:
    f.write(content)

cnx.commit()
cursor.close()
cnx.close()
