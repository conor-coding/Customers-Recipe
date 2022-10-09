class MyCalendar:
    class Node:
        def __init__(self,start,end,left=None,right=None):
            self.start,self.end,self.left,self.right=start,end,left,right

    def __init__(self):
        self.root=None

    def book(self, start: int, end: int) -> bool:
        #call recursive or iterative methods randomly
        return self.bookITR(start,end) if random.randrange(0,2)==1 else self.bookREC(start,end)
        
    def bookITR(self, start: int, end: int) -> bool:
            print('itr',end=' ')
            pre=dummy=self.Node(-1,0)
            root=self.root
            dummy.right=root
            while root:
                s,e=root.start,root.end
                pre=root
                #if e>=end>s or s<=start<e :
                if start<=s<end or e>start>=s:
                    return False
                elif start<s:
                    root=root.left
                else:
                    root=root.right
            newnode=MyCalendar.Node(start,end)
            if start<pre.start:
                pre.left=newnode
            else:
                pre.right=newnode
            self.root=dummy.right
            return True
        
    def bookREC(self, start: int, end: int) -> bool:
        print('rec',end=' ')
        def helper(root):
            s,e=root.start,root.end
            if start>=e:
                if root.right is None:
                    root.right=self.Node(start,end)
                    return True
                else:
                    return helper(root.right)
            elif end<=s:
                if root.left is None:
                    root.left=MyCalendar.Node(start,end)
                    return True
                else:
                    return helper(root.left)
            else: #start<e and end>s
                return False
            
        if not self.root:
            self.root=self.Node(start,end)
            return True
        return helper(self.root)
