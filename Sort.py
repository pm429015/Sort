'''
    Created on Oct 22, 2013
    
    @author: pm429015
    '''

class Sort(object):
    '''
        classdocs
        '''
    
    
    def __init__(self, array):
        self._list = array
    
    def listprint(self):
        print self._list
    
    def insertSort(self, array=None):
        # classic insert sort algorithm
        # insert a value until we find the right position
        if array == None:
            array = self._list
        
        for i in range(1, len(array)):
            j = 1;
            while array[i] < array[i - j] and (i - j) >= 0:
                j = j + 1;
            temp = array[i]
            array[i - j + 2:i + 1] = array[i - j + 1:i]
            array[i - j + 1] = temp
    
    
    
    
    def merge(self,divid1,divid2):
        # comparison of two lists
        # add the small item from the two lists
        # add the largest item in the end
        sorted_list = []
        i = 0
        j = 0
        while i< len(divid1) and j< len(divid2):
            if divid1[i] <= divid2[j]:
                sorted_list.append(divid1[i])
                i += 1
            else:
                sorted_list.append(divid2[j])
                j += 1
        sorted_list += divid1[i:]
        sorted_list += divid2[j:]
        
        return sorted_list
    
    def mergesort(self, array=None):
        # recurison approach split an array into two part
        # if only one item, return
        # spilt two partrs
        if array == None:
            array = self._list
        
        if len(array) < 2:
            return array
        else:
            index = len(array)/2
            left = array[: index]
            right = array[index :]
            self._list = self.merge(self.mergesort(left),self.mergesort(right))
            return self._list
    
    
    
    def quicksort(self, array=None):
        # make the first value as threshold
        # recurison spilt the array until length > 1
        # combine togother
        if array == None:
            array = self._list
        
        if len(array) > 1:
            less = []
            equal = []
            greater = []
            threshold = array[0]
            for x in array:
                if x < threshold:
                    less.append(x)
                elif x == threshold:
                    equal.append(x)
                elif x > threshold:
                    greater.append(x)
            
            self._list = self.quicksort(less) + equal + self.quicksort(greater)
            return self._list
        else:
            return array


if __name__=="__main__":
    
    unsorted_array = [12, 11,5,4,1,7,6,3,10,13,15,12,18,2]
    
    sort = Sort(unsorted_array)
    sort.insertSort()
    sort.mergesort()
    sort.quicksort()
    sort.listprint()









