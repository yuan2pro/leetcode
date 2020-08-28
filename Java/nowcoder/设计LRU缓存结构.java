package nowcoder;

import java.util.*;


class Solution {
    /**
     * lru design
     *
     * @param operators int整型二维数组 the ops
     * @param k         int整型 the k
     * @return int整型一维数组
     */
    public int[] LRU(int[][] operators, int k) {
        // write code here
        Map<Integer, Integer> lru = new LinkedHashMap<>(k, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > k;
            }
        };
        List<Integer> res = new ArrayList<>();

        int n = operators.length;
        for (int i = 0; i < n; i++) {
            int[] cur = operators[i];
            if (cur[0] == 1) {
                lru.put(cur[1], cur[2]);
            } else {
                int orDefault = lru.getOrDefault(cur[1], -1);
                res.add(orDefault);
            }
        }
        int size = res.size();
        int[] ans = new int[size];
        int i = 0;
        for (int re : res) {
            ans[i++] = re;
        }
        return ans;
    }
}
