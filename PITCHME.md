### Pythonのクラスを書こう
---

### 公式サイトを読んでみよう。

9. クラス — Python 3.8.2rc1 ドキュメント
https://docs.python.org/ja/3/tutorial/classes.html

```
クラスはデータと機能を組み合わせる方法を提供します。 
新規にクラスを作成することで、新しいオブジェクトの 型 を作成し、その型を持つ新しい インスタンス が作れます。 
クラスのそれぞれのインスタンスは自身の状態を保持する属性を持てます。 
クラスのインスタンスは、その状態を変更するための (そのクラスが定義する) メソッドも持てます。
```

---

### ∑(ﾟДﾟ)
---

### 習うより慣れてみるのが一番
---

### お題
ファーストフードのレジシステムをクラスで作ろう
---

### まずなにが必要？

ファーストフードレジシステムに必要な機能
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

|変更前                |変更後 |
|--                   |-- |--- |
| ファーストフードレジシステム | FirstFoodSystem | 
| メニューを登録          | set_menu |
| 注文を登録            | set_order |
| 注文を確認            | get_order |
| 注文の合計金額を確認    | get_total_price |
| お金を受領しよう        | set_deposit |
| お釣りを確認しよう       | get_change |
| 領収書を発行          | get_receipt |

---


### 並べてみる

```
FirstFoodSystem
    set_menu
    set_order
    get_order
    get_total_price
    set_deposit
    get_change
    get_receipt
```

---

### Pythonのお作法に従うとクラスの原型完成

```
class FirstFoodSystem:
    def set_menu(self, menu):
    def set_order(self, order):
    def get_order(self):
    def get_total_price(self):
    def set_deposit(self, deposit):
    def get_change(self):
    def get_receipt(self):
```

---

### 肉付け


---

### 利用方法 1

```
mcdonalds = FirstFoodSystem()
mcdonalds.set_menu(menu_dict)
mcdonalds.set_order('ハンバーガー')
mcdonalds.set_order('ポテト')
mcdonalds.set_order('コーラー')
mcdonalds.get_order()
mcdonalds.get_total_price()  # 300
mcdonalds.set_deposit(500)
mcdonalds.get_change()       # 200
mcdonalds.get_receipt()
```
---
### 利用方法 2

```
yoshinoya = FirstFoodSystem()
yoshinoya.set_menu(menu_dict)
yoshinoya.set_order('牛丼並')
yoshinoya.set_order('牛丼並')
yoshinoya.get_order()
yoshinoya.get_total_price()  # 300
yoshinoya.set_deposit(500)
yoshinoya.get_change()       # 200
yoshinoya.get_receipt()
```



### おわり
