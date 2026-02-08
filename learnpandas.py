from sklearn.datasets import load_iris
import pandas as pd
import logging as lg
import random
import datetime as dt



iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names,) 
df['target'] = iris.target
df['target_names'] = df['target'].apply(lambda x: iris.target_names[x])


"""observe the first 7 rows and all columns of the data"""
print(df.head(7))

df.tail(10) #last 10 rows of the iris dataset

"""inspect the data"""
df.info()

df1 = df.reset_index() #create a new dataframe and make row_index a column

"""Use iloc to slice rows or columns by index(lower limit is always plus one while the lower limit is -1)"""
print(df.iloc[:5,]) 

print(df.iloc[2:8,3:6]) #slice fm 3th row to the 7th row and 4th column to 6th column. 6th column is at index 5 so :6 slices indes 5

print(df.iloc[50:,:4])

print(df.iloc[:,3:])

print("we are here! \n")
print(df.iloc[2:15,[1,2,5]]) # columns 1 2 and 5.

"""use loc to slice a dataframe by column names. Rows can be sliced by conditions based on column value"""
print(df.loc[df['target_names'] == "setosa",['target','target_names']]) # retrieve target and target_names of setosa

df.loc[:,"sepal length (cm)":"petal width (cm)"] #retrieve columns between sepal length and petal width inclusive

"""use iat to acces cell values by index"""
print(r'The value at row {} and column {} is:'.format(15,5),df.iat[12,5]) 

"""use at to access cell value by index and column name"""
print(r'The value at row {} and column {} is:'.format(15,5),df.at[13,"petal width (cm)"]) 

"""Convert long data to wide"""
print(df1.loc[:,"target"].unique(),"\n")

print(df1.head())

df1 = df.pivot(columns="target_names", values="petal width (cm)")

df1names = list(df1.columns)

dfnames = list(df.columns)

print("df1 names:",df1names, "\n","df names:",dfnames)

"""Trim unwanted parts of column names"""
def textrim(lis):
    for tex in lis:
        if "(cm)" in tex:
            lis[lis.index(tex)] = tex[:-len("(cm) ")]
    return lis

print(textrim(dfnames))

df.columns = dfnames

df.rename(columns={"sepal lenght":"sepalL", "sepal width":"sepalW","petal lenth":"petalL","petal width":"petal"}, inplace=True)

print(list(df.columns)) 



# creating pandas DataFrames
'''Pandas dataframes are one of the most used datastructure in Data Science. Data is stored in form of a 2D table structure. The columns and rows of a dataframe maybe be labelled.
The Data in a pandas DataFrame can be accessed by Column, Row or combination of Column and Row.
Pandas is designed to run on a single machine so its performance is bound on the memory of this machine. This is a drawback for pandas dataframes.
To optimize its performance pandas uses chunking so the data is choped in a size that will fit in the memory of the machine'''

## Create empty pandas DataFrame: By importing the pandas modul an empty pandas dataframe is created automatically.

## Create pandas Dataframe from a python dictionary: The keys of the dictionary are column names while the values are column values.

pan_dict = {'first name': ["yufeyuy","adhiambo","nyuydzedzey","leinyuy"], "last name": ["tardze","simba","sunjo","nyuy"],
            "age":[31,25,31,24], 'height':[1.62,1.70,1.65,1.61],"id_created_on": ['2021.11.21','2014.07.13','2015.08.12','2011.03.08']}

pan_dict_df = pd.DataFrame(pan_dict)

print(pan_dict_df.head(2), '\n')

'''Function takes a dataframe and returns list of column names for this dataframe otherwise it will raise and Exception'''
def getcolnames(df) -> list:
    if isinstance(df,pd.DataFrame):
        lis = [col for col in df.columns]
        return lis
    raise Exception(f'Expected a DataFrame but got {type(df)}') 
colnames = getcolnames(pan_dict_df)

