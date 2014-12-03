from bitcoin import *

###

addr = '13g6Nx6BekMhirerj1VdJeqegQdUVcVxgi'
h = history(addr)
priv = 'L2ERERJmMcM8USz1ziNnYGZDn8S8SgBPfm3mZ5ZV5qGSo2WTTSq8'
outs = [{'value': 1000, 'address': '1JyQgHmsqVN9BvDJz9MZPhEJeK9byJQFhy'}]
tx = mktx(h,outs)
print tx
tx2 = sign(tx,0,priv)
# tx3 = sign(tx2,1,priv)
pushtx(tx2) 