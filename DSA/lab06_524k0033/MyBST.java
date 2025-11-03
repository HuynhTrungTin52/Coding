package lab06_524k0033;

public class MyBST {
	private Node root;

	private Node insert(Node x, Integer key) {
		if (x == null)
			return new Node(key);
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			x.left = insert(x.left, key);
		else if (cmp > 0)
			x.right = insert(x.right, key);
		else

			x.key = key;
		return x;
	}

	public void insert(Integer key) {
		root = insert(root, key);
	}

	private void NLR(Node x) {
		if (x != null) {
			System.out.print(x.key + " ");
			NLR(x.left);
			NLR(x.right);
		}
	}

	private void LNR(Node x) {
		if (x != null) {
			LNR(x.left);
			System.out.print(x.key + " ");
			LNR(x.right);
		}
	}

	private void LRN(Node x) {
		if (x != null) {
			LRN(x.left);
			LRN(x.right);
			System.out.print(x.key + " ");
		}
	}
	//Ex3
	public static void RNL(Node x) {
		if (x != null) {
			RNL(x.right);
			System.out.print(x.key + " ");
			RNL(x.left);
		}
	}
	public void NLR() {
		NLR(root);
	}

	public void LNR() {
		LNR(root);
	}

	public void LRN() {
		LRN(root);
	}
	
	public void RNL() {
		RNL(root);
	}
	private boolean contains(Node x, Integer key) {
		if (x == null)
			return false;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			return contains(x.left, key);
		else if (cmp > 0)
			return contains(x.right, key);
		else
			return true;
	}
	
	public boolean contains(Integer key) {
		return contains(root, key);
	}
	private Node search(Node x, Integer key) {
		if (x == null)
			return null;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			return search(x.left, key);
		else if (cmp > 0)
			return search(x.right, key);
		else
			return x;
	}

	public Node search(Integer key) {
		return search(root, key);
	}

	private Node min(Node x) {
		if (x.left == null)
			return x;
		else
			return min(x.left);
	}

	private Node max(Node x) {
		if (x.right == null)
			return x;
		else
			return min(x.right);
	}

	public Node min() {
		return min(root);
	}

	public Node max() {
		return max(root);
	}

	private Node deleteMin(Node x) {
		if (x.left == null)
			return x.right;
		x.left = deleteMin(x.left);
		return x;
	}

	public void deleteMin() {
		root = deleteMin(root);
	}

	private Node deleteMax(Node x) {
		if (x.right == null)
			return x.left;
		x.right = deleteMin(x.right);
		return x;
	}

	public void deleteMax() {
		root = deleteMax(root);
	}

	private Node delete(Node x, Integer key) {
		if (x == null)
			return null;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			x.left = delete(x.left, key);
		else if (cmp > 0)
			x.right = delete(x.right, key);
		else {
			// node with only one child or no child
			if (x.right == null)
				return x.left;
			if (x.left == null)
				return x.right;

			// node with two children: Get the successor (smallest in the right subtree)
			x.key = min(x.right).key;
			x.right = deleteMin(x.right);
		}
		return x;
	}

	public void delete(Integer key) {
		root=delete(root, key);
	}

	public static void main(String[] args) {
		Integer[] array = {42, 21, 62, 2, 29, 46, 93, 26, 48, 82, 96, 52, 74, 87, 94, 85};
		MyBST bst = new MyBST();


		for(Integer value : array) {
			bst.insert(value);
		}
		bst.LNR();
		bst.deleteMax();
		bst.deleteMin();
		System.err.println();
		bst.LNR();
	}

}
