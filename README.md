#COLAB LINK FOR ML SESSION
https://colab.research.google.com/drive/1ez1t6A2qkeEwIsdciZnOoEfwZOjmuKCH?usp=sharing
## Tasks for students

**1. What will be the output of the following Python code? Explain.**
```python
a = [1,2]
b = [1,2]

c = [(x,y**2) for x in a for y in b] 
print(c)﻿
```
- a. [(1, 1), (1, 4), (2, 1), (2, 4)]
- b. [(1, 1), (1, 2), (2, 1), (2, 2)]
- c. [(1, 1), (1, 2), (2, 2), (2, 4)]
- d. [(1, 1), (1, 4), (2, 1), (2, 2)]
- e. Error

**2. What will be the output of the following Python code? Explain.**
```python
a = [1,2,3,4,5,6,7,8,9,10]
print(a[-1:-5])﻿
```
- a. [2,3,4,5]
- b. [5,4,3,2]
- c. [10,9,8,7]
- d. []
- e. Error

**3. What will be the output of the following Python Code? Explain.**
```python
def fn(data1, data2):
    return {data1, data2}

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

z= fn(tuple(list1),tuple(list2))

print(z, type(z))﻿
```
- a. {1:5, 2:6, 3:7, 4:8, 5:9} <class 'dict'>
- b. {1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>
- c. {[1, 2, 3, 4, 5], [5,6,7,8,9]} <class 'dict'>
- d. {(1, 2, 3, 4, 5), (5, 6, 7, 8, 9)} <class 'set'>
- e. Error

**4. What will be the output of the following Python code? Explain.**
```python
def product(a, b):
    return a * b


def add(a, b):
    return a + b


answer = (product if True else add)(2, 3)
print(answer)﻿
```
- a. 5
- b. 6
- c. 11
- d. Error

**5. What will be the output and why it is so ?**
```python
d = {True: "guvi", 1: "Good night"}

print(d)
 ```
