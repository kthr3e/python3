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
