# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        next_page = Node(url)
        
        self.node.next = next_page
        next_page.prev = self.node
        
        self.node = self.node.next

    def back(self, steps: int) -> str:
        while steps and self.node.prev:
            steps -= 1
            self.node = self.node.prev
        
        return self.node.val

    def forward(self, steps: int) -> str:
        while steps and self.node.next:
            steps -= 1
            self.node = self.node.next
        
        return self.node.val
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)  