public class Fraction {
    private int numer=0;
    private int denom=0;

    public Fraction(){}
    public Fraction(int x, int y) {
        this.numer=x;
        this.denom=y;
    }
    public Fraction(Fraction f) {
        this.numer=f.numer;
        this.denom=f.denom;
    }
    @Override
    public String toString(){
        return numer+"/"+denom;
    }
    @Override
    public boolean equals(Object f){
        if(this==f) {
            return true;
        }
        //If the object is compared to itself
        if(!(f instanceof Fraction)){
            return false;
        }
        //If the object is a Fraction or not
        Fraction temp = (Fraction) f;

         return this.numer==temp.numer && this.denom==temp.denom;
        
    }


}
