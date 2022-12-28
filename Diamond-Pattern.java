/******************************************************************************
		      ** Diamond pattern with (2n+1) **
    *
   ***
  *****
 *******
  *****
   ***
    *
*******************************************************************************/




public class Main {
	
    public static void main(String[] args) {
	
	// Input value
        int input = 3;

	    
	// Up
        for (int i = 0; i <= input; i++) {
		
	    // Space
            for (int s = input - i; s > 0; s--) {
                System.out.print(" ");
            }
		
	    // Star
            for (int j = 0; j < (2 * i + 1); j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
	
	// Down
        for (int i = input - 1; i >= 0; i--) {
		
	    // Space
            for (int s = input - i; s > 0; s--) {
                System.out.print(" ");
            }

	    // Star
            for (int j = 0; j < (2 * i + 1); j++) {
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
