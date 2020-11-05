import logging
from datetime import datetime, timedelta
# import azure.storage.blob as azureblob
from azure.storage.blob import (
    BlobClient,
    generate_blob_sas,
    BlobSasPermissions
)

def parse_conn_string(storage_connection_string):
    conn = storage_connection_string.split(';')
    for l in conn:
        ss = l.split('=',1)
        if len(ss) != 2:
            continue
        if ss[0] == 'AccountName':
           storage_account = ss[1] 
        if ss[0] == 'AccountKey':
           storage_key = ss[1]
    return storage_account, storage_key


def get_blob_sas(account_name,account_key, container_name, blob_name, ttl):
    sas_blob = generate_blob_sas(account_name=account_name, 
                                container_name=container_name,
                                blob_name=blob_name,
                                account_key=account_key,
                                permission=BlobSasPermissions(read=True),
                                expiry=datetime.utcnow() + timedelta(hours=1))
    return sas_blob


def get_signed_url(storage_connection_string,
        container_name,
        blob_name,
        ttl
    ):
    logging.debug('In generate token function')
    storage_account_name , storage_account_key = parse_conn_string(storage_connection_string)
    logging.debug(storage_account_name)
    blob = get_blob_sas(storage_account_name,storage_account_key, container_name, blob_name, ttl)
    return (f'https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}?{blob}')
