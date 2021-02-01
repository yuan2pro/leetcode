/*
 * @lc app=leetcode.cn id=888 lang=java
 *
 * [888] 公平的糖果交换
 */

// @lc code=start
class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int[] res = new int[2];
        int a = A.length;
        int b = B.length;
        int sa = 0, sb = 0;
        for(int i:A){
            sa += i;
        }
        for(int i:B){
            sb += i;
        }
        int x, y;
        for(int i = 0;i < a; i++){
            x = A[i];
            for(int j = 0;j < b; j++){
                y = B[j];
                if(sa - x + y == sb - y + x){
                    res[0] = x;
                    res[1] = y;
                    break;
                }
            }
        }
        return res;
    }
}
// @lc code=end

