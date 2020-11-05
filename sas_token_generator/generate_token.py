import logging
from datetime import datetime, timedelta
import azure.storage.blob as azureblob

_DEFAULT_SAS_EXPIRY_DAYS = 365 * 30

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

def get_token(storage_connection_string,
        container_name,
        blob_name
    ):
    logging.debug('In generate token function')
    storage_account_name , storage_account_key = parse_conn_string(storage_connection_string)
    logging.debug(storage_account_name)
    blob_service_client = azureblob.BlockBlobService(
        account_name=storage_account_name,
        account_key=storage_account_key
    )
    try:
        perm = azureblob.BlobPermissions(
        read=True, create=True, write=True, delete=True)
        sas_signature = blob_service_client.generate_blob_shared_access_signature(
            ccontainer_name=container_name,
            blob_name=blob_name,
            permission=perm,
            expiry=datetime.now() + timedelta(days=_DEFAULT_SAS_EXPIRY_DAYS)
        )
    except Exception as e:
        logging.debug(e)
    logging.debug(sas_signature)
    return(f'https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_signature}')
