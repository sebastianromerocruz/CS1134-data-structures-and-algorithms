def gen_one():
    yield 1
    yield 2
    yield 3


def gen_two():
    yield 0

    # for value in gen_one():
    #     yield value
    yield from gen_one()

    yield 4
    yield 5


if __name__ == "__main__":
    for value in gen_two():
        print(value)
