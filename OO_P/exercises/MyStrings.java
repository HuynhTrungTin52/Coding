package exercises;
import java.util.*;
public class MyStrings {

	public static String reverseStr(String str)
	{
		String rts="";
		for(int i=str.length()-1;i>=0;i--)
		{
			rts+=str.charAt(i);
		}
	return rts;
	}
	public static boolean isVowel(char Char)
	{
		Char= Character.toLowerCase(Char);
		return Char=='a' || Char=='e' || Char=='i' || Char=='o' || Char=='u';
		
	}
	public static boolean isCon(char Char)
	{
		Char =Character.toLowerCase(Char);
		return Char>='a' && Char<='z' && !isVowel(Char);
	}
	public static boolean isPalin(String str)
	{
		for(int i=0,j=str.length()-1;i<=str.length()/2;i++,j--)
		{
			if(str.charAt(i)!=str.charAt(j)) return false;
		}
	return true;
	}
	public static char mostChar(String str)
	{
		return 'a';
	}
	public static void main(String[] args) {
		
		try (Scanner in = new Scanner(System.in)) {
			System.out.print("Enter a string :");
			String str=in.nextLine();
			String rts=reverseStr(str);
			System.out.println("The reversed string is : "+rts);
			int vowelCount=0;
			int conCount=0;
			for(int i=0;i<str.length();i++)
			{
				if(isVowel(str.charAt(i))) vowelCount++;
				if(isCon(str.charAt(i))) conCount++;
			}
			System.out.println("Number of vowels is :" + vowelCount);
			System.out.println("Number of Consonants is :"+conCount);
			boolean isPal=isPalin(str);
			if(isPal) System.out.println("The string above is a Palindrome"); else System.out.println("The string above is NOT a Palindrome");
		}

	}	
}
