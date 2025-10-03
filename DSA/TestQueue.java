import java.util.*;

public class TestQueue {

	public static int reverseInt(int num) {
		Queue<Integer> que= new LinkedList<>();
		while(num>0) {
			que.offer(num%10);
			num/=10;
		}
		int r=0;
		int i=0;
		while(!que.isEmpty()) {
			r=(10*r)+que.poll();
			i++;
		}
		return r;
	}
	public static void main(String[] args) {

	System.out.print(reverseInt(12308124));	
	}
}
