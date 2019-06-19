class RoundRobin:
    '''
    The constructor for this class will take a list of strings as the parameter.
    If there are an odd number of strings in the list, the program will append 'bye' to the end of the given list.
    '''
  
    # overriding default __init__
    def __init__(self, listOfStrings):
        '''
        This will make a shallow copy of the list given.
        '''
        self.copiedList = list(listOfStrings)
        self.nameList = list(listOfStrings)
        self.counter = 0

  def generate_round(self):
        '''
        parameter is self.
        return value will be a list of tupples. 
        one round of this method will generate one list.
        you can keep calling the method until the maximum number of unique, and distinct, teams can be generated.
        '''
        self.counter += 1
        size = int(len(self.copiedList))
        list_of_pairs = []
        maximumRoundsGenerated = 'You have generated the maximum number of unique rounds to pair each person.'

        if (self.counter >= size):
            return maximumRoundsGenerated

        if (int(size%2)!=0):
            self.copiedList.append('bye')
            self.nameList.append('bye')
            size = int(len(self.copiedList))

        for i in range(size//2):
          new_pair = (self.copiedList[i], self.copiedList[-i-1])
          list_of_pairs.append(new_pair)

        self.copiedList[1] = self.nameList[-1]
        for i in range(2, size):
          self.copiedList[i] = self.nameList[i-1]
        self.nameList = list(self.copiedList)
        return list_of_pairs

if __name__ == '__main__':
    x = RoundRobin(['Amy', 'Bill', 'Charles', 'Dan', 'Edd', 'Frank', 'Gary', 'Helen'])
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
    print(x.generate_round())
