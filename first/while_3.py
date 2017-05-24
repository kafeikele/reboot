#_*_coding:utf8_*_
#场景：我在银行存了10000元，利率是3.33%，多久可以翻一翻
money = 10000
i = 0
while money < 20000:
    money = money * (1 + 0.033)
    i += 1
print i