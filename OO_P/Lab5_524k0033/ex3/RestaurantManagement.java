import java.util.Scanner;

public class RestaurantManagement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        FoodItem[] foodMenu = {
                new FoodItem("Chicken Rice", 50000.0),
                new FoodItem("Beef Noodles", 40000.0)
        };
        DrinkItem[] drinkMenu = {
                new DrinkItem("Coca Cola", 15000.0),
                new DrinkItem("Iced Tea", 5000.0)
        };
        Invoice invoice = new Invoice();

        while (true) {
            System.out.println("\n1. Order Food");
            System.out.println("2. Print Invoice");
            System.out.println("3. Pay and Exit");
            System.out.print("Select an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (option) {
                case 1:
                    System.out.println("\nSelect food item:");
                    for (int i = 0; i < foodMenu.length; i++) {
                        System.out.println((i + 1) + ". " + foodMenu[i]);
                    }
                    for (int i = 0; i < drinkMenu.length; i++) {
                        System.out.println((foodMenu.length + i + 1) + ". " + drinkMenu[i]);
                    }
                    System.out.print("Enter item number: ");
                    int itemNumber = scanner.nextInt();
                    System.out.print("Enter quantity: ");
                    int quantity = scanner.nextInt();
                    scanner.nextLine(); // Consume newline

                    if (itemNumber <= foodMenu.length) {
                        invoice.addItem(new OrderItem(foodMenu[itemNumber - 1].getName(), quantity, foodMenu[itemNumber - 1].getPrice()));
                    } else {
                        invoice.addItem(new OrderItem(drinkMenu[itemNumber - foodMenu.length - 1].getName(), quantity, drinkMenu[itemNumber - foodMenu.length - 1].getPrice()));
                    }
                    break;
                case 2:
                    invoice.printInvoice();
                    break;
                case 3:
                    System.out.println("Payment successful!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }
}