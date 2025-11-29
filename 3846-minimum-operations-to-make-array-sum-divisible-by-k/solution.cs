public class Solution
{
    public int MinOperations(int[] Nums, int K)
    {
        int Sum = 0;

        for(int i = 0; i < Nums.Length; i++)
            Sum += Nums[i];
        
        return Sum % K;
    }
}
