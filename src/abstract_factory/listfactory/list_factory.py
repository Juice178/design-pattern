from factory import Factory 
from listfactory.list_link import ListLink
from listfactory.list_page import ListPage
from listfactory.list_tray import ListTray


class ListFactory(Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)
    def create_tray(self, caption):
        return ListTray(caption)
    def create_page(self, title, author):
        return ListPage(title, author)