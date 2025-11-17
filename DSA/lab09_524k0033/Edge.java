package lab09_524k0033;

public class Edge {
	private int src;
	private int dest;
	private int weight;

	public Edge(int u, int v, int w) {
		this.src=u;
		this.dest=v;
		this.weight=w;
	}

	@Override
	public String toString() {
		return "Edge [src=" + src + ", dest=" + dest + ", weight=" + weight + "]";
	}

	
}
