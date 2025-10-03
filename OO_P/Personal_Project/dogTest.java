package Personal_Project;
public class dogTest {
	public static void main(String[] args) {
		dog momo = new dog();
		momo.shape();
		momo.eat("pizza");
		momo.poop();
		dog nah = new dog("purple","weird");
		dog ok = new dog();
		System.out.print(dog.getNumOfDogs());
	}
}
