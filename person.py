import pickle
import sys


class Person:
	def __init__(self, name):
		'''
		When a margaret is created, serialize and store the messages
		into self.messagesDict

		'''
		self.name = name
		self.messagesDict = dict()
		self.myMessages = list()
		self.otherMessages = list()
		# Reads dictionary object
		self.deserialize()


	def printMyMessages(self):
		print(self.myMessages)
		return self.myMessages

	def serialize(self):
		with open('messages.pkl', 'wb')	as writer:
			pickle.dump(self.messagesDict, writer)

	def deserialize(self):
		with open('messages.pkl', 'rb') as reader:
			data = pickle.load(reader)
			self.messagesDict = data
			return self.messagesDict

	def printMessageLog(self):
		# Get highest number of messages from a single user
		max_length = len(self.myMessages)
		if(len(self.otherMessages) > max_length):
			max_length = len(self.otherMessages)

		for i in range(0, max_length):
			try:
				print("({}) MARY     -->  {}".format(i, self.myMessages[i]))
			except:
				print("     MARY     -->  __NO RESPONSE__")
				pass
			try:
				print("    MARGARET -->  {}".format(self.otherMessages[i]))
			except:
				print("    MARGARET -->  __NO RESPONSE__")
				pass
