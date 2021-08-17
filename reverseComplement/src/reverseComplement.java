public class reverseComplement {
    public static void reverseComplement(String pattern){
        StringBuilder builder = new StringBuilder();

        for(int i=0;i<pattern.length();i++){
            char c = pattern.charAt(i);
            if(pattern.charAt(i) == 'T'){
                builder.append('A');
            }
            if(pattern.charAt(i) == 'A'){
                builder.append('T');
            }
            if(pattern.charAt(i) == 'C'){
                builder.append('G');
            }
            if(pattern.charAt(i) == 'G'){
                builder.append('C');
            }
        }
        String reverse = "";


        for(int i = builder.length() - 1; i >= 0; i--)
        {
            reverse = reverse + builder.charAt(i);
        }
        System.out.println("Reversed string is:");
        System.out.println(reverse);
        //return builder.toString();
    }
    public static void main(String[] args) {
           String pattern = args[0];
           //Methode namens revereseComplement mit String aus Kommandozeile als Input für den Parameter
           //Output gibt das revereseComplement zurück
           reverseComplement(pattern);
    }
}
