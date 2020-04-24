def division():
    for n in range(0, 5):
        try:
            print("n->", n)
            print(" 10.0 / n ->", 10.0 / n)
        except ZeroDivisionError:
            msg = "ZeroDivisionError"
            print("msg->", msg)


division()


