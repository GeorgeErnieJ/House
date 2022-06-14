#Proof of concept for an exploration game

def init():
	player_location = 7
	#matrix in form [[[0location + connectors], [1name], [2name pointer], [3locked flag], [4story_flag]], [another one]]
	location_matrix = [
[[0, 5], ['Attic', 'Attic [out of reach]', 'Attic [opened]'], [0], [1], [0]],
[[1, 10], ['Cellar', 'Cellar [rusted]', 'Cellar [open]'], [0], [1], [0]],
[[2, 5], ['Master Bedroom', 'Master Bedroom [locked]', 'Master Bedroom [unlocked]'], [0], [1], [0]],
[[3, 5], ['Bedroom'], [0], [0], [0]],
[[4, 5], ['Bathroom'], [0], [0], [0]],
[[5, 2, 3, 4, 0, 9], ['Upper Floor'], [0], [0], [0]],
[[6, 9], ['Living Room'], [0], [0], [0]],
[[7, 8, 9], ['Dining Room'], [0], [0], [0]],
[[8, 7, 9], ['Kitchen'], [0], [0], [0]],
[[9, 11, 6, 7, 8, 5, 10], ['Ground Floor'], [0], [0], [0]],
[[10, 1, 9], ['Basement'], [0], [0], [0]],
[[11], ['Front Door', 'Front Door [locked]', 'Front Door [unlocked]'], [0], [1], [0]]]
	
	#careful with this bit
	look_matrix = [
['Attic', '\nThe attic is covered in dust.\nThere are all sorts of relics up here.\n'],
['Cellar', '\nThe cellar smells dank.\nThere is a little window letting in a small ammount of light.\n'],
['Master Bedroom', '\nThis room smells bad... Looks fancy though.\n'],
['Bedroom', '\nLooks like a typical bedroom...\n Not much else to say.\n'],
['Bathroom', '\nIt\'s a bit cramped in here... \nThe walls are made of white tiles. \nWell, used to be white, anyway.\n'],
['Upper Floor', '\nThis is the upper floor of the house. The bannistair is pretty fancy.\n'],
['Living Room', '\nThis room is very ornate, looks like someone rich lives here.\nStrange... The fire is on, and candles are lit.\nAm I alone?\n'],
['Dining Room', '\nBig oak table, silver cutlery... fancy.\n'],
['Kitchen', '\nFairly large kitchen, huge work surfaces. \n'],
['Ground Floor', '\nThe ground floor is quite long and thin.\nThere are stairs leading up, and down.\n'],
['Basement', '\nThis place is pretty dark and cramped.\n'],
['Front Door', '\nYou shouldn\'t be reading this.\n']]

	item_matrix = [
[[1], ['Oil'], ['\nThe label reads "DW-50: Rust Remover". Hmm...\n']],
[[2], ['House Key'], ['\nYes! This is my ticket out of here!\n']],
[[3], ['Newspaper'], ['\nThis is from a few days ago, I\'ve already read it.\nNothing really interesting.\n']],
[[4], ['Knife'], ['\nA very thin ornate silver knife.\n']],
[[5], ['Meat Hook'], ['\nThis thing is huge!\n Why would this be in a kitchen?\n']],
[[6], ['Bucket'], ['\nQuite a large bucket.\n']],
[[7], ['Bucket With Water'], ['\nExactly what it says on the tin.\n']],
[[8], ['Key'], ['\nThis key is small, and looks special.\n']],
[[9], ['Kinky Rope'], ['\nOooh, lovely and silky.\n Just holding it is giving me naughty thoughts.\n']],
[[10], ['Makeshift Grappling Hook'], ['\nThis will help me hook onto things I can\'t reach.\n']],
[[11], ['Valve Tool'], ['\nThis looks important... but looks brittle.\n']]]

	player_inv = []

	burning = [[0], [0]]

	investigate_matrix = [
['Attic', [
[[0], ['Shelves'], [0], [0], [
'\nThe shelves house an array of trinkets and other items... Nothing of use here.\n']],
[[1], ['Toolbox', 'Toolbox [empty]'], [0], [1], [
'\nThis is a standard red toolbox. You pick up some oil.\n',
'\nThe toolbox is empty, save for a few rusty nails.\n']],
[[2], ['Crates', 'Crates [empty]'], [0], [11], [
'\nLooks like junk storage...\nMaybe this will come in handy.\n[You take a valve tool from the crate]\n',
 '\nThe crate has nothing left of use.\n']],
[[3], ['Junk'], [0], [0], [
'\nOld broken bike, old desktop towers... even a broken fish tank enscribed "Vladolf Pitler".\n']],
[[4], ['Hatch'], [0], [0], [
'\nThis is the way back down to the upper floor.\n']]]],
['Cellar', [
[[5], ['Barrels'], [0], [0], [
'\nThe barrels have pictures of grapes on them.\n Probably wine inside.\n']],
[[6], ['Cannisters'], [0], [0], [
'\nLooks like cannisters of gas to power the fireplace upstairs.\nOne has a valve on it connected to a pipe.\n']],
[[7], ['Gas valve', 'Gas valve [on]', 'Gas valve [off]'], [0], [0], [
'\nThe valve is in the on position.\n',
'\nThe valve is in the on position.\n',
'\nI turned this off earlier. Theres no way to turn it back on.\n']],
[[8], ['Wine Rack'], [0], [0], [
'\nThis wine was what I used to drink when I was an alcoholic. I\'m not going to drink it.\n']],
[[9], ['Door to basement'], [0], [0], [
'\nThis is the way back to the basement staircase.\n']]]],
['Master Bedroom', [
[[10], ['Double Bed'], [0], [0], [
'\nTheres a body here... \nI think he locked himself in and died in his sleep.\n']],
[[11], ['Desk'], [0], [0], [
'\nThe desk is covered in useless documents.\n']],
[[12], ['Bedside table'], [0], [0], [
'\nThere are a few books and a desk lamp here.\nSome of the titles here are just... Lovely.\n']],
[[13], ['Trinket Box [locked]', 'Trinket Box [empty]'], [0], [0], [
'\nThis box looks important, but it\'s locked.',
'\nI got the house key from here!']],
[[14], ['Wardrobe'], [0], [0], [
'\nThis one is full of old person clothes.\n']],
[[15], ['Door to hallway'], [0], [0], [
'\nThis door takes you back to the upper floor\n']]]],
['Bedroom', [
[[16], ['Single Bed'], [0], [0], [
'\nThis bed looks pretty girly, with pink floral bedsheets.\n']],
[[17], ['Small Desk'], [0], [0], [
'\nThe desk is completely clear of clutter.\nWhoever owns this room obviously has OCD.\n']],
[[18], ['Wardrobe', 'Wardrobe [empty]'], [0], [9], [
'\nHey hey hey! Looks like whoever lives in this room likes BDSM. \nThis wardrobe is full of bondage gear!\nI won\'t take anything that\'s been used... But there is some rope that\'s in fresh packaging.\n',
'\nVery kinky.\n']],
[[19], ['Shelves'], [0], [0], [
'\nThe shelves have lots of toy dolls sitting on them in odd positions. \nOne is even missing it\'s head.\n']],
[[20], ['Door'], [0], [0], [
'\nThis takes me out of the room.\n']]]],
['Bathroom', [
[[21], ['Sink'], [0], [0], [
'\nA small sink. It is stained.\nIn fact, this is probably the smallest sink I have ever seen.\n']],
[[22], ['Bathtub'], [0], [0], [
'At least the bath looks cleaner.\n There is water dripping from the tap.\n']],
[[23], ['Cupboard', 'Cupboard [empty]'], [0], [6], [
'\nThere is your usual assortment of cleaning products here.\nI think this bucket will come in handy.\n',
'\nI\'ll come back for the bleach if I can\'t escape and need an easy out.\n']],
[[24], ['Toilet'], [0], [0], [
'\nYou sit on the toilet and try to strain out a shit.\nTo your dismay, nothing but a sad fart escapes.\n']],
[[25], ['Door'], [0], [0], [
'\nDoor to the upper floor\n']]]],
['Upper Floor', [
[[26], ['Attic Hatch', 'Attic Hatch'], [0], [0], [
'\nThat looks like the way to the attic, but I can\'t reach it...\n', 
'\nAttic hatch is open.\n']],
[[27], ['Master Bedroom Door', 'Master Bedroom Door', 'Master Bedroom Door'], [0], [0], [
'\nLook\'s like it\'s locked.\n Looking inside the keyhole, it appears the key is in the door on the other side...\nThat\'s strange, how did it get there?\n',
'\nI just slid some newspaper under there.\nStill need a way to get that key though...\n',
'\nThe door is unlocked now.\n']],
[[28], ['Bedroom Door'], [0], [0], [
'\nJust a plain door.\n']],
[[29], ['Bathroom Door'], [0], [0], [
'\nThere\'s a sign on the door: "Toxic Waste Zone". Heh.\n']],
[[30], ['Stairs To Ground Floor'], [0], [0], [
'\nThese stairs take me downstairs.\n']],
[[31], ['Window'], [0], [0], [
'\nThis window overlooks the front of the house.\nIt\'s dark outside, I can\'t see too much.\n']]]],
['Living Room', [
[[32], ['Coffee Table', 'Coffee Table'], [0], [3], [
'\nThere is a fancy candle lit coffee table here. \nThere is a newspaper on it, might be useful to read if I need a shit.\n',
'\nThis is a fancy candle lit coffee table.\n']],
[[33], ['Fireplace', 'Fireplace [off, hot]', 'Fireplace [off]', 'fireplace [off]'], [0], [0], [
'\nLooks like a gas fireplace. There is a roaring fire at the moment.\n', '\nWell, the fire is off, but this thing is still piping hot.\nThere is a fancy looking key at the back.\n', '\nIt\'s not hot anymore, but a bit wet.\n', '\nIt\'s not hot anymore, but a bit wet.\n', ]],
[[34], ['Armchair'], [0], [0], [
'\nThis is really quite comfortable, actually.\n']],
[[35], ['Door'], [0], [0], [
'\nYes. This is definitely a door.\n']],
[[36], ['Mirror'], [0], [0], [
'\nThis mirror takes up most of the wall.\n You see an ugly person in it, staring back at you.\n']]]],
['Dining Room', [
[[37], ['Dining Table', 'Dining Table'], [0], [4], [
'\nThis is one fancy dining table... I want to take this knife with me for self defence.\n',
'\nYou have already taken the knife.\n']],
[[38], ['Dining Chairs'], [0], [0], [
'\nVery decorative chairs. I woke up on one of these.\n']],
[[39], ['Double Doors to kitchen'], [0], [0], [
'\nYep, that\'s a kitchen alright.\n']],
[[40], ['Door to Hallway'], [0], [0], [
'\nIt\'s just a plain door.\n']],
[[41], ['Painting'], [0], [0], [
'\nThis is a painting of...\nWait, what is he doing with that banana?!?\n']]]],
['Kitchen', [
[[42], ['Window to garden'], [0], [0], [
'\nI can just make out a shed and a pen... looks like this house keeps pigs.\nThat would explain the meat hook on the counter.\n']],
[[43], ['Counter', 'Counter'], [0], [5], [
'\nThere are cleavers and meat hooks on here... spooky.\nA meat hook looks like it might be useful.\n',
'\nThere\'s lots of room now that I have taken the meat hook.\n']],
[[44], ['Door to dining room'], [0], [0], [
'\nThis takes be back to the dining room.\n']],
[[45], ['Door to hallway'], [0], [0], [
'\nThis takes me to the hallway.\n']],
[[46], ['Fridge'], [0], [0], [
'Hey, theres a note on the fridge:\n\n"Reminder: Get key from behind fireplace.\n          Fix hinges on cellar door."\n hmm...\n']]]],
['Ground Floor', [
[[47], ['Front Door'], [0], [0], [
'\nThis is my way out of the house.\n']],
[[48], ['Door to dining room'], [0], [0], [
'\nThis takes me to the dining room, where I woke up.\n']],
[[49], ['Door to kitchen'], [0], [0], [
'\nThis door takes me to the kitchen.\n']],
[[50], ['Door to Living room'], [0], [0], [
'\nThis door takes me to the living room.\n']],
[[51], ['Stairs up'], [0], [0], [
'\nThese will take me to the upper floor.\n']],
[[52], ['Stairs down'], [0], [0], [
'\nThese will take me to the basement.\n']]]],
['Basement', [
[[53], ['Stairs Up'], [0], [0], [
'\nThese will take me back to the ground floor.\n']],
[[54], ['Door to cellar', 'Door to cellar'], [0], [0], [
'\nThis door is rusted shut!\n', '\nI can just about open and close it now.\n']]]],
['Front Door']]

	drunk = [0]  

	data = [player_location, location_matrix, look_matrix, investigate_matrix, player_inv, item_matrix, burning, drunk]

	return(data)

