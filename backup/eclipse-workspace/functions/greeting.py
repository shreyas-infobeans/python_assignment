def display(name):
    def message():
        return "Hello "
    res = message()+name
    return res

print(display("shreyas"))