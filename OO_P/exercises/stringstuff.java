package exercises;
import java.util.*;
public class stringstuff {
	public static int findSpaces(String name)
	{
		int totalSpaces=1;
		for(int i=0;i<name.length();i++)
			{
				while(name.charAt(0)==' ')
				{
					name=name.substring(1);
				}
				while(name.charAt(i)==' ' && name.charAt(i+1)==' ')
				{

					name=name.substring(0,i)+name.substring(i+1);
				}
				if(name.charAt(i)==' ')
				{
					totalSpaces++;
				}
					
			}
	
		return totalSpaces;
	}
	public static void main(String arg[])
	{
		try(Scanner in = new Scanner(System.in))
		{
			System.out.print("Enter a name :");
			String name = in.nextLine();
			name=name.substring(0,1).toUpperCase()+name.substring(1);
			String firstName="";
			String lastName="";
			String middleName="";
			int total=findSpaces(name);
			int spaces=1;
			int counter=0;
			for(int i=0;i<name.length();i++)
			{

				while(name.charAt(0)==' ')
				{
					name=name.substring(1);
				}
				if(Character.isLowerCase(name.charAt(0)))
				{
					name=name.substring(0,1).toUpperCase()+name.substring(1);
				}
				while(name.charAt(i)==' ' && name.charAt(i+1)==' ')
				{

					name=name.substring(0,i)+name.substring(i+1);
				}
				if(name.charAt(i)==' ')
				{
					
					spaces++;
					name=name.substring(0,i+1)+name.substring(i+1,i+2).toUpperCase()+name.substring(i+2);
					if(spaces !=1 && spaces != total && counter!=1)
					{
						i++;
						counter++;
					}
				}
				
				if(spaces==1){
				firstName+=name.charAt(i);
				}else 
				if(spaces==total)
				{
				lastName+=name.charAt(i);
				} else
				if(spaces !=1 && spaces != total)
				{
					middleName+=name.charAt(i);
				}
			}
			
			System.out.println("The amount of spaces in your string is " + total);
			System.out.println("First name :" + firstName);
			System.out.println("Last name :" + lastName);
			System.out.println("Middle name :" + middleName);
			System.out.print("Full name :"+ name);
		}
	}	
}
