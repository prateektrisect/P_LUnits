import java.util.*;
import java.util.Scanner;
public class Main{

  void solution(String[] array) {
      
    // Write code here
   
    
//     print new array here
        System.out.println(Arrays.toString()) // type name of new array inside Arrays.toString()
   
  }

  //Test code
  //Don't change anything below this line
  public static void main(String[] args){
    Main test = new Main();
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] array = new String[n]; 
    Scanner sc1 = new Scanner(System.in);
    for(int i=0; i<n; i++)  
    {  
         
        array[i]=sc1.nextLine();  
    }  
    test.solution(array);
  }
}
