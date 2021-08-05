package estruturaSequencial;

import java.util.Scanner;

public class Q11 {

	public static void main(String[] args) {

		Scanner e = new Scanner(System.in);

		int n1 = 0, n2 = 0;
		double n3 = 0, total = 0;

		System.out.println("Digite um número inteiro: ");
		n1 = e.nextInt();
		System.out.println("Digite novamente um número inteiro: ");
		n2 = e.nextInt();
		System.out.println("Digite um número real: ");
		n3 = e.nextInt();

		total = (n1 + n2 + n3);
		System.out.println("Soma total: " + total);
		System.out.println("----------------------------");

		System.out.println("Dobro do primeiro com a metade do segundo: " + (Math.pow(n1, 2) + n2 / 2));
		System.out.println("Soma do triplo do primeiro com o terceiro: " + (n1 * 3) + n3);
		System.out.println("O terceiro elevado ao cubo: " + Math.pow(n3, 3));
	}

}
