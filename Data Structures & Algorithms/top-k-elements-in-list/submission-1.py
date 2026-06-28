class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n,0) +1

        print(counts)
        sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True, ))
        print(sorted_dict)
        first_k_keys = list(sorted_dict.keys())[:k]

        return first_k_keys
    