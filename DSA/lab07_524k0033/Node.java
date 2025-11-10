package lab07_524k0033;

public class Node {
	Integer key;
	Node left, right;
	int height;

	public Node(Integer key) {
		this.key = key;
		this.height=0;
		this.left = this.right = null;
	}
}
