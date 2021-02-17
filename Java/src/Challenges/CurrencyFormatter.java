import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        Locale usLocale = new Locale("en", "US");
        Locale indiaLocale = new Locale("en", "IN");
        Locale chinaLocale = new Locale("zh", "CN");
        Locale franceLocale = new Locale("fr", "FR");
        
        NumberFormat usCurrencyFormat = NumberFormat.getCurrencyInstance(usLocale);
        NumberFormat indiaCurrencyFormat = NumberFormat.getCurrencyInstance(indiaLocale);
        NumberFormat chinaCurrencyFormat = NumberFormat.getCurrencyInstance(chinaLocale);
        NumberFormat franceCurrencyFormat = NumberFormat.getCurrencyInstance(franceLocale);
        
        String us = usCurrencyFormat.format(payment);
        String india = indiaCurrencyFormat.format(payment);
        String china = chinaCurrencyFormat.format(payment);
        String france = franceCurrencyFormat.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
