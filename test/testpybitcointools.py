from bitcoin import *

###

addr = '129SGWJUFZymU7gVHZ1R2RWQaP58HTKvJ3'
h = history(addr)
priv = 'L4hXB87fhsfh686kuxq5T2HNSpkeYWmZVnn3BNWm73oUm8CZXaJG'
outs = [{'value': 1000, 'address': '1DKAa3hzeM47U3RcuafZkZNJQdm78NgFyW'}]
tx = mktx(h,outs)
print tx
tx2 = sign(tx,0,priv)
# tx3 = sign(tx2,1,priv)
pushtx(tx2) 