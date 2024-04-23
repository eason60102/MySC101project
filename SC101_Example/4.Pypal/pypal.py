WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self._w = withdraw_limit

    def withdraw(self, amount):
        if self._w < amount:
            print('Exceed Limit')
        elif amount > self.__m:
            print('Error')
        else:
            self.__m -= amount
            print(f'{self._n} remains: {self.__m}')

    def set_username(self, new_name):
        self._n = new_name

    def get_money(self):
        return self.__m

    def __str__(self):
        return f"Name: {self._n}/Money: {self.__m}/Limit: {self._w}"

    def __iter__(self):
        self.withdraw = 0
        return  self

    def __next__(self):
        if self.withdraw < self.__m:
            self.withdraw += 100
            return 100
        else:
            raise StopIteration  # (raise)系統的return 傳送 Stop

def bank():
    jerry_a = Pypal('jerry', money=1000, withdraw_limit=700)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    jerry_a.withdraw(700)

def test():
    jerry_a = Pypal('YangHung', money=1000, withdraw_limit=700)  # __init__
    # print(jerry_a)  # __str__ # 教學1
    # 教學2
    for _ in jerry_a:
        print(_)



if __name__ == '__main__':
    # bank()
    test()
if __name__ == 'pypal':
    print('Thanks for using pypal.py! I am glad I am happy :)')