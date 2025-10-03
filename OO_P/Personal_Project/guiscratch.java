package Personal_Project;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class guiscratch {
	
	public static void main(String[] args) {
		JFrame frame = new JFrame("Testing");
		JPanel panel1 = new JPanel();
		JLabel label = new JLabel("You stupid");
		JLabel label2 = new JLabel();
		panel1.add(label);
		panel1.add(label2);
		frame.add(panel1);
		frame.setSize(300, 200);

		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		frame.setVisible(true);
	}
}
