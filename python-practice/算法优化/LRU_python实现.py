#基于普通dict和list实现
class LRU_object(object):
    def __init__(self,size=3):
        self.size = size
        self.cache_Dict = dict()
        self.key = []

    def get(self,Ikey):
        if Ikey in self.cache_Dict.keys():
            self.key.remove(Ikey) # remove直接传入值移除元素，pop转入位置索引移除元素
            self.key.insert(0,Ikey)
            return self.cache_Dict[Ikey]
        else:
            return None 

    def set(self,Ikey,value):
        if Ikey in self.cache_Dict.keys():
            self.cache_Dict[Ikey]=value
            self.key.remove(Ikey)
            self.key.insert(0,Ikey)
            return self.cache_Dict[Ikey]
        elif len(self.cache_Dict.keys())==self.size:
            old = self.key.pop()
            self.key.insert(0,Ikey)
            self.cache_Dict.pop(old)
            self.cache_Dict[Ikey] = value
        else:
            self.cache_Dict[Ikey] = value
            self.key.insert(0,Ikey)
        

if __name__ == '__main__':
    test = LRU_object()
    test.set('a',1)
    test.set('b',2)
    test.set('c',3)
    test.set('a',4)
    test.set('e',5)
    # test.set('f',6)
    print(test.get('a'))




