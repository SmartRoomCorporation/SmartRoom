from Server import SmartroomServer
from ServerGui.ServerGui import ServerGui

server = SmartroomServer()
server.setIp("95.239.24.91")
server.start()
gui = ServerGui(server)
gui.run()
