import asyncio
import os
import logging
import json

import azure.functions as func
from azure.identity import DefaultAzureCredential
from .resource_group_operations import list_rgs
from azure.mgmt.web import WebSiteManagementClient

async def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    The main entry point to the function.
    """

    # if "MSI_ENDPOINT" in os.environ:
    credentials = DefaultAzureCredential(logging_enable=True)
    # else:
    #     credentials, *_ = get_azure_cli_credentials()
    
    # logging.debug(credentials.__dict__())
    subscription_id = os.environ.get(
        'AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')
    
    logging.debug(os.environ.get('ResourceGroupName'))
    logging.debug(f'subscription id {subscription_id}')
    #list_of_rgs = await list_rgs(credentials, subscription_id)
    resource_group_name = 'spzpl'
    name='spzpl'

    web_client=WebSiteManagementClient(
        credentials,
        subscription_id
    )
    result =web_client.web_apps.get_configuration(resource_group_name, name,raw=True)
    return func.HttpResponse(json.dumps(result.response.json()))

    #return func.HttpResponse(list_of_rgs, mimetype="application/json")