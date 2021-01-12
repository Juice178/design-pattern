from printer_proxy import PrinterProxy


def main() -> None:
    p = PrinterProxy("Alice")
    print(f"Current name is: {p.get_printer_name()}.")
    p.set_printer_name("Bob")
    print(f"Current name is: {p.get_printer_name()}.")
    p.print("Hello, world.")


if __name__ == "__main__":
    main()