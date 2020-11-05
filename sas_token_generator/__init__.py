import logging
import json
import os

import azure.functions as func
from .generate_token import get_token

_ALLOWED_HTTP_METHOD = "POST"


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
        # if 'ttl' in  req_body:
        #     token_ttl = req_body.get('ttl')
        #     if token_ttl < 1:
        #         return write_http_response(
        #         400,
        #         { 'message': 'Token ttl must be digit and more than 0' }
        #     )
    except ValueError:
        return func.HttpResponse(
            status_code=400,
            body='Invalid HTTP request body'
        )
    logging.debug(f'Container Name: {container}')
    logging.debug(f'Blob Name: {blob_name}')
    if container and blob_name:
        token = get_token(
            storage_connection_string,
            container,
            blob_name
            )
        logging.info(f'Token generated : {token}')
        return func.HttpResponse(
            body=token,
            status_code=200,
            headers=dict(req.headers)
            )
    else:
        return func.HttpResponse(
            body='Not able to generate token',
            status_code=500
        )
