import pypal



def bank():
    jerry_a = pypal.Pypal('YoungHung', money=1000, withdraw_limit=700)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    # jerry_a.__m = 100000
    jerry_a.set_username('YoungHong')
    jerry_a.withdraw(70)
    print(jerry_a.get_money())


if __name__ == '__main__':
    bank()