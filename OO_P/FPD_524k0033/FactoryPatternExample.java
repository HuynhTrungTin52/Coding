// FactoryPatternExample.java
public class FactoryPatternExample {
    public static void main(String[] args) {
        VehicleFactory vehicleFactory = new VehicleFactory();

        // Get a car object
        Vehicle car = vehicleFactory.getVehicle("Car");
        if (car != null) {
            car.move();
        }

        // Get a truck object
        Vehicle truck = vehicleFactory.getVehicle("Truck");
        if (truck != null) {
            truck.move();
        }

        // Get an unknown vehicle
        Vehicle unknown = vehicleFactory.getVehicle("Bike");
        if (unknown != null) {
            unknown.move();
        } else {
            System.out.println("Unknown vehicle type.");
        }
    }
}