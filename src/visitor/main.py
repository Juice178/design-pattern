from directory import Directory
from list_visitor import ListVisitor
from file import File


def main():
    try:
        print("Making root entries ...")
        root_dir = Directory("root")
        bind_dir = Directory("bin")
        tmp_dir = Directory("tmp")
        usr_dir = Directory("usr")

        root_dir.add(bind_dir)
        root_dir.add(tmp_dir)
        bind_dir.add(File("vi", 10000))
        bind_dir.add(File("latext", 20000))
        # print(len(root_dir._dir), len(bind_dir._dir))
        print(root_dir._dir)
        root_dir.accept(ListVisitor())

        print("")
        print("Making user entries ...")
        yuki = Directory("yuki")
        hanako = Directory("hanako")
        tomura = Directory("tomura")
        usr_dir.add(yuki)
        usr_dir.add(hanako)
        usr_dir.add(tomura)
        yuki.add(File("diary.html", 100))
        yuki.add(File("Composite.java", 200))
        hanako.add(File("memo.txt", 300))
        tomura.add(File("game.doc", 400))
        tomura.add(File("junk.mail", 500))
        root_dir.accept(ListVisitor())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()