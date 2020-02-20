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

### クラスの作成方法

---

### 値を入出力するだけのクラス

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
@[3,6,9](メソッド：「def」に続けてメソッド名を記述、第一引数に必ずselfを記述)
@[4,7,10](インスタンス変数: 「self.」を変数名の前に記述)
@[4,7,10](インスタンス変数: そのインスタンスだけで使う属性)
@[3-4](コンストラクタ：クラスのインスタンスが生成された際に呼び出される)
@[6-7](インスタンス変数に値をセットするメソッド)
@[9-10](インスタンス変数から値を取得するメソッド)


---

#### クラスの使用方法

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
@[1-10](先ほど作成したクラス)
@[12-15](クラスを呼び出して使う側)
@[12](クラスのインスタンスを生成)
@[1-4,12](クラスのインスタンスを生成)
@[13](インスタンス変数 value に HelloWorld がセットされる)
@[6-7,13](インスタンス変数 value に HelloWorld がセットされる)
@[14](インスタンス変数 value の値を取得)
@[9-10,14](インスタンス変数 value の値を取得)
@[15](HelloWorld が 出力される)

---

### 実用的なものを作ろう

---

### お題

ファーストフードのレジシステムをクラスを使用して作ってみる
---

### 必要な機能

- メニューを登録 |
- 注文を登録 |
- 注文を確認 |
- 注文の合計金額を確認 |
- お金を受領しよう |
- お釣りを確認しよう |
- 領収書を発行 |

---

### 必要な機能に名前を付ける

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

### クラスを作成してみる

---

```python
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
```
@[2,4,7,10,13,16,19](日本語名)
@[1,3,6,9,12,15,18](英語名)
@[5,8,11,14,17,20](pass：なにもしない)
@[1-20](これだけでクラスができちゃう)

---

### 利用想定

```python
menu_dict = {'コーラー': 100, 'ハンバーガー': 110, 'ポテト': 100}
macdonald = FastFoodSystem()
macdonald.set_menu(menu_dict)
macdonald.set_order('ハンバーガー')
macdonald.set_order('ポテト')
macdonald.set_order('コーラー')
macdonald.get_order()        # ['ハンバーガー', 'ポテト', 'コーラー']
macdonald.get_total_price()  # 310
macdonald.set_deposit(500)
macdonald.get_change()       # 190
macdonald.get_receipt()      # {'change': 190,
                             #  'deposit': 500,
                             #  'order_list': ['ハンバーガー', 'ポテト', 'コーラー'],
                             #  'total_price': 310}

```
### では実際に肉付けしてみよう٩(ˊᗜˋ*)و 

ここにソースがあるよ！
https://raw.githubusercontent.com/mykysyk/slide-python-class/master/vanilla.py 

---

### 実例

https://github.com/mykysyk/slide-python-class/blob/master/fastfoodsystem.py

---

### おわり
