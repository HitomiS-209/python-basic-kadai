# -*- coding: utf-8 -*-
"""python_basic_15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lzu2PG_gE-pOwYI-DCIAIJPdL6F7ZDLC
"""


class Human:
    #コンストラクタを定義する
    def __init__(self,name,age):
      self.name = name
      self.age = age

    #メソッドを定義する
    def set_name(self, name):
      self.name = name

    def printinfo(self):
      print(self.name)

#インスタンス化する
human = Human("侍太郎", "36")

#属性にアクセスし、値を出力する
print(human.name)
print(human.age)