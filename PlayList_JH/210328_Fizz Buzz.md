### LEET 412 Fizz Buzz

영어판 369 문제. 조건문이 걸린 List Comprehension을 사용하다가 잠깐 헤맸는데, 조건이 하나 뿐이라면 맨 뒤에, `else`로 여러 개가 걸려 있다면 반복문 이전에 위치해야 한다.

```python
# LEET 412
# <https://bit.ly/3lXa7Fi>

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return list(str(i) if i%3 and i%5 else ('Fizz', '')[min(1, i%3)] + ('Buzz', '')[min(1, i%5)] for i in range(1, n+1))
```