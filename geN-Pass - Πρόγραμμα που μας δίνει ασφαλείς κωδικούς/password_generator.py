#	geN-Pass - Πρόγραμα που μας δίνει τυχαίους ασφαλείς κωδικούς
#	Δημιουργία: Νίκος-Νικήτας

#	η βιβλιοθήκη secrets για ασφαλείς 'τυχαίους' αριθμούς.
#	η βιβλιοθήκη string για να εργαζόμαστε με κείμενο.
#	η βιβλιοθήκη tkinter για γραφικό περιβάλλον
import secrets
import string
from tkinter import *

#	Όταν πατήσουμε το κουμπί
#	η συνάρτηση παρακάτω διαλέγει τουλάχιστον

#	+ ένα μικρό και ένα κεφαλαίο γράμμα.
#	+ έναν αριθμό
#	+ ένα σύμβολο
#	χαρακτήρες μεγέθους συνολικά 8 και
#	τυχαία με όσο γίνεται ασφαλή τρόπο.
#	Τα ενώνει σε κείμενο και κοιτάζει να έχει τουλάχιστον 1 
#	απ'όλα και 3 ή περισσότερους αριθμούς.
#	Μας δίνει το αποτέλεσμα και αυτόματα το αντιγράφει στο πρόχειρο,
#	ώστε να το επικολλήσουμε όπου χρειαζόμαστε κωδικό

def genPass():
    
    myWordlist = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    while True:
        pw = ''.join(secrets.choice(myWordlist) for x in range(8))
        if (any(c.islower() for c in pw)
                and any(c.isupper() for c in pw)
                and sum(c.isdigit() for c in pw) >= 3):
            break

    print("Your Password is: ",pw)

    Entry.delete(myEn,0,"end")
    Entry.insert(myEn,0,pw)
    win.clipboard_clear()
    win.clipboard_append(pw)
    Label.config(myTxt,text="Ο κωδικός σας αντιγράφτηκε.\nΜπορειτε να τον επικολλήσετε.")

win = Tk()
win.title("geN-Pass - Γεννήτρια Κωδικών")
win.geometry("200x200") # Το μέγεθος του παραθύρου
win.resizable(False,False)# δεν μεγαλώνει ούτε μικραίνει.

myEn = Entry(win)
myEn.grid(row=2,column=2)

myTxt = Label(win)
myTxt.grid(row=3, column=2)

b = Button(win,text="Δώσε μου Κωδικό", command=genPass)
b.grid(row=4,column=2)

win.mainloop()

# Το παράθυρο φαίνεται όσο τρέχει το πρόγραμμα.