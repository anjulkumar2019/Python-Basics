"""
Pandas: Pandas objects are enhanced versions of NumPy structured array in which the 
rows and columns are identified with lables rather than simple integer indices.
Fundamental Pandas data structures are: Series, DataFrame, and Index 
"""
# Following code includes pandas and numpy library in the program
import pandas as pd
import numpy  as np


"""
1. Pandas Series: One dimensional array of indexed data and it can be created from a list or array as follows
"""

data=pd.Series([1,2,3,4,5])
print(data)
"""
Output:
0    1
1    2
2    3
3    4
4    5
dtype: int64

Pandas series object wraps both a sequence of values and a sequence of indices, which we can access with the 
values and index attributes.
"""
print('print index' ,data.index)
print('print values', data.values)
"""
Following code is used to access specific columns 

data[startindex:endindex]
startindex is inclusive and endindex is exclusive
"""
print(data[1])
print(data[1:3])

"""
The essential difference is the presence of the index: while the NumPy array has an implicitly defined 
integer index used to access the values, the Pandas series has an explicitly defined index associated 
with the values. The index need not be an integer, but can consist of values of any desired type.
"""

data_index = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(data_index)
"""
Output:
a    1
b    2
c    3
d    4
e    5
dtype: int64

"""

"""
So index is basically used to map rows with the key. In turn, this type of structure is a bit like a specialization
of a python dictionary. A dictionary is a structure that maps arbitrary keys to a set of arbitrary values, and a
series is a structure that maps typed keys to a set of typed values.
Also, we can create pandas series object directly from python dictionary. Let's see how it happens...
"""

dictionary = {'Name':'Anjul', 'School':'Don Bosco School','City':'Delhi'}
data_dict  = pd.Series(dictionary)
print(data_dict)

"""
Output:
City                 Delhi
Name                 Anjul
School    Don Bosco School
dtype: object

By default: a series will be created where the index is drawn from the sorted keys
"""
print(data_dict['Name'])
"""
Key is used to access the particular row in dictionary
Output:
Anjul
"""

"""
Now, let's see what will happen when number of explicitly supplied keys are lesser in number than the number
of dictionary values
"""
data_dict=pd.Series(dictionary, index=['Name','City'])
print(data_dict)
"""
Series is populated for explicitly defined keys only.
output:
Name    Anjul
City    Delhi
dtype: object
"""
"""
2. Pandas DataFrame: Pandas series is an analog of a one dimensional array having flexible indices, a DataFrame
   is an analog of a two dimensional array with both flexible row  indices and flexible column names 
"""
population_city = {'India': '1.32bn' , 'USA':'300mn', 'UK':'80mn','France':'30mn'}
capital_city = {'India': 'New Delhi','USA':'Washington DC','UK':'London', 'France':'Paris'}
data_capital = pd.Series(capital_city)
"""
Now we use a dictionary to construct a single two dimensional object containing this information
"""

states = pd.DataFrame({'Capital City':capital_city, 'Population':population_city})
print(states)
"""
Also, Dataframe has a columns attribute, which is an index object handling the column index
Output:
         Capital City Population
France          Paris       30mn
India       New Delhi     1.32bn
UK             London       80mn
USA     Washington DC      300mn

"""

print(states['Population'])
"""
Print population column for all the rows
Output
France      30mn
India     1.32bn
UK          80mn
USA        300mn
Name: Population, dtype: object
"""
print(states.loc['UK'])
"""

.loc is used for label based indexing and .iloc is used for positional indexing

Print information about the row
Output:
Capital City    London
Population        80mn
Name: UK, dtype: object

"""
"""
Constructing a dataframe object
1. From a single series object
2. From a list of dictionarys
3. From a dictionary of series objects
4. From a two dimensional Numpy array
5. From a Numpy structured array  - try it yourself
"""
#1. From a single series object
pd.DataFrame({'population':population_city})
#2. From a list of dictionarys
data=[{'x':i,'y':3*i} for i in range(10)]
pd.DataFrame(data)
#3. From a dictionary of series objects
states = pd.DataFrame({'Capital City':capital_city, 'Population':population_city})
print(states)
#4. From a two dimensional Numpy array
pd.DataFrame(np.random.rand(4,3), columns=['x1','x2','x3'], index=['y1','y2','y3','y4'])


"""
Index object can be thought as an immutable array or as an ordered set
"""
ind=pd.Index([i for i in range(5)])
print(ind)
"""
Output

Int64Index([0, 1, 2, 3, 4], dtype='int64')
"""
"""
below statement will generate error because Index object is immutable 

ind[3]=6

TypeError: Index does not support mutable operations
"""

indA = pd.Index([1,2,3,4])
indB = pd.Index([2,3,4,5])

print(indA & indB) # Intersection of two index's
print(indA | indB) #Union 
print(indA ^ indB) # symmetric difference

"""
Data selection and Indexing
"""
# Data selection in a series

data_sel = pd.Series([1,2,3,4], index=['a','b','c','d'])
data_sel['a']
"""
output
1
"""
# we can use dictionary like expressions and methods to examine the indices and values
print('a' in data_sel) # output: True
print('e' in data_sel) # output: False
"""
Series objects can be modified with the dictionary like syntax
"""
data_sel['d']=9
print(data_sel)

print(data_sel['a':'c'])
"""
Output
a    1
b    2
c    3
dtype: int64
"""
print(data_sel[0:2])
"""
Output
a    1
b    2
dtype: int64
"""

data_sel[(data_sel >=2) & (data_sel <8) ]
"""
Output
b    2
c    3
dtype: int64
"""

"""
Notice: When you are slicing using explicit index (data_sel['a':'c']) then final index is included in the slice, while
when you are slicing with an implicit index(data_sel[0:2]) then final index value is excluded 
"""

# Indexers loc, iloc, and ix
data_indexer= pd.Series(['A','B','C','D','E'], index=[1,2,3,4,5])

data_indexer.loc[1:3]
"""
output:
1    A
2    B
3    C
dtype: object
"""

data_indexer.iloc[1:3]
"""
Output
Out[56]: 
2    B
3    C
dtype: object
"""
#ix is a hybrid of the two

"""
Data selection in DataFrame
"""
print(states)
print(states['Population'])  # Print population column
print(states.Population is states['Population']) # True

# Print transpose 
print(states.T)
"""
Output

             France      India      UK            USA
Capital City  Paris  New Delhi  London  Washington DC
Population     30mn     1.32bn    80mn          300mn
"""

print(states.values)

a=np.random.randint(10, size=(3,4))
print(a)
df=pd.DataFrame(a, columns=list('QSRT'))
printf(df)
"""
output
   Q  S  R  T
0  8  8  6  3
1  8  1  6  6
2  4  1  5  2

"""
df-df.iloc[0]
"""
output
   Q  S  R  T
0  0  0  0  0
1  0 -7  0  3
2 -4 -7 -1 -1
"""

