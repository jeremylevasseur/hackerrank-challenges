package Challenges;

import java.util.Scanner;

public class Loops {

    public static void main(String[] args) {
        int q = 2;
        int[] a = {0, 5};
        int[] b = {2, 3};
        int[] n = {10, 5};

        for (int i = 0; i < q; i++) {

            String outputString = "";
            int oldSum = a[i];
            for (int j = 0; j < n[i]; j++) {
                int seriesElementSum = (int) ((Math.pow(2, j) * b[i])) + oldSum;
                outputString += seriesElementSum + " ";
                oldSum = seriesElementSum;
            }

            System.out.println(outputString);

        }
    }
}
