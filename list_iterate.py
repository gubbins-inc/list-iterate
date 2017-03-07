# -*- coding: cp1252 -*-
import time

def dict_something(d):
    stack = d.items()
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(v.iteritems())
        else:
            do_something(v)
    return
    

def do_something(x):
    if x is not None:
        if str(type(x)) == "<type 'list'>":
            for xx in x:
                do_something(xx)
        elif str(type(x)) == "<type 'dict'>":
            dict_something(x)
        elif str(type(x)) == "<type 'str'>" or str(type(x)) == "<type 'float'>" or str(type(x)) == "<type 'int'>":
            print x
        else:
            print type(x)
        time.sleep(0.2)
    else:
        pass
    return

    
def sprint (listy):
    if str(type(listy)) == "<type 'list'>":
        for x in listy:
            do_something(x)
    elif str(type(listy)) == "<type 'dict'>":
        dict_something(listy)
    elif str(type(listy)) == "<type 'str'>":
        print (listy)
    return

rand = {'£':'$', '$':'£', 'aa':'22', 'rr':'ii', '44':'55', 'tt':'88', }
val = {'thing1':'thing2', 'hi':'ho','gosh':{'golly':'goodness', 'blimey':[1, 2, 3, [3.5, 3.6, 3.7, rand, 3.8], 5, 6]}, 'easy':'peasy'}
jk = [0.123, 0.44, 0.55, 1.4, 6]
ppp = [val, val['thing1'], jk]
mv = ['item 1', 'item2', 6, 1, ppp, 2, 44]
t = ['patient zero', val.get('gosh', {}).get('blimey'), 'object x']
listy = [t, 1, None, None, mv, None, 2, 3, None, "gubbins", val['thing1']]
#listy = "gotcha"


sprint(listy)

