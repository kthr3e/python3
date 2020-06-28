# coding: utf-8
# メソッドをオーバーライドしよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")
