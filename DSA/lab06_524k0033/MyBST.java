package lab06_524k0033;

import java.util.*;


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

	private int height(Node x, Integer key,int level) {
		if (x == null)
			return -1;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			return height(x.left, key,level+1);
		else if (cmp > 0)
			return height(x.right, key,level+1);
		else
			return level;
	}

	public int height(Integer key) {
		return height(root, key,0);
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
			return max(x.right);
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
		root = deleteMax(root);
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

	private Node delete_succ(Node x, Integer key) {
		if (x == null)
			return null;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			x.left = delete_succ(x.left, key);
		else if (cmp > 0)
			x.right = delete_succ(x.right, key);
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
	
	public void delete_succ(Integer key) {
		root=delete_succ(root, key);
	}

	private Node delete_pre(Node x, Integer key) {
		if (x == null)
			return null;
		int cmp = key.compareTo(x.key);
		if (cmp < 0)
			x.left = delete_pre(x.left, key);
		else if (cmp > 0)
			x.right = delete_pre(x.right, key);
		else {
			// node with only one child or no child
			if (x.right == null)
				return x.left;
			if (x.left == null)
				return x.right;

			// node with two children: Get the predecessor (largest in the left subtree)
			x.key = max(x.left).key;
			x.left = deleteMax(x.left);
		}
		return x;
	}

	public void delete_pre(Integer key) {
		root=delete_pre(root, key);
	}
	
	private int sum(Node x) {
		if(x==null) {
			return 0;
		}
		return x.key+sum(x.left)+sum(x.right);
	}

	public int sum() {
		return sum(root);
	}
	private int sumInRange(Node x, int a, int b) {
		if (x == null) return 0;
		int sum = 0;
		int key = x.key;
		if (key >= a && key <= b) sum += key;
		if (key > a) sum += sumInRange(x.left, a, b);
		if (key < b) sum += sumInRange(x.right, a, b);
		return sum;
	}

	public int sumInRange(int a, int b) {
		if (a > b) {
			int t = a; a = b; b = t;
		}
		return sumInRange(root, a, b);
	}
	private int sumEven(Node x) {
		if(x==null) {
			return 0;
		}
		if(x.key%2==0) {
			return x.key+sumEven(x.left)+sumEven(x.right);
		}
		return sumEven(x.left)+sumEven(x.right);
	}

	public int sumEven() {
		return sumEven(root);
	}

	private int countLeaves(Node x) {
		if(x==null) {
			return 0;
		}
		if(x.right==null && x.left==null) {
			return 1;
		}
		return countLeaves(x.left)+countLeaves(x.right);
	}

	public int countLeaves() {
		return countLeaves(root);
	}
	private int countOneChild(Node x) {
		if (x == null) return 0;
		int children = (x.left != null ? 1 : 0) + (x.right != null ? 1 : 0);
		int self = (children == 1) ? 1 : 0;
		return self + countOneChild(x.left) + countOneChild(x.right);
	}

	public int countOneChild() {
		return countOneChild(root);
	}
	// Count nodes in a subtree (helper)
	private int count(Node x) {
		if (x == null) return 0;
		return 1 + count(x.left) + count(x.right);
	}

	// Size of the whole tree
	public int count() {
		return count(root);
	}

	// Size of the subtree rooted at the node with the given key
	public int count(Integer key) {
		return count(search(key));
	}

	private int sumEvenKeysAtLeaves(Node x) {
		if(x==null) {
			return 0;
		}
		if(x.right==null && x.left==null && x.key%2==0) {
			return x.key;
		}
		return sumEvenKeysAtLeaves(x.left)+sumEvenKeysAtLeaves(x.right);
	}

	public int sumEvenKeysAtLeaves() {
		return sumEvenKeysAtLeaves(root);
	}

	private void bfs(Node x) {
		if(x!=null) {
			Queue<Node> queue = new LinkedList<Node>();
       queue.add(root);
       while (!queue.isEmpty()) {
           Node temp = queue.poll();
           System.out.print(temp.key + " ");

           if (temp.left != null) {
               queue.add(temp.left);
           }

           if (temp.right != null) {
               queue.add(temp.right);
           }
       }
		}
	}
	public void bfs() {
		bfs(root);
	}
	public static void main(String[] args) {
		Integer[] array = {42, 21, 62, 2, 29, 46, 93, 26, 48, 82, 52, 74,85, 87, 94, 96};
		MyBST bst = new MyBST();

		for(Integer value : array) {
			bst.insert(value);
		}
		bst.bfs();
		System.out.print(bst.count(Node(42)));
	}

}
