/*		JVet a veterinary management system in Java.
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

/*importing necessary classes from packages
for file, IO/FileNotFound exceptions, writing to file, scanner for input 
and Arrays to work with arrays
*/
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.util.Scanner;
import java.util.Arrays;

public class JVet {
	
	public static class Pet {
		
		int age = 0;

		String name = "";
		
		boolean isHealthy = true;
		
		String species = "";

		char gender = 'M';
	}
	
	public static void Add() {

		/*
		Values are added by the user here.
		Input is taken and stored making a new Pet object.
		*/
//ToDo: Replace String[] and ArrayList<String> with plain variables
		Pet userMade = new Pet();
		
		//add name to variable
		Scanner s = new Scanner(System.in);
		System.out.println("Enter your pet's name: ");
		userMade.name = s.nextLine();
		
		System.out.println("Enter your pet's age: ");
		userMade.age = s.nextInt();
		
		s.nextLine(); //input so that species won't be skipped.
		
		System.out.println("Enter your pet's species: ");
		userMade.species = s.nextLine();

		System.out.println("Enter your pet's gender: ");
		userMade.gender = s.next().charAt(0);
		
		//writing data to file
		//formatting to string
		
																
		try { FileWriter fw = new FileWriter("data.txt"); // true appends to the file instead of overwriting it.
	
				fw.write("User added\n__________\nName: "+ String.format("%s \n",userMade.name));
				System.lineSeparator();
				
				fw.write("Age: "+ String.format("%s \n",userMade.age));
				System.lineSeparator();
				
				fw.write("Species: "+ String.format("%s \n",userMade.species));
				System.lineSeparator();
				
				fw.write("Gender: "+ String.format("%s \n",userMade.gender));
				System.lineSeparator();
				
			fw.close();
			System.out.println("User wrote data successfully!");

		}catch (IOException e) {
			System.out.println("Error writing to file.");
		}

		//Viewing data
		View();
		menu(); //returns to main menu
	}
	

	//Creates the data file unless an error occurs	
	public static void makeFile() {

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
	}

	
	public static void View() {
		
		//tries to open the file if it exists and reads the data. Throws error if the file is not found.

		try {
			File f = new File("data.txt");
			Scanner r = new Scanner(f);
			while (r.hasNextLine()) {
				String dataRead = r.nextLine();
				System.out.println(dataRead);
			}
			r.close();
			menu();

		} catch (FileNotFoundException e) {
			System.out.println("Error finding file.");
			System.exit(0);
		}

	}
	
	//makes the main menu
	public static void menu() {
		
		//Making the main menu
		
		//'here' tracks if the user is in menu and loops.

		boolean here=true;
		
			/*giving the user options 'ops' to choose from.
			 * Looping through each option in the array with 'i' 
			 * and printing it to the screen. 
*/
			String[] ops = {"Main Menu","[1] View all Pets data","[2] Add Pets data","[3] Exit"};
			for(int i=0; i < ops.length; i++) {

				System.out.println(ops[i]);
			}
		
			Scanner s = new Scanner(System.in); //scans for user input
			
			System.out.println("Your choice: ");
		while(here) {
				
			//user's choice is asked and read
				
			int c = s.nextInt();

			//if the user makes a valid choice the loop breaks

			switch(c){
				case 1:
					View(); //calls to view data
					break;
				case 2:
					Add(); //calls to add data
					break;
				case 3:
					System.exit(0); //exits the program
					break;
					}
				
			}
		
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
		

	//we try to write the data of our pets to the file
		
		makeFile(); //call to create the file
	
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
		
		menu();
		
		}
	}		
		/*					
								-- Note --
		So far the user adds data by overwriting the previous one.
		Hopefully in a future update there will be a way to not overwrite.
		*/
