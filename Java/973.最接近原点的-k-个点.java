/*
 * @lc app=leetcode.cn id=973 lang=java
 *
 * [973] 最接近原点的 K 个点
 */

// @lc code=start
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[][] kClosest(int[][] points, int K) {
        int[][] ans = new int[K][];
        int len = points.length;
        int[] dis = new int[len];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < len; i++) {
            int[] point = points[i];
            int d = point[0] * point[0] + point[1] * point[1];
            map.put(i, d);
        }
        List<Map.Entry<Integer, Integer>> list = map.entrySet().stream()
                .sorted((entry1, entry2) -> entry1.getValue().compareTo(entry2.getValue()))
                .collect(Collectors.toList());
        for (int i = 0; i < K; i++) {
            int t = list.get(i).getKey();
            ans[i] = points[t];
        }
        return ans;
    }
}
// @lc code=end
