# zerosensor httpd server
# http://nwgat.ninja

# simple httpd server that serves files in folder
# http://stackoverflow.com/questions/8234266/8675236#8675236

import SimpleHTTPServer
import SocketServer
import os
import commands

port = 9000

os.chdir(os.path.join(os.path.abspath(os.curdir),'html'))
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", port), Handler)
myip = commands.getoutput("hostname -I")

print "### Zerosensor ###"
print "http://" + myip, port

httpd.serve_forever()
