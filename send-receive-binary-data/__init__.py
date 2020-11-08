import logging
import io
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_body()
    return func.HttpResponse(status_code=200,
    body=req_body
    )
