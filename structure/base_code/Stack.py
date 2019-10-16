# 一，py 实现一个栈类, 栈抽象数据的py实现
# 栈的基本操作包括，压入，弹出，判断空，大小判断等
class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, value):
        self.items.append(value)      # 此时性能O(1) 比 insert(0, value)  O(n)高
    def pop(self):
        return self.items.pop()      # 默认弹出栈顶，性能高于 pop(n)
    def peek(self):
        return self.items[len(self.items)-1]  # 返回最上层数据
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    st = Stack()
    st.push(8)
    print(st.items)
    print(st.peek())
    print(st.size())