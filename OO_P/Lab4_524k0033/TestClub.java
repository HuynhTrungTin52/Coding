package Lab4_524k0033;



public class TestClub {
    public static void main(String[] args) {
        Club club1 = new Club();
        System.out.println("Club 1 (Default): " + club1);

        Club club2 = new Club("Chelsea", 1, 2, 0);
        System.out.println("Club 2: " + club2);

        Club club3 = new Club(club2);
        System.out.println("Club 3 (Copy): " + club3);

        club1.setName("Liverpool");
        club1.setWins(5);
        club1.setDraws(3);
        club1.setLosses(2);
        System.out.println("Club 1 (Modified): " + club1);

        System.out.println("Club 1 Name: " + club1.getName());
        System.out.println("Club 1 Wins: " + club1.getWins());
        System.out.println("Club 1 Draws: " + club1.getDraws());
        System.out.println("Club 1 Losses: " + club1.getLosses());
        System.out.println("Club 1 Matches Played: " + club1.numMatchesPlayed());
        System.out.println("Club 1 Finished League: " + club1.isFinish());
        System.out.println("Club 1 Points: " + club1.getPoints());

        club2.setWins(10);
        club2.setDraws(0);
        club2.setLosses(0);
        System.out.println("Club 2 (Modified): " + club2);
        System.out.println("Club 2 Matches Played: " + club2.numMatchesPlayed());
        System.out.println("Club 2 Finished League: " + club2.isFinish());
    }
}
