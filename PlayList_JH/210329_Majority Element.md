### LEET 169 Majority Element

과반수인 숫자라면 정렬했을 때 반드시 중앙을 차지하게 된다. 'more than'이라서 딱 반반으로 나눠지는 경우도 없다.

```python
# LEET 169
# <https://bit.ly/3m13hi2>

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
```