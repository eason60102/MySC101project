class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ds = []
        self.min = None

    def push(self, val: int) -> None:
        self.ds.append(val)
        if self.min is None:
            # First data
            self.min = val
        else:
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if len(self.ds) != 0:
            self.ds.pop()

    def top(self) -> int:
        if len(self.ds) != 0:
            return self.ds[-1]

    def get_min(self) -> int:
        return self.min
        # if len(self.ds) != 0:
        #     my_min = self.ds[0]
        #     for num in self.ds:
        #         if num < my_min:
        #             my_min = num
        #     return my_min


if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')  # None
    print(my_stack.get_min(), end=', ')  # None
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')  # -1
    print(my_stack.top(), end=', ')  # 3
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')  # -2
    print(my_stack.top())  # -2
