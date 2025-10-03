package Lab01_524k0033;

import java.util.Scanner;

public class ex1 {
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {

			System.out.print("Enter your name :");
			String name = in.nextLine();
			System.out.print("Enter your date of birth :");
			String dateBirth = in.nextLine();
			System.out.print("Enter your student ID :");
			String studentID = in.nextLine();
			System.out.println();
			System.out.printf("Name :%s\nDate of birth :%s\nStudent ID :%s", name, dateBirth, studentID);
			//kill me
		}
	}
}
