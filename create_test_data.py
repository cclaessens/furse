import numpy as np


" grid"
size = 101
x = np.linspace(0, 100, size)
y = np.linspace(0, 100, size)
X, Y = np.meshgrid(x, y)

" backround"
z = np.random.rand(size,size)
data= z.copy()


" create lines "

" fat line 1"
i_index = np.linspace(10, 20, 41)
j_index = np.linspace(10, 30, 41)
i_index2 = np.linspace(10, 20, 41)
j_index2 = np.linspace(11, 31, 41)

" line 2"
h_index = np.linspace(60, 80, 41)
k_index = np.linspace(60, 80, 41)

" put lines in spectrogram"
for i in range(np.shape(i_index)[0]):
    data[int(i_index[i]), int(j_index[i])] = 1.3
    data[int(i_index2[i]), int(j_index2[i])] = 1.1
    data[int(h_index[i]), int(k_index[i])] = 1.3
    
#np.save("spectrogram_data/test_data", data)