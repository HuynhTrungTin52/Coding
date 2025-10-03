
public class OrderItem {
    private String itemName;
    private int quantity;
    private double price;

    public OrderItem() {
    }

    public OrderItem(String itemName, int quantity, double price) {
        this.itemName = itemName;
        this.quantity = quantity;
        this.price = price;
    }

    public String getItemName() {
        return itemName;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return itemName + " - Qty: " + quantity + " - Price: " + price;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        OrderItem orderItem = (OrderItem) obj;
        return quantity == orderItem.quantity && Double.compare(orderItem.price, price) == 0 && itemName.equals(orderItem.itemName);
    }
}