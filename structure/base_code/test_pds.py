class BinarySearchTree(object):
    """二叉搜索树
    """
    def __init__(self):
        self.root = None
        self.size = 0
        self.path = []    # 添加路径

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        """迭代器,用于实现for的循环"""
        return self.root.__iter__()

    def _put(self, key, val, currentNode, insert_path):  # currentNode root节点
        insert_path.append(currentNode.key)
        if key < currentNode.key:  # 如果参数key 比 当前节点的key小，进入树的左子树进行 递归插入

            if currentNode.hasLeftChild():
                # insert_path.append(currentNode.leftChild.key)  # 更新插入记录
                self._put(key, val, currentNode.leftChild, insert_path)  # 递归左子树

            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)  # 插入位置，树的节点

        else:  # 如果key 等于大于 当前节点key，进入树的右子树进行递归插入
            if currentNode.hasRightChild():
                # insert_path.append(currentNode.rightChild.key)  # 更新插入记录
                self._put(key, val, currentNode.rightChild, insert_path)  # 递归右子树
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)  # 插入位置，增加一个树的节点

        return insert_path

    def put(self, key, val):
        """BST高度 log_2 N ,如果key列表随机分布，大于小于根节点key的键值大致相等。性能在于二叉树的高度(最大层次),高度也受数据项key插入顺序影响
        算法分析，最差O(log_2 N)"""
        insert_path = []
        if self.root:  # 有root根节点
            self._put(key, val, self.root, insert_path)
            if insert_path in self.path:
                self.path.remove(insert_path)
            insert_path.append(key)
            self.path.append(insert_path)
            # self.path = insert_path
        else:  # 没有root，则构造单个节点的二叉查找树
            self.root = TreeNode(key, val)
            self.path.append([self.root.key])
        self.size = self.size + 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        """只要是平衡树，get的时间复杂度可以保持在O(logN)"""
        if self.root:
            res = self._get(key, self.root)  # 递归函数
            if res:
                return res.payload  # 找到节点
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """

        :param key:
        :param currentNode: 当前节点，即要插入的二叉查找树 子树的根，为当前节点
        :return:
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        """实现val=myZipTree['PK']"""
        return self.get(item)

    def __contains__(self, item):
        """实现'PK' in myZipTree的归属判断运算符 in

         mytree[3]='red'
         mytree[6]='yellow'
          print(3 in mytree)
          print(mhytree[6])"""
        if self._get(item, self.root):
            return True
        else:
            return False

    def yield_path(self, lis):
        for item in lis:
            yield item

    def ret_path_lis(self):
        """从左到右排序路径"""
        self.path.sort()
        return self.yield_path(self.path)

    def print_path_lis(self):
        """输出排序"""
        path_lis = self.ret_path_lis()

        while path_lis:
            path_str = ''
            connect_str = '->'
            try:
                path = next(path_lis)
            except StopIteration as stp:
                # print(f'finished to display,error:{stp}')
                break
            else:
                for path in path:
                    path_str += str(path) + connect_str
            print(path_str[:-len(connect_str)])


class TreeNode(object):
    """二叉搜索树节点"""

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键值
        self.payload = val  # 数据项
        self.leftChild = left  # 左子节点
        self.rightChild = right  # 右子节点
        self.parent = parent  # 父节点
        self.balanceFactor = 0  # 平衡因子
        self.path_lis = []

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):  # 是否根节点
        return not self.parent

    def isLeaf(self):  # 是否叶节点
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def __iter__(self):
        """迭代器函数用来for函数，实际上递归函数yield是对每次迭代的返回值，
        中序遍历的迭代
        BST类中的 __iter__方法直接调用了TreeNode中同名方法"""
        if self:  # 根不为空，基本结束条件
            if self.hasLeftChild():  # 左子树不为空
                for elem in self.leftChild:  # 遍历左子树
                    yield elem  # 生成器，返回左子树一个元素
            yield self.key  # 生成器，返回根
            if self.hasRightChild():  # 右子树不为空
                for elem in self.rightChild:  # 遍历右子树
                    yield elem  # 生成器，返回右子树一个元素
    ''''
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def spliceOut(self):
        """摘出节点"""
        if self.isLeaf():  # 挑出叶子节点
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None  # 同时有两个左右子树，有左下角的情况，不会执行该代码
        elif self.hasAnyChildren():
            if self.hasLeftChild():  # 挑出左子节点
                if self.isLeftChild():  # 这一块if-else,在同时有两个左右子树，有左下角的情况，不会执行该代码
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
            else:  # 挑出带右子节点的节点
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild  # 摘出带右子节点的节点
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        """寻找后继节点"""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:  # 教材中的代码，处理的是情况是，该节点没有右子树，需要去其他地方找后继，但是在本例中，前提就是当前节点同时有左右子树
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        """当前节点的左子树的最左下角的值"""
        current = self
        while current.hasLeftChild():  # 直到找到最左下角的值，就是直接后继
            current = current.leftChild
        return current

    '''

if __name__ == '__main__':
    """输入样例：
    5 2 6 1 3 7 4
    输出样例：
    5->2->1
    5->2->3->4
    5->6->7

    """
    def build_bst():
        bst1 = BinarySearchTree()
        bst1.put(5, 0)
        bst1.put(2, 0)
        bst1.put(6, 0)
        bst1.put(1, 0)
        bst1.put(3, 0)
        bst1.put(7, 0)
        bst1.put(4, 0)
        # bst1.put(-5, 0)
        # bst1.put(-3, 0)
        # bst1.put(-6, 0)
        # bst1.put(16, 0)
        # bst1.put(5.8, 0)
        return bst1
    bst1 = build_bst()
    print(bst1.size)
    print(bst1.root.key)
    print(bst1.root.findMin().key)
    bst1.path.sort()
    print(bst1.path)
    print(bst1.print_path_lis())

