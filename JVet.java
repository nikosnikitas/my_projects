/*		JVet a veterinary management system in Java. (INCOMPLETE yet)
 *		
 *			Author: Nikos-Nikitas
 *
 *	****************************************************************
 *	*	Pets and their info are written to a file and accessed *
 *	*	when the user wants.				       *
 *	*						       	       *
 *	****************************************************************
 *	For more find me on GitHub: nikosnikitas
 * */

//importing necessary classes from packages
//for file, exception, writing to file, scanner for input

import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;

public class JVet {
	
	public static class Pet {
		
		int age = 0;

		String name = "";
		
		boolean isHealthy = true;
		
		String species = "";

		char gender = 'M';
	}


	public static void main(String[] args) {
		Pet rufus = new Pet();
		rufus.age = 3;
		rufus.name="Rufus";
		rufus.species="Dog";
		rufus.gender='M';
		
		Pet katia = new Pet();
		katia.age = 5;
		katia.name="Katia";
		katia.species="Cat";
		katia.gender='F';

		Pet rico = new Pet();
		rico.name="Rico";
		rico.age = 9;
		rico.species="Parrot";
		rico.gender='M';
		
//try to create file unless an error happens
//then we try to write the data of our pets to the file

	try {
		File f = new File("data.txt");
		if (f.createNewFile()) {
			System.out.println("Created file " + f + " successfully!");
		}
		else {
			System.out.println("File " + f + " already exists.");
		}
	}
	catch (IOException e) {

		System.out.println("Error creating file.");
	}

	
	try { FileWriter fw = new FileWriter("data.txt");
		
		fw.write("Pet names: "+ String.format("%s %s %s \n",rufus.name,katia.name,rico.name));
		System.lineSeparator(); //adds new line
		
		fw.write("Pet species: "+ String.format("%s %s %s \n",rufus.species,katia.species,rico.species));
		System.lineSeparator();
		
		fw.write("Pet age: "+ String.format("%s %s %s \n",rufus.age,katia.age,rico.age));
		
		fw.close();
		System.out.println("Wrote data successfully!");

	}catch (IOException e) {
		System.out.println("Error writing to file.");
	}



		//Making the main menu
		
		//'here' tracks if the user is in menu and loops.

		boolean here=true;
		
		
		//TODO: add methods to read, view data and exit.

			/*giving the user options 'ops' to choose from.
			 * Looping through each option in the array with 'i' 
			 * and printing it to the screen. 
*/
			String[] ops = {"Main Menu","[1] View all Pets","[2] Add Pet","[3] Exit"};
			for(int i=0; i < ops.length; i++) {

				System.out.println(ops[i]);
			}
		
			Scanner s = new Scanner(System.in); //scans for user input
			
			System.out.println("Your choice: ");
		while(here) {
				
				//user's choice is asked and read
				
				int c = s.nextLine();

			//if the user makes a valid choice the loop breaks
			if(c=1 || c=2 || c=3) {
				
				here=false;
			
			}
		}
			
		switch(c){
			case 1:
			//	View(); //to be added
				break;
			case 2:
			//	Add(); //to be added
				break;
			case 3:
				System.exit(0)
				break;
		}

	}
}