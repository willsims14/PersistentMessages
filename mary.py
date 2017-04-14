import sys
import pickle
import pprint
from person import Person


##########################################
###   MARY WORKS, MARGAREET DOES NOT   ###
##########################################



if __name__ == '__main__':
	mary = Person('Mary')
	mary.myMessages = mary.messagesDict['Mary']
	mary.otherMessages = mary.messagesDict['Margaret']

	if len(sys.argv) == 2:
		if(sys.argv[1] == 'ls'):
			# Print the message log
			mary.printMessageLog()
		else:
			try:
				if(sys.argv[1] == 'delete'):
					for index, msg in enumerate(mary.messagesDict['Mary']):
						print(' -' + str(index) + ': ' + msg)
					user_input = input(" > Which one?\n > ")
					del mary.messagesDict['Mary'][int(user_input)]
				elif(sys.argv[1] == 'add'):
					# Get user's new message and extend dictionary with it
					user_input = input(" > What do you want to say?\n > ")
					mary.messagesDict['Mary'].extend([str(user_input)])
				else:
					print(' > "{}" command not found.'.format(sys.argv[1]))
				# Serialize any changes that were made above to the persistant file (messages.pkl)
				mary.serialize()
			except:
				pass

	elif len(sys.argv) == 1:
		mary.printMessageLog()
	else:
		print("Too many arguments!")


