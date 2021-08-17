import java.util.Scanner;

public class CountingPointMutations {


    public static int output(String s, String t) {
        //Given two strings of equal length, the Hamming distance is the # of corresponding symbols that are different from each other
        int hammingDistance = 0;

        //both strings are of equal length
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) != t.charAt(i))
                hammingDistance++;
        }

        return hammingDistance;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please input your first sequence here: ");
        String s = sc.nextLine();
        System.out.println("Please input your second sequence here: ");
        String t = sc.nextLine();

        System.out.println("The hamming distance is: " + output(s,t));
    }
}
