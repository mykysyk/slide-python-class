class FastFoodSystem:
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
      
menu_dict = {'コーラー': 100, 'ハンバーガー': 110, 'ポテト': 100}
mc = FastFoodSystem()
mc.set_menu(menu_dict)
mc.set_order('ハンバーガー')
mc.set_order('ポテト')
mc.set_order('コーラー')
mc.get_order()        # ['ハンバーガー', 'ポテト', 'コーラー']
mc.get_total_price()  # 310
mc.set_deposit(500)
mc.get_change()       # 190
