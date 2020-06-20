from framework import Application


def index_view(request):
    return '200 OK', 'Index Page'

def about_view(request):
    if 'secret' in request:
        return '200 OK', f'<h1>About Page {request["secret"]}</h1>'
    return '200 OK', f'<h1>About Page</h1>'

urls = {
    '/': index_view,
    '/about/': about_view
}

def secret_middleware(request):
    request['secret'] = 'secret'

# middlewares = [secret_middleware]
middlewares = []

application = Application(urls, middlewares)
