from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("87.16.33.144")
server.start()
gui = ServerGui(server)
gui.run()
