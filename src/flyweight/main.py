import sys
from bigstring import BigString


def main(args) -> None:
    if len(args) == 1:
        print("Usage: python main.py digits")
        print("Example: python main.py 1212123")
        sys.exit(0)
    print(args)
    bs = BigString(args[1])
    bs.print()


if __name__ == "__main__":
    main(sys.argv)
