import pytest

from arnparse import arnparse
from arnparse.arnparse import MalformedArnError


def test__definition():
    arn = arnparse('arn:partition:service:region:account-id:resource')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type is None
    assert arn.resource == 'resource'

    arn = arnparse('arn:partition:service:region:account-id:resourcetype/resource')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type == 'resourcetype'
    assert arn.resource == 'resource'

    arn = arnparse('arn:partition:service:region:account-id:resourcetype/resource/qualifier')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type == 'resourcetype'
    assert arn.resource == 'resource/qualifier'

    arn = arnparse('arn:partition:service:region:account-id:resourcetype/resource:qualifier')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type == 'resourcetype'
    assert arn.resource == 'resource:qualifier'

    arn = arnparse('arn:partition:service:region:account-id:resourcetype:resource')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type == 'resourcetype'
    assert arn.resource == 'resource'

    arn = arnparse('arn:partition:service:region:account-id:resourcetype:resource:qualifier')
    assert arn.partition == 'partition'
    assert arn.service == 'service'
    assert arn.region == 'region'
    assert arn.account_id == 'account-id'
    assert arn.resource_type == 'resourcetype'
    assert arn.resource == 'resource:qualifier'


def test__arnparse__resource_type_with_slash():
    arn_str = 'arn:aws:ec2:us-east-1:123456789012:vpc/vpc-fd580e98'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'ec2'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'vpc'
    assert arn.resource == 'vpc-fd580e98'


def test__arnparse__resource_type_with_colon():
    arn_str = 'arn:aws:codecommit:us-east-1:123456789012:MyDemoRepo'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'codecommit'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type is None
    assert arn.resource == 'MyDemoRepo'


def test__arnparse__resource_type_with_multiple_colons():
    arn_str = 'arn:aws:logs:us-east-1:123456789012:log-group:my-log-group*:log-stream:my-log-stream*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'logs'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'log-group'
    assert arn.resource == 'my-log-group*:log-stream:my-log-stream*'


def test__arnparse__no_resource_type():
    arn_str = 'arn:aws:cloudwatch:us-east-1:123456789012:alarm:MyAlarmName'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'cloudwatch'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'alarm'
    assert arn.resource == 'MyAlarmName'


def test__arnparse__resource_with_single_slash():
    arn_str = 'arn:aws:kinesisvideo:us-east-1:123456789012:stream/example-stream-name/0123456789012'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'kinesisvideo'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'stream'
    assert arn.resource == 'example-stream-name/0123456789012'


def test__arnparse__resource_with_multiple_slashes():
    arn_str = 'arn:aws:macie:us-east-1:123456789012:trigger/example61b3df36bff1dafaf1aa304b0ef1a975/alert/example8780e9ca227f98dae37665c3fd22b585'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'macie'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'trigger'
    assert arn.resource == 'example61b3df36bff1dafaf1aa304b0ef1a975/alert/example8780e9ca227f98dae37665c3fd22b585'


def test__arnparse__no_region__no_acount_id():
    arn_str = 'arn:aws:s3:::my_corporate_bucket'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 's3'
    assert arn.region is None
    assert arn.account_id is None
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_bucket'


def test__arnparse__spaces():
    arn_str = 'arn:aws:artifact:::report-package/Certifications and Attestations/SOC/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'artifact'
    assert arn.region is None
    assert arn.account_id is None
    assert arn.resource_type == 'report-package'
    assert arn.resource == 'Certifications and Attestations/SOC/*'


def test__arnparse__wildcard():
    arn_str = 'arn:aws:ec2:us-east-1:123456789012:instance/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'ec2'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'instance'
    assert arn.resource == '*'


def test__arnparse__double_wildcard():
    arn_str = 'arn:aws:events:us-east-1:*:*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'events'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '*'
    assert arn.resource_type is None
    assert arn.resource == '*'


def test__malformed_arn__no_arn_prefix():
    arn_str = 'something:aws:s3:::my_corporate_bucket'
    with pytest.raises(MalformedArnError) as exc_info:
        arnparse(arn_str)

    assert exc_info.value.arn_str == arn_str


def test__malformed_arn__empty_string():
    arn_str = ''
    with pytest.raises(MalformedArnError) as exc_info:
        arnparse(arn_str)

    assert exc_info.value.arn_str == arn_str


# ======================
# Service-specific tests
# ======================

def test__api_gateway():
    # Case 1
    arn_str = 'arn:aws:apigateway:us-east-1::a123456789012bc3de45678901f23a45:/test/mydemoresource/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'apigateway'
    assert arn.region == 'us-east-1'
    assert arn.account_id is None
    assert arn.resource_type is None
    assert arn.resource == 'a123456789012bc3de45678901f23a45:/test/mydemoresource/*'

    # Case 2
    arn_str = 'arn:aws:execute-api:us-east-1:123456789012:8kjmp19d1h/*/*/*/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'execute-api'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type is None
    assert arn.resource == '8kjmp19d1h/*/*/*/*'


def test__sns():
    # Case 1
    arn_str = 'arn:aws:sns:*:123456789012:my_corporate_topic'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'sns'
    assert arn.region == '*'
    assert arn.account_id == '123456789012'
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_topic'

    # Case2
    arn_str = 'arn:aws:sns:us-east-1:123456789012:my_corporate_topic:02034b43-fefa-4e07-a5eb-3be56f8c54ce'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'sns'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_topic:02034b43-fefa-4e07-a5eb-3be56f8c54ce'


def test__s3():
    # Case 1
    arn_str = 'arn:aws:s3:::my_corporate_bucket/exampleobject.png'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 's3'
    assert arn.region is None
    assert arn.account_id is None
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_bucket/exampleobject.png'

    # Case 2
    arn_str = 'arn:aws:s3:::my_corporate_bucket/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 's3'
    assert arn.region is None
    assert arn.account_id is None
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_bucket/*'

    # Case 3
    arn_str = 'arn:aws:s3:::my_corporate_bucket/Development/*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 's3'
    assert arn.region is None
    assert arn.account_id is None
    assert arn.resource_type is None
    assert arn.resource == 'my_corporate_bucket/Development/*'


def test__cloudwatch_logs():
    arn_str = 'arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/my-function:*'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'logs'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'log-group'
    assert arn.resource == '/aws/lambda/my-function:*'


def test__secrets_manager():
    arn_str = 'arn:aws:secretsmanager:us-east-1:123456789012:secret:myfolder/MyFirstSecret-ocq1Wq'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'secretsmanager'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'secret'
    assert arn.resource == 'myfolder/MyFirstSecret-ocq1Wq'


def test__batch():
    arn_str = 'arn:aws:batch:us-east-1:123456789012:job-definition/my-job-definition:1'

    arn = arnparse(arn_str)

    assert arn.partition == 'aws'
    assert arn.service == 'batch'
    assert arn.region == 'us-east-1'
    assert arn.account_id == '123456789012'
    assert arn.resource_type == 'job-definition'
    assert arn.resource == 'my-job-definition:1'
