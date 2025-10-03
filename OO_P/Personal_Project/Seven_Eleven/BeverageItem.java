package Personal_Project.Seven_Eleven;

public class BeverageItem extends Product {
	protected char size;

	@Override
	public double calculateFinalPrice() {
		int charge=0;
            switch (size) {
                case 'M' -> charge =3000;
                case 'L' -> charge=6000;
			}
        return (basePrice*promotionDiscount/100)+charge;
            
	}
}
