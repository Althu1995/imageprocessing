from functools import lru_cache
import boto3


@lru_cache(maxsize=10)
def initialize_client(service, client_type, logger, region=None):
    if client_type == "resource":
        client = boto3.resource(service, region_name=region)
    elif client_type == "client":
        client = boto3.client(service, region_name=region)
    else:
        logger.error("The client type is not proper.")
    return client
