"""test cases"""
import sys
import os
from moto import mock_s3
get_status_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(get_status_dir)
from config import Data
from perform_image_operations import perform_image_operations

query_state = Data()


@mock_s3
def test_upload_image():
    query_state._setup_resources_with_companycode_from_jwt()
    result = perform_image_operations(query_state.event, None)
    assert result['statusCode'] == 200


@mock_s3
def test_download_image():
    query_state._setup_resources_with_companycode_from_payload()
    result = perform_image_operations(query_state.event, None)
    assert result['statusCode'] == 200
