public class EmployeeClass {

/**
 * Evaluates employee status
 *
 * @param empID a String variable storing employee ID
 * @param empAge an integer variable storing employee age
 * @return void
 */
public void evaluateStatus(String empID, int empAge){
// local final variable
final int age=40;
/**
 * Local inner class Rank
 *
 */
class Rank{

/**
 * Returns the rank of an employee
 *
 * @param empID a String variable that stores the employee ID
 * @return char
 */
public char getRank(String empID){
System.out.println("Getting Rank of employee: "+ empID);
// assuming that rank ‘A’ was returned from server
return 'A';
}
}

// Check the specified age
if(empAge>=age){
// Instantiate the Rank class
Rank objRank = new Rank();

// Retrieve the employee’s rank
char rank = objRank.getRank(empID);

// Verify the rank value
if(rank == 'A') {
System.out.println("Employee rank is:"+ rank);
System.out.println("Status: Eligible for upgrade");
}
else{
System.out.println("Status: Not Eligible for upgrade");
}
}
else{
System.out.println("Status: Not Eligible for upgrade");
}
}
}
