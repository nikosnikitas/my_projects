#FPA-Py Εφαρμογή προσθαφαίρεσης του Φ.Π.Α
#Δημιουργία Εφαρμογής: Νικόλαος-Νικήτας Γκουτέβαινος-Λάμπρου

from tkinter import * #Εισαγωγή βιβλιοθήκης Tkinter για το γραφικό περιβάλλον
from tkinter import messagebox #Εισαγωγή παραθύρου ειδοποίησης

def AddF(): #Συνάρτηση που προσθέτει το Φ.Π.Α
	try:
		Entry.delete(En3,0,'end') #καθαρίζει το πεδίο
		pf=Entry.get(En1)	#παίρνουν τις τιμές ως δεκαδικούς αριθμούς από τα πεδία
		f=Entry.get(En2)	#και υπολογίζουν προσθέτοντας το ΦΠΑ
		pf=float(pf)		
		f=float(f)			
		
		mf=round((1+f/100)*pf,2) #Η συνάρτηση round(mf,2) στρογγυλοποιεί στα 2 ψηφία.
		
		Entry.insert(En3,0,mf)
		
		print(mf)
	except ValueError:	#διαχειριζόμαστε την περίπτωση που ο χρήστης δεν εισάγει αριθμό.
		messagebox.showwarning("Παρακαλώ εισάγετε αριθμό.")

def SubF(): #Αφαιρεί το Φ.Π.Α
	try:
		Entry.delete(En3,0,'end') 
		pf=Entry.get(En1)
		f=Entry.get(En2)
		pf=float(pf)
		f=float(f)
		
		mf=round(pf/(1+f/100),2)
		
		Entry.insert(En3,0,mf)
		print(mf)
	except ValueError:
		messagebox.showwarning("Παρακαλώ εισάγετε αριθμό.")

win = Tk() #Ο σχεδιασμός του γραφικού περιβάλλοντος, παράθυρο, τίτλος, ετικέτες, πεδία, κουμπί και τοποθέτησή τους στο παράθυρο
win.title("Προσθαφαίρεση Φ.Π.Α")

Lb1 = Label(win, text="FPA-Py (by Nik)")
Lb1.grid(row=0, column=1) #Διάταξη με στήλες και σειρές και τοποθέτηση των γραφικών στοιχείων σε αυτές
Lb2 = Label(win, text="Χρηματική Τιμή")
Lb2.grid(row=1, column=0)
Lb3 = Label(win, text="Τιμή % Φ.Π.Α")
Lb3.grid(row=2, column=0)
Lb4 = Label(win, text="Αποτέλεσμα")
Lb4.grid(row=3, column=0)

En1 = Entry(win, bd=5)
En1.grid(row=1, column=1)
En2 = Entry(win, bd=5)
En2.grid(row=2, column=1)
En3 = Entry(win, bd=5)
En3.grid(row=3, column=1)

Btn1 = Button(win, text="Προσθήκη Φ.Π.Α", command=AddF)
Btn1.grid(row=4, column=0)

Btn2 = Button(win, text="Αφαίρεση Φ.Π.Α", command=SubF)
Btn2.grid(row=4, column=1)

win.mainloop() #μένει το παράθυρο ώστε να το βλέπουμε

#Τέλος Προγράμματος
#Όταν πατηθεί το κουμπί Btn1 εκτελεί τη συνάρτηση που προσθέτει το Φ.Π.Α από την αρχική τιμή που του δίνουμε και δείχνει το αποτέλεσμα.
#Αντίστοιχα όταν πατηθεί το κουμπί Btn2 εκτελεί τη συνάρτηση που αφαιρεί το Φ.Π.Α από την αρχική τιμή.
#Σχεδιάστηκε το γραφικό περιβάλλον με τύπο διάταξης grid.