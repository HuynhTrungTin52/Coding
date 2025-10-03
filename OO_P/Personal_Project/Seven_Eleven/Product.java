package Personal_Project.Seven_Eleven;

public class Product {
	protected String name;
	protected double basePrice;
	protected int stock;
	protected double promotionDiscount;

	public double calculateFinalPrice() {
		return basePrice*promotionDiscount/100;
	}

	public boolean sellIten(int quanity) {
		if(stock-quanity>=0) {
			stock=stock-quanity;
			return true;
		} else return false;
	}

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Product{");
        sb.append("name=").append(name);
        sb.append(", basePrice=").append(basePrice);
        sb.append(", stock=").append(stock);
        sb.append(", promotionDiscount=").append(promotionDiscount);
        sb.append('}');
        return sb.toString();
    }


}
