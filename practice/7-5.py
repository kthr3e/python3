# RPGの攻撃シーン

def attack(person):
    print(person + "はスライムを攻撃した")

def output_ememy_hp(enemy_hp):
    print("敵のHPは残り" + str(enemy_hp) + "です")

enemy_hp = int(input())
team = {"勇者" : 200, "戦士" : 150, "魔法使い" : 100}

for person, power in team.items():
    attack(person)
    # 以下に、敵の体力を減少させるコードを書く
    enemy_hp -= power
    output_ememy_hp(enemy_hp)
