![Build Status][https://api.travis-ci.org/AhuPersonal/524_lab1_Exercise1.svg?branch=master]
===========
ahupythonpackage
===========

This package includes function calculating standard deviation.



#### Installation

Start the command line  

`pip install git+git://github.com/AhuPersonal/524_lab1_Exercise1.git`

OR

`pip install git+https://github.com/AhuPersonal/524_lab1_Exercise1.git`

#### Usage

Calculating standard deviation via standard_deviation():  
```
from ahupythonpackage import standard_deviation
standard_deviation([10,20,30,40])

```


# Update

Addition of standard error function by Amol Mane

**Definition:**

The standard error of a sample statistic (such as sample mean) is the estimated standard deviation of the error in the process by which it was generated. In other words, it is the standard deviation of the sampling distribution of the sample statistic.

**A usage example:**

    standard_error(c(1,2,3,4))
