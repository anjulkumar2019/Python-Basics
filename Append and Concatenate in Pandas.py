"""
Combining datasets: Concat and Append
Pandas includes functions and methods that make this sort of data wrangling fast and straightforward
"""

import pandas as pd
df1 = pd.DataFrame(['a','b','c','d'],columns=['df1'], index=[1,2,3,4])

df2=pd.DataFrame(['e','f','g','h'], columns=['df2'], index=[1,2,3,4])

"""
Pandas has a function pd.concat() to perform concatination
"""
pd.concat([df1,df2])
"""
Output
   df1  df2
1    a  NaN
2    b  NaN
3    c  NaN
4    d  NaN
1  NaN    e
2  NaN    f
3  NaN    g
4  NaN    h
"""
# By default concatenation takes place row wise within the DataFrame
# Duplicate indices : by default pandas preserve indices, even if the result will have duplicate indices
pd.concat([df1,df2], axis=1)
"""
Output
  df1 df2
1   a   e
2   b   f
3   c   g
4   d   h
"""
"""
If you want to verify that indices in the result of pd.concat() do not overlap, you can specify the 
verify_integrity flag. With this set to True, the concatenation will raise an exception if there are
duplicate indices.
"""

try:
    pd.concat([df1,df2], verify_integrity=True)
except ValueError as e:
    print('ValueError:', e)

"""
output
('ValueError:', ValueError("Indexes have overlapping values: Int64Index([1, 2, 3, 4], dtype='int64')",))
"""

"""
Ignoring index
Sometimes index does not matter then they can be ignored
"""
pd.concat([df1,df2], ignore_index=True)
"""
Output
   df1  df2
0    a  NaN
1    b  NaN
2    c  NaN
3    d  NaN
4  NaN    e
5  NaN    f
6  NaN    g
7  NaN    h
"""
"""
Concatenation with Joins
By default entries for which no data is available are filled with NA values. To change this, we can specify
one of the several options for the join and join_axes parameters of the concatenate function. By default join
is a union of the input columns (join="outer"), but we can change to 'inner' for intersection and 'left' for 
left join
"""
df3=pd.DataFrame(['z','x','y','g'], columns=['df2'], index=[1,2,3,4])
pd.concat([df3,df2], join='inner')
"""
Output
1   z
2   x
3   y
4   g
1   e
2   f
3   g
4   h
"""
pd.concat([df1,df2], join='inner')
"""
Output
Empty DataFrame
Columns: []
Index: [1, 2, 3, 4, 1, 2, 3, 4]
"""
"""
Append() method
Accomplish the same thing in fewer keystrokes
"""
df1.append(df2)
"""
Out[17]: 
   df1  df2
1    a  NaN
2    b  NaN
3    c  NaN
4    d  NaN
1  NaN    e
2  NaN    f
3  NaN    g
4  NaN    h
"""

"""
Difference between append and extend
Append method does not modify the oroginal object, instead it creates a new object with the combined data.
Extend method modify the object
"""

"""
Combining datasets: merge and join
pd.merge() implements a number of types of joins: the one-to-one, many-to-one, and many-to-many joins
"""
"""
df4=pd.merge(df1,df3)
MergeError: No common columns to perform merge on. 
Merge options: left_on=None, right_on=None, left_index=False, right_index=False
"""

df4=pd.DataFrame({'country':['India','Nepal', 'USA','UK', 'France'],
                  'Population':[132,123,12,65,23]})

df5=pd.DataFrame({'country':['India','Nepal', 'USA','UK', 'France'],
                  'GDP':[12,13,14,15,16]})
    
df6=pd.merge(df4,df5)
"""
   Population country  GDP
0         132   India   12
1         123   Nepal   13
2          12     USA   14
3          65      UK   15
4          23  France   16
"""
# Specifying merge key

df7=pd.merge(df4,df5,on = 'country')
"""
Output
   Population country  GDP
0         132   India   12
1         123   Nepal   13
2          12     USA   14
3          65      UK   15
4          23  France   16
"""
"""
At times you don't have same column name in two dataframes then you can specify column name on which merge 
to happen
"""

df8=pd.DataFrame({'name':['India','Nepal', 'USA','UK', 'France'],
                  'GDP':[12,13,14,15,16]})

    
df9=pd.merge(df4, df8, left_on="country", right_on="name")
"""
Output
   Population country  GDP    name
0         132   India   12   India
1         123   Nepal   13   Nepal
2          12     USA   14     USA
3          65      UK   15      UK
4          23  France   16  France
"""

"""
Set_index is used to set the index of a dataframe
"""

df8.set_index('name')
"""
        GDP
name       
India    12
Nepal    13
USA      14
UK       15
France   16
"""
"""
Join() method performs a merge that defaults to joining on indices

"""
df4.set_index('country', inplace=True)
df5.set_index('country', inplace=True)
df10=df4.join(df5 )
"""
Output
         Population  GDP
country                 
India           132   12
Nepal           123   13
USA              12   14
UK               65   15
France           23   16
"""

