# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:41:36 2016

@author: claessen
"""

import numpy as np
import ROOT as r
import matplotlib.pyplot as plt

f = r.TFile("powerspectrogramzoom.root")
print f.ls()


h = f.Get("PowerSpectrogram_0")
print h.ls()
imax = h.GetNbinsX()
jmax = h.GetNbinsY()

a = np.zeros([int(imax), int(jmax)])

for i in range(int(imax)):
    for j in range(int(jmax)):
        a[i,j] = h.GetBinContent(i,j)
        
np.savetxt("out.txt", a)

X = h.GetXaxis()
Y = h.GetYaxis()




xax = np.linspace(X.GetXmin(), X.GetXmax(), int(imax))
yax = np.linspace(Y.GetXmin(), Y.GetXmax(), int(jmax))


np.savetxt("xaxis.txt", xax)
np.savetxt("yaxis.txt", yax)
#tmeta = open("outmeta.txt", "w")
#tmeta.write("\n" + h.GetTitle()+"\n"+X.GetTitle()+"\n"+Y.GetTitle())
#tmeta.close()
