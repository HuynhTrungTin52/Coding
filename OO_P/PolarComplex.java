public class PolarComplex extends Complex{
	private double modulus;
	private double angle;
	public PolarComplex(double modulus,double angle) {
		this.modulus=modulus;
		this.angle=angle;
	}
	@Override
	public double modulus() {
		return this.modulus;
	}
	@Override
	public double argument() {
		return angle;
	}
	@Override
	public double getReal() {
		return this.modulus*Math.cos(angle);
	}
	@Override
	public double getImaginary() {
		return this.modulus*Math.sin(angle);
	}
	public static void main(String[] args) {
		PolarComplex a = new PolarComplex(1,Math.PI);
		System.out.println(a.modulus());
		System.out.println(a.argument());
		System.out.println(a.getReal());
		System.out.println(Math.round(a.getImaginary()));
	}
}
