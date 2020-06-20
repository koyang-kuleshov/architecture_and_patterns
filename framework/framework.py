from framework.body_generator import body_generator


class Application:

    # def __init__(self, urls, middlewares):
    def __init__(self, urls):
        self.urls = urls
        # self.middlewares = middlewares

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        data = []

        # request = {}

        # for middleware in self.middlewares:
        #     middleware(request)

        if path in self.urls:
            view = self.urls[path]
            # code, text = view(request)
            code, text = view()
            start_response(code, [('Content-Type', 'text/html')])
            for row in text:
                data.append(list(row))
            data = body_generator(data)
            return [str(data).encode(encoding='utf-8-sig')]
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return [b'Not Found']
