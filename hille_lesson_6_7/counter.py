class Counter:
    """Class Counter"""

    def __init__(self, min_value=0, max_value=100, current_value=None):
        self.current_value = current_value
        self.__min_value = min_value
        self.__max_value = max_value

    def increase(self):
        """Counter + 1"""
        if self.current_value < self.__max_value:
            self.current_value += 1
            return self.current_value
        else:
            self.current_value = self.__min_value
            return self.current_value

    def get_current_value(self):
        """Display value counter"""
        print(self.current_value)
        return self.current_value


if __name__ == "__main__":
    cnt = Counter()
    cnt.current_value = 10
    cnt.get_current_value()
    cnt.increase()
    cnt.get_current_value()
    for _ in range(99):
        cnt.increase()
    cnt.get_current_value()