def look(data):
	print(data[2][data[0]][1])
	return(data)
	
def investigate(data):
	player_location = data[0]
	options = [0]
	string_list = []
	for i in range(len(data[3][player_location][1])):
		options.append(i + 1)
		string_list.append(data[3][player_location][1][i][1][data[3][player_location][1][i][2][0]])
	print('Investigate what?\n')
	for i in range(len(options) - 1):
		print('[' + str(i + 1) + ']        ' + str(string_list[i]))
	print('\n[0]        Never Mind....\n')
	ans = str(input('Answer:	'))
	valid = False
	for item in options:
		if str(item) == ans:
			valid = True
	if valid == False:
		print('Unknown input.')
		print('')
		return(data)
	if valid == True:
		if ans == '0':
			print('')
			return(data)
		if int(ans) > 0:
			print(data[3][player_location][1][int(ans) - 1][4][data[3][player_location][1][int(ans) - 1][2][0]])
			if data[3][player_location][1][int(ans) - 1][0][0] == 33:
				if data[3][player_location][1][int(ans) - 1][2][0] == 2:
					print('You take the key behind the fireplace')
					data[4].append(data[5][7])
					return(data)
				if data[3][player_location][1][int(ans) - 1][2][0] == 3:
					print('You take the key behind the fireplace')
					data[4].append(data[5][7])
					data[6][0][0] = 1
					return(data)
			if data[3][player_location][1][int(ans) - 1][3][0] > 0:
				item = []
				for thing in data[5]:
					if thing[0][0] == data[3][player_location][1][int(ans) - 1][3][0]:
						item.append(thing)
				data[4].append(item[0])
				data[3][player_location][1][int(ans) - 1][3][0] = 0
				data[3][player_location][1][int(ans) - 1][2][0] = 1
				return(data)
			print('')
			return(data)

		

