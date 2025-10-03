package FractionADT;

public class Fraction implements FractionI {
	private int numer;
	private int denom;
	
	public Fraction() {
		this(1,1);
	}
	public Fraction(int numer,int denom) {
		setNumer(numer);
		setDenom(denom);
	}
	private static int gcd(int a, int b) {
		int rem;
		while (b > 0) { 
			//a =6,b=4
			rem = a%b;
			//rem=2
			a = b;
			//6->4
			b = rem;
			//b=2
			
		}
		return a;
	}

	@Override
	public FractionI add(FractionI f) {
		
		return new Fraction((this.numer*f.getDenom())+(f.getNumer()*this.denom),this.denom*f.getDenom());
	}
	@Override
	public int getDenom() {
		
		return denom;
	}
	@Override
	public int getNumer() {
		
		return numer;
	}
	@Override
	public FractionI minus(FractionI f) {
		return new Fraction((this.numer*f.getDenom())-(f.getNumer()*this.denom),this.denom*f.getDenom());
	}
	@Override
	public void setDenom(int denom) {
		this.denom=denom;
	}
	@Override
	public void setNumer(int numer) {
		this.numer=numer;
	}
	@Override
	public FractionI simplify() {
		return new Fraction(this.numer/gcd(numer, denom),this.denom/gcd(numer, denom));
	}
	@Override
	public FractionI times(FractionI f) {
		return new Fraction(this.numer*f.getNumer(),this.denom*f.getDenom());
	}
	@Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Fraction{");
        sb.append("numer=").append(numer);
        sb.append(", denom=").append(denom);
        sb.append('}');
        return sb.toString();
    }
    
	public static void main(String[] args) {
		FractionI a = new Fraction(3,5);
		FractionI b = new Fraction(2,8);
		FractionI c = a.times(b);
		System.out.print(c.simplify().toString());
	}

	
}
