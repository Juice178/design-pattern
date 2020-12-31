from director import Director
from text_builder import TextBuilder
from html_builder import HTMLBuilder


def main(text_kind):
    if text_kind == "plain":
        print("Create a plain text.")
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)
    elif text_kind == "html":
        print("Create a html file.")
        html_builder = HTMLBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.get_result()
        print(f"{filename} is created.")
    else:
        print("No argument is passed.")

if __name__ == "__main__":
    main("plain")
    main("html")
