package estruturaSequencial;

import java.util.Scanner;

public class Q14 {

	public static void main(String[] args) {
		// 50 kilos
		// multa de 4 reais

		Scanner e = new Scanner(System.in);

		double pesoPeixe = 0;
		double excessoPeixe = 0;
		double multa = 0;

		System.out.println("Digite o peso de peixes: ");
		pesoPeixe = e.nextDouble();
		excessoPeixe = pesoPeixe - 50;
		System.out.println("Excesso de peso ultrapassado: " + excessoPeixe + " quilos");

		multa = excessoPeixe * 4;
		System.out.println("Você deverá pagar uma multa de : " + multa + "R$");

	}

}
