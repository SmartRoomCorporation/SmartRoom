from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("80.116.203.153")
server.start()
gui = ServerGui(server)
gui.run()
