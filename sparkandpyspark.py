
#Distributed solutions for big data
'''Due to the limitations of working with pandas when data becomes to large or big data(e.g terrabytes) other methodes have been developed to handle
such cases. Hadoop and spark are are solutions suitable for big data then use distributed computing. This means workload is distributed accross
several nodes (e.g virtual machines, computers etc) horizontally and in a case where more resources are required nodes can also be increased.
Spark performs calculations in memory as such requires large memory to support this. Behind the scene it uses dataframes built on java virtual machines.
Spark is developed in scala but has a pyspark library that allows this to be used in python. Spark uses lazy evaluation to do calculations. This means
that all calculations occure behind the scene so that only the final result is outputed. In pandas, which uses eager evaluation, every operation or line of code
is evaluated and results are calculated.'''


# Creating dask dataframes
'''Despite the performance advanted offered by pyspark, this library is not feature reach to allow python take advantage of its performance.
An altenative to pyspark which also uses lazy evaluation is Dask. Dask is developed on python and supports distributed operations. It also
uses pandas dataframes and numpy arrays to perform computations'''

import pandas as pd
import random as rd

df = pd.DataFrame(data= {"height":[rd.uniform(1.0,2.0) for i in range(100000)], "weight":[rd.uniform(30.0,87.5) for j in range(100000)]})
print(df.head(10))

print(df.apply(max))


import dask.dataframe as dd

"Convert pandas dataframe to dask dataframe and chunk it."
ddf = dd.from_pandas(df, npartitions=9)

"print a chunk of the dask dataframe"
print(ddf)

'you will notice how results are not shown even though the calculation is done'
print(f'the mean of the columns in the dataframe is:\n{ddf.mean()}')

'compute and show result'
print(f'the mean of the columns in the dataframe is:\n{ddf.mean().compute()}')

"calculate body mass index"
result = ddf.height / ddf.weight

"compute the body mass index"
bmi = result.compute()

"show values of body mass index"
print(f'the first nine bmis are:\n{bmi}')

"create column for body mass index in ddf"
ddf["bmi"] = bmi

"show head of ddf"
print(ddf.head(9))


"""In dask one can display the graph that shows how results are calculated. It is also possible to see the visualizations for the"""
bmi.visualize()





