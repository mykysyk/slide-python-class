#coding: utf-8

class FastFoodSystem:


    def __init__(self):
        self.menu_dict = {}
        self.order_list = []
        self.total_price = 0
        self.deposit = 0
        self.change = 0
        self.receipt = {}

    def set_menu(self,menu):
        """ メニューを登録 """
        self.menu_dict = menu

    def set_order(self, order):
        """ 注文を登録 """
        if order in self.menu_dict:
            self.order_list.append(order)

    def get_order(self):
        """ 注文を確認 """
        return self.order_list

    def get_total_price(self):
        """ 注文の合計金額を確認 """
        for order in self.order_list:
            self.total_price += self.menu_dict[order]
        return self.total_price

    def set_deposit(self, deposit):
        """ お金を受領しよう"""
        self.deposit = deposit
        self.change = deposit - self.total_price

    def get_change(self):
        """ お釣りを確認しよう """
        return self.change

    def get_receipt(self):
        """ 精算内容を伝えよう """
        self.receipt = {
            'order_list': self.order_list,
            'total_price': self.total_price,
            'deposit': self.deposit,
            'change': self.change,
        }
        return self.receipt


def sample():
    MENU_DICT = {
        'ハンバーガー': 110,
        'ポテト' : 290,
        'コーラー': 100
        }

    mc = FastFoodSystem()
    mc.set_menu(MENU_DICT)              # メニューを登録
    mc.set_order('ハンバーガー')        # 注文を登録
    mc.set_order('ポテト')              # 注文を登録
    mc.set_order('コーラー')            # 注文を登録
    order = mc.get_order()              # 注文を確認
    print('注文を確認: {}'.format(order))
    total_price = mc.get_total_price()  # 注文の合計金額を確認
    print('注文の合計金額を確認: {}'.format(total_price))
    mc.set_deposit(1000)                # お金を受領しよう
    change = mc.get_change()            # 釣りを確認しよう
    print('お釣りを確認: {}'.format(change))
    sample_output(mc.get_receipt())     # 領収書を発行

def sample_output(receipt):
    print('')
    print('---------- キリトリ ----------')
    print('')
    print('=== 領収書 ===')
    print('')
    print('-' * 50)
    for order in receipt['order_list']:
        print(order)
    print('-' * 50)
    print('合計請求金額: {}円'.format(receipt['total_price']))
    print('お預かり金額: {}円'.format(receipt['deposit']))
    print('お釣り      : {}円'.format(receipt['change']))
    print('-' * 50)

if __name__ == '__main__':
    sample()
