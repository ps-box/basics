### LEET 237 Delete Node

부모 노드를 안 알려주길래 어떻게 풀라는 거지 싶어서 처음에 좀 헤맸다. 간단하게 생각하서 삭제할 노드부터 배열 정보만 있다면, 현재 배열을 노드의 자식 배열로 바꿔치기 하면 된다. 제한된 데이터를 가지고 원하는 결과를 만들어낼 수 있는지 생각의 전환을 테스트하는 문제 같다.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```