
##WordCount Spark Example:

#Upload a large file into HDFS

```
wget http://www.gutenberg.org/files/5000/5000-8.txt
hdfs dfs -mkdir /user/sshuser
hdfs dfs -copyFromLocal 5000-8.txt /user/sshuser
```

#Start pyspark interactive session

```
pyspark
```
Initialize the Spark Context

text_file = sc.textFile("/user/sshuser/5000-8.txt")

Create flatmap variable

counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

Save it

counts.saveAsTextFile("/user/sshuser/output")

Load Databrick

df1 = sqlContext.sql("SELECT * FROM default.hivesampletable")
df1.show()



pyspark --packages com.databricks:spark-csv_2.10:1.4.0

df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('/users/sshuser/cars.csv')

df.show()
df.printSchema()

 df.select("mpg").show()

 df.select(df['mpg'],df['hp']+ 1).show()

 df.filter(df['mpg'] > 9).show()

 df.groupBy("_c0").count().show()

HomeWork:

1. Take a large text file 10 GB, and run the word count program and compare the performance between MapReduce and Spark
2. Take a CSV file create hive table out of it, compare performance between SparkSQL and Hive queries

