import httplib2
from bitcoinrpc.authproxy import AuthServiceProxy
access = AuthServiceProxy('http://bitcoinrpc:4RJsy6z8X8F6xA7SpksrasYvKtBcFZYhLwiFpRtc541x@etukent.ddns.net:8338')
try:
        blockCount = access.getblockcount()
except Exception as e:
        print "Problems connecting to bitcoin wallet:"
else:
        try:
                response, trueBlockCount = httplib2.Http().request("http://blockexplorer.com/q/getblockcount/")
        except Exception as e:
                print "Unable to get true blockcount from blockexplorer:"+str(e)
        else:
                if (int(trueBlockCount) - 5) > blockCount :
                        print "blockchain not up to date: true block count is: "+str(trueBlockCount)+", while bitcoind is at: "+str(blockCount)
                else :
                        print "Sync Completed Total Black Count:" , blockCount