"""
Sample script to test ad-hoc scanning by table drive.
This accepts term,test and long
NOTE: not suitable for longest/optional matches
"""

def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None
	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" scans `text` while transitions exist in
	'transition_table'. After that, if in a state belonging to
	`accept_states`, it returns the corresponding token, else ERROR.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if c in transition_table[state]:
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
			# check if new state is accepting
			if state in accept_states:
				return accept_states[state],pos

			
		else:	# no transition found
			return 'ERROR',pos
			
	
# the transition table, as a dictionary
td = { 's0':{ '0':'s1','1':'s1','2': 's2','3': 's3','4': 's3','5': 's3','6': 's3','7': 's3','8': 's3','9':'s3' },
       's1':{ '0':'s4','1':'s4','2':'s4','3':'s4','4':'s4','5':'s4','6':'s4','7':'s4','8':'s4','9':'s4' },
       's2':{ '0':'s6','1':'s6','2':'s6','3':'s6' },
       's3':{ ':': 's5','.': 's5'},
       's4':{ ':': 's5','.': 's5' },
       's5':{ '0':'s7','1':'s7','2':'s7','3':'s7','4':'s7','5':'s7' },
       's6':{ ':': 's5','.': 's5' },
       's7':{ '0':'s8f','1':'s8f','2':'s8f','3':'s8f','4':'s8f','5':'s8f','6':'s8f','7':'s8f','8':'s8f','9':'s8f' },
     } 

# the dictionary of accepting states and their
# corresponding token
ad = { 's8f':'TIME_TOKEN'
     }


# get a string from input
words = input('give some input>')

# scan text until no more input
while len(words)>0:
	# get next token and position after last char recognized
	tok,pos = scan(words,td,ad)
	if tok=='ERROR':
		print('unrecognized input at pos',pos,'of',words)
		break
	print("token:",tok,"text:",words[:pos])
	# new text for next scan
	words = words[pos:]

