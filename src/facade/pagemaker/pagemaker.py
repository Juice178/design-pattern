from pagemaker.writer import FileWriter
from pagemaker.database import Database
from pagemaker.html_writer import HtmlWriter
import traceback


class PageMaker:
    @staticmethod
    def make_welcome_page(mailaddr: str, filename: str) -> None:
        try:
            mailprop = Database.get_propetries("maildata")
            username = mailprop["DEFAULT"][mailaddr]
            writer = HtmlWriter(FileWriter(filename))
            writer.title(f"Welecome to {username}'s page!")
            writer.paragraph(f"{username}のページへようこそ！")
            writer.paragraph(f"Waiting for an email")
            writer.mailto(mailaddr, username)
            print(f"{filename} is created for {mailaddr} ({username})")
        except Exception as e:
            traceback.print_exc()
            print(e)