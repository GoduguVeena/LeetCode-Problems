class Solution {
    public int twoCitySchedCost(int[][] costs) {
        int n = costs.length;
        int[][] diff = new int[n][2];

        for (int i = 0; i < n; i++) {
            diff[i][0] = costs[i][0] - costs[i][1]; // cost difference A vs B
            diff[i][1] = i;                          // remember original index
        }

        Arrays.sort(diff, (a, b) -> a[0] - b[0]);

        int cost = 0;
        for (int i = 0; i < n / 2; i++) {
            cost += costs[diff[i][1]][0]; // cheapest-to-switch half → City A
        }
        for (int i = n / 2; i < n; i++) {
            cost += costs[diff[i][1]][1]; // rest stay in City B
        }

        return cost;
    }
}
