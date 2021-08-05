package estruturaSequencial;

import java.util.Scanner;

public class Q05 {

	public static void main(String[] args) {

		Scanner e = new Scanner(System.in);

		double metros;
      System.out.println("===Conversão de metros para centímetros===");
		System.out.println("Metros: ");
		metros = e.nextDouble();

		double conversao = metros * 100;
		System.out.println("Centímetros: " + conversao + " cm");

	}

}
