# module1.py in the _shared directory


class SharedClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name} greet instance method from DB shared module was called!"


def shared_function(x, y):
    return x + y
