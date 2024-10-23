You are given a sequence of integers and you need to process it and display the sum of the first five numbers from this sequence, then the sum of the second five, and so on
But the sequence is not given to you all at once. Over time, successive parts of it come to you. For example, first the first three elements, then the next six, then the next two, and so on.
Implement a Buffer class that will accumulate elements of a sequence and output the sum of quintuples of consecutive elements as they accumulate.
One of the requirements for the class is that it should not store more elements than it really needs, i.e. it should not store elements that are already in the top five for which the sum was derived.

The class should look like this:
class Buffer:
    def __init__(self):
        # class constructor without arguments
    
    def add(self, *a):
        # add next part of the sequence

    def get_current_part(self):
        # return the currently saved elements of the sequence in the 
        # order they were added

Example of working with a class:

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # return [1, 2, 3]
buf.add(4, 5, 6) # print(15) – print sum of first quintuple
buf.get_current_part() # return [6]
buf.add(7, 8, 9, 10) # print(40) – print sum of second quintuple
buf.get_current_part() # return []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – print sum of third and fourth quintuples
buf.get_current_part() # return [1]

Note that during the execution of the <add> method, the output of the sum of fives may be turned on several times until there are fewer than five elements left in the buffer.