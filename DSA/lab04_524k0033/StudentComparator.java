package lab04_524k0033;

import java.util.Comparator;

public  class StudentComparator implements Comparator<Student>  {
	@Override
	public int compare(Student s1, Student s2) {
		if(s1.avg>s2.avg) {
			return 1;
		} else if(s1.avg<s2.avg) {
			return -1;
		} else return 0;
	}

}