// VehicleFactory.java
public class VehicleFactory {
    public Vehicle getVehicle(String vehicleType) {
        if (vehicleType == null || vehicleType.isEmpty()) {
            return null;
        }
        if ("Car".equalsIgnoreCase(vehicleType)) {
            return new Car();
        } else if ("Truck".equalsIgnoreCase(vehicleType)) {
            return new Truck();
        }
        return null;
    }
}