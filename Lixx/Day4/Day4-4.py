"""
猜数字游戏

Version: 0.1
Author: Lixx
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('答对了')
        break
print('猜了%d次' % counter)
if counter > 7:
    print('你太笨了')