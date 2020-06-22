from framework.framework import Application
from framework.views import index_view, add_item, add_item_script, styles

urls = {
    '/': index_view,
    '/add-item/': add_item,
    '/add-item-script/': add_item_script,
    '/templates/styles.css/': styles,
}

application = Application(urls)
