class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        for i in range(arr_len-1):
            arr_slice = arr[i+1:]
            arr[i] = max(arr_slice)
        arr[arr_len-1] = -1
        return arr