class Solution {
    public int twoCitySchedCost(int[][] costs) {
        // Sort the costs array based on the difference between flying to city A vs city B
        // The difference (costA - costB) represents how much more expensive city A is compared to city B
        // Sorting in ascending order puts people who benefit most from going to city A at the beginning
        Arrays.sort(costs, (a, b) -> {
            int differenceA = a[0] - a[1];  // How much more expensive city A is for person a
            int differenceB = b[0] - b[1];  // How much more expensive city A is for person b
            return differenceA - differenceB;
        });
      
        // Initialize total cost
        int totalCost = 0;
      
        // Calculate n as half of the total number of people
        int n = costs.length / 2;
      
        // Send first n people to city A (those who benefit most from going to A)
        // Send last n people to city B (those who benefit most from going to B)
        for (int i = 0; i < n; i++) {
            totalCost += costs[i][0];      // Add cost for person i to go to city A
            totalCost += costs[i + n][1];  // Add cost for person (i+n) to go to city B
        }
      
        return totalCost;
    }
}

