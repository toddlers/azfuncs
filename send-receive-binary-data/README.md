* HttpResponse class has the function defined which sets the content.

```python
class HttpResponse(_abc.HttpResponse):
    """An HTTP response object.

    :param str/bytes body:
        Optional response body.

    :param int status_code:
        Response status code.  If not specified, defaults to 200.

    :param dict headers:
        An optional mapping containing response HTTP headers.

    :param str mimetype:
        An optional response MIME type.  If not specified, defaults to
        ``'text/plain'``.

    :param str charset:
        Response content text encoding.  If not specified, defaults to
        ``'utf-8'``.
    """

    def __init__(self, body=None, *,
                 status_code=None, headers=None, mimetype=None, charset=None):
        if status_code is None:
            status_code = 200
        self.__status_code = status_code

        if mimetype is None:
            mimetype = 'text/plain'
        self.__mimetype = mimetype

        if charset is None:
            charset = 'utf-8'
        self.__charset = charset

        if headers is None:
            headers = {}
        self.__headers = HttpResponseHeaders(headers)

        if body is not None:
            self.__set_body(body)
        else:
            self.__body = b''
..

    def __set_body(self, body):
        if isinstance(body, str):
            body = body.encode(self.__charset)

        if not isinstance(body, (bytes, bytearray)):
            raise TypeError(
                f'response is expected to be either of '
                f'str, bytes, or bytearray, got {type(body).__name__}')

        self.__body = bytes(body)
...
```

* Making the request

```sh
curl  -v  --data-binary @sample.jpg -H "x-functions-key : <CODE>" https://<function_app_name>.azurewebsites.net/api/<function_name> -o out.jpg
```
