package estruturaSequencial;

import java.util.Scanner;

public class Q17 {

	public static void main(String[] args) {

		double metros = 0, qtdLatas = 0, vLitros = 0, valorTotalLatas = 0;
		double qtdGaloes = 0, valorTotalGaloes = 0;
		

		Scanner e = new Scanner(System.in);

		System.out.println("Digite o tamanho em metros quadrados da área: ");
		metros = e.nextDouble();
		
		// 18 litros
		vLitros = (metros / 6);
		qtdLatas = vLitros / 18;
        valorTotalLatas = qtdLatas * 80.0;
        
        // 3,6 litros
        vLitros = (metros / 6);
		qtdGaloes = vLitros / 3.6;
        valorTotalGaloes = qtdGaloes * 25.0;
        
        // misturar galoes
        double a1 = vLitros / 18;
        double a2 = vLitros%18;
        double a3 = Math.ceil(a2/3.6);
        double a4=((a1*80) + (a3*25));
        
        System.out.println("== Comprar apenas latas de 18 litros == ");
       
        System.out.println("Quantidade de latas de tintas necessária: " + Math.round(qtdLatas));
        System.out.printf("Valor total: %.2f \n" , valorTotalLatas);
        
       
        
        System.out.println("______________________________________________________________________");
        
        System.out.println("== Comprar apenas galões de 3,6 litros == ");
       
        System.out.println("Quantidade de galões de tintas necessária: " + Math.round(qtdGaloes));
        System.out.printf("Valor total: %.2f \n " , valorTotalGaloes);
        
       System.out.println("_________________________________________________________________________");
       
       System.out.println("Valor com desconto de 10% de Latas mais Galões: " +Math.ceil(a4) );
       
	}

}
 