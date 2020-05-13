package estruturaSequencial;

import java.util.Scanner;

public class Q09 {
	// C = (5 * (F-32) / 9).
	public static void main(String[] args) {
		Scanner e = new Scanner(System.in);
		System.out.println("Temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius");

		double f, c;
		System.out.println("Graus Farenheit: ");
		f = e.nextDouble();
		c = (5 * (f - 32) / 9);
		System.out.println("Graus Celsius: " + c);

	}

}
