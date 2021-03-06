conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

./bin/pyspark --master local[4] --py-files code.py


data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)


rdd = sc.parallelize(range(1, 4)).map(lambda x: (x, "a" * x))
rdd.saveAsSequenceFile("path/to/file")
sorted(sc.sequenceFile("path/to/file").collect())
[(1, u'a'), (2, u'aa'), (3, u'aaa')]


RDD Operations

lines = sc.textFile("data.txt")


lineLengths = lines.map(lambda s: len(s))


totalLength = lineLengths.reduce(lambda a, b: a + b)

totalLength.collect()





lineLengths.persist()


>>> accum = sc.accumulator(0)
>>> accum
Accumulator<id=0, value=0>

>>> sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))
...
10/09/29 18:41:08 INFO SparkContext: Tasks finished in 0.317106 s

>>> accum.value
10


from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
