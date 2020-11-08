* The request has to be made in the following format with header as `Content-Type=application/json`

```json
 {
    "container": "<container_name>",
    "blobname": "<blob_name>",
    "encoded_image" : "<base64 encoded file>"
 }
 ```
 
 ```sh
 curl -X POST -H "Content-Type: application/json" -d '{"encoded_image": $(base64 ~/Pictures/1.jpg), "blobname" : "<blob_name>", "container" : "<contaienr_name>"}' http://some/url
```

* As of now setting the content type as `image/png` in the code, update the code to handle the file type.
