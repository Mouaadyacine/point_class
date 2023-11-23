public class Main {
    public static void main(String[] args) {
        Point pts1 = new Point(4, 3);
        System.out.println("Distance is: " + pts1.distance(new Point(0, 0)));
        System.out.println("Norm: " + pts1.norm());
        }
    }