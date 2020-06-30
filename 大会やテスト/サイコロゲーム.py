"""
あなたは友人たちとスゴロクで遊ぶことにしました。参加者はあなたを含めて M 人います。
スゴロクは分岐のない N マスから構成され、スタートマスからゴールマスまでの間には、1 から N-2 まで順番に番号がつけられたマスがあります。

スゴロクを始める前に、各プレイヤーは自分の駒をスタートマスに置きます。また、プレイヤー M 人に 1 から順番に番号を振ります。
スゴロクはターン制で進めていきます。各ターンでは、番号が 1 の人から順にサイコロを振ります。そして、サイコロの出た目の数だけ自分の駒を進めます。
K ターン終了した時点で、コインを一番多く持っていたプレイヤーが優勝となります。最初の時点では、各プレイヤーのコイン所持数は 0 です。
各マスには、移動に関する効果とコインに関する効果があります。これらの効果は、サイコロで移動したときにのみ適用されます。
移動に関する効果は以下の 4 種類のいずれかです。

・b マス進む
・b マス戻る
・何もしない

コインに関する効果は以下の 3 種類のいずれかです。

・コインを c 枚得る
・コインを c 枚失う
・何もない

「移動に関する効果」で移動したマスの効果は適用されないことに注意してください。

また、1 ~ 3 番目までにゴールした人は、次の回からボーナスがあります。サイコロの目に応じて以下のボーナスコインが付与されます。
・1 位の人は、サイコロの目 × 3 枚
・2 位の人は、サイコロの目 × 2 枚
・3 位の人は、サイコロの目 × 1 枚
・4 位以下の人はボーナスは付与されません。ただし、ゴールした後も暇なのでサイコロは振ります。

サイコロや効果による移動で駒がそれ以上進めなくなったときは、進めなくなったマスに止まることとします。 例えば、ゴールから 1 つ前のマスでサイコロの目が 6 だった場合、駒はゴールに移動します。 また、スタートの次のマスの効果が "3 マス戻る" だった場合、その効果で駒はスタートに移動します。
また、効果によってコインを失うとき、手持ちの枚数が 0 を下回ることはありません。

全員がサイコロを振り終わった時、優勝者の番号と所持しているコインの枚数を出力するプログラムを作成してください。
ただし、所持しているコインが同じ場合は、番号が小さい人が優勝とします。

以下は入力例 1 の 2 番目の人の例を図示したものです。
"""

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

list = input().split(" ")
masu = []
goal_count = 1
for i in range(int(list[0])-2):
    mas = input().split(" ")
    masu.append(mas)

moves = []
for i in range(int(list[2])):
    move = input().split(" ")
    moves.append(move)

#ます、コイン、ゴール順
players = [[0 for i in range(3)] for j in range(int(list[1]))]

#何回目の行動か
for i in range(int(list[2])):
    #何人目の行動か
    for j in range(int(list[1])):
        #goal
        if 1 <=players[j][2]<= 3:
            players[j][1] += int(moves[i][j]) * (4 - int(players[j][2]))
            continue


        players[j][0] += int(moves[i][j])


     #saikoroでゴールするとき
        if(int(players[j][0]) >= int(list[0]) and int(players[j][2]) == 0):
            players[j][2] = goal_count
            goal_count += 1
            continue

        #coin add
        players[j][1] = players[j][1] + int(masu[players[j][0]-1][1])

        #coin<0
        if players[j][1] < 0:
            players[j][1] = 0
        #masu add
        players[j][0] = players[j][0] + int(masu[players[j][0]-1][0])

        # マスの効果でゴールするとき
        if(int(players[j][0]) >= int(list[0]) and int(players[j][2]) == 0):
            players[j][2] = goal_count
            goal_count += 1

        #ゴールの外側行くとき
        if players[j][0] > int(list[0]):
            players[j][0] = int(list[0])

    #スタートよりもドルとき
        if int(players[j][0]) < 0:
            players[j][0] = 0

#一番多い人探し
coin = players[0][1]
hito = 1
for i in range(int(list[1])):
    if coin < players[i][1]:
        coin = players[i][1]
        hito = i + 1

print(str(hito) + " "+ str(coin))
