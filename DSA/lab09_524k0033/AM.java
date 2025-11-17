package lab09_524k0033;

import java.util.Scanner;

public class AM extends Graph{
	private int[][] am ;

	@Override
	public void read() {
		Scanner in = new Scanner(System.in);
		V= in.nextInt();
		E= in.nextInt();
		am= new int[V][V];
		for(int i=0;i<V;i++) {
			for(int j=0;j<V;j++) {
				am[i][j]=in.nextInt();
			}
		}
	in.close();
	}

	@Override
	public void print() {
		System.out.println(V+","+E);
		for(int i=0;i<V;i++) {
			for(int j=0;j<V;j++) {
				System.out.printf("%-3d",am[i][j]);
			}
		}
		System.out.println();
	}

	@Override
	public boolean isAdjacent(int v, int u) {
		return am[v][u]!=0;
	}


}
