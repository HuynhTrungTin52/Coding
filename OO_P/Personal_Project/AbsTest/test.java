package Personal_Project.AbsTest;


public class test {

	public static void main(String[] args) {
		double[] sides={5,4,5};
		double[] angles={0,0,0};
		
		triangle shape1 = new isoTri(sides, angles);
		System.out.print(shape1.getPeri());
	}
	
}
