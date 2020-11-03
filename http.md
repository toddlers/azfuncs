# azfunc
azure http functions

# Directory structure

Below directory structure is kind of mandatory , I wasnt able to create the function without it , in some cases it does work. But try to stick to this.

```sh
├── hello
│   ├── __init__.py
│   └── function.json
├── hello1
│   ├── __init__.py
│   └── function.json
├── hello3
│   ├── __init__.py
│   └── function.json
├── host.json
└── proxies.json
└── requirements.txt
```

* Make sure we are only making a zip out of the above directory structure do not include the top level dir.
* Install the requirements using something like below and package them in the zip.

```sh
pip  install --target=<target_dir> -r requirements.txt
```

## function.json

If parsing of this file fails your function doesnt gets created , even when you mention your entrypoint `scriptFile` wrong. Nothing will be created and no error will be displayed in console or events logs. 

```json
{
    "scriptFile": "__init__.py",
    "bindings": [
      {
        "authLevel": "function",
        "type": "httpTrigger",
        "direction": "in",
        "name": "req",
        "methods": [
          "get",
          "post"
        ]
      },
      {
        "type": "http",
        "direction": "out",
        "name": "$return"
      }
    ]
  }
```

## First Part of Bindings

* `scriptFile` : Required : entrypoint for the function. Can be any file you have in your source dir
* `type` : Required : What kind of trigger you want to have for your function. For more trigger types check [this](https://github.com/Azure/azure-functions-host/wiki/function.json)
* `direction` : Required : direction of this binding clause.
* `name` : Required: what kind of inputs var your function will be receiving. Can be any name or left empty. In our function we have

```python
def main(req: func.HttpRequest) -> func.HttpResponse:
```

* `methods`: what kind of methods your function support,  not sure if `get` is needed there , because even for my testing
   I had to call via a sepcial code via `POST` call.

## Second part of bindings

* `type` : what kind of output it is `http|blob` etc.
* `direction`: direction of this binding clause
* `name` : usually the name of the returned object in my case `$return` of the function.

### NOTES

1. Make sure you specify the correct entry path.
2. Make sure if you specify the output , you are returning something from your function. Otherwise it will fail something like below:

```txt
[Error]   Executed 'Functions.<function_name></function_name>' (Failed, Id=adsadasdas1312312, Duration=13ms)
```

3. We can leave the `Out` section of the function binding if we dont want to return anything followed by not returning anything from the function as well.
4. Details explanation can be found [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python#configuration)

## host.json

* described perfectly fine [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json)

## How to invoke the function

* Covered [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function)