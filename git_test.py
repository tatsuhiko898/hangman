class Item:
    total=[]

    def __init__(self,name):
        self.name=name
        self.total.append(self.name)


a=Item('いも')
b=Item('ねぎ')
c=Item('トマト')
d=Item('タマネギ')
print(a)
print(Item.total)