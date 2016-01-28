{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Create test data:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\" grid\"\n",
    "size = 101\n",
    "x = np.linspace(0, 100, size)\n",
    "y = np.linspace(0, 100, size)\n",
    "X, Y = np.meshgrid(x, y)\n",
    "\n",
    "\" backround\"\n",
    "z = np.random.rand(size,size)\n",
    "data= z.copy()\n",
    "\n",
    "\n",
    "\" create lines \"\n",
    "\n",
    "\" fat line 1\"\n",
    "i_index = np.linspace(10, 20, 41)\n",
    "j_index = np.linspace(10, 30, 41)\n",
    "i_index2 = np.linspace(10, 20, 41)\n",
    "j_index2 = np.linspace(11, 31, 41)\n",
    "\n",
    "\" line 2\"\n",
    "h_index = np.linspace(60, 80, 41)\n",
    "k_index = np.linspace(60, 80, 41)\n",
    "\n",
    "\" put lines in spectrogram\"\n",
    "for i in range(np.shape(i_index)[0]):\n",
    "    data[int(i_index[i]), int(j_index[i])] = 1.3\n",
    "    data[int(i_index2[i]), int(j_index2[i])] = 1.1\n",
    "    data[int(h_index[i]), int(k_index[i])] = 1.3\n",
    "    \n",
    "np.save(\"spectrogram_data/test_data\", data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "spectrogram plot funtion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import cm\n",
    "\n",
    "def plot_function(X, Y, Z, figno):\n",
    "    \n",
    "    plt.figure(figno)\n",
    "\n",
    "    delta = (np.max(Z)-np.min(Z))/20\n",
    "    plt.contourf(X, Y, Z, cmap = cm.jet, levels = np.arange(np.min(Z), np.max(Z), delta))\n",
    "    plt.colorbar()\n",
    "    plt.title(\"spectrogam\")\n",
    "    plt.xlabel(\"time\")\n",
    "    plt.ylabel(\"frequency\")\n",
    "    plt.show()\n",
    "    return"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "plot test data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "plot_function(X, Y, data, 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "filter by substracting some backround"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "rate = data.copy()/np.average(z)\n",
    "plot_function(X, Y, rate, 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "give score to datapoints"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "aplus = 10.0\n",
    "aminus = 0.3\n",
    "bplus = 1.5\n",
    "bminus = 1.0\n",
    "t = 1.5\n",
    "\n",
    "s = np.zeros(np.shape(z))\n",
    "s[np.where(rate>=t)] = aplus*(rate[np.where(rate>=t)]-t)**bplus\n",
    "s[np.where(rate<t)] = aminus*(t-rate[np.where(rate<t)])**bminus\n",
    "\n",
    "plot_function(X, Y, s, 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Furses algorithm"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "line object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class line:\n",
    "    def __init__(self, startpos, startfreq, score):\n",
    "        self.scorelist = []\n",
    "        self.scorelist.append(score)\n",
    "        \n",
    "        self.startpos = startpos\n",
    "\n",
    "        self.startfreq = startfreq\n",
    "        self.curpos = self.startpos\n",
    "        self.curfreq = self.startfreq\n",
    "        \n",
    "        self.slope = 0\n",
    "        self.duration = 0\n",
    "\n",
    "        \n",
    "    def investigate_point(self, pos, freqin, curslice):\n",
    "        \n",
    "        success = 0\n",
    "        \n",
    "            \n",
    "        if np.abs(pos-self.curpos)<freq_delta and np.abs(freqin -self.curfreq) < freq_delta:\n",
    "    \n",
    "            freqin, score = converge_function(freqin, curslice)\n",
    "                \n",
    "            self.curpos = pos\n",
    "            self.curfreq = freqin\n",
    "            self.duration = self.curpos - self.startpos\n",
    "            self.slope = np.abs(self.curfreq-self.startfreq)/(self.curpos-self.startpos)\n",
    "            self.scorelist.append(score)\n",
    "            success = 1\n",
    "            \n",
    "        return success, freqin "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "function to inspect nearby datapoint and recalculated weighed frequency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def converge_function(f, s1):\n",
    "    delta = freq_delta + 1\n",
    "    loop_counter = 0\n",
    "    while np.abs(delta) > freq_delta:\n",
    "        loop_counter += 1\n",
    "        if loop_counter > 5:\n",
    "            print \"loop error\"\n",
    "            break\n",
    "        \n",
    "        else:\n",
    "\n",
    "            weighing = s1[round(f)-freq_delta:round(f)+freq_delta+1] / np.sum(s1[round(f)-freq_delta:round(f)+freq_delta+1])\n",
    "            score = np.sum(s[f-freq_delta:f+freq_delta+1])\n",
    "            new_freq = (np.sum(weighing*np.linspace(f-freq_delta,f+freq_delta, 2*freq_delta+1)))\n",
    "            delta = np.abs(new_freq-f)\n",
    "            f = new_freq\n",
    "                    \n",
    "    f1 = f\n",
    "    global slice1\n",
    "    slice1[round(f)-freq_delta:round(f)+freq_delta+1] = -sigma\n",
    "    \n",
    "    return f1, score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "find lines in instreaming data slices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60 60.0 1.00179016376 80\n",
      "10 10.0 0.477950432006 31\n"
     ]
    }
   ],
   "source": [
    "tresh = np.max(s)*0.3\n",
    "freq_delta = 3\n",
    "sigma = -5.0\n",
    "lan = 10.0\n",
    "\n",
    "candidates = {}\n",
    "\n",
    "counter = 0\n",
    "\n",
    "for ii in range(size):\n",
    "    freq = 0\n",
    "    slice1 = s[:, ii]\n",
    "    freq_list = np.where(slice1>=tresh)\n",
    "    \n",
    "    if len(slice1[freq_list]) > 0:\n",
    "                    \n",
    "        for ll in range(len(slice1[freq_list])):    \n",
    "            old_freq = freq\n",
    "            freq = freq_list[0][ll]\n",
    "            \n",
    "                        \n",
    "            if np.abs(old_freq-freq) > freq_delta and freq < size-freq_delta and freq > freq_delta:\n",
    "                success = 0 \n",
    "                \n",
    "                for jj in range(len(candidates)):\n",
    "                    success, freq1 = candidates[str(jj)].investigate_point(ii, freq, slice1) \n",
    "\n",
    "                    if success == 1:\n",
    "                        freq = freq1\n",
    "                        break\n",
    "                    \n",
    "                if success == 0:\n",
    "                    freq, score = converge_function(freq, slice1)\n",
    "                    candidates[str(counter)] = line(ii,round(freq), score)\n",
    "                    \n",
    "                    counter += 1\n",
    "    \n",
    "                    \n",
    "                \n",
    "                               \n",
    "candidates = {k:v for (k,v) in candidates.iteritems() if (v.slope!=0 and v.duration>=lan)}\n",
    "          \n",
    "\n",
    "for mm in candidates.keys():\n",
    "\n",
    "    print candidates[mm].startpos, candidates[mm].startfreq, candidates[mm].slope, candidates[mm].curpos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
