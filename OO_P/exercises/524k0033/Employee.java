class Employee {
    private String id;
    private double[] salaries;

    public Employee(String id, double[] salaries) throws InvalidSalariesLengthException {
        this.id = id;
        if (salaries == null || salaries.length != 12) {
            throw new InvalidSalariesLengthException("Salaries array must have a length of 12.");
        }
        this.salaries = salaries;
    }

    public double getAverageSalary() {
        if (salaries == null || salaries.length == 0) {
            return 0.0;
        }
        double sum = 0;
        for (double salary : salaries) {
            sum += salary;
        }
        return sum / salaries.length;
    }

    public String getCategory() {
        double averageSalary = getAverageSalary();
        if (averageSalary >= 20000) {
            return "High Income";
        } else if (averageSalary >= 15000) {
            return "Middle Income";
        } else if (averageSalary >= 10000) {
            return "Low Income";
        } else {
            return "Below Poverty Line";
        }
    }

    public String getId() {
        return id;
    }

    public double[] getSalaries() {
        return salaries;
    }

    public static void main(String[] args) {
        try {
            double[] validSalaries = {5000, 5200, 5500, 5100, 5300, 5400, 5600, 5700, 5800, 5900, 6000, 6100};
            Employee emp1 = new Employee("E123", validSalaries);
            System.out.println("Employee ID: " + emp1.getId());
            System.out.println("Average Salary: " + emp1.getAverageSalary());
            System.out.println("Category: " + emp1.getCategory());
            System.out.println();

            double[] invalidSalariesShort = {7000, 7500, 8000, 7200};
            Employee emp2 = new Employee("E456", invalidSalariesShort);
            System.out.println("Employee ID: " + emp2.getId());
            System.out.println("Average Salary: " + emp2.getAverageSalary());
            System.out.println("Category: " + emp2.getCategory());

        } catch (InvalidSalariesLengthException e) {
            System.err.println("Error creating employee: " + e.getMessage());
        }

        try {
            double[] invalidSalariesNull = null;
            Employee emp3 = new Employee("E789", invalidSalariesNull);
            System.out.println("Employee ID: " + emp3.getId());
            System.out.println("Average Salary: " + emp3.getAverageSalary());
            System.out.println("Category: " + emp3.getCategory());
        } catch (InvalidSalariesLengthException e) {
            System.err.println("Error creating employee: " + e.getMessage());
        }
    }
}