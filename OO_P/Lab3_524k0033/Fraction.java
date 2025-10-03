package Lab3_524k0033;

public class Fraction {
	private int numerator;
    private int denominator;

    
    public Fraction() {
        this.numerator = 0;
        this.denominator = 1; 
    }

    
    public Fraction(int num, int den) {
        this.numerator = num;
        if (den != 0) {
            this.denominator = den;
        } else {
            this.denominator = 1; 
            System.err.println("Denominator cannot be zero. Setting it to 1.");
        }
        reducer(); 
    }

    public Fraction(Fraction f) {
        this.numerator = f.numerator;
        this.denominator = f.denominator;
    }

    
    public Fraction add(Fraction f) {
        int newNum = this.numerator * f.denominator + f.numerator * this.denominator;
        int newDen = this.denominator * f.denominator;
        return new Fraction(newNum, newDen); 
    }

    
    public Fraction sub(Fraction f) {
        int newNum = this.numerator * f.denominator - f.numerator * this.denominator;
        int newDen = this.denominator * f.denominator;
        return new Fraction(newNum, newDen); 
    }

    
    public Fraction mul(Fraction f) {
        int newNum = this.numerator * f.numerator;
        int newDen = this.denominator * f.denominator;
        return new Fraction(newNum, newDen); 
    }

    
    public Fraction div(Fraction f) {
        int newNum = this.numerator * f.denominator;
        int newDen = this.denominator * f.numerator;
        return new Fraction(newNum, newDen); 
    }

    
    public void reducer() {
        if (numerator == 0) {
            denominator = 1;
            return;
        }
        int gcd = gcd(Math.abs(numerator), Math.abs(denominator));
        numerator /= gcd;
        denominator /= gcd;
        if (denominator < 0) { 
            numerator *= -1;
            denominator *= -1;
        }
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    @Override
    public String toString() {
        return "Fraction[" + numerator + ", " + denominator + "]";
    }

    public static void main(String[] args) {
        Fraction a = new Fraction(32, 8);
        System.out.print(a.toString());
    }
}
