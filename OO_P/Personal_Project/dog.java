package Personal_Project;

public class dog {
	private String colour;
	private String shape;
	private int food=0;
	private static int numOfDogs=0;
	public dog() {
		colour="Black";
		shape="Short";
		food=0;
		numOfDogs++;
	}

	public dog(String colour, String shape) {
		this.colour=colour;
		this.shape=shape;
		food=0;
		numOfDogs++;
	}
	public static int getNumOfDogs() {
		return numOfDogs;
	}
	public void bark() {
		System.out.println("Woof");
	}

	public void shape() {
		System.out.println("This is a "+shape+" and "+colour+" dog" );
	}

	public void eat(String food) {
		System.out.println("The dog has eaten (a) "+food);
		this.food++;
	}

	public void poop() {
		if(food >=10 ) {
			System.out.println("The dog has pooped");
		} else {
			System.out.println("The dog hasn't eaten enough");
		}
	}
}
