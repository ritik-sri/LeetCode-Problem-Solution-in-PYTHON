class Solution(object):
    def __init__(self, head):
        self.nodes = []  # convert linked list to a list, cost O(N) Space and O(N) Time
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self):  # cost O(1) Time
        return random.choice(self.nodes)