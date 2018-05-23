#!/usr/bin/python3
# -*- coding: utf8 -*-

import matplotlib
matplotlib.use("Agg")

import libxml2
from libxml2 import xmlAttr
from matplotlib import pylab

import sys

fname = sys.argv[1]
output = sys.argv[2]

doc = libxml2.parseFile(fname)

ctxt = doc.xpathNewContext()

x = map(float,map(xmlAttr.getContent,ctxt.xpathEval("//StateInfo/State/@delta")))
y = map(float,map(xmlAttr.getContent,ctxt.xpathEval("//StateInfo/State/Prop[@name='CPUTemp']/@value")))

x = list(x)
y = list(y)

pylab.plot(x,y)

pylab.title("Teplota v čase")
pylab.ylabel("Teplota CPU")
pylab.xlabel("Čas")

pylab.axis([x[0],x[-1],min(y),max(y)])

pylab.savefig(output,figsize=(50,50),dpi=300)