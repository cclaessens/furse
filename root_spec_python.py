# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:41:36 2016

@author: claessen
"""

import numpy as np
import ROOT as r
import matplotlib.pyplot as plt

f = r.TFile("~/Dokumente/katydid_files/spectrogram/powerspectrogram.root")
print f.ls()


h = f.Get("PowerSpectrogram_0")
print h.ls()
imax = h.GetNbinsX()
jmax = h.GetNbinsY()

a = np.zeros([int(imax), int(jmax)])

for i in range(int(imax)):
    for j in range(int(jmax)):
        a[i,j] = h.GetBinContent(i,j)
        
np.savetxt("spectrogram_data/out_1.txt", a)

X = h.GetXaxis()
Y = h.GetYaxis()




xax = np.linspace(X.GetXmin(), X.GetXmax(), int(imax))
yax = np.linspace(Y.GetXmin(), Y.GetXmax(), int(jmax))


np.savetxt("spectrogram_data/xaxis_1.txt", xax)
np.savetxt("spectrogram_data/yaxis_1.txt", yax)
#tmeta = open("outmeta.txt", "w")
#tmeta.write("\n" + h.GetTitle()+"\n"+X.GetTitle()+"\n"+Y.GetTitle())
#tmeta.close()
