package Personal_Project.AbsTest;

public class isoTri extends triangle {

	private double equalSide=0;
	private double base=0;
	public isoTri(double[] sides, double[] angles) {
		for (int i = 0; i < sides.length; i++) {
			this.sides[i] = sides[i];
			this.angles[i] = angles[i];
		}
		if(sides[0] == sides[1]) { 
			equalSide=sides[0]; 
			base=sides[2];
		}
		if(sides[0] == sides[2]) {
			equalSide=sides[0];
			base=sides[1];
		}
		if(sides[1] == sides[2]) {
			equalSide=sides[1];
			base=sides[0];
		}
	}
	
	@Override
	public double getArea() {
		
		
		return ((double)1/2)*base*Math.sqrt(Math.pow(equalSide,2)-(Math.pow(base,2)/4));
	}

	@Override
	public double getPeri() {
		return 2.0*equalSide+base;
	}
}