def cont():
	a = input('\nPress enter to continue...\n')

def use(data):
	items = []
	for i in data[4]:
		items.append(i)
	options = [0]
	print('Use what?')
	print('')
	for j in range(len(data[4])):
		options.append(j + 1)
	for k in range(1, len(options)):
		print('[' + str(k) + ']        ' + data[4][k - 1][1][0])
	print('')
	print('[0]        Never mind...\n')
	valid = False
	
	ans = input('Choice:    ')
	for item in options:
		if ans == str(item):
			valid = True
	if valid == False:
		print('Unknown input')
		print('')
		return(data)
	if valid == True:
		if int(ans) == 0:
			return(data)
		if int(ans) > 0:
			item_1 = [0, data[4][int(ans) -1][0][0]]
			valid_2 = False
			options_2 = [0, 1, 2]
			print('Use ' + str(data[4][int(ans) - 1][1][0]) + ' with?')
			print('')
			print('[1]        Environment')
			print('[2]        Inventory\n')
			print('[0]        Never Mind...\n')
			ans2 = input('Choice:    ')
			for item in options_2:
				if str(item) == ans2:
					valid_2 = True
			if valid_2 == False:
				print('Unknown input')
				print('')
				return(data)
			if valid_2 == True:
				if ans2 == '1':
					player_location = data[0]
					options_3 = [0]
					string_list = []
					for i in range(len(data[3][player_location][1])):
						options_3.append(i + 1)
						string_list.append(data[3][player_location][1][i][1][data[3][player_location][1][i][2][0]])
					print('')
					for i in range(len(options_3) - 1):
						print('[' + str(i + 1) + ']    ' + str(string_list[i]))
					print('\n[0]    Never Mind....\n')
					ans3 = str(input('Choice:	'))
					valid = False
					for item in options_3:
						if str(item) == ans3:
							valid = True
					if valid == False:
						print('Unknown input.')
						print('')
						return(data)
					if valid == True:
						if ans3 == '0':
							print('')
							return(data)
						if int(ans3) > 0:
							item_2 = [1, data[3][player_location][1][int(ans3) - 1][0][0]] 
				if ans2 == '2':
						items2 = []
						for i in data[4]:
							items2.append(i)
						options = [0]
						
						print('')
						for j in range(len(data[4])):
							options.append(j + 1)
						for k in range(1, len(options)):
							print('[' + str(k) + ']        ' + data[4][k - 1][1][0])
						print('')
						print('[0]        Never mind...\n')
						valid = False
	
						ans4 = input('Choice:    ')
						for item in options:
							if ans4 == str(item):
								valid = True
						if valid == False:
							print('Unknown input')
							print('')
							return(data)
						if valid == True:
							if int(ans4) == 0:
								return(data)
							if int(ans4) > 0:
								item_2 = [0, data[4][int(ans4) -1][0][0]]
								if item_1[1] == item_2[1]:
									print('Unknown input')
									print('')
									return(data)
				
				if ans2 == '0':
					return(data)
				
				data = use_check(item_1, item_2, data)
				return(data)
					
			
