### Pythonでクラスを書こう

2020年2月20日

---

### 公式ドキュメント

#### 9. クラス — Python 3.8.2rc1 ドキュメント

https://docs.python.org/ja/3/tutorial/classes.html

- クラスはデータと機能を組み合わせる方法を提供します。 
新規にクラスを作成することで、新しいオブジェクトの 型 を作成し、その型を持つ新しい インスタンス が作れます。 
クラスのそれぞれのインスタンスは自身の状態を保持する属性を持てます。 
クラスのインスタンスは、その状態を変更するための (そのクラスが定義する) メソッドも持てます。

---

### 簡単なクラスを書いてみる

---

### 値を入出力するだけのクラス

```python
class ClassName:

    def __init__(self):
        self.value = None

    def set(self, value):
        self.value = value

    def get(self):
        result = '!!'
        return self.value + result
```

@[1](クラス名)
@[1](「class」に続けてクラスの名前を記述します)
@[3,6,9](メソッド)
@[3,6,9](「def」に続けてメソッド名を記述します)
@[3,6,9](メソッドはクラスに対して操作を定義します)
@[3,6,9](第一引数に必ず「self」を記述します)
@[6](メソッドに引数が欲しいときは第二引数に明記します)
@[4,7,11](インスタンス変数)
@[4,7,11](必ず変数名の前に「self.」を記述します)
@[4,7,11](クラス内で共通利用する変数になります)
@[10](「self.」がつかない変数のスコープはそのメソッド内のみとなります)
@[1-11]()

---

### じゃー実際どうやってそのクラスを使うのか

---

### クラスの使用方法

```python
class ClassName:

    def __init__(self):
        self.value = None

    def set(self, value):
        self.value = value

    def get(self):
        result = '!!'
        return self.value + result

instance_name = ClassName()
instance_name.set('HelloWorld')
value = instance_name.get()
print(value)
```
@[1-11](先ほど作成したクラス)
@[13-16](クラスを呼び出して使う側)
@[13](クラスのインスタンスを生成)
@[1-4,13](クラス側ではこちらにあたります)
@[14](instance_name.set に HelloWorld を渡すと)
@[6-7,14](setメソッドの第二引数 value に HelloWorld がセットされ)
@[6-7,14](self.value に HelloWorld がセットされます)
@[15](instance_name.get を使うと)
@[9-11,15](クラス側ではこちらが実行され)
@[9-11,15](self.value と result が結合され)
@[9-11,15](「HelloWorld!!」 を返します)
@[16](「HelloWorld！！」 が 出力される)
@[1-16]()

---

### もうすこし複雑なクラスを作る

---

### お題

ファーストフードのレジシステム

---

### レジシステムに必要な機能

- メニューを登録 |
- 注文を登録 |
- 注文を確認 |
- 注文の合計金額を確認 |
- お金を受領しよう |
- お釣りを確認しよう |
- 領収書を発行 |

---

### クラス名/メソッド名を命名する

pythonの命名規則に従い名前をつけてみよう

https://pep8-ja.readthedocs.io/ja/latest/

---

|システム名/機能名       |クラス名/メソッド名|
|--                   |-- |--- |
| ファーストフードレジシステム |  | 
| メニューを登録          |  |
| 注文を登録            |  |
| 注文を確認            |  |
| 注文の合計金額を確認    |  |
| お金を受領しよう        |  |
| お釣りを確認しよう       |  |
| 領収書を発行          |  |
---

|システム名/機能名       |クラス名/メソッド名|
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

### クラスを作成

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
@[2,4,7,10,13,16,19](機能名はコメントに利用)
@[1,3,6,9,12,15,18](クラス名とメソッドを設置)
@[5,8,11,14,17,20,23](ちなみに pass はコードとしては何も実行したくない場合のプレースホルダです)
@[1-20](これだけでなにもしないクラスが完成)
@[1-20](pass 部分を書き換えることで目的にあったクラスが完成する)

---

このプログラムが実行できたらOK

```python
macdonald = FastFoodSystem()
macdonald.set_menu({'コーラー': 100, 'ハンバーガー': 110, 'ポテト': 100})
macdonald.set_order('ハンバーガー')
macdonald.set_order('ポテト')
macdonald.set_order('コーラー')
macdonald.set_order('モスバーガー')
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
```

---

### では実際にメソッド内に手を加えてみよう٩(ˊᗜˋ*)و 

ここにソースがあるよ！
https://raw.githubusercontent.com/mykysyk/slide-python-class/master/vanilla.py 

---

### 実例

https://github.com/mykysyk/slide-python-class/blob/master/fastfoodsystem.py

---

### おわり
