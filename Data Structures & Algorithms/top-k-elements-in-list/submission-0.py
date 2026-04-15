class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies (Your original logic)
        # Create a map where key = number, value = how many times it appears
        counts = {}
        for x in nums:
            counts[x] = 1 + counts.get(x, 0)

        # Step 2: Create the "Buckets"
        # We need a list of lists. The index will represent the frequency.
        # The size is len(nums) + 1 because a number can't appear more than len(nums) times.
        buckets = [[] for i in range(len(nums) + 1)]

        # Step 3: Populate the Buckets
        # Iterate through the dictionary items (number, frequency)
        # Add the number into the bucket at the index of its frequency
        # Example: if '3' appears 5 times, add '3' to buckets[5]
        for num, freq in counts.items():
            buckets[freq].append(num)

        # Step 4: Collect the results
        # Create a list to store our final top k elements
        result = []

        # Step 5: Iterate backwards through the buckets
        # Start from the highest frequency (the end of the list) down to 0
        for i in range(len(buckets) - 1, 0, -1):
            # For every number in the current bucket...
            for n in buckets[i]:
                # Add it to our result
                result.append(n)
                # If we have found 'k' elements, return the result immediately
                if len(result) == k:
                    return result