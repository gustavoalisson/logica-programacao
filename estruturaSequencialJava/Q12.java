package estruturaSequencial;

import java.util.Scanner;

public class Q12 {

	public static void main(String[] args) {
        
		/* 
		 * Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
		 * calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
		 */
		
		Scanner entrada = new Scanner(System.in);
		
		double altura = 0;
		
		
		System.out.println("Digite a sua altura: ");
		altura = entrada.nextDouble();
		
		double pesoIdeal = (72.7 * altura) - 58;
		System.out.println(pesoIdeal);
	}

}
