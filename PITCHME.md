### Pythonのクラスを書こう

---

### 公式ドキュメント

#### 9. クラス — Python 3.8.2rc1 ドキュメント

https://docs.python.org/ja/3/tutorial/classes.html


```txt
クラスはデータと機能を組み合わせる方法を提供します。 
新規にクラスを作成することで、新しいオブジェクトの 型 を作成し、その型を持つ新しい インスタンス が作れます。 
クラスのそれぞれのインスタンスは自身の状態を保持する属性を持てます。 
クラスのインスタンスは、その状態を変更するための (そのクラスが定義する) メソッドも持てます。
```

---

### 簡単なクラスを作成

---

### 値をセットしてその値を出力するだけの簡単なクラス

```python
class ClassName:

    def __init__(self):
        self.value = None

    def set(self, value):
        self.value = value

    def get(self):
        return self.value
```

@[1](クラス名：「class」に続けてクラスの名前を記述)
@[6,9](メソッド：「def」に続けてメソッド名を記述、第一引数に必ずselfを記述)
@[4,7,10](インスタンス変数: 「self.」を変数名の前に記述)
@[4,7,10](インスタンス変数: そのインスタンスだけで使う属性)
@[6-7](インスタンス変数に値をセットするメソッド)
@[9-10](インスタンス変数から値を取得するメソッド)
@[3-4](コンストラクタ：クラスのインスタンスが生成された際に呼び出される)

---

#### クラスの使い方 

```python
class ClassName:

    def __init__(self):
        self.value = None

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

instance_name = ClassName()
instance_name.set('HelloWorld')
value = instance_name.get()
print(value)
```

@[12-15](クラスを実際に使う)
@[12](クラスのインスタンスを生成)
@[13](インスタンス変数 value に HelloWorld がセットされる)
@[14](インスタンス変数 value の値を取得)
@[15](HelloWorld が 出力される)

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
{'change': 500,
 'deposit': 1000,
 'order_list': ['ハンバーガー', 'ポテト', 'コーラー'],
 'total_price': 500}
```

---

### 肉付け

https://github.com/mykysyk/slide-test/blob/master/fastfoodsystem.py

---

### おわり
