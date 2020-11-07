import logging
import base64
# from azure.common import AzureException
from azure.storage.blob import (
    BlobServiceClient,
    ContentSettings
)

def upload_blob(storage_connection_string, container_name, blob_name, encoded_image):
    image = encoded_image.replace(' ', '+')

    # decoding base64 image from json body
    decoded_image = base64.b64decode(image)
    logging.debug(decoded_image)
    logging.debug('In upload blob function')
    #storage_account_name , storage_account_key = parse_conn_string(storage_connection_string)
    logging.debug('creating blob service client')
    blob_service_client = BlobServiceClient.from_connection_string(
        conn_str=storage_connection_string
        )
    # # create container if not present
    # if not container_name:
    #     blob_service_client.create_container(container_name)
    # upload blob
    #BlobPermissions(container_name, blob_name, file_path, content_settings=None,
    # metadata=None, validate_content=False, progress_callback=None, max_connections=2,
    # lease_id=None, if_modified_since=None, if_unmodified_since=None, if_match=None,
    # if_none_match=None, timeout=None)

    #get container specific client
    logging.debug(f'getting client for container : {container_name}')
    container_client = blob_service_client.get_container_client(container=container_name)
    blob_client = container_client.get_blob_client(blob_name)
    if blob_client.exists():
        blob_client.delete_blob()
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    logging.debug('uploading blob now')
    try:
        blob_client.upload_blob(decoded_image)
        content_settings =ContentSettings(content_type='image/png')
        logging.debug(f'setting the content type : {content_settings}')
        # the below commented code works for standalone scripts not for functions
        # with open(full_path_to_file, "rb") as data:
        #     blob_client.upload_data(data)
        # # blob_service_client.create_blob_from_path(
        # #     container_name=container_name,
        # #     blob_name=blob_name,
        # #     file_path=full_path_to_file,
        # # )
    except Exception as e:
        logging.error(str(e))