# coding: utf-8

class FastFoodSystem:
    """ ファーストフードレジシステム
    """

    def __init__(self):
        self.menu_dict = {}
        self.order_list = []
        self.total_price = 0
        self.deposit = 0
        self.change = 0
        self.receipt = {}

    def set_menu(self, menu):
        """ メニューを登録
        Args:
            menu (dict): {'order1': price, }
        Examples:
            >>> set_menu({'cola': 100, 'coffee': 200})
        """
        self.menu_dict = menu

    def set_order(self, order):
        """ 注文を登録
        Examples:
            >>> set_order('cola')
            >>> set_order('coffee')
        """
        if order in self.menu_dict:
            self.order_list.append(order)

    def get_order(self):
        """ 注文を確認
        Examples:
            >>> get_order()
                ['cola', 'coffee']
        """
        return self.order_list

    def get_total_price(self):
        """ 注文の合計金額を確認
        Examples:
            >>> get_total_price()
                300
        """
        for order in self.order_list:
            self.total_price += self.menu_dict[order]
        return self.total_price

    def set_deposit(self, deposit):
        """ お金を受領しよう
        Args:
            deposit (int) : 預かった金額
        Examples:
            >>> set_deposit(1000)
        """
        self.deposit = deposit
        self.change = deposit - self.total_price

    def get_change(self):
        """ お釣りを確認しよう
        Examples:
            >>> get_change()
                700
        """
        return self.change

    def get_receipt(self):
        """ 精算内容を伝えよう
        Examples:
            >>> get_receipt()
                {'order_list': ['cola', 'coffee'],
                 'total_price': 300,
                 'deposit': 1000,
                 'change': 700}
        """
        self.receipt = {
            'order_list': self.order_list,
            'total_price': self.total_price,
            'deposit': self.deposit,
            'change': self.change,
        }
        return self.receipt


def sample():

    from pprint import pprint

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
    receipt = mc.get_receipt()          # 領収書を発行
    pprint(receipt)

if __name__ == '__main__':
    sample()
