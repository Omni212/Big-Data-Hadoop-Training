## Sample and Practice code from the training session


# Environment setup 

If you are using it for first time, then please install 

1. Gitbash https://git-scm.com/downloads works for Windows, Linux, Mac
2. Clone the Repo: 

``` git clone https://github.com/Omni212/Big-Data-Hadoop-Training.git
``` 

# Instructions for Module 4

Once cloned the repo, make sure the code works by doing a local map reduce

```
echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py
bar	1
foo	3
labs	1
quux	2
```

Download the sample file 

```
wget http://www.gutenberg.org/files/5000/5000-8.txt
```

Upload it to HDFS

```
hdfs dfs -mkdir /user/ssh
hdfs dfs -copyFrom 5000-8.txt /user/ssh
```

Run the Map reduce job [ Azure HDInsight ]

```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming-2.7.3.2.6.2.3-1.jar \
-file /home/sshuser/mapper.py    -mapper /home/sshuser/mapper.py \
-file /home/sshuser/reducer.py   -reducer /home/sshuser/reducer.py \
-input /user/ssh/5000-8.txt -output /user/ssh/output

```

Run the MapReduce job [ Cloudera Sandbox ]

```
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -file /home/cloudera/mapper.py    -mapper /home/cloudera/mapper.py -file /home/cloudera/reducer.py   -reducer /home/cloudera/reducer.py -input /user/cloudera/*.py -output /user/cloudera/output
```

