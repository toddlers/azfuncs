#Request successfully matched the route with name 'function' and template 'api/function'
#https://{FunctionAppName}.azurewebsites.net/api/function?code=adasdasdsdsa
#Post  https://{FunctionAppName}.azurewebsites.net/admin/functions/{functionName}

import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )