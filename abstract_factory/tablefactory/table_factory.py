from factory import Factory
from tablefactory.table_link import TableLink
from tablefactory.table_tray import TableTray
from tablefactory.table_page import TablePage

class TableFactory(Factory):
    def create_link(self, caption, url):
        return TableLink(caption, url)
    
    def create_tray(self, caption):
        return TableTray(caption)
    
    def create_page(self, title, author):
        return TablePage(title, author)
