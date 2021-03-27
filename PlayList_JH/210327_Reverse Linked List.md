### LEET 206 Reverse Linked List

가장 바깥쪽 노드가 가장 안쪽으로 들어가야 하므로, `head` 안으로 하나씩 들어가면서 역으로 안쪽부터 채워가는 새로운 객체를 생성하면 된다. 새로운 객체는 반복문을 돌면서 이전의 자기자신을 next 값으로 가진다. `head`가 빈 객체라면 연산 없이 그대로 반환.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:        
        if head:
            ans = ListNode(head.val)
            while head.next:
                head = head.next
                ans = ListNode(head.val, ans)
        
            return ans
        
        return head
```