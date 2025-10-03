package Lab01_524k0033;

import java.util.Scanner;


public class ex5 {
	
	public static boolean  isLeapYear(int year)
	{
	
		boolean is_leap_year=false;

		
		if (year % 4 == 0) {
			is_leap_year = true;

			if (year % 100 == 0) {
                            is_leap_year = year % 400 == 0;
			}
		}

		else

			is_leap_year = false;
		return  is_leap_year;
	}

	public static void main(String[] args)
	{
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter a year :");
			int year=in.nextInt();
			if(isLeapYear(year)) System.out.print("The year above is a leap year"); else System.out.print("The year above is NOT a leap year");
		}
	}
}