def use_check(item_1, item_2, data):
	if item_1[0] == item_2[0]:
	#hook
		if item_1[1] == 5:
			if item_2[1] == 9:
				print('You combine the kinky rope and the meathook to make a grappling hook')
				val = 0
				for i in range(len(data[4])):
					if data[4][i][0][0] == 5:
						val =  i
				data[4].pop(val)
				val = 0
				for j in range(len(data[4])):
					if data[4][j][0][0] == 9:
						val =  j
				data[4].pop(val)
				data[4].append(data[5][9])
				
				return(data)

		if item_1[1] == 9:
			if item_2[1] == 5:
				print('You combine the kinky rope and the meathook to make a grappling hook')
				val = 0
				for i in range(len(data[4])):
					if data[4][i][0][0] == 5:
						val =  i
				data[4].pop(val)
				val = 0
				for j in range(len(data[4])):
					if data[4][j][0][0] == 9:
						val =  j
				data[4].pop(val)
				data[4].append(data[5][9])
				
				return(data)
	if item_1[0] != item_2[0]:
	#oil
		if item_1[1] == 1:
			if item_2[1] == 54:
				print('You use the oil on the rusty hinges. The door seems to be looser now.')
				data[1][1][2][0] = 2
				data[1][1][3][0] = 0
				data[3][10][1][1][2][0] = 1
				return(data)

	#grappling
		if item_1[1] == 10:
			if item_2[1] == 26:
				print('You throw the hook and manage to open the hatch')
				data[1][0][2][0] = 2
				data[1][0][3][0] = 0
				data[3][5][1][0][2][0] = 1
				return(data)

	#gas valve
		if item_1[1] == 11:
			if item_2[1] == 7:
				print('Meh, you turn the valve off... but the tool breaks')
				data[3][1][1][2][2][0] = 1
				data[3][6][1][1][2][0] = 1
				val = 0
				for i in range(len(data[4])):
					if data[4][i][0][0] == 11:
						val =  i
				data[4].pop(val)
				
				
				return(data)

	#mbedroom1
		if item_1[1] == 3:
			if item_2[1] == 27:
				if data[3][5][1][1][2][0] == 0:
					print('You slip the newspaper under the door')
					data[3][5][1][1][2][0] = 1
					val = 0
					for i in range(len(data[4])):
						if data[4][i][0][0] == 3:
							val =  i
					data[4].pop(val)
					return(data)

	#mbedroom2
		if item_1[1] == 4:
			if item_2[1] == 27:
				if data[3][5][1][1][2][0] == 1:
					print('You poke the key out of the keyhole with the knife, and catch it on the newspaper.\n You retrieve the key and open the door')
					data[3][5][1][1][2][0] = 2
					val = 0
					for i in range(len(data[4])):
						if data[4][i][0][0] == 4:
							val =  i
					data[4].pop(val)
					data[1][2][2][0] = 2
					data[1][2][3][0] = 0
					return(data)


	#bucket
		if item_1[1] == 6:
			if item_2[1] == 22:
				print('You fill the bucket with water from the tap in the bathtub')
				data[4].append(data[5][6])
				val = 0
				for i in range(len(data[4])):
					if data[4][i][0][0] == 6:
						val =  i
				data[4].pop(val)
				return(data)
	
	#waterbucket
		if item_1[1] == 7:
			if item_2[1] == 33:
				if data[3][6][1][1][2][0] == 1:
					data[3][6][1][1][2][0] = 2
					print('You throw the water into the fireplace to cool it down')
					data[4].append(data[5][5])
					val = 0
					for i in range(len(data[4])):
						if data[4][i][0][0] == 7:
							val =  i
					data[4].pop(val)
					return(data)
				if data[3][6][1][1][2][0] == 0:
					data[3][6][1][1][2][0] = 3
					print('You throw the water into the fireplace to extinguish the fire')
					data[4].append(data[5][5])
					val = 0
					for i in range(len(data[4])):
						if data[4][i][0][0] == 7:
							val =  i
					data[4].pop(val)
					data[6][0][0] = 1
					return(data)

	#Trinket box
		if item_1[1] == 8:
			if item_2[1] == 13:
				print('You open the trinket box, inside is the front door key')
				data[4].append(data[5][1])
				data[3][2][1][3][2][0] = 1
				return(data)

	#house key
		if item_1[1] == 2:
			if item_2[1] == 47:
				print('You unlock the front door, and escape the house')
				victory()
				exit()
				
	print('That doesnt work\n')
	return(data)


