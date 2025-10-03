package FractionADT;

public interface FractionI {
	public int getNumer();   
	public int getDenom();   
	public void setNumer(int numer);  
	public void setDenom(int denom);  

	public FractionI add(FractionI f);    
	public FractionI minus(FractionI f);  
	public FractionI times(FractionI f);  
	public FractionI simplify(); 
} 
