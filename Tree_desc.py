class tree:
  def __init__(self,Data):
    self.right = None
    self.left = None
    self.node = Data
  def show(self):
    if self.left:
      self.left.show()
    print(self.node)
    if self.right:
      self.right.show()
  def insert(self,new_data):
    if new_data<self.node:
      if self.left is None:
        self.left=tree(new_data)
      else:
        self.left.insert(new_data)
    elif new_data>self.node:
      if self.right is None:
        self.right = tree(new_data)
      else:
        self.right.insert(new_data)

mp = tree(55)
mp.insert(25)
mp.insert(60)
mp.insert(75)
mp.insert(79)
mp.insert(-20)
mp.insert(66)
mp.insert(0)
mp.insert(-50)
mp.insert(300)
mp.insert(240)
mp.insert(-2.454)
mp.insert(5)

mp.show()
