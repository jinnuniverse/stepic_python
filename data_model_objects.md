Implement a program that will calculate the number of different objects in a list.
Two objects <a> and <b> are considered different if <a is b> is False.

Your program has a variable called <objects> that refers to a list containing no more than 100 objects. Print the number of different objects in this list.

Expected program format:
ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)

Note:
The number of distinct objects is the maximum size of a set of objects in which any two objects are distinct.

Let's look at an example:
objects = [1, 2, 1, 2, 3] # we will assume that the same numbers correspond to the same objects, and different numbers correspond to different ones

Then all distinct objects are the set {1, 2, 3}. Thus, the number of distinct objects is three.