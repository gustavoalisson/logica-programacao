package estruturaSequencial;

import java.util.Scanner;

public class Q08 {

	public static void main(String[] args) {
		/*
		 * Faça um Programa que pergunte quanto você ganha por hora e o número de horas
		 * trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
		 */
		Scanner e = new Scanner(System.in);
		double hTrabalhadas = 0, totalMes = 0;
		int horas;
		
		System.out.println("Quanto você ganha por hora ? ");
		hTrabalhadas = e.nextDouble();
		System.out.println("Número de horas trabalhadas no mês: ");
		horas = e.nextInt();
		
		totalMes = hTrabalhadas * horas;
		
		System.out.println("Salário no mês: R$ " + totalMes);
		
		

	}

}
