"""app.py"""
import json
import http
from common.logger import get_logger
from image_operations import utils


def image_operation(event):
    logger = get_logger(
                    logger_name='image operations',
                    logging_level=event.get("logging_level", "error"))
    logger.info('Received event and starting the process')
    if "operation" in event and event.get("operation") == "upload":
        msg = utils.perform_upload_operation(
            s3_client=event.get("s3_client"),
            bucket_name=event.get("image_bucket_name"),
            image_path=event.get("image_path"),
            image_name=event.get("imageName"),
            logger=logger)
    elif "operation" in event and event.get("operation") == "download":
        msg = utils.generate_presigned_url(
                s3_client=event.get("s3_client"),
                bucket_name=event.get("image_bucket_name"),
                thumbnail_name=event.get("thumbnailName"),
                logger=logger)
    else:
        logger.error("Not a recognized method")
        msg = {
                "statusCode": http.HTTPStatus.SERVICE_UNAVAILABLE,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "errors":
                    [
                        {
                            "status": "400",
                            "title": "Unknown Operation"
                        }
                    ]
                })
            }
    return msg
