from ctypes import py_object  # provides low-level arrays

from ArrayList import ArrayList

OPERATORS = "+-*/"


def make_array(n):
    return (n * py_object)()


class StaticArrayStack:
    def __init__(self, max_capacity):
        self.data = make_array(max_capacity)
        self.capacity = max_capacity
        self.n = 0

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) == self.capacity

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")

        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return item

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.data[self.n - 1]

    def __len__(self):
        return self.n


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()


def print_in_reverse(string):
    stack = ArrayStack()

    for char in string:
        stack.push(char)

    while not stack.is_empty():
        char = stack.pop()
        print(char, end="")

    print()


def eval_postfix_exp(expression_string):
    expression_list = expression_string.split()
    operand_stack = ArrayStack()

    for token in expression_list:
        if token not in OPERATORS:
            operand_stack.push(int(token))
        else:
            operand_one = operand_stack.pop()
            operand_two = operand_stack.pop()

            if token == "+":
                result = operand_two + operand_one
            elif token == "-":
                result = operand_two - operand_one
            elif token == "*":
                result = operand_two * operand_one
            elif token == "/":
                if operand_one == 0:
                    raise ZeroDivisionError
                else:
                    result = operand_two / operand_one
            operand_stack.push(result)

    return operand_stack.pop()


if __name__ == "__main__":
    string = "Phaedrus, by Plato"
    postfix_expr = "2  3  4  +  3  *  -"

    print_in_reverse(string)
    print(eval_postfix_exp(postfix_expr))
