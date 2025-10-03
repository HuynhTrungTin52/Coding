
import java.util.*;

class Jaba {
    public static double[] decimals(double[] a) throws NoSuchElementException {
        List<Double> resultList = new ArrayList<>();
        for (double num : a) {
            double decimalPart = num - Math.floor(num);
            if (decimalPart < 0.5) {
                resultList.add(num);
            }
        }

        if (resultList.isEmpty()) {
            throw new NoSuchElementException("No elements found with a decimal part less than 0.5.");
        }

        double[] resultArray = new double[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            resultArray[i] = resultList.get(i);
        }
        return resultArray;
    }

    public static void main(String[] args) {
        double[] arr1 = {12.345, 7.89, 5.0, 9.12, 10.7};
        double[] arr2 = {0.6, 1.8, 2.9};
        double[] arr3 = {3.0, 4.0, 5.0};
        try {
            double[] result1 = Jaba.decimals(arr1);
            System.out.print("Elements with decimal part < 0.5 in arr1: ");
            for (double num : result1) {
                System.out.print(num + " ");
            }
            System.out.println();
        } catch (NoSuchElementException e) {
            System.out.println("Error processing arr1: " + e.getMessage());
        }

        try {
            double[] result2 = Jaba.decimals(arr2);
            System.out.print("Elements with decimal part < 0.5 in arr2: ");
            for (double num : result2) {
                System.out.print(num + " ");
            }
            System.out.println();
        } catch (NoSuchElementException e) {
            System.out.println("Error processing arr2: " + e.getMessage());
        }

        try {
            double[] result3 = Jaba.decimals(arr3);
            System.out.print("Elements with decimal part < 0.5 in arr3: ");
            for (double num : result3) {
                System.out.print(num + " ");
            }
            System.out.println();
        } catch (NoSuchElementException e) {
            System.out.println("Error processing arr3: " + e.getMessage());
        }
    }
}