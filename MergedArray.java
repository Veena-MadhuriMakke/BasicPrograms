import java.util.Arrays;
public class MergedArray {
    public static void main (String[] args){
        int[] Arr1 = {1,3,5,7};
        int[] Arr2 = {2,4,6,8};
        int[] MergedArray = mergedSortedArray( Arr1, Arr2);
        System.out.println("Merged Array: " + Arrays.toString(MergedArray));
    }
    public static int[] mergedSortedArray (int[] Arr1, int[] Arr2){
        int n1 = Arr1.length;
        int n2 = Arr2.length;
        int[] MergedArray = new int[n1+n2];
        int i=0, j=0, k=0;
        while(i<n1 && j<n2){
            if (Arr1[i] <= Arr2[j]){
                MergedArray[k++] = Arr1[i++];
            }else{
                MergedArray[k++] = Arr2[j++];
            }
        }
        while(i<n1){
            MergedArray[k++] = Arr1[i++];
        }
        while(j<n2){
            MergedArray[k++] = Arr2[j++];
        }
        return MergedArray;
    }
}
