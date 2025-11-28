package lab09_524k0033;
import java.util.*;

class EL extends Graph {
    LinkedList<Edge> edges;

    @Override
    public void read() {
        Scanner sc = new Scanner(System.in);
        V = sc.nextInt();
        E = sc.nextInt();
        edges = new LinkedList<>();
        int u, v, w;
        for(int i = 0; i < E; i++) {
            u = sc.nextInt();
            v = sc.nextInt();
            w = sc.nextInt();
            edges.add(new Edge(u, v, w));
        }
        sc.close();
    }

    @Override
    public void print() {
        System.out.println(V + ", " + E);
        for(Edge e: edges) {
            System.out.println(e);
        }
    }

    @Override
    public boolean isAdjacent(int u, int v) {
        for(Edge e: edges) {
            if (e.src == u && e.dest == v) {
                return true;
            }
        }
        return false;
    }

	public static void main(String[] args) {
		EL graph = new EL();
		graph.read();
		graph.print();
	}
}
