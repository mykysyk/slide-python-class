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
とりあえず実物を見てみよう
---

### 基本系

```python

class ClassName:                # クラス名 (クラスの名前は CapWords 方式)
    COUNTER = 0                 # クラス変数 (すべてのインスタンスで共有して使う属性)
    def __init__(self):         # コンストラクタ (クラスのインスタンスが生成された際に呼び出される)
        self.value = None       # インスタンス変数 (そのインスタンスだけで使う属性)
        
    def set(self, value):       # メソッド
        self.value = value
        ClassName.COUNTER += 1
        
    def get(self):              # メソッド
        return self.value

# example
class_name = ClassName()        # クラスのインスタンスを生成
class_name.set('HelloWorld')    # class_name.value に HelloWorld がセットされる
value = class_name.get()        # class_name.value の値を取得
print(value)                    # HelloWorld が 出力される
```

https://pep8-ja.readthedocs.io/ja/latest/
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

### 先ほどの必要な機能をプログラムぽい名前に変更してみる

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

---

```python
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
```
---

### ٩(ˊᗜˋ*)و 

---

### 利用想定

```python
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

```
---


```python
mc.get_receipt()
```


```


=== 領収書 ===

--------------------------------------------------
ハンバーガー
ポテト
コーラー
--------------------------------------------------
合計請求金額: 310円
お預かり金額:  500円
お釣り      : 190円
--------------------------------------------------
```

---

### 肉付け

https://github.com/mykysyk/slide-test/blob/master/fastfoodsystem.py

---

### おわり
