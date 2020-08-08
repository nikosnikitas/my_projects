/*
Ένα απλο πρόγραμμα Αυτόματου Τερματικού Μηχανήματος (ATM) γραμμένο σε C

Δημιουργία: Νίκος-Νικήτας

A Simple ATM Program by Nikos-Nikitas.

*/

#include <stdio.h> // η βιβλιοθήκη για standard input/output της C.
#include <stdlib.h> // η βιβλιοθήκη για την συνάρτηση exit(status) που μας βοηθάει να τερματίσουμε το πρόγραμμα όταν θέλουμε.

int here = 1; // θα τρέχει τον έλεγχο για τον κωδικό μας.

long balance = 3000; // το χρηματικό ποσό του λογαριασμού μας σε long για μεγάλα ψηφία.

int pins[] = {1234,28962,56581,550569,12345678,25647983}; // οι κωδικοί που δέχεται (Κανονικά είναι κρυπτογραφημένοι. Μην το χρησιμοποιήσετε έτσι για ένα ασφαλές ΑΤΜ. Είναι απλά μια επίδειξη.)

int pin; // Ο κωδικός ΠΙΝ που θα δώσει ο χρήστης θα συγκριθεί με τους αποθηκευμένους. Αν υπάρχει τον δέχεται, αλλιώς συνεχίζει να ελέγχει.

void menu(), add(), withdraw(), show();
/* οι συναρτήσεις που θα χρησιμοποιήσουμε για:
    - βασικό μενού με τις επιλογές
    - πρόσθεση/αφαίρεση στο ποσό μας
    - εμφάνιση του ποσού του λογαριασμού μας.
    Όλες οι συναρτήσεις εκτός της main() στο τέλος επιστρέφουν στο βασικό μενού.
*/
void menu() {

    puts("\t\t\t - Main Menu - \t\t\t");

    puts("\t\t\t[1] Show Account Balance\n\t\t\t[2] Add\n\t\t\t[3] Withdraw\n\t\t\t[4] Exit\n");

    int c;

    scanf("%d",&c); // παίρνει την επιλογή του χρήστη και εκτελεί την ανάλογη συνάρτηση ανά περίπτωση. Αν δεν επιλεχτεί κάποια από τις επιλογές συνεχίζει να ελέγχει.


switch(c) {

case 1:
    show();
    break;
case 2:
    add();
    break;
case 3:
    withdraw();
    break;
case 4:
    exit(0);
    break;
default:
    menu();
    }
}

void add() {

    long a;

    puts("Insert amount to add: ");

    scanf("%ld",&a);

    balance = balance+a;

    printf("Your balance now is: %ld",balance);

    return menu();
}

void withdraw() {
    long w;

    printf("Your balance is: %ld \n",balance);
    puts("Insert amount to withdraw: ");

    scanf("%ld",&w);

    balance = balance-w;

    printf("Your balance now is: %ld",balance);

    return menu();

}

void show() {

    printf("Your balance is: %ld",balance);

    return menu();
}

void main(){

     puts("#\t\t\t oNe\t\t\t#\n#\t\t\t Simple\t\t\t#\n#\t\t\t A-T-M\t\t\t#");

     puts("#\t\t\t by nikosnikitas\t#\n");

     while(here==1) {

     puts("Insert PIN\n");

     scanf("%d",&pin);

    for(int i=0; i<sizeof(pins); i++) {
     if(pins[i] == pin) {
        here=0;
     }
     }
     }
     menu();
 }
