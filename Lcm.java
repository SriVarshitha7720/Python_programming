import java.util.Scanner;
public class LCM {
  static int getGCD(int a, int b) {
    // Generate factors of a
    int gcd = 1;
    for (int i = 1; i <= a; i++) {
      if (a % i == 0 && b % i == 0) {
        gcd = i;
      }
    }
    return gcd;
  }
  static int getLCM(int a, int b) {
    // Generate the multiples of any number
    int i = 1;
    int lcm = 1;
    while (true) {
      // Generating the multiples of a
      int m = a * i;
      if (m % b == 0) {
        lcm = m;
        break;
      }
      i++;
    }
    return lcm;
  }
  public static void main(String[] args) {
    Scanner read = new Scanner(System.in);
    int a = read.nextInt();
    int b = read.nextInt();
    System.out.println(getLCM(a, b));
    System.out.println(getGCD(a, b));
  }
}