package Personal_Project;
import java.util.*;

public class GetMeANumber8 {
	
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	System.out.print("Enter the amount of money :");
	int money=in.nextInt();
	int five00k=0,one00k=0,five0k=0,two0k=0,one0k=0;
	if(money%10000!=0)
	{
		System.out.print("Invalid amount of money, ending program.");
		System.exit(1);
	}
	while(money>=500000)
	{
		five00k++;
		money-=500000;
	}
	while(money>=100000)
	{
		one00k++;
		money-=100000;
	}while(money>=50000)
	{
		five0k++;
		money-=50000;
	}while(money>=20000)
	{
		two0k++;
		money-=20000;
	}while(money>=10000)
	{
		one0k++;
		money-=10000;
	}
	System.out.println("You will have :");
	System.out.printf("%d 500k bill(s), %d 100k bill(s), %d 50k bill(s), %d 20k bill(s), %d 10k bill(s)",five00k,one00k,five0k,two0k,one0k);
	//Viết chương trình để xây dựng hệ thống đổi tiền như sau: Nhập vào số tiền (phải chia hết
	// cho 10000) cần đổi. Nếu nhập dữ liệu sai (số tiền không chia hết cho 10000) thì xuất ra thông báo
	// “Nhap du lieu sai” và kết thúc chương trình. Ngược lại, tính và xuất ra số tờ tờ tiền đổi được theo
	// mệnh giá ưu tiên từ lớn đến nhỏ 500000, 100000, 50000, 20000 và 10000.
	// Ví dụ: Nhập n = 15000 thì thông báo “Nhập dữ liệu sai và kêt thúc chương trình”.
	// Nhập n= 1380000  đổi: 2 tờ 500000, 3 tờ 100000, 1 tờ 50000, 1 tờ 20000, 1 tờ 10000.
	
	

	in.close();
	}

	
}
