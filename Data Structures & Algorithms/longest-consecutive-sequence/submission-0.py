class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # ==========================================================================================
        # ==========================================================================================
        # ====== NOTE: ======
        # THE SOLUTION BELOW ASSUMES THAT THE ELEMENTS NEED TO APPEAR IN ORDER IN THE ORIGINAL ARRAY
        # THIS IS NOT THE CASE!
        # THE ANSWER TO Input: nums = [0,3,2,5,4,6,1,1] IS Output: 7
        # BECAUSE, REARRANGING INPUTS GIVES: [0, 1, 1, 2, 3, 4, 5, 6]
        # ==========================================================================================
        # ==========================================================================================

        # if len(nums) == 0:
        #     return 0

        # # brute force is just looping over the rest of the list, 
        # # starting from each individual element in the list, 
        # # and taking the max consecutive sequence.

        # seen = {} # a map from the longest consecutive sequence ending at a particular num, 
        #           # to the length of said sequence

        # longest = 1

        # for num in nums:
            
        #     if num - 1 in seen:
        #         sequence_length = seen[num - 1] + 1
        #         seen[num] = sequence_length

        #         if sequence_length > longest:
        #             longest = sequence_length
            
        #     else:
        #         seen[num] = 1
        
        # return longest

        # ==========================================================================================
        # ================================== CORRECT SOLUTION BELOW ================================
        # ==========================================================================================

        """
        - Consider nums = [100, 4, 200, 1, 3, 2], which sorted is [1, 2, 3, 4, 100, 200]
        - This gives 3 distinct sequences: (1, 2, 3, 4), (100), (200)
        - Things to note:
            - The start of each sequence (i.e., 1, 100, 200) has no left neighbor:
                - We can check this by simply making our input list into a set (hash map) in O(1) time.
                - Then, from a given start number, we check whether that number + 1 is in the set and so on.
        """

        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            
            if num - 1 not in num_set: # i.e., num is the start of a sequence
                curr_num = num
                length = 1
                
                while curr_num in num_set:
                    if curr_num + 1 in num_set:
                        length += 1
                    curr_num += 1

                longest = max(longest, length)
        
        return longest



