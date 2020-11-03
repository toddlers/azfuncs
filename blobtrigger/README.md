## connection string in the `function.json` check [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#configuration)
    The name of an app setting that contains the Storage connection string to use for this binding. If the app setting name 
    begins with "AzureWebJobs", you can specify only the remainder of the name here. For example, if you set connection to 
    "MyStorage", the Functions runtime looks for an app setting that is named "AzureWebJobsMyStorage." If you leave connection empty, the Functions runtime uses the default Storage connection string in the app setting that is named AzureWebJobsStorage.

THERE IS A PROBLEM WITH VSCODE AUTO GENERATED CODE.
IT DOESNT SETS THE CORRECT VALUE
FROM  VSCODE 
```json
 "connection": "<STORAGE_ACCOUNT_NAME>_STORAGE"
 ```

 IT SHOULD BE

 ```json
 "connection": "Storage"
 ```


## To trigger the function

* Check in the app settings if the `AzureWebJobsStorage` setting name is reflecting correct `connection string` for the storage account
* Create the corresponding `container` under the storage name mentioned above. For example as we have 

```json
"path": "samples-workitems/{name}",
```

It is looking for container name as `sample-workitems` and whatever is in the braces is just a placeholder for the object coming in.

