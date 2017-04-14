import sys
import pickle
import pprint
from person import Person



##########################################
###   MARY WORKS, MARGAREET DOES NOT   ###
##########################################


if __name__ == '__main__':
	margaret = Person('Margaret')
	margaret.myMessages = margaret.messagesDict['Margaret']
	margaret.otherMessages = margaret.messagesDict['Mary']

	if len(sys.argv) == 2:
		if sys.argv[1] == 'ls':
			# Print the message log
			margaret.printMessageLog()
		else:
			try:
				if sys.argv[1] == 'delete':
					for index, msg in enumerate(margaret.messagesDict['Margaret']):
						print(' -' + str(index) + ': ' + msg)
					user_input = input(" > Which one?\n > ")
					del margaret.messagesDict['Margaret'][int(user_input)]
				elif sys.argv[1] == 'add':
					# Get user's new message and extend dictionary with it
					user_input = input(" > What do you want to say?\n > ")
					margaret.messagesDict['Margaret'].extend([str(user_input)])

					margaret.myMessages = margaret.messagesDict['Margaret']

					print("--------  Message Log --------")
					margaret.printMessageLog()
				else:
					print(' > "{}" command not found.'.format(sys.argv[1]))
				# Serialize any changes that were made above to the persistant file (messages.pkl)
				margaret.serialize()
			except:
				pass

	elif len(sys.argv) == 1:
		margaret.printMessageLog()
	else:
		print("Too many arguments!")
		