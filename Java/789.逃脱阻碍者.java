/*
 *                        .::::.
 *                      .::::::::.
 *                     :::::::::::
 *                  ..:::::::::::'
 *               '::::::::::::'
 *                 .::::::::::
 *            '::::::::::::::..
 *                 ..::::::::::::.
 *               ``::::::::::::::::
 *                ::::``:::::::::'        .:::.
 *               ::::'   ':::::'       .::::::::.
 *             .::::'      ::::     .:::::::'::::.
 *            .:::'       :::::  .:::::::::' ':::::.
 *           .::'        :::::.:::::::::'      ':::::.
 *          .::'         ::::::::::::::'         ``::::.
 *      ...:::           ::::::::::::'              ``::.
 *     ````':.          ':::::::::'                  ::::..
 *                        '.:::::'                    ':'````..
 * 
 * @Author       : William
 * @Date         : 2021-08-22 21:48:08
 * @LastEditTime : 2021-08-22 21:58:29
 * @LastEditors  : Do not edit
 * @FilePath     : /undefined/Users/william/leetcode/Java/789.逃脱阻碍者.java
 * @Description  : 
 */

/*
 * @lc app=leetcode.cn id=789 lang=java
 *
 * [789] 逃脱阻碍者
 */

// @lc code=start
class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        int[] source = { 0, 0 };
        int distance = manhattanDistance(source, target);
        for (int[] ghost : ghosts) {
            int t = manhattanDistance(ghost, target);
            if (t <= distance) {
                return false;
            }
        }
        return true;

    }

    public int manhattanDistance(int[] p1, int[] p2) {
        return Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
    }
}
// @lc code=end
