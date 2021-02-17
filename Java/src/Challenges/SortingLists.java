import java.util.Scanner;

public class SortingLists {

    public static String getSmallestAndLargest(String s, int k) {
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        java.util.ArrayList<String> substrings = new java.util.ArrayList<String>();
        for (int i = 0; i < s.length() - k + 1; i++) {
            substrings.add(s.substring(i, k + i));
        }
        
        java.util.Collections.sort(substrings);
        java.util.Collections.reverse(substrings);
        
        return substrings.get(s.length() - k) + "\n" + substrings.get(0);

    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}