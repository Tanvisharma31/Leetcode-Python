// Last updated: 02/03/2026, 14:01:59
class Solution {
    // This method calculates the minimum number of steps to get 'n' 'A's on the notepad
    // starting with only one 'A'. It involves a series of copy-all and paste operations.
    public int minSteps(int n) {
        // Initialize the result to store the minimum number of steps
        int steps = 0;
        // Start dividing 'n' from factor 2 onwards, as 1 wouldn't change the number
        for (int i = 2; n > 1; ++i) {
            // While 'n' is divisible by 'i', keep dividing it and add 'i' to the result.
            // This is because, in terms of operations, if 'n' is divisible by 'i',
            // it means we can get to 'n' by doing 'i' operations (copy, paste 'i'-1 times) that many times.
            while (n % i == 0) {
                steps += i; // Add the factor to the total steps
                n /= i;     // Divide 'n' by the current factor 'i'
            }
        }
        // Once 'n' is reduced to 1, we have found the minimum steps and return it
        return steps;
    }
}
