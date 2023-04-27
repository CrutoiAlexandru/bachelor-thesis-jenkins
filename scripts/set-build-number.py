import sys
import os
import boto3
import mysql.connector

product_name = sys.argv[1].toLower()
build_number = sys.argv[2]

rds = boto3.client('rds')
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

select_stmt = f"SELECT * FROM {rds_table} WHERE product = {product_name} AND build_number = {build_number}"
if (cursor.execute(select_stmt) > 0):
    print("Build number already exists")
    sys.exit(0)

insert_stmt = f"INSERT INTO {rds_table} (product, build_number) VALUES ({product_name}, {build_number})"
cursor.execute(insert_stmt, insert_stmt)

cnx.commit()
cursor.close()
cnx.close()

print("Build number set")
