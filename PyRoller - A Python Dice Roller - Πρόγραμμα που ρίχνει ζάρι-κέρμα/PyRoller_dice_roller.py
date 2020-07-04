# Πρόγραμμα που ρίχνει ζάρι/κέρμα για επιτραπέζια παιχνίδια ή παιχνίδια ρόλων.
# Δημιουργία: Νίκος-Νικήτας
# PyRoller - Python Dice Roller - Author: Nikos-Nikitas

# οι βιβλιοθήκες που θα χρησιμοποιήσουμε για (ψευδο)τυχαίους αριθμούς, παύση του προγράμματος και καθαρισμό της οθόνης
import random, time, os 

# ελέγχει αν τρέχει το πρόγραμμα
run = True

# το βασικό μενού με τη βασική λειτουργία.
# ξεκινάει καθαρίζοντας την οθόνη, εμφανίζει τον τίτλο του προγράμματος,
# κάνει μια μικρή παύση και ρωτάει τον χρήστη πόσες πλευρές θέλει να έχει το ζάρι που θα ρίξει.
# Πατώντας τον αριθμό 2 ρίχνει κέρμα το οποίο αξιολογείται αν είναι κορώνα ή γράμματα.
# Μπορούμε να ρίξουμε ένα ζάρι με όσες πλευρές θέλουμε αρκεί να είναι στα όρια των αριθμών που αντέχει η Python.

def Main():
	os.system('cls')
	print("*******************************************************")
	print("* Welcome to Nik's PyRoller - the Python Dice Roller! *")
	print("*******************************************************")
	time.sleep(0.6)

	# δέχεται μόνο ακέραιο αριθμό, αλλιώς προειδοποιεί και επιστρέφει.
	try:
		d = int(input("How many sides do you want your dice to have? (HINT: Type 2 for a coin)\n Choice: "))

		if d == 2:
			res = int(random.randint(1,d))
			if res == 1:
				print("The coin is HEADS.")
			else:
				print("The coin is TAILS.")
		else:
			print(random.randint(1,d))
		UsrChoice()
	
	except ValueError:
			time.sleep(0.3)
			print("Insert an integer number only.")
			time.sleep(0.6)
			Main()

# Ρωτάει τον χρήστη αν θέλει να συνεχίσει ξαναρίχνοντας. 
# Αν δεν θέλει, το πρόγραμμα τερματίζει, αλλιώς επαναλαμβάνεται.
def UsrChoice():
	try:
		global run
	
		# δέχεται μόνο κείμενο, αλλιώς προειδοποιεί και επιστρέφει.
	
		a = str(input("Would you like to roll/toss again? (y/n)\nChoice: "))

		if a == "y" or a == "Y":

			Main()

		elif a == "n" or a == "N":

			print("Thank you for trying out the dice roller! Farewell and have fun!")
			run = False
			
	except ValueError:
		time.sleep(0.3)
		print("Insert 'y/Y' or 'n/N' only.")
		time.sleep(0.6)
		UsrChoice()
		
while run:
	Main()