package lab09_524k0033;
import java.util.*;

class AL extends Graph{
    LinkedList<Edge>[] al;

    public AL(LinkedList<Edge>[] al,int V,int E) {
        this.V=V;
        this.E=E;
        this.al=al;
    }

    public AL() {

    }

    @SuppressWarnings("unchecked")
    @Override
    public void read() {
        Scanner sc = new Scanner(System.in);
        V = sc.nextInt();
        E = sc.nextInt();
        al = new LinkedList[V]; // null
        for(int i = 0; i < V; i++) {
            al[i] = new LinkedList<>();
        }
        int u, v, w;
        for(int i = 0; i < E; i++) {
            u = sc.nextInt();
            v = sc.nextInt();
            w = sc.nextInt();
            al[u].add(new Edge(u, v, w));
            al[v].add(new Edge(v, u, w));
        }
        sc.close();
    }

    @Override
    public void print() {
        System.out.println(V + ", " + E);
        for(int i = 0; i < V; i++) {
            System.out.print(i + ": ");
            System.out.println(al[i]);
        }
    }

    @Override
    public boolean isAdjacent(int u, int v) {
        for(Edge e: al[u]) {
            if (e.dest == v) {
                return true;
            }
        }
        return false;
    }

	public static void main(String[] args) {
		AL graph = new AL();
		graph.read();
		graph.print();
	}
}
