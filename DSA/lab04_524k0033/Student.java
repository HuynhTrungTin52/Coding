import java.util.Arrays;

public class Student {
	protected String name;
	protected double math,program,DSA1, avg;

	public Student(String name, double math, double program, double DSA1) {
		this.name=name;
		this.math=math;
		this.program=program;
		this.DSA1=DSA1;
		this.avg=1.0/3*(math+program+DSA1);
	}

	
	public static double getRand() {
		return Math.round(Math.random()*10 * 100.0) / 100.0;
	}
	public static void main(String[] args) {
		Student[] students = new Student[5];
		students[0] = new Student("Alice", getRand(), getRand(), getRand());
		students[1] = new Student("Bob", getRand(), getRand(), getRand());
		students[2] = new Student("Carol", getRand(), getRand(),getRand());
		students[3] = new Student("Dave", getRand(),getRand(),getRand());
		students[4] = new Student("Eve",getRand(),getRand(),getRand());
		for (Student s : students) {
			System.out.printf("%s - avg: %.2f%n", s.name, s.avg);
		}
		System.out.println();
		Arrays.sort(students, new StudentComparator());
		for (Student s : students) {
			System.out.printf("%s - avg: %.2f%n", s.name, s.avg);
		}
		
	}
}
