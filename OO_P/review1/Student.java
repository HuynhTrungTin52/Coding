package review1;

public class Student{
	public String StudentID;
	public String Email;
	public String Surname;
	public String CourseID;
	public String CourseName;
	public String Group;
	public String Sub;
	public double scores;

	public Student() {
		StudentID="";
		Email="";
		Surname="";
		CourseID="";
		CourseName="";
		Group="";
		Sub="";
		scores=0;
	}

	public Student( String StudentID,String Email,String Surname,String CourseID,String CourseName,String Group,String Sub,double scores) {
		this.StudentID=StudentID;
		this.Email=Email;
		this.Surname=Surname;
		this.CourseID=CourseID;
		this.CourseName=CourseName;
		this.Group=Group;
		this.Sub=Sub;
		this.scores=scores;
	}
}