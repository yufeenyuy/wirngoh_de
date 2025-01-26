-------------------------------------------------------------------------------------------------------------------------------
--when working in python, it is recommendable to work in virtual environments as it enhances code sharing as it maintains the conditions within which a code or project was developed. The versions of packages installed within a virtual environment does not change. In this project there are two virtual environments namely; .venv and venv.

--requirement.txt file is used to consolidate all the packages or libraries used within a project. This is usually shared alongside the code so other developers will run this or continue development with the same packages or libraries.

--learn.py
In this script i learned python from the basics starting from creating variables through calculations(precedence), datatypes, if statements, loops, and using and writing functions. This is the foundation of all the work i was able to do in this project. As a resource i used the Tutorial_EDIT.pdf file which i got on the internet. I also recommend the learnpython.pdf file. I found this resources quite helpful for someone wanting to refresh python skills. I also recommend this for anyone who has never had an experience learning or using python before. If this resource cannot help you download and install python, then you can find other sources on the internet. There are several youtube videos that show how to get started with python as well.

--learnpandas.py
After learning the basics of python and understanding python datatypes, i used the Pandas_Cheat_Sheet.pdf to get started with pandas for working with data. Pandas is a great library in python that one can use to transform data and create dataframes that can be ingested in a database for further analysis. A dataframe is a particular datatype in python that takes the form of a table making it easy to manupulate with functions from the pandas library.

--postgres_ingest_operations.py
Here i started learning how to use python to interact with databases. Starting with creating connections and creating and ingesting tables. Postgresql is the database i used. I don't recommend anyone to use this if they don't know what they are doing. Most of the functions in quotes where with a lot of support from chatgpt. As such i can't guarantee its functionality as this moment.

--postgresops.py
In this script i wrote a few operations that can be used to interact with a postgresql database when doing data ingestion. The most imortant functions are
checkschema_and_table: To check the existence of a particular schema and table
ingest_data: To incrementally ingest data in a database
delete_row: Delete all entries that older than five days since ingestion. Don't use this function if you don't know what you are doing because delete operations can lead to complete data loss.

--websockets.py
In this script i learned how the concept of REST APIs and how to use REST to interact with web services to retrieve data, and also how to do web scraping. I equally learned how to create XML and JSON, and read data from them. I also learned how to convert json to
python dictionary. I practiced this skill using the libraries urllib and beautifulsoup.

--createlogsandnumpy.py
In this python script i leaned how to create log files in different ways. Log files are used to store different information
about the behavior of a code during execution. This can help to track errors and also analyse performance of a code.

--dataextraction.py
 In this script i practiced how to extract data from yelp using the yelp fussion rest api. The data extracted is later ingested in a postgresql database. This is done in the main.py script. Yelp is a platform that advertises businesses and provide user-generated reviews for these businesses. Yelp provide developers with APIs that allow them to querry their public database. This public database is accessible via Yelp fussion or GraphQl. There is a comprehensive documentation to help you get started with Yelp fussion and GraphQl. You can find this via the following links.

Yelp Developer Documentation:  https://docs.developer.yelp.com/docs/getting-started.
Yelp fussion API: REST API with several endpoints for querying the public database.
GraphQl: An efficient way to query NoSQL graph databases as it offers the possibility to make several requests with a single query, unlike REST.

--exchangerate.py
In this script i implemented a scraper to get exchange rate data from exchangerate.org. It is important to explicitly state it here that it is illegal to scrape any site without consent of the owners site. In the event of any legal issues, i take no responsibility 
for anyone who uses my script to scrape data from exchangerate.org.

--fake_microfinance_data.py
I created fake sample data in the context of microfinance. The data is used to create a power bi demo report.

--regex.py
In this script, i learned the basics of writing regular expressions in python.

--sharepoint.py
Sharepoint is a microsoft online service that can be used for internal communication as well as managing files between user groups and
even departments. Sometimes data used for analysis can be stored in sharepoint. Since this is not a database, it might be necessary to
move data into a database for teams or departments considering scalability and better data management. In this script i used the graph api endpoint provided by microsoft to access my personal sharepoint subscription to read data from a particular sharepoint site.
The data retrieved is later ingested in a postgresql database. In order to use the graph api endpoint one must have a microsoft azure subscrition and a Microsoft Entra ID which can be created in azure. Additional one must create an app in microsoft azure to get login credentials necessary to access sharepoint programatically. When creating the app consider storing the client secrete where you can retrieve it for use because you will not be able to retrieve this in azure once you complete the process of creating the app. Also consider granting necessary read and write permissions to this app as it is necessary for interacting with sharepoint. The data retrieved from share point is ingested in a postgresql database. This is done in main.py.

--sparkandpyspark.py
In this file i learned the basics of spark and pyspark.

--main.py
In this script the data from different sources i.e exchange rate, sharepoint and yelp, are ingested.