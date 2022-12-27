// with (2n+1)


public class Main
{
	public static void main(String[] args) {


		int input = 3;
		
		for (int i =0;i<=input;i++ ) {
		    for (int s =input-i;s> 0;s--){
		        System.out.print(" ");
		    }
		    
		    for (int j=0;j<(2*i+1);j++ ) {
		      System.out.print("*");  
		    }
		    System.out.println("");
		}
		
		for (int i =input-1;i>= 0;i-- ) {
		    for (int s =input-i;s > 0;s--){
		        System.out.print(" ");
		    }
		
		    for (int j=0;j<(2*i+1);j++ ) {
		      System.out.print("*");  
		    }
		    System.out.println("");
		}
	}
}
