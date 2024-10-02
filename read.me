Implement a program that will emulate working with namespaces. It is necessary to implement support for creating namespaces 
and adding variables to them.

In this task, each namespace has a unique text identifier - its name.

The following requests are sent to your program as input:

- create <namespace> <parent> –  create a new namespace with the name <namespace> inside namespace <parent>
- add <namespace> <var> – add variable named <var> to a namespace <namespace>  
- get <namespace> <var> – get the name of the namespace from which the variable <var> will be taken when requested from the namespace 
named <namespace> , or None, if such namespace does not exist.

Let's consider a set of queries

- add global a
- create foo global
- add foo b
- create bar foo
- add bar a

The namespace structure described by these queries will be equivalent to the namespace structure created by executing this code.

a = 0
def foo():
  b = 1
  def bar():
    a = 2
	
In the main body of the program, we declare the variable <a>, thereby adding it to the namespace <global>. Next, we declare 
the function <foo>, which entails the creation of a local namespace for it inside the <global> namespace. In our case, this is 
described by the command <create foo global>. Next, we declare the function <bar> inside the function <foo>, thereby creating 
the <bar> namespace inside the <foo> namespace, and add the variable <a> to <bar>.

Let's add <get> requests to our queries

- get foo a
- get foo c
- get bar a
- get bar b

Let's imagine how this might look in code

a = 0
def foo():
  b = 1
  get(a)
  get(c)
  def bar():
    a = 2
    get(a)
    get(b)
	
The result of a <get> request is the name of the namespace from which the variable is taken.
For example, the result of <get foo a> is <global> because the <foo> namespace has not declared a variable named <a>, 
but the <global> namespace that contains <foo> has declared a variable named <a>. Similarly, the result of <get bar b> is <foo>, 
and the result of <get bar a> is <bar>.

The result of <get foo c> is None because neither <foo> nor its outer <global> namespace has declared a variable <c>.

More formally, the result of get <namespace> <var> is

- <namespace> if the variable <var> was declared in the space <namespace>
- get <parent> <var> - is the result of a query on the namespace within which the namespace <namespace> was created, 
if the variable was not declared
- None if there is no <parent>, i.e. <namespace> is <global>

Input data format

The first line contains a number n (1 ≤ n ≤ 100) – the number of queries.
Each of the next n lines contains one query.
The queries are executed in the order in which they are given in the input data.
The namespace names and variable names are strings of length no more than 10, consisting of lowercase Latin letters.

Output data format

For each <get> request, print its result on a separate line.

Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:

global
None
bar
foo