# -*- coding: utf-8 -*-
"""python_basic_13

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wQIPYtS03yrJTKK9cd5CzchCF852NRjV
"""


#13章課題
#商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
#第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。

def amount(price,ctax):

    total = price + (price * ctax * 0.01)

    return total

print(amount(1200,10))