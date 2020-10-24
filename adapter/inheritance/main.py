from print_banner import PrintBanner 
from printing import Printing

def main():
    p = PrintBanner("Hello")
    assert isinstance(p, Printing)
    p.print_weak()
    p.print_strong()

if __name__ == "__main__":
    main()
