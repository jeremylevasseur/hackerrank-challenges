package Challenges;

import java.util.Scanner;

public class FormattingStrings {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();
            //Complete this line
            String formattedString = String.format("%-15s", s1);
            String formattedInt = String.format("%03d", x);
            System.out.println(formattedString + formattedInt);
        }
        System.out.println("================================");
    }

}
