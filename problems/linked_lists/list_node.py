class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}(val={self.val}, next={self.next.val if self.next else None})'
