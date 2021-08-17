import java.util.Scanner;

public class DnaIntoRna {

    public static String transcription (String seq1) {

try {
    for (int i = 0; i <= seq1.length(); i++) {

        if (seq1.charAt(i) == 'T') {
            seq1 = seq1.replace('T', 'U');

        }

    }
}catch(IndexOutOfBoundsException e){
    e.getMessage();
}
        return seq1;
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Input your sequence please: ");
        String seq1 = input.next();


        System.out.println(transcription(seq1));


    }

}

