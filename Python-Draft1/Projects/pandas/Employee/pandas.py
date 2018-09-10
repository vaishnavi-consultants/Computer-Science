# Pandas
# Pandas is an open-source, BSD-licensed Python library providing
# high-performance, easy-to-use data structures and data analysis
# tools for the Python programming language. Python with Pandas is
# used in a wide range of fields including academic and commercial
# domains including finance, economics, Statistics, analytics, etc.
# 
# importing pandas package
import pandas as pd
 
# making data frame from csv file 
data = pd.read_csv("employees.csv")
 
# removing null values
data.dropna(inplace = True)
 
# extracting least 5
least5 = data.nsmallest(5, "Salary")
 
# display
least5
