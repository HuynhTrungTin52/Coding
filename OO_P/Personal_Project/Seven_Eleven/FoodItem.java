package Personal_Project.Seven_Eleven;

public class FoodItem extends Product {
	protected boolean isHot;

	@Override
	public double calculateFinalPrice() {
		if(isHot) {
		return (basePrice*promotionDiscount/100)+5000;
	} else
	 return basePrice*promotionDiscount/100;
}
}