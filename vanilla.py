# coding: utf-8

class FastFoodSystem:
    """ ファーストフードレジシステム """
    
    def set_menu(self, menu):
        """ メニューを登録 """
        pass
    
    def set_order(self, order):
        """ 注文を登録 """
        pass
    
    def get_order(self):
        """ 注文を確認 """
        pass
    
    def get_total_price(self):
        """ 注文の合計金額を確認 """
        pass
    
    def set_deposit(self, deposit):
        """ お金を受領しよう """
        pass
    
    def get_change(self):
        """ お釣りを確認しよう """
        pass
    
    def get_receipt(self):
        """ 領収書を発行 """
        pass

macdonald = FastFoodSystem()
macdonald.set_menu({'コーラー': 100, 'ハンバーガー': 110, 'ポテト': 100})
macdonald.set_order('ハンバーガー')
macdonald.set_order('ポテト')
macdonald.set_order('コーラー')
macdonald.set_order('モスバーガー')
macdonald.get_order()           # ['ハンバーガー', 'ポテト', 'コーラー']
macdonald.get_total_price()     # 310
macdonald.set_deposit(500)
macdonald.get_change()          # 190
macdonald.get_receipt()         # {'change': 190,
                                #  'deposit': 500,
                                #  'order_list': ['ハンバーガー', 'ポテト', 'コーラー'],
                                #  'total_price': 310}

