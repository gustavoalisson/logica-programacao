package estruturaSequencial;

import java.util.Scanner;

public class Q07 {

	public static void main(String[] args) {
		
		Scanner e = new Scanner(System.in);
		
		double lado = 0, area = 0;
		System.out.println("====Mostrar o dobro da área para o usuário====");
		System.out.println("Digite a área do quadrado: ");
		lado = e.nextDouble();
		
		area = Math.pow(lado, 2);
		System.out.println("Área: " + area);
		System.out.println("_______________________________");
		System.out.println("Dobro da área: " + (area * 2));
		
		
		
		

	}

}
