public class Prisoners implements Comparable<Prisoners>{
	String name;
	int priority;

	public Prisoners(String name, int priority) {
		this.name=name;
		this.priority=priority;
	}

	public String getName() {
		return name;
	}

	public int getPriority() {
		return priority;
	}

	@Override
	public int compareTo(Prisoners p) {
		return this.priority-p.priority;
	}
	
}
