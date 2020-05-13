package estruturaSequencial;

import java.util.Scanner;

public class Q06 {

	public static void main(String[] args) {

		Scanner e = new Scanner(System.in);
		
		float raio = 0, area = 0;
		
		System.out.println("Digite o raio do círculo: ");
		raio = e.nextFloat();
		
		area = (float) (3.14 * Math.pow(raio, 2));
		System.out.println("Área do círculo = " + area);
		
				
		
	}

}