def victory():
	print('\nCongratulations! You escaped the house.')
	cont()

def view_inv(data):
	items = []
	for i in data[4]:
		items.append(i[1][0])
	print('You have:')
	print(items)
	print('')
	print('[1]        Use')
	print('[2]        Info')
	print('')
	print('[0]        Never Mind...\n')
	ans = input('Choice:    ')
	options = [0, 1, 2]
	valid = False
	for item in options:
		if ans == str(item):
			valid = True
	if valid == False:
		print('Unknown input')
		print('')
		return(data)
	if valid == True:
		if ans == '1':
			data = use(data)
			return(data)
		if ans == '2':
			options2 = [0]
			for j in range(len(data[4])):
				options2.append(j + 1)
			for k in range(1, len(options2)):
				print('[' + str(k) + ']        ' + data[4][k - 1][1][0])
			print('\n[0]        Never Mind...\n')
			ans2 = input('Choice:    ')
			valid = False
			for answer in options2:
				if str(answer) == ans2:
					valid = True
			if valid == True:
				if int(ans2) > 0:
					print(data[4][int(ans2) - 1][2][0])
					return(data)
				if int(ans2) == 0:
					return(data)
			if valid == False:
				print('Unknown input')
				print('')
				return(data)
			
		if ans == '0':
			return(data)
	

