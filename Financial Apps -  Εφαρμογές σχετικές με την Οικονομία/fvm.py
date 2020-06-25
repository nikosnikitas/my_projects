﻿#FVM-Py - εφαρμογή που υπολογίζει τη μελλοντική αξία των χρημάτων μας στην τράπεζα
#Δημιουργία Εφαρμογής: Νίκος-Νικήτας

#Εισαγωγή της βιβλιοθήκης tkinter για σχεδιασμό γραφικού περιβάλλοντος
from tkinter import * #για κάποιο λόγο δεν το έβρισκε χωρίς 'from ... import *'
#Εισαγωγή του παραθύρου προειδοποίησης
from tkinter import messagebox
#Η συνάρτηση που παίρνει τις τιμές από τα πεδία και υπολογίζει με βάση τον τύπο τη μελλοντική αξία FV
def myDef():
	try: #ελέγχει για το αν είναι όλες οι τιμές αριθμοί
		Entry.delete(En4,0,"end") #καθαρίζει το πεδίο
		P=Entry.get(En1) # p = αρχική τιμή
		i=Entry.get(En2) # i = ο τόκος interest και υπολογίζεται από % σε δεκαδικό
		X=Entry.get(En3) # Χ = τα έτη που είναι τα χρήματα στην τράπεζα
		P=float(P) #εδώ δεχόμαστε και δεκαδικές τιμές. Γίνονται δεκτές και ακέραιες τιμές
		i=float(i)
		X=float(X)
	
	
		FV=round(P*((1+(0.01*i))**X),2) #Ο τύπος υπολογισμού της μελλοντικής αξίας των χρημάτων. 
		#Ο τύπος στην χρηματοοικονομία είναι: Μελλοντική Αξία = Παρούσα Αξία επί(1+τόκος)με δύναμη τα έτη.
                #Η μέθοδος round(FV,2) παιρνει τη μελλοντική αξία και μας δίνει μέχρι 2 δεκαδικά ψηφία.
	
		Entry.insert(En4,0,FV) #Η μελλοντική αξία εισάγεται στο πεδίο που την βλέπουμε (ως δεκαδική τιμή)

		print(FV)

	except ValueError: #εκτελεί προειδοποίηση αν δεν εισάγουμε αριθμό
		messagebox.showwarning("Παρακαλώ εισάγετε αριθμό.")
win = Tk() #Ο σχεδιασμός του γραφικού περιβάλλοντος, παράθυρο, τίτλος, ετικέτες, πεδία, κουμπί
win.title("ΥΠΟΛΟΓΙΣΜΟΣ ΜΕΛΛΟΝΤΙΚΗΣ ΑΞΙΑΣ ΧΡΗΜΑΤΩΝ")

Lb1 = Label(win, text="FVM-Py (by Nik)")
Lb1.grid(row=0, column=1) #Διάταξη με στήλες και σειρές και τοποθέτηση των γραφικών στοιχείων σε αυτές
Lb2 = Label(win, text="Χρηματικό Ποσό ")
Lb2.grid(row=1, column=0)
Lb3 = Label(win, text="Τόκος")
Lb3.grid(row=2, column=0)
Lb4 = Label(win, text="Χρόνια")
Lb4.grid(row=3, column=0)
Lb5 = Label(win, text="Μελλοντική Αξία")
Lb5.grid(row=4, column=0)

En1 = Entry(win, bd=5)
En1.grid(row=1, column=1)
En2 = Entry(win, bd=5)
En2.grid(row=2, column=1)
En3 = Entry(win, bd=5)
En3.grid(row=3, column=1)
En4 = Entry(win, bd=5)
En4.grid(row=4, column=1)
#Με το command τρέχει η συνάρτηση του υπολογισμού.
Btn = Button(win, text="Υπολογισμός", command=myDef) 
Btn.grid(row=5,column=1)

win.mainloop() #μένει το παράθυρο ώστε να το βλέπουμε συνέχεια.

#Τέλος Προγράμματος