The request has to be made in the following format with header as `Content-Type=application/json`

```json
 {
    "container": "<container_name>",
    "blobname": "<blob_name>",
    "encoded_image" : "<base64 encoded file>"
 }
 ```

* As of now setting the content type as `image/png` in the code, update the code to handle the file type.
