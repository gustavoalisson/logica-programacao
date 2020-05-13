package estruturaSequencial;

import java.util.Scanner;

public class Q16 {

	public static void main(String[] args) {

		// tinta lata de 18 litros custa 80 reais.
		double metros = 0, vLitros = 0, qtdLatas = 0, precoTotal = 0;
	
		Scanner e = new Scanner(System.in);
		System.out.println("== Loja de Tintas ==");

		System.out.println("Metros quadrados da área: ");
		metros = e.nextDouble();
		
		vLitros = (metros / 3);
		qtdLatas = vLitros / 18;
		precoTotal = qtdLatas * 80;
		
		System.out.println("Quantidade de latas de tinta necessária: " + Math.round(qtdLatas));
		System.out.printf("Preço total: %.2f " , precoTotal);
		
	}
}
