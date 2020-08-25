/*----------------------------
##############################
# A Calculator program in C# #
# Author: Nikos-Nikitas      #
# GitHub: nikosnikitas       #
##############################
----------------------------*/

using System;

namespace Calculator
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Hello!");
			Console.WriteLine("This is a calculator.");
			Console.WriteLine("Add an operator (+ , - , * or /) followed by 2 numbers to make your calculation.\n");
			
			//Reads the operator
			string op = Console.ReadLine();
			
			
			int num1 = Convert.ToInt32(Console.ReadLine());
			
			int num2 = Convert.ToInt32(Console.ReadLine());
			
			switch(op) {
			    
			    case "+":
			        Console.WriteLine(num1+num2);
			        break;
			    case "-":
			        Console.WriteLine(num1-num2);
			        break;
			    case "*":
			        Console.WriteLine(num1*num2);
			        break;
			    case "/":
			        Console.WriteLine(num1/num2);
			        break;
			}
			
			
		}
	}
}
