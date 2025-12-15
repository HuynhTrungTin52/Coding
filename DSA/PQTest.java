import java.util.Comparator;
import java.util.PriorityQueue;

public class PQTest {
	public static void main(String[] args) {
        // The list of keys
        Integer[] keys = {89, 40, 46, 55, 54, 5, 50, 73, 23, 47};

        // Create the custom comparator
        Comparator<Integer> customComparator = (a, b) -> {
            boolean isAEven = a % 2 == 0;
            boolean isBEven = b % 2 == 0;

            // 1. Even numbers have higher priority than odd ones (Rule a)
            if (isAEven && !isBEven) {
                return -1; // a is Even, b is Odd -> a has higher priority
            }
            if (!isAEven && isBEven) {
                return 1;  // a is Odd, b is Even -> b has higher priority
            }

            // 2. Both have the same parity
            if (isAEven && isBEven) {
                // Both are Even (Rule b: Larger has higher priority - Max-Heap)
                return b - a; 
            } else {
                // Both are Odd (Rule c: Smaller has higher priority - Min-Heap)
                return a - b; 
            }
        };

        // Initialize the PriorityQueue with the custom comparator
        PriorityQueue<Integer> customPQ = new PriorityQueue<>(customComparator);

        // Add all keys to the PriorityQueue
        for (int key : keys) {
            customPQ.add(key);
        }

        System.out.println("The PriorityQueue (internal order may vary): " + customPQ);
        
        // Iteratively extract items to demonstrate the custom priority order
        System.out.println("\nItems extracted in order of priority (Highest to Lowest):");
        while (!customPQ.isEmpty()) {
            System.out.print(customPQ.poll() + " ");
        }
        // Output will be: 54 50 46 40 (Evens, largest first) then 5 23 47 55 73 89 (Odds, smallest first)
    }
}

