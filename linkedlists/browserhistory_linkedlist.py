class history:
    def __init__(self,url):
        self.url=url
        self.prev=None
        self.next=None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr=history(homepage)
    def visit(self, url: str) -> None:
        self.curr.next=history(url)
        self.curr.next.prev=self.curr
        self.curr=self.curr.next
    def back(self, steps: int) -> str:
        while steps>0 and self.curr.prev:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.url
    def forward(self, steps: int) -> str:
        while steps>0 and self.curr.next:
            self.curr=self.curr.next
            steps-=1
        return self.curr.url
obj=BrowserHistory("Leetcode.com")
obj.visit("Google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
s=obj.back(1)
print(s)
s=obj.back(1)
print(s)
s=obj.forward(1)
print(s)
obj.visit("Linkedin.com")
# while obj.curr.prev:
#     print(obj.curr.url)
#     obj.curr=obj.curr.prev
s=obj.forward(2)
print(s)
s=obj.back(2)
print(s)
s=obj.back(7)
print(s)

