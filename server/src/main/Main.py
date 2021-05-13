from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("79.43.58.243")
server.start()
gui = ServerGui(server)
gui.run()
