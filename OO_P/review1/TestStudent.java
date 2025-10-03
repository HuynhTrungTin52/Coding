package review1;

public class TestStudent {

	public static int count(Student[] students, String Group, String CourseID) {
		int count = 0;
		for (Student i : students) {
			if (i.scores < 5) {
				count++;
			}
		}
		return count;
	}

	public static void main(String args[]) {
		Student[] students = {
				new Student("524k0011", "524k0011@student.tdtu.edu.vn", "Nguyen Gia", "12345", "Software Engineer",
						"Tin va Khiem", "Idk", -2500),
				new Student("524k0006", "524k0006@student.tdtu.edu.vn", "Than Vu Gia", "12345", "Software Engineer",
						"Tin va Phuc", "Idk", 5.1),
				new Student("524k0031", "524k0031@student.tdtu.edu.vn", "Dinh Ngoc", "12345", "Software Engineer",
						"ITZone", "Idk", 7),
				new Student("524k0032", "524k0032@student.tdtu.edu.vn", "Tran Minh", "12345", "Software Engineer",
						"Ai ma biet", "Idk", 2),
				new Student("523v0005", "524v0005@student.tdtu.edu.vn", "Hong Bao", "12346", "Software Engineer",
						"AimaBiet2.0", "Idk", 8),
				new Student("524k0033", "524k0033@student.tdtu.edu.vn", "Huynh Trung", "12345", "Software Engineer",
						"Phuc va Khiem", "Idk", 100)
		};
	Student phuc = new Student();
	Scanner in = new Scanner();
		System.out.print(count(students, "IDk", "ok"));
	}
}