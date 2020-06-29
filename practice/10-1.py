# coding: utf-8
# Your code here!

def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        raise e
    print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)
