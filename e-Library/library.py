#	Ηλεκτρονική Βιβλιοθήκη - e-Library
#	Δημιουργία: Νίκος-Νικήτας -	Made by Nikos-Nikitas
#----------------------------------------------------

#	Η κλάση Book περιλαμβάνει τα βιβλία με τίτλο και συγγραφέα.
#	Η συνάρτηση Add() προσθέτει τα βιβλία και τους συγγραφείς 
#	στις αντίστοιχες λίστες. Μετά δημιουργούμε αντικείμενα βιβλία
#	και τα προσθέτουμε από τη φόρμα.

class Book:
	
	def __init__(self,title,author):
		self.title = title
		self.author = author
	
	def Add(self):
		books.append(self.title)
		authors.append(self.author)

books = []

authors = []

b1 = Book("This is Book 1","Author 1")

b2 = Book("This is Book 2","Author 2")

b1.Add()

b2.Add()

giveBook = Book(input("Title\n> "),input("Author\n> "))
giveBook.Add()

print(books)
print(authors)
