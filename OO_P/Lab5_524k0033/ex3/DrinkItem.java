
public class DrinkItem {
    private String name;
    private double price;

    public DrinkItem() {
    }

    public DrinkItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return name + " - " + price;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        DrinkItem drinkItem = (DrinkItem) obj;
        return Double.compare(drinkItem.price, price) == 0 && name.equals(drinkItem.name);
    }
}