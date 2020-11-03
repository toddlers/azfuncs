# azfunc
azure non http functions

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
      "type": "manualTrigger",
      "direction": "in",
      "name": "input"
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
def main(input: str):
```

if we dont specify this input name function will fail with below error:

```txt
[Error]   Executed 'Functions.<function_name></function_name>' (Failed, Id=adsadasdas1312312, Duration=13ms)
```

### NOTES

1. Make sure you specify the correct entry path.
2. We can leave the `Out` section of the function binding if we dont want to return anything followed by not returning anything from the function as well.
3. Details explanation can be found [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python#configuration)

## host.json

```json
{
    "version": "2.0",
    "logging": {
      "logLevel": {
        "default": "Trace"
      },
      "applicationInsights": {
        "samplingSettings": {
          "isEnabled": true,
          "excludedTypes": "Request"
        }
      }
    }
  }
  ```

* described perfectly fine [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json)

## How to invokve non http function

* Covered [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-manually-run-non-http)