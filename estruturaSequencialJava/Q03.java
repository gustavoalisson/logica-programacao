package estruturaSequencial;

import java.util.Scanner;

public class Q03 {

	public static void main(String[] args) {
		Scanner e = new Scanner(System.in);

		double a = 0, b = 0;
		System.out.println("==SOMA DE DOIS NÚMEROS==");
		System.out.println("Digite o primeiro número: ");
		a = e.nextDouble();
		
		System.out.println("Digite o segundo número: ");
		b = e.nextDouble();
		
		System.out.println("A soma é igual a " + (a+b));

	}

}
