
"""
Aggregation and counting
An essential piece of analysis of large data is efficient summarization: computing aggregations like
1. sum()
2. median()
3. mean()
4. min()
5. max()
Above methods summarize information and provide insight into the nature of a potentially large dataset
"""
import pandas as pd
dictionary_1 = {'continent': ['Asia', 'America', 'Europe']}
dictionary_2 = {'country': ['India', 'China', 'USA','Canada','UK','France'],
                'continent':['Asia', 'Asia','America','America', 'Europe','Europe'],
                'Income'   :[10,12,13,14,55,12],
                'Area' : [121,150,200,139,78,89]
                }

df1=pd.DataFrame(dictionary_1)
df2=pd.DataFrame(dictionary_2)

df3 = pd.merge(df1,df2)
"""
Output
  continent  Area  Income country
0      Asia   121      10   India
1      Asia   150      12   China
2   America   200      13     USA
3   America   139      14  Canada
4    Europe    78      55      UK
5    Europe    89      12  France
"""
print('mean',df3.Area.mean())
print('sum',df3.Area.sum())
print('median',df3.Area.median())
print('min',df3.Area.min())
print('max',df3.Area.max())

"""
Output
('mean', 129.5)
('sum', 777)
('median', 130.0)
('min', 78)
('max', 200)
"""
# other way of performing above things
df3.describe()
"""
Output
             Area     Income
count    6.000000   6.000000
mean   129.500000  19.333333
std     44.374542  17.523318
min     78.000000  10.000000
25%     97.000000  12.000000
50%    130.000000  12.500000
75%    147.250000  13.750000
max    200.000000  55.000000
"""
# This is the useful way of understanding properties of a dataset
# Groupby: Split, Apply, combine
"""
Grouby accomplishes following things:
    1. Split step involves breaking and grouping data based on the specified key
    2. Apply step involves computing some function, usually an aggregate, transformation, or filtering
    3. Combine step involves merging the results of these operations into an output array

These intermediate steps need not to be explicitly instantiated rather, the Groupby can (often) do this in
a single pass over the data
"""
df3.groupby('continent')
#Output
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x08CEE690>
df3.groupby('continent').sum()
"""
           Area  Income
continent              
America     339      27
Asia        271      22
Europe      167      67
"""
"""
column indexing

"""
df3.groupby('continent')['Area']
# output
#  <pandas.core.groupby.generic.SeriesGroupBy object at 0x08E2A2D0>
df3.groupby('continent')['Area'].mean()
"""
continent
America    169.5
Asia       135.5
Europe      83.5
Name: Area, dtype: float64
"""
# we provide multiple columns
df3.groupby('continent')['Area','Income'].mean()
"""
            Area  Income
continent               
America    169.5    13.5
Asia       135.5    11.0
Europe      83.5    33.5
"""

df3.groupby('continent')['Area'].describe().T
"""
Output
continent     America        Asia     Europe
count        2.000000    2.000000   2.000000
mean       169.500000  135.500000  83.500000
std         43.133514   20.506097   7.778175
min        139.000000  121.000000  78.000000
25%        154.250000  128.250000  80.750000
50%        169.500000  135.500000  83.500000
75%        184.750000  142.750000  86.250000
max        200.000000  150.000000  89.000000

"""
df3.groupby('continent').aggregate({'Area': 'min',
                                   'Income': 'min'
                                   })

"""
Output
           Income  Area
continent              
America        13   139
Asia           10   121
Europe         12    78
"""
"""
Transformation
It return transformed version of the full data to recombine
"""
df3.groupby('continent').transform(lambda x:x-x.mean())
"""
Output
   Area  Income
0 -14.5    -1.0
1  14.5     1.0
2  30.5    -0.5
3 -30.5     0.5
4  -5.5    21.5
5   5.5   -21.5

"""
"""
Apply() method : It helps to apply an arbitrary function to the group results. The function should take a 
DataFrame, and return either a pandas object or a scalar
"""
def example(x):
    x['Area']/=x['Area'].sum()
    return(x)

df3.groupby('continent').apply(example)
"""
Output
  continent      Area  Income country
0      Asia  0.446494      10   India
1      Asia  0.553506      12   China
2   America  0.589971      13     USA
3   America  0.410029      14  Canada
4    Europe  0.467066      55      UK
5    Europe  0.532934      12  France
"""
df4=df3.set_index('continent')
mapping={'Asia':'A','America':'B','Europe':'C'}
df4.groupby(mapping).sum()
"""
Output
   Area  Income
A   271      22
B   339      27
C   167      67
"""

"""
Pivot tables
It is a similar operation that is commonly seen in spreadsheets and other programs that operate on tabular
data. The pivot table takes simple column wise data as input, and groups the entries into a two-dimensional
table that provides a multidimensional summarization of the data.
"""
df3.pivot_table('Area', index='continent', columns='country')
"""
Output
country    Canada  China  France  India    UK    USA
continent                                           
America     139.0    NaN     NaN    NaN   NaN  200.0
Asia          NaN  150.0     NaN  121.0   NaN    NaN
Europe        NaN    NaN    89.0    NaN  78.0    NaN
"""
"""
fill_value : fill with default value if the data is not present
margins : compute totals along each grouping
"""

df3.pivot_table('Area', index='continent', columns='country' , fill_value=0, margins=True)
"""
Output
country    Canada  China  France  India  UK  USA    All
continent                                              
America       139      0       0      0   0  200  169.5
Asia            0    150       0    121   0    0  135.5
Europe          0      0      89      0  78    0   83.5
All           139    150      89    121  78  200  129.0
"""

