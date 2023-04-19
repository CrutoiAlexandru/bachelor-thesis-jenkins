#!/bin/bash

# Get the instance IDs
instance_ids=$(aws ec2 describe-instances --region eu-central-1 --query 'Reservations[].Instances[].InstanceId' --output text)

# Stop the instances
aws ec2 stop-instances --region eu-central-1 --instance-ids $instance_ids
