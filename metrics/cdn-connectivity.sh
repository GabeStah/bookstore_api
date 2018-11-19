#!/bin/bash
EC2_INSTANCE_ID="$(ec2metadata --instance-id)"

while sleep 10
do
    if nc -zv -w 5 cdn.bookstore.pingpublications.com 80 2>&1 | grep --line-buffered -i succeeded; then
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name cdn-connectivity --namespace Bookstore --dimensions Instance=$EC2_INSTANCE_ID --value 1
    else
        echo "Connection to cdn.bookstore.pingpublications.com 80 port [tcp/http] failed!"
        /home/ubuntu/.local/bin/aws cloudwatch put-metric-data --metric-name cdn-connectivity --namespace Bookstore --dimensions Instance=$EC2_INSTANCE_ID --value 0
    fi
done
