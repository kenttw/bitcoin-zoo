from bitcoin import *

###

addr = '1JyQgHmsqVN9BvDJz9MZPhEJeK9byJQFhy'
h = history(addr)
priv = 'L45dFVfjzPh1gSYks7f3TPegsx1mresgdidFYxfkY18JKUefiVTp'
outs = [{'value': 1000, 'address': '1J15a53ecfH9dwYnzxhK3EEWyhbK6G9JZX'}]
tx = mktx(h,outs)
print tx
tx2 = sign(tx,0,priv)
# tx3 = sign(tx2,1,priv)
pushtx(tx2) 