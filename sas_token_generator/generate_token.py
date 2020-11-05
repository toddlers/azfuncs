import logging
from datetime import datetime, timedelta
# import azure.storage.blob
# from azure.storage.blob import BlobPermissions
from azure.storage.blob import (
    BaseBlobService,
    generate_blob_shared_access_signature,
    BlobPermissions
)


def parse_conn_string(storage_connection_string):
    storage_conn = storage_connection_string.split(';')
    *_, name = storage_conn[1].split('=')
    *_, key = storage_conn[2].split('=')
    return name, key

def get_token(storage_connection_string,
        container_name,
        blob_name
    ):
    # sas_token = generate_account_sas(
    #     account_name="<storage-account-name>",
    #     account_key="<account-access-key>",
    #     resource_types=ResourceTypes(service=True),
    #     permission=AccountSasPermissions(read=True),
    #     expiry=datetime.utcnow() + timedelta(hours=1)
    # )
    storage_account_name , token_credential = parse_conn_string(storage_connection_string)
    # blob_service_client = baseblobservice.BaseBlobService(connection_string=storage_connection_string)
    blob_service_client = BaseBlobService(
        account_url=f'https://{storage_account_name}.blob.core.windows.net',
        credential=token_credential
    )
    # sas_token = generate_account_sas(
    #     storage_account_name,
    #     storage_account_key,
    #     resource_types=ResourceTypes(service=True),
    #     permission=AccountSasPermissions(read=True),
    #     expiry=datetime.utcnow() + timedelta(hours=1)
    # )

    sas_signature = blob_service_client.generate_blob_shared_access_signature(
        container_name,
        blob_name,
        permission=BlobPermissions.READ,
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    # sas_url = blob_service_client.generate_blob_shared_access_signature(
    #     container,
    #     blob_name,
    #     ,
    #     datetime.now() + timedelta(hours=1)
    # )
    # sas_token = generate_account_sas(
    # account_name=storage_account_name,
    # account_key=storage_account_key,
    # resource_types=ResourceTypes(service=True),
    # permission=AccountSasPermissions(read=True),
    logging.debug(sas_signature)
    return(f'https://+{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_signature}')
