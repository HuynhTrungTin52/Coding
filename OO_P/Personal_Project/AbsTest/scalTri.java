package Personal_Project.AbsTest;

public class scalTri extends triangle {

	public scalTri(double[] sides,double[] angles) {
		for(int i=0;i<sides.length;i++) {
			this.sides[i]=sides[i];
			this.angles[i]=angles[i];
		}
	}

	@Override
	public double getArea() {
		double s=getPeri()/2;
		return Math.sqrt(s*((s-sides[0])*(s-sides[1])*(s-sides[2])));
	}	

	@Override
	public double getPeri() {
		return sides[0] + sides[1] +sides[2];
	}
}
