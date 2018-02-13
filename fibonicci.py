startGame=7
print("------------- Welcome to Fibonicci Game!! --------------------")
print("a player is not allowed to take all the coins!! THE PLAAYER WHO TAKES THE LAST COIN WINS" )
x=int(input("To start the game choice 1 or 2, please"))
if x==1:
	move1=int(input("player1 MOVE UP,choice at least one, but NOT all the coins"))

	while True:
		if(move1>6 or move1<1):
			print("error!!! try againg latter!")
			break
		else:
			startGame=startGame-move1
			if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")
					break
			if(startGame==0):
					print("Game is over------- the palyer1 is win")
					break
			print("remainig the game is ",startGame)
		move2=int(input("player2,Choice at least one, but NOT more than double the previews move: "))

		if(move2>move1*2):
				print("error!!! try againg latter!")
				break
		else:
			startGame=startGame-move2
			if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")		
					break
			if(startGame==0):
					print("Game is over------- the palyer2 is win")
					break
			print("remaining the game is ",startGame)
		move1=int(input("player1,Choice at least one, but NOT more than double the previews move: "))

		if(move1>move2*2):
				print("error!!! try againg latter!")
				break
		else:
			startGame=startGame-move1
			if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")
					break
			if(startGame==0):
					print("Game is over------- the palyer1 is win")
					break
			print("remainig the game is ",startGame)
elif x==2:
	move2=int(input("player2 MOVE UP,choice at least one, but NOT all the coins"))	
	while startGame>0:
			if(move2>6 or move2<1):
				print("error!!! try againg latter!")
				break
			else:
				startGame=startGame-move2
				if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")
					break
			if(startGame==0):
					print("Game is over------- the palyer2 is win")
					break
			print("remainig the coins are ",startGame)
			move1=int(input("player1,Choice at least one, but NOT more than double the previews move: "))

			if(move1>move2*2):
				print("error!!! try againg latter!")
				break
			else:
				startGame=startGame-move1
			if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")		
					break
			if(startGame==0):
					print("Game is over------- the palyer1 is win")
					break
			print("remaining the game is ",startGame)
			move2=int(input("player2,Choice at least one, but NOT more than double the previews move: "))

			if(move2>move2*2):
				print("error!!! try againg latter!")
				break
			else:
				startGame=startGame-move2
				if(startGame<0):
					print("Error!!,you are not allowed to enter more than the remaining coins")
					break
				if(startGame==0):
					print("Game is over------- the palyer2 is win")
					break
				print("remainig the game is ",startGame)
else:
	print("You can choice only 1 or 2 ")
	
	

