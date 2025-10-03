package Personal_Project;

import java.util.Scanner;

public class ticTacToe {

	private static void printTheBoard(char[] board) {
		System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
		System.out.println(" - + - + - ");
		System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
		System.out.println(" - + - + - ");
		System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
	}
	public static void restart(char[] board)
	{
		for(int i=0;i<9;i++)
		{
			board[i]=(char)('1'+i);
		}
	}
        @SuppressWarnings("ConvertToTryWithResources")
	public static void main(String[] args) {
		char[] board = { '1', '2', '3',
				'4', '5', '6',
				'7', '8', '9' };
		int numberOfTurns = 0;
		char turn = 'x';
		Scanner in = new Scanner(System.in);
		while (numberOfTurns <= 9) {
			if(numberOfTurns==9)
			{
				System.out.println("Tied ! Would you like to try again ? Y/N");
				char retry = in.next().charAt(0);
				if(retry=='Y')
				{
					restart(board);
					numberOfTurns=0;
					turn='x';
				}else break; 
			}
			printTheBoard(board);
			System.out.printf("Choose a square player %s : ", turn);
			
			int input = in.nextInt();
			board[input - 1] = turn;
			if ((board[0] + board[1] + board[2] == (turn * 3)) // first row
					|| (board[3] + board[4] + board[5] == (turn * 3)) // second row
					|| (board[6] + board[7] + board[8] == (turn * 3)) // third row
					|| (board[0] + board[3] + board[6] == (turn * 3)) // first column
					|| (board[1] + board[4] + board[7] == (turn * 3)) // second column
					|| (board[2] + board[5] + board[8] == (turn * 3)) // third column
					|| (board[0] + board[4] + board[8] == (turn * 3)) // first diagonal
					|| (board[2] + board[4] + board[6] == (turn * 3)) // second diagonal
			) {
				printTheBoard(board);
				System.out.println("You won!!! Congratulations!");
				break;
			} else {
				numberOfTurns++;
				turn = (turn == 'x') ? 'o' : 'x';
			}
		
		}
	in.close();
	}
}
