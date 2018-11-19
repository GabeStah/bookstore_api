#!/bin/bash
INSTANCE_ID="$(ec2metadata --instance-id)"
TAG_NAME="$(aws ec2 describe-tags --filter "Name=resource-id,Values=$EC2_INSTANCE_ID" "Name=key,Values=Name" --query "Tags[*].Value" --output text)"

while sleep 10
do
    if nc -zv -w 5 cdn.bookstore.pingpublications.com 80 2>&1 | grep --line-buffered -i succeeded; then
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name cdn-connectivity --namespace Bookstore --dimensions Host=$TAG_NAME --value 1
    else
        echo "Connection to cdn.bookstore.pingpublications.com 80 port [tcp/http] failed!"
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name cdn-connectivity --namespace Bookstore --dimensions Host=$TAG_NAME --value 0
    fi
done
