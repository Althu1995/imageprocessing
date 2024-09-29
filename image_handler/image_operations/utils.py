import os
import http
import json
import uuid
import io
from PIL import Image


def perform_upload_operation(
                s3_client, image_path, image_name,
                bucket_name, logger):
    try:
        id = uuid.uuid4().hex
        file_path = os.path.join(image_path, image_name + ".jpg")
        upload_image_response = s3_client.upload_file(
                            file_path, bucket_name, f'original/{image_name}.jpg')
        with Image.open(file_path) as img:
            thumbnail_size = (128, 128)
            img.thumbnail(thumbnail_size)
            in_mem_file = io.BytesIO()
            img.save(in_mem_file, format='JPEG')
            in_mem_file.seek(0)
            upload_image_response = s3_client.upload_file(
                            in_mem_file, bucket_name, f'thumbnail/{image_name}.jpg')
        if upload_image_response:
            return {
                "statusCode": http.HTTPStatus.OK,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "data": {
                        "id": id,
                        "attributes": {
                            "name": "image-upload-operation",
                            "description": "The image upload operation",
                            "state": f"{image_name} successfully uploaded"
                        }
                    }
                })
            }
    except Exception as e:
        logger.error("Error while uploading to s3 due to %s", e)
        return {
                "statusCode": http.HTTPStatus.INTERNAL_SERVER_ERROR,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "errors":
                    [
                        {
                            "status": "500",
                            "title": "Internal Server Error"
                        }
                    ]
                })
            }


def generate_presigned_url(
        s3_client, thumbnail_name, bucket_name, logger):
    try:
        presigned_url = s3_client.generate_presigned_url(
                                ClientMethod='get_object',
                                Params={
                                    'Bucket': bucket_name,
                                    'Key': f'thumbnail/{thumbnail_name}.jpg'
                                },
                                ExpiresIn=3600
                            )
        if presigned_url:
            return {
                "statusCode": http.HTTPStatus.OK,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "data": {
                        "attributes": {
                            "name": "image-url-genration",
                            "description": "The thumbnail image generated",
                            "presignedUrl": presigned_url
                        }
                    }
                })
            }
    except Exception as e:
        logger.error("Error while generating presigned url due to %s", e)
        return {
                "statusCode": http.HTTPStatus.INTERNAL_SERVER_ERROR,
                "headers": {
                        'Access-Control-Allow-Origin': '*'
                    },
                "body": json.dumps({
                    "errors":
                    [
                        {
                            "status": "500",
                            "title": "Internal Server Error"
                        }
                    ]
                })
            }