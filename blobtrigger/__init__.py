import logging
import azure.functions as func
# connection string check here
# https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#configuration
# The name of an app setting that contains the Storage connection string to use for this binding. If the app setting name 
# begins with "AzureWebJobs", you can specify only the remainder of the name here. For example, if you set connection to 
# "MyStorage", the Functions runtime looks for an app setting that is named "AzureWebJobsMyStorage." If you leave connection empty, 
# the Functions runtime uses the default Storage connection string in the app setting that is named AzureWebJobsStorage.

# THERE IS A PROBLEM WITH VSCODE AUTO GENERATED CODE.
# IT DOESNT SETS THE CORRECT VALUE
# FROM  VSCODE 
# "connection": "<STORAGE_ACCOUNT_NAME>_STORAGE"
# IT SHOULD BE
# "connection": "Storage"

def main(myblob: func.InputStream):
    logging.info("entering the function====================")
    logging.info('Python Blob trigger function processed %s', myblob.name)
    logging.info("exitingt the function====================")


    