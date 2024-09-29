import os
import json
import http
from common.logger import get_logger
from common.boto3_initialization import initialize_client
from image_operations import app

logger = get_logger(logger_name='image_operations',
                    logging_level='error')


def perform_image_operations(event, context):
    try:
        logger.debug("event :%s", event)
        event["s3_client"] = initialize_client(
            service="s3", client_type='client', logger=logger)
        event['image_bucket_name'] = os.environ["image_bucket_name"]
        event['image_path'] = os.environ["image_path"]
        if "logging_level" in os.environ:
            event["logging_level"] = os.environ["logging_level"]
        msg = app.image_operation(event)
    except Exception as e:
        logger.exception(
            "Error in executing perform_image_operations module: %s", e)
        msg = {
                "statusCode": http.HTTPStatus.INTERNAL_SERVER_ERROR,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "errors":
                    [
                        {
                            "status": "500",
                            "title": "INTERNAL SERVER ERROR"
                        }
                    ]
                })
            }
    return msg