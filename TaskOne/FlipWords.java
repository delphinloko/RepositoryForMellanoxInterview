package TaskOne;

public class FlipWords {
    public static void main(String[] args) {
        String input = "The quick brown fox jumps over the lazy dog";
        String[] foo = input.split(" ");
        for (int i = foo.length - 1; i >= 0; i--) {
            System.out.print(foo[i] + " ");
        }
    }
}
