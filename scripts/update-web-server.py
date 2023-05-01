import sys
import os
import boto3
import mysql.connector
from scripts.get_docker_images import get_versions

rds = boto3.client('rds', region_name='eu-central-1')
response = rds.describe_db_instances(DBInstanceIdentifier='build-number')
content = None

rds_host = response['DBInstances'][0]['Endpoint']['Address']
rds_user = os.environ['RDS_USER']
rds_password = os.environ['RDS_PASSWORD']
rds_database = 'build_number'
rds_table = 'build_number'

cnx = mysql.connector.connect(user=rds_user, password=rds_password,
                              host=rds_host,
                              database=rds_database)

cursor = cnx.cursor()

repository = 'crutoialexandru/flask-file-hosting'
versions = get_versions(repository)

for version in versions:

    select_stmt = f"SELECT * FROM {rds_table} WHERE product = '{product_name}' ORDER BY build_number DESC LIMIT 1"
    cursor.execute(select_stmt)

    response = cursor.fetchone()

content = f"""
<table>
<tr>
    <th>Version</th>
    <th>Tag</th>
</tr>
"""

for version in versions:
    content += f"""
    <tr>
        <td>{version}</td>
        <td>{versions[version]}</td>
    </tr>
    """

content += "</table>"

with open('/server/index.html') as f:
    f.write(content)

cnx.commit()
cursor.close()
cnx.close()
