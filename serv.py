from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver

class Chat(LineOnlyReceiver):

	name_client=""

	def getClientName(self):
		if self.name_client!="":
			return self.name_client
		return self.transport.getPeer().host

	def MadeConnection(self):
		print("New client from" + self.getClientName())
		self.sendLine("Welcome, client! You are user of my chat")
		self.factory.sendMessageToAllClients(self.getClientName() + "has joined")
		self.factory.clientProtocols.append(self)
		self.sendLine("Send me '/EXIT' if you want to exit") 

	def LostConnection(self, reason):
		print("Connection was lost from client" + self.getClientName)
		self.factory.clientProtocols.remove(self)
		self.factory.sendMessageToAllClients(self.getClientName() + "has disconnected")

	def ReceivedLine(self, line):
		print(self.getClientName() + "said: " + line)
		if line == "/EXIT/":
			self.transport.LostConnection()
		else:
			self.factory.sendMessageToAllClients(self.getClientName() + "says: " + line)

	def sendLine(self, line):
		self.transport.write(line+ "\r\n")

class ChatFactory(ServerFactory):
	protocol = Chat

	def __init__(self):
		self.clientProtocols= []

	def sendMessageToAllClients(self, message):
		for client in self.clientProtocols:
			client.sendLine(message)

print("Server is starting!")
factory = ChatFactory()
reactor.listenTCP(8080, factory)



