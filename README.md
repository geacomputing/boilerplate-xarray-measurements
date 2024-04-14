# boilerplate-xarray-measurements
Example of how to use xarray to ingest and re-organise measurement data

## Description - 
This unit example demonstrates the process of importing data from a PostgreSQL database, then ingesting it into xarray for easy and extensive data manipulation. Finally, xarray can be utilized to store the data in netCDF4 format. All tools and modules used here are of course open-source, it means they require no license. You are free to download, use and -if you feel like - develop it further by expanding potentialities. 

### PosteSQL
PostgreSQL is an advanced open-source relational database management system (RDBMS) known for its robustness, reliability, and feature set. It supports SQL (Structured Query Language) for querying and managing data. PostgreSQL offers features such as transactions, sub-selects, triggers, views, foreign keys, and more. It is commonly used for applications that require complex queries, data integrity, and scalability. 

### xarray
xarray is a powerful Python library designed for working with labeled multi-dimensional arrays, providing an intuitive and efficient way to analyze and manipulate such data structures.

### The data
The data utilized in this example is real-world data with slight modifications made to comply with current data policies. Specifically, the dataset includes information from one weather station (groundstation) in Cyprus, with fictional coordinates assigned to it. Additionally, a small random white noise was introduced to the data, rendering it scientifically unusable while still maintaining technical relevance for showcasing the functionality of xarray.

The data is stored in a CSV file, with values not ordered chronologically but structured to reflect database relationships. Each line in the CSV file links a value to a timestamp, a single station, and a sensorId denoting the measured variable. This CSV file represents a typical database query output and will undergo modifications before being used in xarray.

This example aims to demonstrate the straightforward storage of multidimensional data in xarray, complete with metadata. The resulting dataset will not only contain the raw data but also its accompanying metadata descriptions. Also, the final product will be saved to disk as a netCDF4 file. 


## How to run this code? 
You have two options for accessing the code: downloading it locally using "git clone" or running it on the cloud using Binder (more details below). When using Binder, you simply need to paste the GitHub repository address into the Binder user interface (https://mybinder.org/). Binder will then set up everything for you, including the required environment to run this example, handling imports, package installations, and running the code on a cloud-based Jupyter notebook.

While the second option is the easiest, we highly recommend giving the first option a try. It offers much more control over the process and the final outcome, reducing dependence on external dependencies to execute your code.