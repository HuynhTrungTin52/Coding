package lab06_524k0033;

public class Ex2 {
	
	public static MyBST createTree(String strKey) {
		MyBST res = new MyBST();

		for(String split_value : strKey.split(" ")) {
			res.insert(Integer.parseInt(split_value));
		}
		return res;
	}
	public static void main(String[] args) {
		MyBST bst = new MyBST();
		String str= "42 21 62 2 29 46 93 26 48 82 96 52 74 87 94 85";
		
		bst=createTree(str);
		bst.LNR();
	}	
}
