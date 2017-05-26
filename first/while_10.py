#_*_coding:utf8_*_
#场景：让用户输入年份，输入quit时退出，判断是否是闰年，告知用户

year = None
while True:
    year = raw_input('Please input the year you want: ')
    try:
        if int(year) % 4 == 0 and int(year) % 100 != 0:
            print year + ' is 闰年'
        elif int(year) % 400 == 0:
            print year + ' is 闰年'
        else:
            print year + ' is not 闰年'
    except:
        try:
            if year == "quit":
                break
        except:
            continue
        print "Wrong , Please input num"


