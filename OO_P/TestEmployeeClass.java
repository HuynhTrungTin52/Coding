/**
 * Define the class TestEmployeeClass.java
 *
 */
public class TestEmployeeClass {

/**
 * @param args the command line arguments
 */
public static void main(String[] args)
{
if(args.length==2) {
// Object of outer class
EmployeeClass objEmp1 = new EmployeeClass();
// Invoke the evaluateStatus() method
objEmp1.evaluateStatus(args[0], Integer.parseInt(args[1]));
}
else{
System.out.println("Usage: java EmployeeClass <Emp-Id> <Age>");
}
}
}
