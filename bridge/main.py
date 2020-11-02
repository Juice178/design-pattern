from display import Display
from count_display import CountDisplay
from string_display_impl import StringDisplayImpl


def main():
    d1 = Display(StringDisplayImpl("Hello, Japan."))
    d2 = Display(StringDisplayImpl("Hello, World."))
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d1.display()
    d2.display()
    d3.display()
    d3.multi_display(5)

if __name__ == "__main__":
    main()