from bitcoin import *

random_keys = [ random_key() for i in range(3)]
pubs = [ privtopub(priv) for priv in random_keys ]
# addrs = [ pubtoaddr(pub) for pub in pubs ]
script = mk_multisig_script(pubs, 2, 3) # 2 0f 3 multisig script
tx_address = scriptaddr(script)
print tx_address
h = history(tx_address)
print h