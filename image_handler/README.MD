# Perform image operations lambda function
Perform image operations lambda function helps in uploading image to s3 bucket and generating a thumbnail for it which can be later downloaded.

## Layer
- common
- PILLOW to perform image resize operations

## Triggers
- APIGATEWAY

## Destinations Supported
- S3

## Permissions
- KMS: If SSE is enabled for DynamoDB
    + GenerateDataKey
    + Encrypt
    + Decrypt
    + DescribeKey
    + RotateKeyOnDemand
    + GetKeyRotationStatus
- S3: Permission for lambda to access the s3 bucket
    + MultipartUpload
    + GetObject
    + UploadObject
## Environment Variables
| Name | Description | Type | Environment Variable Sample |
| ------ | ------- | ----------- | --------------------|
| image_bucket_name | The bucket where image are to be uploaded| String | images-collection |
| image_path | The path where image is stored | String | images/ |
| logging_level | Priority level of the logger. | Optional; String | Values possible: info,debug,error |

## Enhancements Possible
As enhancements we can implement features like uploading multiple images at the same time, thumbnail images to be extracted with their image names for multiple ones. Then invoking the lambda usinga s3 notification feature to make it more automated and storing the details indynamodb for historical purposes.