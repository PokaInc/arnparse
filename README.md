arnparse
========

Parse ARNs using Python

[![Build Status](https://travis-ci.org/PokaInc/arnparse.svg?branch=master)](https://travis-ci.org/PokaInc/arnparse)

Motivation
----------

Sometimes, you want to parse an Amazon Resource Name (ARN) into its
components to get some useful information from the ARN (e.g. AWS region,
account ID, etc).

You can find documentation on ARNs and their components here:
https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html

Installation
------------

`pip install arnparse`

Examples
--------

### S3 Object

```python
from arnparse import arnparse

arn = arnparse('arn:aws:s3:::my_corporate_bucket/exampleobject.png')

assert arn.partition == 'aws'
assert arn.service == 's3'
assert arn.region is None
assert arn.account_id is None
assert arn.resource_type is None
assert arn.resource == 'my_corporate_bucket/exampleobject.png'
```

### VPC

```python
from arnparse import arnparse

arn = arnparse('arn:aws:ec2:us-east-1:123456789012:vpc/vpc-fd580e98')

assert arn.partition == 'aws'
assert arn.service == 'ec2'
assert arn.region == 'us-east-1'
assert arn.account_id == '123456789012'
assert arn.resource_type == 'vpc'
assert arn.resource == 'vpc-fd580e98'
```

### CloudWatch Alarm

```python
from arnparse import arnparse

arn = arnparse('arn:aws:cloudwatch:us-east-1:123456789012:alarm:MyAlarmName')

assert arn.partition == 'aws'
assert arn.service == 'cloudwatch'
assert arn.region == 'us-east-1'
assert arn.account_id == '123456789012'
assert arn.resource_type == 'alarm'
assert arn.resource == 'MyAlarmName'
```

### SNS Topic

```python
from arnparse import arnparse

arn = arnparse('arn:aws:sns:*:123456789012:my_corporate_topic')

assert arn.partition == 'aws'
assert arn.service == 'sns'
assert arn.region == '*'
assert arn.account_id == '123456789012'
assert arn.resource_type is None
assert arn.resource == 'my_corporate_topic'
```

### API Gateway

```python
from arnparse import arnparse

arn = arnparse('arn:aws:apigateway:us-east-1::a123456789012bc3de45678901f23a45:/test/mydemoresource/*')

assert arn.partition == 'aws'
assert arn.service == 'apigateway'
assert arn.region == 'us-east-1'
assert arn.account_id is None
assert arn.resource_type is None
assert arn.resource == 'a123456789012bc3de45678901f23a45:/test/mydemoresource/*'
```
