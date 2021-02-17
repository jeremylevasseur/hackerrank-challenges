import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        // Length
        System.out.println(A.length() + B.length());
        
        // Lexicographical check
        int asciiA = (int) A.charAt(0);
        int asciiB = (int) B.charAt(0);
        
        if (asciiB < asciiA) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        // Capatilizing and combining
        String newA = "";
        for (int i = 0; i < A.length(); i++) {
            if (i == 0) {
                newA = newA + Character.toUpperCase(A.charAt(i));
            } else {
                newA = newA + A.charAt(i);
            }
        }
        
        String newB = "";
        for (int i = 0; i < B.length(); i++) {
            if (i == 0) {
                newB = newB + Character.toUpperCase(B.charAt(i));
            } else {
                newB = newB + B.charAt(i);
            }
        }
        
        System.out.println(newA + " " + newB);

        
        
        
    }
}



