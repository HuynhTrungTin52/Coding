package exercises;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;
import java.util.List;

class BankAccount {
    private String accountNumber;
    private double balance;
    private List<Transaction> transactions;

    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
        this.transactions = new ArrayList<>();
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void addTransaction(Transaction transaction) {
        this.transactions.add(transaction);
    }

    public List<Transaction> getTransactions() {
        return transactions;
    }

    // Non-static nested class (member class)
    public class Transaction {
        private String type;
        private double amount;
        private LocalDate date;

        public Transaction(String type, double amount, LocalDate date) {
            this.type = type;
            this.amount = amount;
            this.date = date;
        }

        public String getType() {
            return type;
        }

        public double getAmount() {
            return amount;
        }

        public LocalDate getDate() {
            return date;
        }

        @Override
        public String toString() {
            return "Transaction{" +
                   "type='" + type + '\'' +
                   ", amount=" + amount +
                   ", date=" + date +
                   '}';
        }
    }
}

public class BankTransactionHistory {
    public static void main(String[] args) {
        BankAccount myAccount = new BankAccount("1234567890", 1000.0);

        // Explicitly create transactions with dates in the previous month (April 2025)
        myAccount.addTransaction(myAccount.new Transaction("Deposit", 500.0, LocalDate.of(2025, Month.APRIL, 5)));
        myAccount.addTransaction(myAccount.new Transaction("Withdrawal", -200.0, LocalDate.of(2025, Month.APRIL, 15)));
        myAccount.addTransaction(myAccount.new Transaction("Deposit", 100.0, LocalDate.of(2025, Month.APRIL, 25)));
        // Add a transaction in the current month to demonstrate filtering
        myAccount.addTransaction(myAccount.new Transaction("Withdrawal", -50.0, LocalDate.now()));

        // Get the current date and the date of the previous month
        LocalDate now = LocalDate.now();
        LocalDate previousMonthStart = now.minusMonths(1).withDayOfMonth(1);
        LocalDate previousMonthEnd = now.minusMonths(1).withDayOfMonth(now.minusMonths(1).lengthOfMonth());

        System.out.println("\nTransactions for account: " + myAccount.getAccountNumber() + " in the previous month (" + previousMonthStart.getMonth() + "):");

        // Iterate through the transactions and print those from the previous month
        for (BankAccount.Transaction transaction : myAccount.getTransactions()) {
            if (transaction.getDate().isAfter(previousMonthStart.minusDays(1)) && transaction.getDate().isBefore(previousMonthEnd.plusDays(1))) {
                System.out.println(transaction);
            }
        }
    }
}