package Personal_Project.AbsTest;
public class equalTri extends triangle {
	
	public equalTri(double[] sides) {
		for(int i=0;i<sides.length;i++) {
			this.sides[i]=sides[i];
			angles[i]=60;
		}
	}

	@Override
	public double getArea() {
		return (Math.sqrt(3)/4)*Math.pow(sides[0], 2);
	}

	@Override
	public double getPeri() {
		return sides[0]*3;
	}
}
