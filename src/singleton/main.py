from singleton import Singleton


def main():
    print("Start. ")
    obj1 = Singleton.get_instance()
    obj2 = Singleton.get_instance()
    if (obj1 == obj2):
        print("obj1 and obj2 are the same instances.")
    else:
        print("obj1 and obj2 are the different instances.")
    print("End.")

if __name__ == "__main__":
    main()