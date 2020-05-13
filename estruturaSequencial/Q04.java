package estruturaSequencial;

import java.util.Scanner;

public class Q04 {

	public static void main(String[] args) {

		Scanner e = new Scanner(System.in);
		double n1 = 0, n2 = 0, n3 = 0, n4 = 0, media;
		System.out.println("MÉDIA DAS QUATRO NOTAS ");

		System.out.println("Nota 01: ");
		n1 = e.nextDouble();
		System.out.println("Nota 02: ");
		n2 = e.nextDouble();
		System.out.println("Nota 03: ");
		n3 = e.nextDouble();
		System.out.println("Nota 04: ");
		n4 = e.nextDouble();

		media = (n1 + n2 + n3 + n4) / 4;

		System.out.println("Média: " + media);

	}

}
