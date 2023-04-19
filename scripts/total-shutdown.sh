#!/bin/bash

# Get the instance IDs and names
instance_info=$(aws ec2 describe-instances --region eu-central-1 --query 'Reservations[].Instances[].[InstanceId, Tags[?Key==`Name`].Value|[0]]' --output text)

# Loop through each instance ID and stop the instance
while read instance_id instance_name; do
    echo "Stopping instance $instance_name ($instance_id)..."
    aws ec2 stop-instances --instance-ids $instance_id
done <<<"$instance_info"
