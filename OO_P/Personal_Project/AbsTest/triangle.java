package Personal_Project.AbsTest;

abstract class triangle {
	protected double[] sides = new double[3];
	protected double[] angles = new double[3];

	abstract double getArea();
	abstract double getPeri();

}
