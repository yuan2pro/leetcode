"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):

    def __init__(self):
        # the stack it self
        self.A = []
        self.minS = []

    # @return an integer
    def push(self, x):
        n = len(self.A)
        if n == 0:
            self.minS.append(x)
        else:
            lastmin = self.minS[-1]
            if x <= lastmin:
                self.minS.append(x)
        self.A.append(x)

    # @return nothing
    def pop(self):
        if len(self.A) > 0 and self.A.pop() == self.minS[-1]:
            self.minS.pop()

    # @return an integer
    def top(self):
        return self.A[-1]

    # @return an integer
    def getMin(self):
        return self.minS[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    l = [1,2]
    l.insert(1,-1)
    print(l)
