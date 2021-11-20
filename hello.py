def greeting(name: str) -> None:
    """Greeting function"""
    print("Hi, {name}".format(name=name))


if __name__ == "__main__":
    greeting("World")
