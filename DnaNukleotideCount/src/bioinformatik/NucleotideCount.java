package bioinformatik;

import java.util.Scanner;

//Was tut der Code?
//Bei Eingabe eines Strings wir die Anzahl an Adenin, Thymin, Cytosin, Guanin ausgegeben.

public class NucleotideCount {

    public static void main(String[] args) {

        // Input the DNA string;
        System.out.println("Please input the DNA string:");
        Scanner input = new Scanner(System.in);
        System.out.print("Sequenz: ");
        String sequence = input.next();
        input.close();

        //Lokale Variablen
        int counterA = 0;
        int counterT = 0;
        int counterC = 0;
        int counterG = 0;

        try {
            for (int i = 0; i <= sequence.length(); i++) {

                if (sequence.charAt(i) == 'A') {
                    counterA++;
                }
                if (sequence.charAt(i) == 'T') {
                    counterT++;
                }
                if (sequence.charAt(i) == 'C') {
                    counterC++;
                }
                if (sequence.charAt(i) == 'G') {
                    counterG++;
                }
            }
        }catch (IndexOutOfBoundsException e){
            e.getMessage();
        }
        System.out.println( "Folgende Basen kommen vor: " + " " + counterA +" "+ counterT + " " +counterC + " "+ counterG);

    }

}
