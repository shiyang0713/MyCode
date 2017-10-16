{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 一般網頁"
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
    "import requests\n",
    "import re\n",
    "from bs4 import BeautifulSoup\n",
    "res = requests.get(\"http://www.newsstu.tp.edu.tw/modules/news/index.php?storytopic=4\")\n",
    "soup = BeautifulSoup(res.text,\"lxml\")\n",
    "for child in soup.body.find_all(text=re.compile('..國小')):\n",
    "    print(child[0:4])"
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
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re \n",
    "cookie = {'over18':'1'}\n",
    "res = requests.get(\"https://www.ptt.cc/bbs/Gossiping/M.1119222660.A.94E.html\",cookies = cookie)\n",
    "soup = BeautifulSoup(res.text,\"lxml\")\n",
    "for div in soup.select('div'):\n",
    "    push=div.select('.push .f3.push-content')\n",
    "    if push != []:\n",
    "        print(push)"
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
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re \n",
    "cookie = {'over18':'1'}\n",
    "res = requests.get(\"https://www.ptt.cc/bbs/Gossiping/M.1119222660.A.94E.html\",cookies = cookie)\n",
    "soup = BeautifulSoup(res.text,\"lxml\")\n",
    "count=0\n",
    "for push in soup.select('span[class=\"hl push-tag\"] '):\n",
    "    if push != \"\":\n",
    "        count=count+1\n",
    "        \n",
    "print(count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 動態網頁"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from bs4 import BeautifulSoup \n",
    "def get_url_dynamic2(url):\n",
    "    driver=webdriver.Chrome()\n",
    "    driver.get(url) #打開瀏覽器視窗\n",
    "    html_text=driver.page_source\n",
    "    driver.quit()\n",
    "    return html_text\n",
    "a=get_url_dynamic2('http://taipei.youbike.com.tw/cht/f12.php')"
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
    "soup = BeautifulSoup(a,\"html5lib\")\n",
    "import pandas as pd\n",
    "b=soup.select('table a')\n",
    "for i in range(len(b)):\n",
    "    print(b[i].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true,
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(a,\"html5lib\")\n",
    "import pandas as pd\n",
    "import re\n",
    "c=soup.select('table a')\n",
    "temp=[]\n",
    "for i in range(len(c)):\n",
    "    string = list(c[i].attrs.values())[0]\n",
    "    reg = re.search(r'\\d.*',string)\n",
    "    latlng=reg.group().split(',')[0:2]\n",
    "    temp.append(latlng[0:2])\n",
    "pd.DataFrame(temp).to_csv('ubike2.csv',index = None)            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(a,\"html5lib\")\n",
    "import pandas as pd\n",
    "import re\n",
    "c=soup.select('table a')\n",
    "lat=[]\n",
    "lng=[]\n",
    "for i in range(len(c)):\n",
    "    string = list(c[i].attrs.values())[0]\n",
    "    reg = re.search(r'\\d.*',string)\n",
    "    latlng=reg.group().split(',')[0:2]\n",
    "    lat.append(latlng[0])\n",
    "    lng.append(latlng[1])\n",
    "pd.DataFrame({'lat':lat,'lng':lng}).to_csv('ubike1.csv',index = None)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
