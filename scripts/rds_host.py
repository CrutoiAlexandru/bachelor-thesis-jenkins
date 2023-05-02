import boto3


rds = boto3.client('rds', region_name='eu-central-1')
response = rds.describe_db_instances(DBInstanceIdentifier='build-number')
print(response['DBInstances'][0]['Endpoint']['Address'])
