# Pandas Interview Questions

In this  tutorial's approach will be on Pandas-Python Interview Questions. If you are getting to be hired as Data Scientist or Data Engineer to be  working with Pandas through the ETL process, some questions could be  asked from your interviewer to ensure you are capable of handling  dynamic tasks with Pandas.

Nonetheless Pandas is one of the best Python Libraries or even on any programming language to perform data analysis or data manipulation. This tutorial will be followed by 40 questions from:

They were adapted and described with more details.

---

1) Define the Pandas/Python pandas?

R.: From the source https://pandas.pydata.org/:

"pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language"

Pandas perform as Excel spredsheets macros to help you out with automatization tasks over some data.

Example:

```python
# Defining data to the example
data = {'data':[[ 4, 40, 35, 36],[23, 34,  3, 16],[32, 35, 33, 46],[14,  2, 13,  4]],
        'target': [22, 23, 37, 29],
        'feature_names': ['month_day','indoor_temperature','outdoor_temperature','number_of_measures'],
        'DESCR': 'This a sample dataset for lecturing purposes to answer the mentioned questions above'}
```

explicação

```python
# Importing library
import pandas
```

explicação

```python
# Defining Pandas DataFrame
matrix_or_matrix_or_pandas_data_frame = pandas.DataFrame(data=data['data'],columns=data['feature_names'])
display(matrix_or_matrix_or_pandas_data_frame)
```

explicação

```python
print(matrix_or_matrix_or_pandas_data_frame['indoor_temperature'].mean())
```

explicação

---

2) Mention the different types of Data Structures in Pandas?

R.: There are two main types of data structures in Pandas:

1 - Series: It behaves as column of a pandas dataframe. For who are  familiar with algebra, it's a vector composing of diferent states.

 Series = pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

2 - DataFrame: It is a matrix, however called in Pandas as DataFrame  because you can change data from the matrxi directly as spredsheets in  excel for example.

 Dataframe=  pandas.DataFrame(data=None, index: Optional[Collection] = None, columns: Optional[Collection] = None, dtype: Union[str,  numpy.dtype, ExtensionDtype, None] = None, copy: bool = False)

Example:

```python
# from the dataset above:
dataframe = pandas.DataFrame(data=data['data'],columns=data['feature_names'])
display(dataframe)
display(dataframe.shape)
```

explain

```python
# from the dataset above:
series = pandas.Series(data=dataframe['outdoor_temperature'],name='outdoor_temperature')
display(series)
display(series.shape)
```

---

3) Define Series in Pandas?

R.: Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. The basic method to create a Series is to call:

s = pd.Series(data, index=index)

So series behave as a vector, with diferent states mesured or collected automatically or manually.

Example:

```python
import numpy as np
import matplotlib.pyplot as plt 
speed = (np.random.randint(0,100,(1,100)))
time_series = pandas.Series(data=speed[0],name = 'cars_speed')
time_series.plot()
_=plt.grid(True)
_=plt.xlabel('time (m)')
_=plt.ylabel('speed (km/h)')
_=plt.title("Car's speed")
```

explain

---

4) How can we calculate the standard deviation from the Series?

R.:

Equation standard deviation

Standard deviation are the aceptable limits to the state measure. It is related to a error having an anchor the mean valeu from the population or sample.

Example:

So we have a time series representing a sample from a power measure:

Power = [84, 83, 85, 85, 82, 98, 91, 93, 89, 96, 96, 95, 87, 94, 86, 94, 96, 93, 91, 84]

The standard deviation on pandas can be calculated as:

```python
power = pandas.Series(data = [84, 83, 85, 85, 82, 98, 91, 93, 89, 96, 96, 95, 87, 94, 86, 94, 96, 93, 91, 84],name='Electric Power')
```

explain

```python
standard_deviation = power.std()
mean = power.mean()
std_minus = mean - standard_deviation
std_max = mean + standard_deviation
lower_bound = power.min()
upper_bound = power.max()
display(standard_deviation)
display(mean)
```

explain

```python
import numpy as np
from scipy.interpolate import interp1d
import seaborn as sns
ax = sns.kdeplot(power,shade=True)
line = ax.lines[0].get_data()
ipf = interp1d(x=line[0], y=line[1])
ax.plot([std_minus, std_minus], [0, ipf(std_minus)])
ax.plot([std_max, std_max], [0, ipf(std_max)])
ax.plot([mean, mean], [0, ipf(mean)])
# Fill between
# Por a legenda das estatistcicas
```

explain

---

5) Define DataFrame in Pandas?

Answer:

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. Like Series, DataFrame accepts many different kinds of input:

    Dict of 1D ndarrays, lists, dicts, or Series
    
    2-D numpy.ndarray
    
    Structured or record ndarray
    
    A Series
    
    Another DataFrame

Example:

```python
d = {'one': pandas.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'd']),
     'two': pandas.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
```

explain

```python
#From dict of Series or dicts

df = pandas.DataFrame(d)
display(df)
```

explain

```python
# From dict of ndarrays / lists

d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
display(pandas.DataFrame(d))
```

explain

```python
data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
display(pandas.DataFrame(data))
```

explain

```python
# From a list of dicts

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
display(pandas.DataFrame(data2))
```

explain

```python
# From a dict of Tuples
display(pandas.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                  ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                  ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                  ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                  ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}}))
```

explain

```python
# From a series
  
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti'] 
article = [210, 211, 114, 178] 
  
auth_series = pandas.Series(author) 
article_series = pandas.Series(article) 
  
frame = { 'Author': auth_series, 'Article': article_series } 
  
result = pandas.DataFrame(frame) 
  
display(result) 
```

explain

```python
df1 = pandas.DataFrame(np.random.randn(5,3), index=pandas.date_range('01/02/2014',periods=5,freq='D'), columns=['a','b','c'] )
df2 = pandas.DataFrame(np.random.randn(8,3), index=pandas.date_range('01/01/2014',periods=8,freq='D'), columns=['a','b','c'] )

# Create an index list from the set of dates in both data frames
Index = list(set(list(df1.index) + list(df2.index)))
Index.sort()

df3 = pandas.DataFrame({'df1': [df1.loc[Date, 'c'] if Date in df1.index else np.nan for Date in Index],\
                'df2': [df2.loc[Date, 'c'] if Date in df2.index else np.nan for Date in Index],},\
                index = Index)

display(df3)
```

