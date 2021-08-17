import java.util.Scanner;

public class MotifFinding {

    static String result = "";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input your sequence: ");
        String s = sc.nextLine();
        System.out.println("Input your pattern: ");
        String t = sc.nextLine();
        System.out.println(output(s,t));
    }

    //return all locations of string s as a substring of string t
    public static String output(String s, String t) {
        for (int i = 0; i <= (s.length() - t.length()); i++) {
            if(s.charAt(i) == t.charAt(0))
                if(s.substring(i, i+t.length()).equals(t)) {
                    if(result.equals(""))
                        //you do i+1 because the index position is in this case assumed to start at 1 for the pattern as well as sequence
                        result += (i+1);
                    else
                        result += " "+ (i+1);
                }
        }

        return result;
    }

}