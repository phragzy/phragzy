import java.util.Scanner;

public class GasMileage {
    public static void main(String[] args) {
        
        Scanner trips = new Scanner(System.in);
        int x = 0;
        int y = 0;
        int counter = 0;
        int miles = 0;
        int gallons =0;
        while ((miles != -1) && (gallons != -1)){
            if (miles == 1|| gallons == -1){
        System.out.println("Enter Miles driven or -1 to quit: ");
        miles = trips.nextInt();
        System.out.println("Enter gallons used or -1 to quit: ");
        gallons = trips.nextInt();

        x += miles;
        y += gallons;
        counter++;
        double mpg = miles / gallons;
        System.out.println("Trip " + counter + " MPG: " + mpg);
        System.out.println("Total Trip Miles: " + x + " Total Gallons: " + y + " Total MPG: " + mpg);
        trips.close();
            }
        }
    }
}