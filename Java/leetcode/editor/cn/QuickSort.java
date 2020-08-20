package leetcode.editor.cn;

import java.util.Arrays;

public class QuickSort {
    public static void quick(int[] arr, int low, int high) {
        if (low < high) {
            int index = sort(arr, low, high);
            quick(arr, 0, index - 1);
            quick(arr, index + 1, high);
        }
    }

    private static int sort(int[] arr, int low, int high) {
        int tmp = arr[low];
        while (low < high) {
            while (low < high && arr[high] >= tmp) {
                high--;
            }
            arr[low] = arr[high];
            while (low < high && arr[low] <= tmp) {
                low++;
            }
            arr[high] = arr[low];

        }
        arr[low] = tmp;
        return low;
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 1, 4, 2, 1, 5};
        QuickSort.quick(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
}
