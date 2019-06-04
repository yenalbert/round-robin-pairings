class RoundRobin:
  '''
  The constructor for this class will take a list of strings as the parameter.
  '''
  
  # overriding default __init__
  def __init__(self, listOfStrings):
    '''
    This will make a shallow copy of the list given.
    '''
    self.copiedList = list(listOfStrings)
    self.name_list = list(listOfStrings)

  def generate_round(self):
    '''
    "parameters" will be self.
    "return value" will be a list of tupples. 
    "one round" of this method will generate one list.
    '''
    copiedList = self.copiedList
    name_list = self.name_list
    size = int(len(copiedList))
    list_of_pairs = []
    if (int(size%2)!=0):
        copiedList.append('bye')
        name_list.append('bye')
        size = int(len(copiedList))
    for i in range(size//2):
      new_pair = (copiedList[i], copiedList[-i-1])
      list_of_pairs.append(new_pair)
    self.copiedList[1] = self.name_list[-1]
    for i in range(2, size):
      self.copiedList[i] = self.name_list[i-1]
    name_list = list(copiedList)
    return list_of_pairs
