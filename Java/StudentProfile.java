/***************************************************************************
   *************************************************************************
   *	A sample student profile class with student's attributes and behavior. *
   *------------------------------------------------------------------------*
   *		Author: Nikos-Nikitas												   *
   *------------------------------------------------------------------------*
   *		GitHub: nikosnikitas												   *
   **************************************************************************
****************************************************************************/


public class StudentProfile

{
	public static class Student
	{
		
		public String firstName="";
		public String lastName="";
		public int expectedGraduationYear=0;
		public double gpa=0.00;
		public boolean declaredMajor;
		
		public Student(String firstName, String lastName, 
						int expectedGraduationYear, double gpa, boolean declaredMajor)
		{
			this.firstName = firstName;
			this.lastName = lastName;
			this.expectedGraduationYear = expectedGraduationYear;
			this.gpa = gpa;
			this.declaredMajor = declaredMajor;
			
			System.out.println("New Student Profile Created!\n");
		}
		public int incrementGraduationYear()
		{	
			expectedGraduationYear += 1;
		
			return expectedGraduationYear; 
		}
	}
	
	public static void main(String args[])
	{	
		//Creating two Student instances for demonstration.
		Student Rey = new Student("Rey", "Masters", 2024, 8.3, false);
		
		Student Kayla = new Student("Kayla", "Johnson", 2023, 9.1, true);
		
		//Printing Kayla's lastName attribute.
		System.out.println(Kayla.lastName);
		
		//Printing Kayla's expectedGraduationYear
		System.out.println(Kayla.expectedGraduationYear);
		
		//Incrementing Kayla's expectedGraduationYear by 1.
		Kayla.incrementGraduationYear();
		
		//Printing the result.
		System.out.println(Kayla.expectedGraduationYear);
		
		
		
	}
	
}
