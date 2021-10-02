class BubbleSortClass{

    public static void main(String[] args) {
        
        BubbleSortClass bs = new BubbleSortClass();

        int arr[] = {20, 50, 0, 2003, -2, -100, 34};

        bs.BubbleSort(arr);

        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }

    }

    //Bubble sort algorithm written in Java
    public void BubbleSort(int array[]){

        int temp = 0;

        for(int x = 0; x < array.length-1; x++){

            for(int y = 0; y < array.length-x-1; y++){

                if(array[y] > array[y+1]){

                    temp = array[y];
                    array[y] = array[y+1];
                    array[y+1] = temp;

                }

            }

        }

    }

}