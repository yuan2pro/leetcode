'''剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，
请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )



示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            if not self.stack1:
                return -1
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        else:
            return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
param_2 = obj.deleteHead()
obj.appendTail(97)
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
obj.appendTail(15)
param_2 = obj.deleteHead()
obj.appendTail(1)
obj.appendTail(43)
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
obj.appendTail(18)
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
obj.appendTail(36)
obj.appendTail(69)
obj.appendTail(21)
obj.appendTail(91)
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
print(param_2)
obj.appendTail(22)
obj.appendTail(40)
print(obj.stack2, obj.stack1)
param_2 = obj.deleteHead()
print(obj.stack2, obj.stack1)
print(param_2)
param_2 = obj.deleteHead()
param_2 = obj.deleteHead()
