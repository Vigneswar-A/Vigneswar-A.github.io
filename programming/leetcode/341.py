# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

def flatten(arr):
    for i in arr:
        if i.isInteger():
            yield i.getInteger()
        else:
            yield from flatten(i.getList())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.it = flatten(nestedList)
        self.nxt = next(self.it, None)
        
    
    def next(self) -> int:
        temp = self.nxt
        self.nxt = next(self.it, None)
        return temp
    
    def hasNext(self) -> bool:
        return self.nxt is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())