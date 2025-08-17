class Solution 
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Stack<Integer> st = new Stack<>();
        
        for (int i = (2 * n) - 1; i >= 0; i--) {
            int idx = i % n;
            
            while (!st.isEmpty() && nums[idx] >= nums[st.peek()]) {
                st.pop();
            }
            
            if (st.isEmpty()) {
                res[idx] = -1;
            } else {
                res[idx] = nums[st.peek()];
            }
            
            st.push(idx);
        }
        
        return res;
    }
