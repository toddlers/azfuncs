import logging
import json
import os

import azure.functions as func
from .generate_token import get_signed_url
from .upload_blob import upload_blob

_ALLOWED_HTTP_METHOD = "POST"
_DEFAULT_SAS_EXPIRY_DAYS = 365 * 30

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    storage_connection_string = os.environ.get('AzureWebJobsStorage')
    logging.debug(storage_connection_string)
    if not storage_connection_string:
        return func.HttpResponse(
            body='function configuration error',
            status_code=400
        )
    if req.method.lower() != _ALLOWED_HTTP_METHOD.lower():
        return func.HttpResponse(
            body='Method not allowed',
            status_code=403
        )
    try:
        req_body = req.get_json()
        logging.debug(req_body)
        container = req_body.get('container')
        blob_name = req_body.get('blobname')
        encoded_image = req_body.get('encoded_image')
        logging.debug(encoded_image)
        sas_ttl = _DEFAULT_SAS_EXPIRY_DAYS
        if 'ttl' in  req_body:
            token_ttl = req_body.get('ttl')
            if token_ttl < 1:
                return func.HttpResponse(
                status_code=400,
                body="Token ttl must be digit and more than 0"
            )
    except ValueError:
        return func.HttpResponse(
            status_code=400,
            body='Invalid HTTP request body'
        )
    logging.debug(f'Container Name: {container}')
    logging.debug(f'Blob Name: {blob_name}')
    logging.debug(f'SAS TTL : {sas_ttl}')

    # upload blob
    upload_blob(
        storage_connection_string,
        container,
        blob_name,
        encoded_image
    )

    # generate signed url
    generated_url = get_signed_url(
        storage_connection_string,
        container,
        blob_name,
        sas_ttl
        )
    logging.info(f'URL generated : {generated_url}')
    return func.HttpResponse(
        body=json.dumps({
            "url": generated_url
        }),
        status_code=200,
        mimetype="application/json"
        )
