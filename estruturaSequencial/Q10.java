package estruturaSequencial;

import java.util.Scanner;

public class Q10 {

	public static void main(String[] args) {
		Scanner e = new Scanner(System.in);
		int c = 0, f = 0;
		System.out.println("Temperatura em graus Celsius, transforme e mostre em graus Farenheit.");

		System.out.println("Celsius: ");
		c = e.nextInt();

		f = (int)(c * 1.8 + 32);
		System.out.println("Farenheit: " + f);
	}

}