## Create pandas Dataframe from a python list of lists: every sublist represent a row and the dataframe has default column names. It is important to pass desired column names.
pand_lis = [
    ["yufeyuy","tardze",31, 1.62,'2021.11.21'],
    ["adhiambo","simba",25,1.70, '2014.07.13'],
    ["nyuydzedzey","sunjo",31,1.64,'2015.08.12'],
    ["leinyuy",  "nyuy",24, 1.61,'2011.03.08'], 
          ]

pand_lis_df = pd.DataFrame(pand_lis, columns=colnames)

print(pand_lis_df)

## Create pandas Dataframe from file e.g csv: To read multiple files from a directory you might need to set a directory with os.chdir(...)

yelp_reviews = pd.read_csv(r'C:\DataAnalysis\reviews.csv')


#Investigating the data in a pandas dataframe: A pandas dataframe has several methods that can be used to inspect its content. See examples!

print('\n',pan_dict_df.tail(2))

print("yelp_reviews structure")
pan_dict_df.info()  #this is like str(df) in R

'''the describe method and other stat methods like min, max can be used to show summary stats for numerical columns,by default, of a pandas dataframe.
if summary stats for non-numerical columns should be shown use the parameter include = np.object or include = "all" '''
print(pan_dict_df.describe())
print(pan_dict_df["height"].median())  
print("average height is:",pan_dict_df["height"].mean())   
print("youngest person is:",pan_dict_df["age"].min())  
print('oldest person is:',pan_dict_df["age"].max()) 
print(pand_lis_df[["first name","height"]].count()) 

## accessing data of a dataframe
'Data can be selected from a dataframe like in dictionaries. The following selects the frist name and height columns from the dataframe'
pand_lis_df[["first name","height"]]

'If the columns in the dataframe does not contain white spaces or special characters, then columns can also be selected using the dot syntax.'
print("select the age column\n",pand_lis_df.age)
print("select the height column\n",pand_lis_df.height)

"""When working with much data, it is recommended to use iloc and loc"""
'loc slices dataframe by rows and columns. The columns must be passed as names'

print('content of last name and age:\n',pand_lis_df.loc[:,["last name",'age']])

pand_lis_df.loc[1:3,"height"]

print(pan_dict_df)

print("give me the first two rows of the dataframe:\n",pan_dict_df.loc[0:1])

'iloc slices dataframe by rows and columns. The columns must be supplied as index'
print(pand_lis_df.iloc[:3,[1,4]])


'at can be used to access a targeted cell content based on a column name'
print(pan_dict_df.at[2,"last name"])

'iat can be used to access a targetted cell content based on an index'
print(pan_dict_df.iat[0,4])

"one can get the content of a column via the . format. Condition is that the column name must not have whitespaces and unwanted characters. This content can also be stored in a list e.g"
print(list(pan_dict_df.height))

print("the cummulative sum of ages is:", list(pand_lis_df.age.cumsum()))


## Selecting data from a pandas dataframe using boolean mask. A boolean is a list of true or false values determined by the defined selection criteria.
'There are several ways to create a boolean mask then use this to filter a dataframe. Most important thing is that the boolean mask must have same lenght as the dataframe'

'first of all define the filter criteria'
bnmast = pan_dict_df.age == 31  
print(f'My first boolean mask:\n{bnmast}')

'use boolean mast to filter dataframe'
print(pan_dict_df.loc[bnmast], '\n')
print(pan_dict_df[bnmast])

'define second filter criteria'
mask = pan_dict_df.age % 2 == 0
print(f'persons with even ages are:\n',pan_dict_df[mask])

'define third filter criteria'
mask = (pan_dict_df.loc[:,"age"] % 2 != 0) & (pan_dict_df["height"] <= 1.65)
print(mask)
print(f'small persons with odd ages are:\n', pan_dict_df[mask])

## creating a new column: New columns can be derived from the dataframe while others can be attached to the dataframe.
'Create a column from an existing dataframe'
pan_dict_df.loc[:,"body_age_index"] = pan_dict_df.height / pan_dict_df.age
print(f'the new dataframe!:\n', pan_dict_df)
pan_dict_df["bodyageindex"] = round(pan_dict_df.height / pan_dict_df.age,3)
print(f'the latest dataframe:\n', pan_dict_df)

