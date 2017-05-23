#_*_coding:utf8_*_
#场景：打印分数，【0-60）不及格，[60-70)一般，[70-80）良好，[80-90）优良，[90-100]优秀。
score = raw_input('Please input your score: ')
score = int(score)
if score < 60 :
    print "you are bujige"
elif score < 70:
    print "you are just soso"
elif score < 80:
    print "You are good"
elif score < 90:
    print "You are well"
else:
    print "You are perfect"