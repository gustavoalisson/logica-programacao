package estruturaSequencial;

import java.util.Scanner;

public class Q13 {

	/*
	 * Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
	 * que calcule seu peso ideal, utilizando as seguintes fórmulas:
	 * 
	 * Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7
	 */

	public static void main(String[] args) {

		double altura = 0;
		String sexo;
		double pesoIdeal = 0;

		Scanner e = new Scanner(System.in);
		System.out.println("Digite a sua altura: ");
		altura = e.nextDouble();
		System.out.println("Digite o seu sexo [M/ Homens e F/ para mulheres] : ");
		sexo = e.next();

		if (sexo.equals("M")) {
			pesoIdeal = (72.7 * altura) - 58;
			System.out.println("Peso ideal: " + pesoIdeal);
		} else if (sexo.equals("F")) {
			pesoIdeal = (62.1 * altura) - 44.7;
			System.out.println("Peso ideal: " + pesoIdeal);
		} else {
			System.out.println("Digite um sexo válido. Apenas[M] ou [F]");

		}

	}

}
