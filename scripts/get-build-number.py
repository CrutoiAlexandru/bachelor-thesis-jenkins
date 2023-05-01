import sys
import os
import boto3
import mysql.connector

product_name = sys.argv[1].lower()
increment = sys.argv[2].lower()

rds = boto3.client('rds', region_name='eu-central-1')
response = rds.describe_db_instances(DBInstanceIdentifier='build-number')

rds_host = response['DBInstances'][0]['Endpoint']['Address']
rds_user = os.environ['RDS_USER']
rds_password = os.environ['RDS_PASSWORD']
rds_database = 'build_number'
rds_table = 'build_number'

cnx = mysql.connector.connect(user=rds_user, password=rds_password,
                              host=rds_host,
                              database=rds_database)

cursor = cnx.cursor()

select_stmt = f"SELECT * FROM {rds_table} WHERE product = '{product_name}' ORDER BY CAST(SUBSTRING_INDEX(build_number, '.', 1) AS UNSIGNED), CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(build_number, '.', 2), '.', -1) AS UNSIGNED), CAST(SUBSTRING_INDEX(build_number, '.', -1) AS UNSIGNED)"
cursor.execute(select_stmt)

response = cursor.fetchall()
if (len(response) <= 0):
    sys.exit(1)

build_number = response[0][1]

if (increment == 'true'):
    build_number = build_number.split('.')
    build_number[-1] = str(int(build_number[-1]) + 1)
    build_number = '.'.join(build_number)

    insert_stmt = f"INSERT INTO {rds_table} (product, build_number) VALUES ('{product_name}', '{build_number}')"
    cursor.execute(insert_stmt)

    select_stmt = f"SELECT * FROM {rds_table} WHERE product = '{product_name}' ORDER BY build_number DESC LIMIT 1"
    cursor.execute(select_stmt)
    response = cursor.fetchall()
    build_number = response[0][1]


print(build_number)

cnx.commit()
cursor.close()
cnx.close()
