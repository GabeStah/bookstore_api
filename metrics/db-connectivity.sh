#!/bin/bash
EC2_INSTANCE_ID="$(ec2metadata --instance-id)"

while sleep 10
do
    if nc -zv -w 5 db.bookstore.pingpublications.com 5432 2>&1 | grep --line-buffered -i succeeded; then
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name db-connectivity --namespace Bookstore --dimensions Instance=$EC2_INSTANCE_ID --value 1
    else
        echo "Connection to db.bookstore.pingpublications.com 5432 port [tcp/postgresql] failed!"
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name db-connectivity --namespace Bookstore --dimensions Instance=$EC2_INSTANCE_ID --value 0
    fi
done
