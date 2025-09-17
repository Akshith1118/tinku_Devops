public class Palindrome {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide a word to check!");
            return;
        }
        String word = args[0];  
        if (isPalindrome(word)) {
            System.out.println(word + " is a palindrome!");
        } else {
            System.out.println(word + " is NOT a palindrome!");
        }
    }

    public static boolean isPalindrome(String str) {
        String reversed = new StringBuilder(str).reverse().toString();
        return str.equalsIgnoreCase(reversed);
    }
}
