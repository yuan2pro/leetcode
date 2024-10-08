import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;
import java.util.Set;

/**
 * Top Interview 150
 * https://leetcode.com/studyplan/top-interview-150/
 */
public class Solution {

    // 45. Jump Game II
    public int jump(int[] nums) {
        if (nums.length <= 1) {
            return 1;
        }
        int curEnd = 0;
        int maxReach = 0;
        int jumps = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            maxReach = Math.max(maxReach, nums[i] + i);
            if (i == curEnd) {
                jumps++;
                curEnd = maxReach;
            }
        }
        System.gc();
        return jumps;
    }

    // 55. Jump Game
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;
            }
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }

    // 169. Majority Element
    public static int majorityElement(int[] nums) {
        int m = nums[0];
        int count = 1;
        for (int n : nums) {
            if (n == m) {
                count++;
            } else {
                count--;
            }
            if (count == 0) {
                m = n;
                count = 1;
            }
        }
        return m;
    }

    // 88. Merge Sorted Array
    public static int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }
        int index = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[index - 2]) {
                nums[index++] = nums[i];
            }
        }
        return index;
    }

    // 121. Best Time to Buy and Sell Stock
    public static int maxProfit(int[] prices) {
        int s = prices[0];
        int total = 0;
        for (int i = 0; i < prices.length; i++) {
            s = Math.min(s, prices[i]);
            total = Math.max(total, prices[i] - s);
        }
        return total;
    }

    // 122. Best Time to Buy and Sell Stock II
    public int maxProfit2(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }

    // 189. Rotate Array
    public static void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        if (k == 0) {
            return;
        }
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    public static void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    // 274. H-Index
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) {
                return n - i;
            }
        }
        return 0;
    }

    // 380. Insert Delete GetRandom O(1)
    class RandomizedSet {
        Set<Integer> seen;
        Random random;

        public RandomizedSet() {
            seen = new HashSet<>();
            random = new Random();
        }

        public boolean insert(int val) {
            if (seen.contains(val)) {
                return false;
            }
            seen.add(val);
            return true;
        }

        public boolean remove(int val) {
            if (seen.contains(val)) {
                seen.remove(val);
                return true;
            }
            return false;
        }

        public int getRandom() {
            if (seen.isEmpty()) {
                throw new IllegalStateException("Set is empty");
            }
            int size = seen.size();
            int index = random.nextInt(size);
            Iterator<Integer> iterator = seen.iterator();
            for (int i = 0; i < index; i++) {
                iterator.next();
            }
            return iterator.next();
        }
    }

    // 238. Product of Array Except Self
    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }
        return result;
    }

    // 134. Gas Station
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        int index = 0;
        int curTank = 0;
        for (int i = 0; i < cost.length; i++) {
            totalCost += cost[i];
            totalGas += gas[i];
            curTank += gas[i] - cost[i];
            if (curTank < 0) {
                index = i + 1;
                curTank = 0;
            }
        }
        if (totalCost > totalGas) {
            return -1;
        }
        return index;
    }

    // 322. Coin Change
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }

    // 518. Coin Change II
    public static int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }

    // 13. Roman to Integer
    public int romanToInt(String s) {
        Map<Character, Integer> romanToIntMap = new HashMap<>();
        romanToIntMap.put('I', 1);
        romanToIntMap.put('V', 5);
        romanToIntMap.put('X', 10);
        romanToIntMap.put('L', 50);
        romanToIntMap.put('C', 100);
        romanToIntMap.put('D', 500);
        romanToIntMap.put('M', 1000);
        int result = 0;
        int preValue = 0;
        for (char c : s.toCharArray()) {
            int value = romanToIntMap.get(c);
            if (preValue < value) {
                result += value - 2 * preValue;
            } else {
                result += value;
            }
            preValue = value;
        }
        return result;
    }

    // 125. Valid Palindrome
    public boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // 58. Length of Last Word
    public int lengthOfLastWord(String s) {
        s = s.strip();
        int len = s.length() - 1;
        while (len >= 0 && s.charAt(len) != ' ') {
            len--;
        }
        return s.length() - len - 1;
    }

    // 14. Longest Common Prefix
    public String longestCommonPrefix(String[] strs) {
        if (strs == null && strs.length == 0) {
            return "";
        }
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        return prefix;
    }

    // 28. Find the Index of the First Occurrence in a String
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }

    // 392. Is Subsequence
    public boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) != t.charAt(j)) {
                j++;
            } else {
                i++;
                j++;
            }
        }
        return i == s.length();
    }


    // 383. Ransom Note
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        for (Character ch : magazine.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        for (Character ch : ransomNote.toCharArray()) {
            if (!map.containsKey(ch)) {
                return false;
            } else {
                Integer i = map.get(ch);
                if (i == 0) {
                    return false;
                } else {
                    map.put(ch, i - 1);
                }
            }
        }
        return true;
    }

    // 205.Isomorphic Strings
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Character> mapSt = new HashMap<>();
        Map<Character, Character> mapTs = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char sc = s.charAt(i);
            char tc = t.charAt(i);
            if (mapSt.containsKey(sc)) {
                if (mapSt.get(sc) != tc) {
                    return false;
                }
            } else {
                mapSt.put(sc, tc);
            }
            if (mapTs.containsKey(tc)) {
                if (mapTs.get(tc) != sc) {
                    return false;
                }
            } else {
                mapTs.put(tc, sc);
            }
        }
        return true;
    }

    // 290.Word Pattern
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) {
            return false;
        }

        HashMap<Character, String> charToWord = new HashMap<>();
        HashMap<String, Character> wordToChar = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];

            if (charToWord.containsKey(c)) {
                if (!charToWord.get(c).equals(word)) {
                    return false;
                }
            } else {
                if (wordToChar.containsKey(word)) {
                    return false;
                }
                charToWord.put(c, word);
                wordToChar.put(word, c);
            }
        }
        return true;
    }

    // 242.Valid Anagram
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (Character c : t.toCharArray()) {
            if (map.containsKey(c) && map.get(c) > 0) {
                map.put(c, map.get(c) - 1);
            } else {
                return false;
            }
        }
        return true;
    }

}
