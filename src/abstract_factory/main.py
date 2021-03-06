from factory import Factory
import sys

def main(*args):
    try:
        factory = Factory.get_factory(args[0][1])
    except IndexError:
        raise Exception("No class argument is given.")

    nytimes = factory.create_link("New York Times", "https://www.nytimes.com/")
    financial_times = factory.create_link("Financial Times", "https://www.ft.com/")
    
    yahoo_us = factory.create_link("Yahoo!", "https://www.yahoo.com/")
    yahoo_jp = factory.create_link("Yahoo!Japan", "https://www.yahoo.co.jp/")

    instagram = factory.create_link("Instagram", "https://www.instagram.com/")
    twitter = factory.create_link("Twitter", "https://twitter.com/")

    tray_news = factory.create_tray("News")
    tray_news.add(nytimes)
    tray_news.add(financial_times)

    tray_yahoo = factory.create_tray("Yahoo!")
    tray_yahoo.add(yahoo_us)
    tray_yahoo.add(yahoo_jp)

    tray_sns = factory.create_tray("SNS")
    tray_sns.add(instagram)
    tray_sns.add(twitter)

    page = factory.create_page("LinkPage", "Mr.X")
    page.add(tray_news)
    page.add(tray_yahoo)
    page.add(tray_sns)
    page.output()


if __name__ == "__main__":
    main(sys.argv)

