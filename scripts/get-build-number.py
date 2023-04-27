import sys
import os
import boto3
import mysql.connector
import logging
logging.basicConfig(level=logging.INFO)

product_name = sys.argv[1].lower()

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

select_stmt = f"SELECT * FROM {rds_table} WHERE product = '{product_name}' ORDER BY build_number DESC"
cursor.execute(select_stmt)

response = cursor.fetchall()
logging.info(response)

cnx.commit()
cursor.close()
cnx.close()
