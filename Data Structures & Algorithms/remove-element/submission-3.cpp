class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(nums.empty()) return 0;

        int left = 0;

        for(int right = 0; right < nums.size(); right++) {
           if(nums[right] != val) {
            nums[left] = nums[right];
            left++;
           }
        }

        return left;
    }
};