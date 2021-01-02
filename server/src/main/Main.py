from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("87.7.152.200")
server.start()
gui = ServerGui(server)
gui.run()
