package leetcode.editor.cn;

public class Sort {

    /**
     * 冒泡排序 时间复杂度 O(n^2) 最好情况 O(n) 空间复杂度 O(1) 稳定
     * 
     * @param arr 排序数组
     */
    public static void bubbleSort(int[] arr) {
        int len = arr.length;
        for (int i = 0; i < len - 1; i++) {
            boolean flag = false;
            for (int j = 0; j < len - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                    flag = true;
                }
            }
            if (!flag) {
                break;
            }
        }
    }

    /**
     * 快速排序 平均时间复杂度 O(nlogn) 最好时间复杂度 O(nlogn) 最坏时间复杂度 O(n^2) 空间复杂度 O(logn) 不稳定
     * 
     * @param arr  数组
     * @param low
     * @param high
     */
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

}
