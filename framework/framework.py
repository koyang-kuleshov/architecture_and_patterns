from cgi import parse_qs, escape, parse_multipart, parse


class Application:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path += '/'
        method = environ['REQUEST_METHOD']

        if path in self.urls:
            view = self.urls[path]
            if method == 'POST':
                try:
                    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
                except ValueError:
                    request_body_size = 0
                print(environ)
                request = environ['wsgi.input'].read(request_body_size)
                # FIXIT: Not working
                d = parse_qs(request)
                print(d)
                spam = d.get('category_id')[0]
                print(spam)
            code, text, type_header = view(request)
            start_response(code, [('Content-Type', type_header)])
            return [str(text).encode(encoding='utf-8-sig')]
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return [b'Not Found']
