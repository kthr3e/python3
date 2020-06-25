# 引数のデフォルト値

def introduce(greeting, name = "村人"):
    print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者")
introduce("こんにちは")

# 可変長引数

def introduce2(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce2("こんにちは", "勇者", "村人", "兵士")

# 可変長引数 - 辞書

def introduce3(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)

introduce3(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします")
