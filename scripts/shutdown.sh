#!/bin/bash

# Get the instance name
INSTANCE_NAME=$1

# Get the instance ID
INSTANCE_ID=$(aws ec2 describe-instances --region eu-central-1 --filters "Name=tag:Name,Values=$INSTANCE_NAME" --query "Reservations[].Instances[].InstanceId" --output text)

# Check if instance ID is empty
if [ -z "$INSTANCE_ID" ]; then
    echo "Error: No instance found with name $INSTANCE_NAME"
    exit 1
fi

# Stop the instance
aws ec2 stop-instances --region eu-central-1 --instance-ids "$INSTANCE_ID"

# Print success message
echo "Instance $INSTANCE_NAME ($INSTANCE_ID) is stopping."
