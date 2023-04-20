#!/bin/bash
set -e

# Set the instance name
INSTANCE_NAME=$1
# Set the new public key
KEY=$2

# Write key to file in current directory
echo "$KEY" >ubuntu.pub
chmod 777 ubuntu.pub

# Get the instance ID
INSTANCE_ID=$(aws ec2 describe-instances --region eu-central-1 --filters "Name=tag:Name,Values=$INSTANCE_NAME" --query "Reservations[].Instances[].InstanceId" --output text)

# Check if instance ID is empty
if [ -z "$INSTANCE_ID" ]; then
    echo "Error: No instance found with name $INSTANCE_NAME"
    exit 1
fi

# Get current directory
DIR="$(pwd)"

aws ec2-instance-connect send-ssh-public-key \
    --region eu-central-1 \
    --instance-id $INSTANCE_ID \
    --instance-os-user ubuntu \
    --ssh-public-key file://./ubuntu.pub

# Set the new authorized_keys file
ssh -i "/home/ubuntu/.ssh/ubuntu" -o "StrictHostKeyChecking=no" ubuntu@"$(aws ec2 describe-instances --region eu-central-1 --instance-ids "$INSTANCE_ID" --query "Reservations[].Instances[].PrivateIpAddress" --output text)" "echo $KEY > ~/.ssh/authorized_keys"

rm ubuntu.pub

# Print success message
echo "New authorized_keys file has been set for instance $INSTANCE_NAME ($INSTANCE_ID)."
