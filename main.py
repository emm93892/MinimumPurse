# お金の種類
MONEY_TYPES = [1000, 500, 100, 50, 10, 5, 1]


def calculate_purse(money):
    """ 金額における紙幣・小銭の数を取得してリスト形式にして返す """
    reminder = money
    purse = []
    for type_ in MONEY_TYPES:
        quotient, reminder = divmod(reminder, type_)
        purse.append(quotient)
    return purse


def subtract_purse(X, Y):
    """ 小銭の枚数の差を計算 """
    difference = list(map(lambda x, y: x-y, X, Y))
    return difference


def get_sum_money(coins):
    """ 小銭の枚数から金額の合計を計算 """
    moneys = map(lambda c, type_: c*type_, coins, MONEY_TYPES)
    sum_money = sum(moneys)
    return sum_money


def calculate(price, in_hand_money):
    """ 小銭の最小化を計算 """

    print(f"代金：{price}, 所持金：{in_hand_money}")

    # http://takeno.iee.niit.ac.jp/~shige/math/lecture/misc/data/kozeni2.pdf
    # 上記リンク、「4 実際の支払時の応用」のA,B,C,A'(,B')を使用する

    # A : 所持金の小銭
    A = calculate_purse(in_hand_money)
    # B : 最終的な残金
    B = calculate_purse(in_hand_money - price)
    # C : AとBの共通部分
    C = []
    for (a, b) in zip(A, B):
        if a == 0 or b == 0:
            C.append(0)
        elif a > b:
            C.append(b)
        elif b > a:
            C.append(a)
        elif a == b:
            C.append(a)

    # A' : AからCを取り除いたもの
    A_dash = subtract_purse(A, C)
    # B' : BからCを取り除いたもの
    # B_dash = subtract_purse(B, C)

    # 店員に渡す金額
    print(f"店員に渡す金額：{get_sum_money(A_dash)}")
    # おつり
    # print(f"お釣り：{get_all_money(B_dash)}")
    # 清算後の所持金
    # print(f"清算後の所持金：{in_hand_money - get_all_money(A_dash) + get_all_money(B_dash)}\n")


if __name__ == '__main__':
    # 入力: calculate(代金, 所持金)
    calculate(716, 1324)
    calculate(694, 1448)
