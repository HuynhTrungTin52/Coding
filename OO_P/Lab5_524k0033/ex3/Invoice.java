
public class Invoice {
    private OrderItem[] items;
    private int itemCount;
    private double totalAmount;

    public Invoice() {
        items = new OrderItem[100];
        itemCount = 0;
        totalAmount = 0;
    }

    public void addItem(OrderItem item) {
        boolean exists = false;
        for (int i = 0; i < itemCount; i++) {
            if (items[i].equals(item)) {
                items[i] = new OrderItem(item.getItemName(), items[i].getQuantity() + item.getQuantity(), item.getPrice());
                exists = true;
                break;
            }
        }
        if (!exists) {
            items[itemCount++] = item;
        }
        totalAmount += item.getPrice() * item.getQuantity();
    }

    public void printInvoice() {
        System.out.println("--- Invoice ---");
        for (int i = 0; i < itemCount; i++) {
            System.out.println(items[i]);
        }
        System.out.println("Total Amount: " + totalAmount);
    }
}