def change_location(data):
	player_location = data[0]
	print('Go where?')
	print('')
	options = [0]
	for i in range(1, len(data[1][data[0]][0])):
		print('[' + str(i) + ']		' + str(data[1][data[1][data[0]][0][i]][1][data[1][data[1][data[0]][0][i]][2][0]]))
		options.append(i)
	print('\n[0]		Stay here')
	print('')
	try:
		ans = int(input('Choice:	'))
	except ValueError:
		print('Unknown input.')
		print('')
		return(data)
	flag_legal = False
	for item in options:
		if ans == item:
			flag_legal = True
	if flag_legal == False:
		print('Unknown input.')
		print('')
		return(data)
	if flag_legal == True:
		if ans != 0:
			flag_locked = False
			if data[1][data[1][data[0]][0][ans]][3][0] == 1: 
				flag_locked = True
			if flag_locked == False:
				temp = data[1][data[0]][0][ans] 
				data[0] = temp
				if data[6][0][0] == 1:
					data[6][1][0] += 1
					if data[6][1][0] == 2:
						print('\n\nYou smell gas.\n')
						cont()
					if data[6][1][0] == 3:
						explosion()
						exit()
					
				return(data)
			if flag_locked == True:
				target = data[1][data[1][data[0]][0][ans]][0][0]
				if target == 0:
					print('\nYou cannot reach the attic door.')
					print('')
				else:
					print('\nYou try to open the door, but it doesn\'t budge.') #In the future, change the location matrix to include text about locked.
					print('')
				if data[1][data[1][data[0]][0][ans]][2][0] == 0:
					data[1][data[1][data[0]][0][ans]][2][0] = 1 
				return(data)
		if ans == 0:
			return(data)

