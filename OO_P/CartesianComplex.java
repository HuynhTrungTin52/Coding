public class CartesianComplex extends Complex{
	private double real;
	private double imaginary;

	public CartesianComplex(double real, double imaginary) {
		this.real=real;
		this.imaginary=imaginary;
	}
	@Override
	public double getReal() {
		return real;
	}
	@Override 
	public double getImaginary() {
		return imaginary;
	}
	@Override 
	public double modulus(){
		return Math.abs(Math.sqrt(real*real+imaginary*imaginary));
	}
	@Override
	public double argument(){
		return Math.atan2(imaginary, real);
	}
	public static void main(String[] args) {
		CartesianComplex a = new CartesianComplex(5, 10);
		System.err.println(a.getImaginary());
		System.err.println(a.getReal());
		System.out.println(a.modulus());
		System.out.println(a.argument());
	}
}
