__spark-workshop__

#Overview

This is just a simple Apache Spark project to get you started with a little playground dataset and some code scaffolding.

#Getting Started

To us this you're going to need to grab a few things:

**Prerequisites:**

* [Apache Spark](http://d3kbcqa49mib13.cloudfront.net/spark-1.1.0-bin-hadoop1.tgz)
* [Sample Data](http://bit.ly/1uz2dBl)

#Usage

	$ spark/bin/spark-submit weights.py ./medical_screening_samples.csv

#Challenges

1. See if you can write a Spark application to tell you how many zombies there are per State.
2. Perform a clustering analysis on the height and weight of the sample population (hint: mllib)

#Super Challenges
1. Analyze the data to figure out if there's any predictive characteristic that can determine if someone may have acute zombilepsy without knowledge of them being symptomatic or not.
2. Analyze the data to see if there are any samples that satisfy the above predictive analysis, but yet still seem to be asymptomatic.


#License
(The MIT License)

Copyright (c) 2014 Nathan Aschbacher

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.