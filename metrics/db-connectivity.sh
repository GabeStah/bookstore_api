#!/bin/bash
INSTANCE_ID="$(ec2metadata --instance-id)"
TAG_NAME="$(aws ec2 describe-tags --filter "Name=resource-id,Values=$INSTANCE_ID" "Name=key,Values=Name" --query "Tags[*].Value" --output text)"

while sleep 10
do
    if nc -zv -w 5 db.bookstore.pingpublications.com 5432 2>&1 | grep --line-buffered -i succeeded; then
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name db-connectivity --namespace Bookstore --dimensions Host=$TAG_NAME --value 1
    else
        echo "Connection to db.bookstore.pingpublications.com 5432 port [tcp/postgresql] failed!"
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name db-connectivity --namespace Bookstore --dimensions Host=$TAG_NAME --value 0
    fi
done
