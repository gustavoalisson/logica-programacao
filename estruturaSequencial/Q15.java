package estruturaSequencial;

import java.util.Scanner;

public class Q15 {

	public static void main(String[] args) {

		Scanner e = new Scanner(System.in);

		double horaSalario = 0;
		double horaMes = 0;
		double salarioBruto = 0, iRenda = 0, inss = 0, sindicato = 0, salarioLiquido = 0;

		System.out.println("Digite quando você ganha por hora: ");
		horaSalario = e.nextDouble();
		System.out.println("Digite o número de horas trabalhadas no mês: ");
		horaMes = e.nextDouble();

		salarioBruto = horaSalario * horaMes;
		iRenda = (11 * salarioBruto) / 100;
		inss = (8 * salarioBruto) / 100;
		sindicato = (5 * salarioBruto) / 100;
		salarioLiquido = (((salarioBruto - iRenda) - inss) - sindicato);
		

		System.out.println("Salário bruto: " + salarioBruto);
		System.out.println("Imposto de renda: " + iRenda);
		System.out.println("INSS: " + inss);
		System.out.println("Sindicato: " + sindicato);
		System.out.println("Salário Líquido: " + salarioLiquido);
		

	}

}