## Manupulating pandas dataframes: Data manupulation is an important aspect of data analysis that may contain a few to numerous steps.
'There are a handful of pandas methods that can be used for data manupulation e.g rename, astype, drop, replace etc'

### rename
'The rename method can be used to rename columns and rows of a dataframe'

mapper = {'first name': 'First Name','last name':'Last Name', 'age':'Age','height':'Height', 'id_created_on':'Id_Creation'}
pand_lis_df.rename(mapper=mapper, axis=1, inplace=True)

print(f'rename column dataframe using mapper and axis:\n', pand_lis_df)

'An altenative to using mapper and axis, specif arguments in this method can be used.'


pand_lis_df.rename(columns= {'First Name': 'FirstName','Last Name':'LastName', 'Age':'Ages','Heights':'Height'}, inplace=True)

print(f'rename dataframe column names:\n',pand_lis_df)

### drop
'drop specific rows...here we drop rows at indices 0 and 2'
pand_lis_df.drop(index=[0,2], inplace=True)

print(pand_lis_df)

### change datatypes
'cast dataframe column to date'
pand_lis_df["Id_Creation"] = pd.to_datetime(pand_lis_df['Id_Creation'], format='%Y.%M.%d').dt.date

print(pand_lis_df.info())

print(pand_lis_df)

## updating data in a pandas dataframe. There are severas ways of doing this.
new_pan_dict_df = pan_dict_df.loc[:,:]
new_pan_dict_df.set_index("first name", inplace=True)
print(new_pan_dict_df)

'update the bodyageindex for nyuydzedzey'
new_pan_dict_df.loc["nyuydzedzey", "bodyageindex"] = 0.058

pan_dict_df.set_index('first name', inplace=True)
print(pan_dict_df)

'now use the new dataframe to update the original dataframe. Take note that update uses row_indices to update records. Thus it is important that the indices for both dfs correspond.'
pan_dict_df.update(new_pan_dict_df)

'reset the row indices as they were'
pan_dict_df.reset_index(inplace=True)

'conditionally updating values..where bodyageindey <= 0.060 then replace the values by 0.062'
pan_dict_df["bodyageindex"][pan_dict_df["bodyageindex"] <= 0.060] = 0.062

'Altenatively, records can be replace using the replace method'

pand_lis_df.loc[:,"Ages"].replace(24,25, inplace=True)

print(f'The current df from dictionary is:\n',pan_dict_df)

print(f'The current df from list of lists is:\n',pand_lis_df)

# applying functions on dataframe

'Asuming one needs to sum a series of numbers. One could do'
count = 0
for i in range(10):
    count += i
print(f'the value of count is {count}')

'There is an altenative solution using a built-in function. Here sum takes an iterable an add its values'
print(sum(range(10)))

## use a built-in function and the apply method from a dataframe to perform an operation accross columns of the dataframe.

'''apply is a dataframe method that takes a function(built-in or third party, self defined functions) an applies it to rows or columns of a dataframe.'''

"Get the max age and height of persons in the persons dataset"
print(pan_dict_df.loc[:,['age','height']].apply(max))

## define function to apply on rows of given column

'In row based apply, every row of a selected number of column(s) are evaluated against a given criteria. This is good for creating new columns.'
def newcol(row):
    if row >= 26:
        return "etwas aelter"
    return "etwas junger"

pan_dict_df["agegroup"] = pan_dict_df.age.apply(newcol)

print(pan_dict_df)

## define function to apply on columns of a dataframe
"""
In column based apply, a function(built-in, self-defined or third party) is applied to each or selected colums of a dataframe.
Most important thing here is that an aggregated result or a single result for each column is returned.
"""
def size(col):
    count = 0
    for ele in col:
        count += 1
    return count
print(pan_dict_df.apply(size))

'The result of the function above can be achieved using a built-in function!'
def size1(col):
    return len(col)

print(pan_dict_df.apply(size1))

'''
In row and column based apply a function is applied to columns taking into consideration pre-defined conditions that must be
evaluated are row levels for each column.
'''
