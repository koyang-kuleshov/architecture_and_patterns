from framework.framework import Application
from mainapp.catalog import Catalog


def index_view():
    data = Catalog.show_all_items()
    return '200 OK', data


def about_view():
    # if 'secret' in request:
    #     return '200 OK', f'<h1>About Page {request["secret"]}</h1>'
    return '200 OK', f'<h1>About Page</h1>'


urls = {
    '/': index_view,
    '/about/': about_view
}


def secret_middleware(request):
    request['secret'] = 'secret'


# middlewares = [secret_middleware]
# middlewares = []

# application = Application(urls, middlewares)
application = Application(urls)