def close_game(data):
	print('\nAre you sure you wish to quit?\n\n[2]        No\n[9]        Yes\n\n')
	options = ['2', '9']
	ans = input('Choice:	')
	flag = False
	for item in options:
		if ans == item:
			flag = True
	if flag == False:
		print('Unknown input.\n\n')
		return(data)
	if flag == True:
		if ans == '2':
			print('\n\n')
			return(data)
		if ans == '9':
			cont()
			exit()

def explosion():
	print('\n\nYou instantly realise your mistake. The gas from the fireplace ignites on the candle in the room, causing an intense wave of heat as the house bursts into flame in a loud explosion. \n\n You died. \n\n GAME OVER')
	cont()

def options(data):			#Keep updating this
	print('Your options are:')
	print('\n[1]		Look around')
	print('[2]		Investigate')
	print('[3]		Go somewhere else')
	print('[4]		View Inventory')
	print('\n[9]        Exit Gane')
	print('')
	options = [1, 2, 3, 4, 9]
	try:
		ans = int(input('Choice:	'))
	except ValueError:
		print('Unknown input')
		print('')
		return(data)
	flag_correct = False
	for item in options:
		if ans == item:
			flag_correct = True
	if flag_correct == False:
		print('Unknown input')
		print('')
		return(data)
	if flag_correct == True:
		if ans == 1:
			data = look(data)
		if ans == 2:
			data = investigate(data)
		if ans == 3:
			data = change_location(data)
		if ans == 4:
			data = view_inv(data)
		if ans == 9:
			data == close_game(data)
	return(data)
	
def run(data):
	print('You are at: ' + str(data[1][data[0]][1][0]))
	data = options(data)
	run(data)
	
data = init()
print('You wake up with your head on a table... you don\'t remember why you are here, but you need to get out!\n\n')
run(data)

		




