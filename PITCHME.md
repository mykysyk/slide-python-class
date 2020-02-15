### Pythonのクラスを書こう
---

### 公式サイトを読んでみよう。

9. クラス — Python 3.8.2rc1 ドキュメント
https://docs.python.org/ja/3/tutorial/classes.html

クラスはデータと機能を組み合わせる方法を提供します。 
新規にクラスを作成することで、新しいオブジェクトの 型 を作成し、その型を持つ新しい インスタンス が作れます。 
クラスのそれぞれのインスタンスは自身の状態を保持する属性を持てます。 
クラスのインスタンスは、その状態を変更するための (そのクラスが定義する) メソッドも持てます。
---

### ∑(ﾟДﾟ)
---

### とりあえずやってみよう
---

### ファーストフードのレジシステムを作ろう
---

### まずなにが必要？

ファーストフードレジシステムに必要な機能を上げてみよう
---

### ファーストフードレジシステムに必要な機能

1. メニューを登録
1. 注文を登録
1. 注文を確認
1. 注文の合計金額を確認
1. お金を受領しよう
1. お釣りを確認しよう
1. 領収書を発行
---

### プログラムにしやすいように名前をつけてみよう

ファーストフードレジシステム -> FirstFoodSystem
1. メニューを登録 -> set_menu
1. 注文を登録 -> set_order
1. 注文を確認 -> get_order
1. 注文の合計金額を確認 -> get_total_price
1. お金を受領しよう -> set_money
1. お釣りを確認しよう -> get_change
1. 領収書を発行 -> get_receipt
---

### 日本語を排除

```
FirstFoodSystem
    set_menu
    set_order
    get_order
    get_total_price
    set_money
    get_change
    get_receipt
```

---

### Pythonのお作法に従うとクラスの原型完成

```
class FirstFoodSystem:
    def set_menu(self, menu):
    def get_order(self, order):
    def get_order(self):
    def get_total_price(self):
    def set_money(self,mony):
    def get_change(self):
    def get_receipt(self):
```

---

### 肉付け

```
class FirstFoodSystem:
    def set_menu(self, menu):
        
    def get_order(self, order):
    
    def get_order(self):
    
    def get_total_price(self):
    
    def set_money(self,mony):
    
    def get_change(self):
    
    def get_receipt(self):
```

---


### おわり
