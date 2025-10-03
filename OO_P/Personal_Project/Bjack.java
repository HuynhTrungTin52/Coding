package Personal_Project;

import java.util.ArrayList;
import java.util.Random;

class Bjack {
	private int value = 0;
	private final ArrayList<String> cards = new ArrayList<>(11);
	private static final int[] numCards = new int[13];
	private boolean ace=false;
	private boolean firstTime=false;
	public static int totalCards() {
		int total = 0;
		for (int num : numCards) {
			total += num;
		}
		return total;
	}
	
	
	public void draw() {
		Random seed = new Random();
		boolean again = true;
		while (again) {
			
			int randomizer = seed.nextInt(13) + 1;
			if(firstTime)
				{
					randomizer=1;
					firstTime=false;
				}
			switch (randomizer) {
				
				case 1 -> {
					
					if (numCards[0] <= 3) {
						again = false;
					} else
						break;
					cards.add("Ace");
					if (value + 11 > 21)
						value++;
					else {
						
						value += 11;
						ace=true;
					}

					numCards[0]++;
				}
				case 11 -> {

					if (numCards[10] <= 3) {
						again = false;
					} else
						break;
					cards.add("Jack");
					value += 10;

					numCards[10]++;
				}
				case 12 -> {

					if (numCards[11] <= 3) {
						again = false;
					} else
						break;
					cards.add("Queen");
					value += 10;

					numCards[11]++;
				}
				case 13 -> {

					if (numCards[12] <= 3) {
						again = false;
					} else
						break;
					cards.add("King");
					value += 10;
					numCards[12]++;
				}
				default -> {

					if (numCards[randomizer - 1] <= 3) {
						again = false;
					} else
						break;
					cards.add(String.valueOf(randomizer));
					value += randomizer;
					numCards[randomizer - 1]++;
				}
			}
			if(ace==true && cards.size()>=3 && value!=20)
			{
				value-=10;
				ace=false;
			} 
		}
	}

	public void draw(int drawMany) {
		Random seed = new Random();
		
		for(int i=0;i<drawMany;i++)
		{
		boolean again = true;
		while (again) {
			
			int randomizer = seed.nextInt(13) + 1;
			switch (randomizer) {
				
				case 1 -> {
					
					if (numCards[0] <= 3) {
						again = false;
					} else
						break;
					cards.add("Ace");
					if (value + 11 > 21)
						value++;
					else {
						
						value += 11;
						ace=true;
					}

					numCards[0]++;
				}
				case 11 -> {

					if (numCards[10] <= 3) {
						again = false;
					} else
						break;
					cards.add("Jack");
					value += 10;

					numCards[10]++;
				}
				case 12 -> {

					if (numCards[11] <= 3) {
						again = false;
					} else
						break;
					cards.add("Queen");
					value += 10;

					numCards[11]++;
				}
				case 13 -> {

					if (numCards[12] <= 3) {
						again = false;
					} else
						break;
					cards.add("King");
					value += 10;
					numCards[12]++;
				}
				default -> {

					if (numCards[randomizer - 1] <= 3) {
						again = false;
					} else
						break;
					cards.add(String.valueOf(randomizer));
					value += randomizer;
					numCards[randomizer - 1]++;
				}
			}
			if(ace==true && cards.size()>=3 && value!=20)
			{
				value-=10;
				ace=false;
			} 
		}
		}
	}

	public String whichCard(int pos)
	{
		return cards.get(pos);
	}

	public void showCards()
	{
		
		for(int i=0;i<cards.size();i++)
		{
			System.out.print(cards.get(i));
			if(i!=cards.size()-1)
			{
				System.out.print(" ");
			}
		}
	}
	public int showVal()
	{
		return value;
	}
	
	public void show() {
		showCards();
		System.out.print(" " +"(" + showVal()+")");
	}
}