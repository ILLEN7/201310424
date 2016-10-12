{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4가지 방식으로 KOSPI 200 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Content-Type: text/html; charset=utf-8\r\n",
      "P3P: CP=\"This is not a P3P policy! See https://support.google.com/accounts/answer/151657?hl=en for more info.\"\r\n",
      "Date: Sun, 02 Oct 2016 17:58:49 GMT\r\n",
      "Expires: Sun, 02 Oct 2016 17:58:49 GMT\r\n",
      "Cache-Control: private, max-age=0\r\n",
      "X-Content-Type-Options: nosniff\r\n",
      "X-Frame-Options: SAMEORIGIN\r\n",
      "X-XSS-Protection: 1; mode=block\r\n",
      "Server: GSE\r\n",
      "Set-Cookie: NID=87=QmrpgxURgT6WqWa0dKdaCB2gZBvS2myQodAXKwVcMP-AxrogSD01R7O_obWcfxssphIJiYpTNJbT0X0Bu7VnjTtmXEqHU_UIhEUjGHL1EyI-4ewkJRNNTjUBhX9B1-nC;Domain=.google.com;Path=/;Expires=Mon, 03-Apr-2017 17:58:49 GMT;HttpOnly\r\n",
      "Alt-Svc: quic=\":443\"; ma=2592000; v=\"36,35,34,33,32\"\r\n",
      "Accept-Ranges: none\r\n",
      "Vary: Accept-Encoding\r\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import urllib\n",
    "response=urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA')\n",
    "_html=response.read()\n",
    "print response.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## regular expression로 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 546,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "_date=re.compile('<td class=\"lm\">(.*?)\\s(\\d+)\\,\\s(\\d+)') # Sep 30, 2016"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 547,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "_sre.SRE_Pattern"
      ]
     },
     "execution_count": 547,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type (_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 548,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "res1=_date.findall(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 549,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "kospi 200 table(date) 30\n"
     ]
    }
   ],
   "source": [
    "print \"kospi 200 table(date)\", len(res1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 550,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 550,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(res1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 551,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "res1_str=str(res1)\n",
    "f=open(\"kospi_date.txt\",'w')\n",
    "f.write(res1_str)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 552,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Sep', '30', '2016')\n",
      "('Sep', '29', '2016')\n",
      "('Sep', '28', '2016')\n",
      "('Sep', '27', '2016')\n",
      "('Sep', '26', '2016')\n",
      "('Sep', '23', '2016')\n",
      "('Sep', '22', '2016')\n",
      "('Sep', '21', '2016')\n",
      "('Sep', '20', '2016')\n",
      "('Sep', '19', '2016')\n",
      "('Sep', '13', '2016')\n",
      "('Sep', '12', '2016')\n",
      "('Sep', '9', '2016')\n",
      "('Sep', '8', '2016')\n",
      "('Sep', '7', '2016')\n",
      "('Sep', '6', '2016')\n",
      "('Sep', '5', '2016')\n",
      "('Sep', '2', '2016')\n",
      "('Sep', '1', '2016')\n",
      "('Aug', '31', '2016')\n",
      "('Aug', '30', '2016')\n",
      "('Aug', '29', '2016')\n",
      "('Aug', '26', '2016')\n",
      "('Aug', '25', '2016')\n",
      "('Aug', '24', '2016')\n",
      "('Aug', '23', '2016')\n",
      "('Aug', '22', '2016')\n",
      "('Aug', '19', '2016')\n",
      "('Aug', '18', '2016')\n",
      "('Aug', '17', '2016')\n"
     ]
    }
   ],
   "source": [
    "for item in res1:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 362,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_ohlc=re.compile('<td class=\"rgt\">(\\d+\\.\\d+)') # Open, High, Low, Close data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 363,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res2=_ohlc.findall(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 481,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "kospi 200 table(open,high,low,close) 120\n"
     ]
    }
   ],
   "source": [
    "print \"kospi 200 table(open,high,low,close)\", len(res2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 482,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res2_str=str(res2)\n",
    "f=open('kospi_ohlc.txt','w')\n",
    "f.write(res2_str)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 419,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "258.30\n",
      "258.91\n",
      "257.29\n",
      "257.49\n",
      "259.60\n",
      "260.95\n",
      "259.60\n",
      "260.35\n",
      "259.32\n",
      "259.46\n",
      "257.96\n",
      "258.21\n",
      "256.16\n",
      "259.87\n",
      "255.16\n",
      "259.57\n",
      "258.07\n",
      "259.32\n",
      "256.90\n",
      "257.48\n",
      "258.44\n",
      "259.14\n",
      "257.71\n",
      "258.37\n",
      "258.46\n",
      "259.99\n",
      "258.13\n",
      "258.34\n",
      "254.65\n",
      "256.55\n",
      "254.56\n",
      "256.52\n",
      "253.86\n",
      "255.23\n",
      "253.33\n",
      "255.09\n",
      "251.51\n",
      "254.54\n",
      "251.38\n",
      "253.93\n",
      "253.39\n",
      "253.55\n",
      "251.66\n",
      "251.77\n",
      "252.37\n",
      "253.43\n",
      "250.53\n",
      "250.53\n",
      "258.68\n",
      "258.94\n",
      "256.21\n",
      "257.31\n",
      "260.72\n",
      "261.48\n",
      "259.41\n",
      "260.86\n",
      "261.15\n",
      "262.10\n",
      "260.31\n",
      "260.31\n",
      "259.39\n",
      "261.16\n",
      "259.26\n",
      "260.93\n",
      "257.85\n",
      "259.74\n",
      "257.63\n",
      "259.64\n",
      "256.16\n",
      "256.73\n",
      "255.57\n",
      "256.50\n",
      "254.95\n",
      "256.13\n",
      "253.86\n",
      "256.03\n",
      "257.21\n",
      "257.49\n",
      "255.90\n",
      "256.87\n",
      "257.27\n",
      "258.93\n",
      "257.00\n",
      "257.49\n",
      "254.93\n",
      "256.66\n",
      "254.45\n",
      "256.49\n",
      "256.17\n",
      "256.76\n",
      "255.02\n",
      "256.23\n",
      "256.78\n",
      "257.76\n",
      "256.00\n",
      "257.26\n",
      "258.40\n",
      "258.65\n",
      "256.54\n",
      "257.30\n",
      "257.57\n",
      "258.63\n",
      "257.09\n",
      "258.42\n",
      "258.54\n",
      "258.63\n",
      "256.92\n",
      "257.27\n",
      "258.42\n",
      "258.84\n",
      "257.54\n",
      "258.69\n",
      "256.62\n",
      "258.23\n",
      "255.80\n",
      "258.11\n",
      "255.82\n",
      "256.32\n",
      "254.60\n",
      "256.04\n"
     ]
    }
   ],
   "source": [
    "for item2 in res2:\n",
    "    print item2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 367,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "_vol=re.compile('<td class=\"rgt rm\">(\\d+\\,\\d+\\,\\d+)')\n",
    "res3=_vol.findall(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 483,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "kospi 200 table(volume) 30\n"
     ]
    }
   ],
   "source": [
    "print \"kospi 200 table(volume)\", len(res3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 484,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res3_str=str(res3)\n",
    "f=open('kospi_volume.txt','w')\n",
    "f.write(res3_str)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 417,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74,918,000\n",
      "65,365,000\n",
      "59,186,000\n",
      "58,684,000\n",
      "43,876,000\n",
      "58,392,000\n",
      "59,904,000\n",
      "51,982,000\n",
      "54,626,000\n",
      "59,750,000\n",
      "74,548,000\n",
      "66,332,000\n",
      "70,053,000\n",
      "79,382,000\n",
      "68,749,000\n",
      "49,969,000\n",
      "54,167,000\n",
      "49,266,000\n",
      "56,098,000\n",
      "66,352,000\n",
      "56,516,000\n",
      "62,755,000\n",
      "68,304,000\n",
      "58,803,000\n",
      "54,461,000\n",
      "65,706,000\n",
      "62,921,000\n",
      "72,796,000\n",
      "64,012,000\n",
      "63,810,000\n"
     ]
    }
   ],
   "source": [
    "for item3 in res3:\n",
    "    print item3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 499,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Sep', '30', '2016'), ('Sep', '29', '2016'), ('Sep', '28', '2016'), ('Sep', '27', '2016'), ('Sep', '26', '2016'), ('Sep', '23', '2016'), ('Sep', '22', '2016'), ('Sep', '21', '2016'), ('Sep', '20', '2016'), ('Sep', '19', '2016'), ('Sep', '13', '2016'), ('Sep', '12', '2016'), ('Sep', '9', '2016'), ('Sep', '8', '2016'), ('Sep', '7', '2016'), ('Sep', '6', '2016'), ('Sep', '5', '2016'), ('Sep', '2', '2016'), ('Sep', '1', '2016'), ('Aug', '31', '2016'), ('Aug', '30', '2016'), ('Aug', '29', '2016'), ('Aug', '26', '2016'), ('Aug', '25', '2016'), ('Aug', '24', '2016'), ('Aug', '23', '2016'), ('Aug', '22', '2016'), ('Aug', '19', '2016'), ('Aug', '18', '2016'), ('Aug', '17', '2016')]\n"
     ]
    }
   ],
   "source": [
    "date_f=open('kospi_date.txt','r')\n",
    "line1=date_f.readline()\n",
    "print line1\n",
    "date_f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 563,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['258.30', '258.91', '257.29', '257.49', '259.60', '260.95', '259.60', '260.35', '259.32', '259.46', '257.96', '258.21', '256.16', '259.87', '255.16', '259.57', '258.07', '259.32', '256.90', '257.48', '258.44', '259.14', '257.71', '258.37', '258.46', '259.99', '258.13', '258.34', '254.65', '256.55', '254.56', '256.52', '253.86', '255.23', '253.33', '255.09', '251.51', '254.54', '251.38', '253.93', '253.39', '253.55', '251.66', '251.77', '252.37', '253.43', '250.53', '250.53', '258.68', '258.94', '256.21', '257.31', '260.72', '261.48', '259.41', '260.86', '261.15', '262.10', '260.31', '260.31', '259.39', '261.16', '259.26', '260.93', '257.85', '259.74', '257.63', '259.64', '256.16', '256.73', '255.57', '256.50', '254.95', '256.13', '253.86', '256.03', '257.21', '257.49', '255.90', '256.87', '257.27', '258.93', '257.00', '257.49', '254.93', '256.66', '254.45', '256.49', '256.17', '256.76', '255.02', '256.23', '256.78', '257.76', '256.00', '257.26', '258.40', '258.65', '256.54', '257.30', '257.57', '258.63', '257.09', '258.42', '258.54', '258.63', '256.92', '257.27', '258.42', '258.84', '257.54', '258.69', '256.62', '258.23', '255.80', '258.11', '255.82', '256.32', '254.60', '256.04']\n"
     ]
    }
   ],
   "source": [
    "ohlc_f=open('kospi_ohlc.txt','r')\n",
    "line2=ohlc_f.readline()\n",
    "print line2\n",
    "ohlc_f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 593,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['74,918,000', '65,365,000', '59,186,000', '58,684,000', '43,876,000', '58,392,000', '59,904,000', '51,982,000', '54,626,000', '59,750,000', '74,548,000', '66,332,000', '70,053,000', '79,382,000', '68,749,000', '49,969,000', '54,167,000', '49,266,000', '56,098,000', '66,352,000', '56,516,000', '62,755,000', '68,304,000', '58,803,000', '54,461,000', '65,706,000', '62,921,000', '72,796,000', '64,012,000', '63,810,000']\n"
     ]
    }
   ],
   "source": [
    "vol_f=open('kospi_volume.txt','r')\n",
    "line3=vol_f.readline()\n",
    "print line3\n",
    "vol_f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 668,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "683"
      ]
     },
     "execution_count": 668,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(line1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 660,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Sep', '30', '2016')\n"
     ]
    }
   ],
   "source": [
    "for i in aa:\n",
    "    print i[1:22] #모르겠따..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 654,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n"
     ]
    }
   ],
   "source": [
    "print i[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from pandas import Series, DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 584,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "date=Series(line1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 587,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "volume=Series(line3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 591,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "kb=Series([line3], index=[line1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 592,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Sep', '30', '2016'), ('Sep', '29', '2016'), ('Sep', '28', '2016'), ('Sep', '27', '2016'), ('Sep', '26', '2016'), ('Sep', '23', '2016'), ('Sep', '22', '2016'), ('Sep', '21', '2016'), ('Sep', '20', '2016'), ('Sep', '19', '2016'), ('Sep', '13', '2016'), ('Sep', '12', '2016'), ('Sep', '9', '2016'), ('Sep', '8', '2016'), ('Sep', '7', '2016'), ('Sep', '6', '2016'), ('Sep', '5', '2016'), ('Sep', '2', '2016'), ('Sep', '1', '2016'), ('Aug', '31', '2016'), ('Aug', '30', '2016'), ('Aug', '29', '2016'), ('Aug', '26', '2016'), ('Aug', '25', '2016'), ('Aug', '24', '2016'), ('Aug', '23', '2016'), ('Aug', '22', '2016'), ('Aug', '19', '2016'), ('Aug', '18', '2016'), ('Aug', '17', '2016')]    ['74,918,000', '65,365,000', '59,186,000', '58...\n",
       "dtype: object"
      ]
     },
     "execution_count": 592,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kb"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
