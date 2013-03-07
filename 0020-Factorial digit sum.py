#! /usr/bin/env python

import operator
print reduce(operator.add,map(int, str(reduce(operator.mul,range(1,101)))))