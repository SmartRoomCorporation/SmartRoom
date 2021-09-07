from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("79.12.248.28")
server.start()
gui = ServerGui(server)
gui.run()
