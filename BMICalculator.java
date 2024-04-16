/*
Sources: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/
Program calculates the Body Mass Index (BMI) based on weight in pounds and height in inches.
BMI meant to be calculated ages 2+. Average weight of a 2 year old is 24 lbs and average height is 30 inches.
1400 lb and 108 in max.
BMI formula: weight (lb) / [height (in)]^2 * 703
*/

import java.util.InputMismatchException;
import java.util.Scanner;

public class BMICalculator {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        boolean continueCalc = true;

        while (continueCalc) {
            System.out.println("Welcome to the BMI Calculator!");
            System.out.println("Enter your weight in pounds:");
            double weight = Inputs(scan, 24, 1400);
            if (weight == -1){
                break;
            }

            System.out.println("Enter your height in inches:");
            double height = Inputs(scan, 30, 108);
            if (height == -1){
                break; 
            } 

            double bmi = calculateBMI(weight, height);
            System.out.printf("Your BMI is: %.2f\n", bmi);

            category(bmi);

            System.out.println("Do you want to calculate again? (yes/no)");
            String answer = scan.next().toLowerCase();
            if (!answer.equals("yes")) {
                continueCalc = false;
            }
        }

        System.out.println("Thank you for using the BMI Calculator!");
    }

    
    //Calculates the BMI 
    public static double calculateBMI(double weight, double height) {
        return (weight / (height * height)) * 703;
    }

    //checks input
    public static double Inputs(Scanner scan, double min, double max) {
        while (true) {
            String inputStr = scan.next();
            if (inputStr.equalsIgnoreCase("quit")){
                return -1;
            }

            try {
                double input = Double.valueOf(inputStr);
                if (input < min | input > max) {
                    System.out.println("Invalid input.");
                } else {
                    return input;
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }

        }
    }

    //3RD METHOD
    public static void category(double bmi) {
        System.out.println("These are the different BMI categories:\nUnderweight = <18.5\nNormal weight = 18.5-24.9\nOverweight = 25-29.9\nObesity = BMI of 30 or greater.");
        if (bmi < 18.5) {
            System.out.println("Your BMI places you into the Underweight category.");
        } else if (bmi >= 18.5 & bmi <= 24.9) {
            System.out.println("Your BMI places you into the Normal Weight category.");
        } else if (bmi >= 25 & bmi <= 29.9) {
            System.out.println("Your BMI places you into the Overweight category.");
        } else {
            System.out.println("Your BMI places you into the Obesity category.");
        }
    }
}





