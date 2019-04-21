
"""
Handling missing values

Generally, there are two strategies involved:
1. Masking :It involve appropriation of one bit in the data representation to locally indicate the null 
            status of a value.
2. Choosing a sentinel value that indicate a missing value like putting -999 or anything else.


"""
import numpy  as np
import pandas as pd

val_o = np.array([1,None,2,3,45,6])
val_o
"""
This dtype object means that the best common type representation NumPy could infer for the contents of the
array is that they are python objects
Output

array([1, None, 2, 3, 45, 6], dtype=object)
"""
"""
Use of python object in an array also means that if you perform aggregations like sum() or min() 
across an array with a None value, you will generally get error
val_o.sum()
"""

val_f = np.array([1,np.nan,2,3,45,6])
val_f
# print the array and notice the difference that this time an array type is create not an object
val_f.sum()
"""
output
nan
"""

"""
Handling missing values in Pandas
NaN and None both have their place, and pandas is built to handle the two of the them interchanageably

Operating on Null values
There are several useful methods for detecting, removing, and replacing null values in Pandas data structures.
They are:
    1. isnull() : Generate a boolean masking indicating missing values
    2. notnull(): opposite of isnull()
    3. dropna() : Return a filtered version of the data
    4. fillna() : Return a copy of the data with missing values filled or imputed

Detecting Null values:
    Pandas data structure have two useful methods for detecting null data:
        1. isnull()
        2. notnull()
"""
data_miss = pd.Series([1,np.nan,2 ,3,np.nan,5])
data_miss.isnull()
"""
Output:
0    False
1     True
2    False
3    False
4     True
5    False
dtype: bool
"""

data_miss.notnull()
"""
Output:
0     True
1    False
2     True
3     True
4    False
5     True
dtype: bool

"""
"""
Dropping null values
"""

data_miss.dropna()
"""
Output:
0    1.0
2    2.0
3    3.0
5    5.0
dtype: float64
"""
"""
Dropping columns in a matrix
"""

df=pd.DataFrame([[np.nan,1,2],[2,3,4],[3,np.nan,5]])
df.dropna() # drop all the rows containing null values
df.dropna(axis=1) # drop all the columns containing null values

"""
This will drop all the columns if any value present in the column is null and thus it leads to loss of 
information. The default is how="any", such that any row or column containing null value will be dropped.
We can specify how="all" , which will only drop rows or columns if all are null values.
"""

df.dropna(how="all")
"""
Output
     0    1  2
0  NaN  1.0  2
1  2.0  3.0  4
2  3.0  NaN  5
"""
"""
Filling null values 
fillna() method return copy of the array with the null values replaced
"""

df.fillna(0)
"""
Outout--> Null values replaced by zero, we can replace it with any other value depending on circumstances
     0    1  2
0  0.0  1.0  2
1  2.0  3.0  4
2  3.0  0.0  5
"""
"""
Other method:
    Forward fill --> to propagate the previous value forward : df.fillna(method='ffill')
    Back fill    --> to propagate the next values backward : df.fillna(method='bfill')
    
"""
