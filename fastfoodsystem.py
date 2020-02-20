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
    menu_dict = {'コーラー': 100, 'ハンバーガー': 110, 'ポテト': 100}
    macdonald = FastFoodSystem()
    macdonald.set_menu(menu_dict)
    macdonald.set_order('ハンバーガー')
    macdonald.set_order('ポテト')
    macdonald.set_order('コーラー')
    order = macdonald.get_order()
    print(order)                        # ['ハンバーガー', 'ポテト', 'コーラー']
    total_price = macdonald.get_total_price()
    print(total_price)                 # 310
    macdonald.set_deposit(500)
    change = macdonald.get_change()
    print(change)                       # 190
    receipt = macdonald.get_receipt()
    print(receipt)                      # {'change': 190,
                                        #  'deposit': 500,
                                        #  'order_list': ['ハンバーガー', 'ポテト', 'コーラー'],
                                        #  'total_price': 310}

if __name__ == '__main__':
    sample()
