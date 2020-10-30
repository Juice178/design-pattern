class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.make_title("Greeting")
        self._builder.make_string("Moring to Afternoon")
        self._builder.make_items(["Good Morning", "Good afternoon"])
        self._builder.make_string("At nignt")
        self._builder.make_items(["Good evening", "Good night", "Goodbye"])
        self._builder.close()