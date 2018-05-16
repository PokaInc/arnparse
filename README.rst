arnparse
========

Parse ARNs using Python

.. image:: https://travis-ci.org/PokaInc/arnparse.svg?branch=master
   :target: https://travis-ci.org/PokaInc/arnparse

Motivation
----------

Sometimes, you want to parse an Amazon Resource Name (ARN) into its
components to get some useful information from the ARN (e.g. AWS region,
account ID, etc).

You can find documentation on ARNs and their components here:
https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html

Installation
------------

``pip install arnparse``

Examples
--------

S3 Object
^^^^^^^^^

.. code:: python

   from arnparse import parse

   arn = parse('arn:aws:s3:::my_corporate_bucket/exampleobject.png')

   assert arn.partition == 'aws'
   assert arn.service == 's3'
   assert arn.region is None
   assert arn.account_id is None
   assert arn.resource_type is None
   assert arn.resource == 'my_corporate_bucket/exampleobject.png'

VPC
^^^

.. code:: python

   from arnparse import parse

   arn = parse('arn:aws:ec2:us-east-1:123456789012:vpc/vpc-fd580e98')

   assert arn.partition == 'aws'
   assert arn.service == 'ec2'
   assert arn.region == 'us-east-1'
   assert arn.account_id == '123456789012'
   assert arn.resource_type == 'vpc'
   assert arn.resource == 'vpc-fd580e98'

CloudWatch Alarm
^^^^^^^^^^^^^^^^

.. code:: python

   from arnparse import parse

   arn = parse('arn:aws:cloudwatch:us-east-1:123456789012:alarm:MyAlarmName')

   assert arn.partition == 'aws'
   assert arn.service == 'cloudwatch'
   assert arn.region == 'us-east-1'
   assert arn.account_id == '123456789012'
   assert arn.resource_type == 'alarm'
   assert arn.resource == 'MyAlarmName'

SNS Topic
^^^^^^^^^

.. code:: python

   from arnparse import parse

   arn = parse('arn:aws:sns:*:123456789012:my_corporate_topic')

   assert arn.partition == 'aws'
   assert arn.service == 'sns'
   assert arn.region == '*'
   assert arn.account_id == '123456789012'
   assert arn.resource_type is None
   assert arn.resource == 'my_corporate_topic'

API Gateway
^^^^^^^^^^^

.. code:: python

   from arnparse import parse

   arn = parse('arn:aws:apigateway:us-east-1::a123456789012bc3de45678901f23a45:/test/mydemoresource/*')

   assert arn.partition == 'aws'
   assert arn.service == 'apigateway'
   assert arn.region == 'us-east-1'
   assert arn.account_id is None
   assert arn.resource_type is None
   assert arn.resource == 'a123456789012bc3de45678901f23a45:/test/mydemoresource/*'

.. _Build Status: https://travis-ci.org/PokaInc/cfn-get-export-value

Developer notes
---------------

- I used reStructuredText for README (instead of Markdown) in order to relax requirements on the minimal version of `setuptools`. If you have `setuptools` < 38.6.0, Markdown does not display correctly on PyPI. See https://stackoverflow.com/a/26737258
