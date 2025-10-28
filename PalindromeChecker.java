public class PalindromeChecker {
    public static boolean isPalindrome(String text) {
        int left = 0;
        int right = text.length() - 1;
        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            String input = args[0];
            if (isPalindrome(input)) {
                System.out.println(input + " is a palindrome");
                System.exit(0);
            } else {
                System.out.println(input + " is not a palindrome");
                System.exit(1);
            }
        } else {
            System.out.println("Usage: java PalindromeChecker <string>");
            System.exit(2);
        }
    }
}
