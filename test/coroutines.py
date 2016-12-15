'''
Created on 2016年12月15日

@author: Administrator
'''

#n = yield r    //yield,放弃本函数的执行，同时把r的值返回给调用者send()。 n的值就是send(n)的参数值

#r = c.send(n)    //r的值就是yield的参数值。
def consumer():
    r = ''
    while True:
        print(r)
        n = yield r
        print(n)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    r = c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


def xxx():
    print('bai wei')
    m = yield 5
    print(m)
    d = yield 12
    print('reach here ')
