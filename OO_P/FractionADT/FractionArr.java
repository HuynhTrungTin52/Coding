package FractionADT;

public class FractionArr implements FractionI{
	private int[] members;

	public FractionArr() {
		this(1,1);
	}
	public FractionArr(int numer,int denom) {
		members = new int[2];
		setNumer(numer);
		setDenom(denom);
	}
	private static int gcd(int a, int b) {
		int rem;
		while (b > 0) {
			rem = a%b;
			a = b;
			b = rem;
		}
		return a;
	}

	@Override
	public FractionI add(FractionI f) {
		
		return new Fraction((this.members[0]*f.getDenom())+(f.getNumer()*this.members[1]),this.members[1]*f.getDenom());
	}
	@Override
	public int getDenom() {
		
		return members[1];
	}
	@Override
	public int getNumer() {
		
		return members[0];
	}
	@Override
	public FractionI minus(FractionI f) {
		return new Fraction((this.members[0]*f.getDenom())-(f.getNumer()*this.members[1]),this.members[1]*f.getDenom());
	}
	@Override
	public void setDenom(int denom) {
		members[1]=denom;
	}
	@Override
	public void setNumer(int numer) {
		members[1]=numer;
	}
	@Override
	public FractionI simplify() {
		return new Fraction(this.members[0]/gcd(members[0], members[1]),this.members[1]/gcd(members[0], members[1]));
	}
	@Override
	public FractionI times(FractionI f) {
		return new Fraction(this.members[0]*f.getNumer(),this.members[1]*f.getDenom());
	}
	@Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Fraction{");
        sb.append("numer=").append(members[0]);
        sb.append(", denom=").append(members[1]);
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
