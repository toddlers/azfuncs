#Request successfully matched the route with name 'function' and template 'api/function'
#https://{FunctionAppName}.azurewebsites.net/api/function?code=adasdasdsdsa
#Post  https://{FunctionAppName}.azurewebsites.net/admin/functions/{functionName}

import logging
#import azure.functions as func

def main(input: str):
    logging.info('This is nonhttp python function')
    logging.debug(f'The value of input is : {input}')
