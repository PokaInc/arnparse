from __future__ import absolute_import

from arnparse.str_utils import empty_str_to_none


class MalformedArnError(Exception):
    def __init__(self, arn_str):
        self.arn_str = arn_str

    def __str__(self):
        return 'arn_str: {arn_str}'.format(arn_str=self.arn_str)


class Arn(object):
    def __init__(self, partition, service, region, account_id, resource_type, resource):
        self.partition = partition
        self.service = service
        self.region = region
        self.account_id = account_id
        self.resource_type = resource_type
        self.resource = resource


def arnparse(arn_str):
    if not arn_str.startswith('arn:'):
        raise MalformedArnError(arn_str)

    elements = arn_str.split(':', 5)

    resource = elements[5]
    resource_type = None

    service = elements[2]
    if service not in ['s3', 'sns', 'apigateway', 'execute-api']:
        if '/' in resource:
            resource_type, resource = resource.split('/', 1)
        elif ':' in resource:
            resource_type, resource = resource.split(':', 1)

    return Arn(
        partition=elements[1],
        service=service,
        region=empty_str_to_none(elements[3]),
        account_id=empty_str_to_none(elements[4]),
        resource_type=resource_type,
        resource=resource,
    )
