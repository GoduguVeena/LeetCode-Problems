class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0;
        int j = 0;
        while (i < g.length && j < s.length) {
            // Compare the current cookie (j) with the current child's greed (i)
            if (s[j] >= g[i]) {
                i++;
            }
            j++;
        }
        return i; // i represents the total number of content children
    }
}
