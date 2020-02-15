### Pythonのクラスを書こう
---

### 公式サイトを読んでみよう。

#### 9. クラス — Python 3.8.2rc1 ドキュメント

https://docs.python.org/ja/3/tutorial/classes.html


```txt
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

ファーストフードのレジシステムをクラスを使用して作ってみる
---

### 必要な機能

1. メニューを登録
1. 注文を登録
1. 注文を確認
1. 注文の合計金額を確認
1. お金を受領しよう
1. お釣りを確認しよう
1. 領収書を発行

---

### 先ほどの機能をプログラムで使いやすい名前に変更してみる

---

|変更前                |変更後 |
|--                   |-- |--- |
| ファーストフードレジシステム | FastFoodSystem | 
| メニューを登録          | set_menu |
| 注文を登録            | set_order |
| 注文を確認            | get_order |
| 注文の合計金額を確認    | get_total_price |
| お金を受領しよう        | set_deposit |
| お釣りを確認しよう       | get_change |
| 領収書を発行          | get_receipt |

---

### ソースコードに落としてみる

```python
class FastFoodSystem:
    def set_menu(self, menu):
        pass
    def set_order(self, order):
        pass
    def get_order(self):
        pass
    def get_total_price(self):
        pass
    def set_deposit(self, deposit):
        pass
    def get_change(self):
        pass
    def get_receipt(self):
        pass
```
---

### ٩(ˊᗜˋ*)و 

---

### 肉付け


---

### 利用方法 1

```python
mcdonalds = FirstFoodSystem()
mcdonalds.set_menu(menu_dict)
mcdonalds.set_order('ハンバーガー')
mcdonalds.set_order('ポテト')
mcdonalds.set_order('コーラー')
mcdonalds.get_order()        # ['ハンバーガー', 'ポテト', 'コーラー']
mcdonalds.get_total_price()  # 500
mcdonalds.set_deposit(1000)
mcdonalds.get_change()       # 500
mcdonalds.get_receipt()
```
---
### 利用方法 2

```python
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


---

### おわり
