//program by arya
import java.util.*;
import java.io.*;
public class Solution  
{  
static void sort(int arr[]) {
    int small;  
    int n = arr.length;  
    for (int i = 0; i < n-1; i++)  
    {  
        small = i;
          
        for (int j = i+1; j < n; j++)  
        if (arr[j] < arr[small])  
            small = j;  

    int temp = arr[small];  
    arr[small] = arr[i];  
    arr[i] = temp;  
    }  
  
}  
static void print(int arr[])
{   
    int n = arr.length;  
    for (int i = 0; i < n; i++)  
    System.out.print(arr[i] + " ");  
}  
  
    public static void main(String[] args) {  
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int[]arr=new int[n];
    for(int i=0;i<n;i++)
    {
      arr[i]=sc.nextInt();
    }
    //Selection s1 = new Selection();  
    System.out.println("Before sort: ");  
    print(arr);  
    sort(arr); 
    System.out.println();  
    System.out.println("After sort: ");  
    print(arr);  
    
    }  
}  
