import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=140 lang=java
 *
 * [140] 单词拆分 II
 */

// @lc code=start
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSets = new HashSet<>(wordDict);
        List<String> res = new ArrayList<>();
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSets.contains(s.substring(j, i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        if(!dp[n]){
            return res;
        }
        Deque<String> path = new ArrayDeque<>();
        dfs(s, n, wordSets, dp, path, res);
        return res;
        
    }

	public void dfs(String s, int n, Set<String> wordSets, boolean[] dp, Deque<String> path, List<String> res) {
        if (n == 0) {
            res.add(String.join(" ", path));
            return;
        }
        for (int i = n-1; i >= 0; i--) {
            String suffix = s.substring(i, n);
            if (wordSets.contains(suffix) && dp[i]){
                path.addFirst(suffix);
                dfs(s, i, wordSets, dp, path, res);
                path.removeFirst();
            }
        }

	}
}
// @lc code=end

