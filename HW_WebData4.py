{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 웹데이터-4: 한국 포털사이트에서 노래 제목을 검색"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## regex 활용해서 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib\n",
    "keyword='벚꽃'\n",
    "f=urllib.urlopen(\"http://music.naver.com/search/search.nhn?query=%EB%B2%9A%EA%BD%83&target=track\")\n",
    "mydata=f.read();\n",
    "pos=mydata.find(\"트랙 리스트\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 벚꽃\n",
      "222676\n"
     ]
    }
   ],
   "source": [
    "if (pos>0): # 이 부분 무슨 말인지 모르겠다...!!!\n",
    "    pos = mydata.find(\"_title title NPI=\", pos);\n",
    "    pos = mydata.find(\"title=\", pos+20)\n",
    "    pos2 = mydata.find(\"\\\"\", pos+8)\n",
    "    print \"---\", mydata[pos+7:pos2]\n",
    "    \n",
    "#pos 가 글자수. 그러니까, 문자는 0,1,2  문자가 없으면 - 값이 나온다. pos>0은 결국, 문자가 있으면 이라는 뜻. \n",
    "    \n",
    "print len(mydata)"
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
    "import re\n",
    "p=re.compile('title=\".*벚꽃.*\"')\n",
    "res=p.findall(mydata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "title=\"검색어 입력\" value=\"벚꽃\" maxlength=\"50\" accesskey=\"s\"\n",
      "title=\"그녀가 보내준 벚꽃편지\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:1,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:2,i:170969\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃놀이\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:3,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"サクラ色 (Sakura Iro) (벚꽃 색) - Sony 사이버 샷 CM송\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"Sakura (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (MR 트랙)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Feat. 제인제이, 진정민)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (꽃이 지다...)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (꽃이 지다...)\" class=\"_album NPI=a:album,r:9,i:585308\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"Sakura (벚꽃) (DenpO115 동일본 에이어 CM 송)\" ><span class=\"ellipsis\"\n",
      "title=\"1집 Sakurasakumachi Monogatari (벚꽃 피는 거리이야기)\" class=\"_album NPI=a:album,r:12,i:321260\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:13,i:170969\"><span class=\"ellipsis\"\n",
      "title=\"Cherry Blossom (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:17,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Acoustic Ver.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:23,i:625868\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Feat. 강윤희)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃축제\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃 여행 2\" class=\"_album NPI=a:album,r:27,i:497654\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:29,i:500208\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Cherry Blossom)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Inst.)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" class=\"_album NPI=a:album,r:36,i:374857\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (외발로 살다 OST)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"サクラ (벚꽃)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 하나 (Cherry Blossom) (Feat. MiMi)\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Cherry Blossom)\" class=\"_album NPI=a:album,r:45,i:623930\"><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃\" ><span class=\"ellipsis\"\n",
      "title=\"벚꽃 (Acoustic Ver.)\" ><span class=\"ellipsis\"\n",
      "title=\"다시 부르기 곰돌이 첫번째 이야기 - 벚꽃 (Acoustic Ver.)\" class=\"_album NPI=a:album,r:50,i:317230\"><span class=\"ellipsis\"\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## CSSSelector 활용해서 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#노래 제목이 있는 위치\n",
    "# body > wrap > div.fix_conts > container > .container_inner > content\\\n",
    "# > div:nth-child(3) > div._tracklist_mytrack.tracklist_table._searchTrack\\\n",
    "# > table > tbody > tr:nth-child(2) > td.name > a.title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "html=lxml.html.fromstring(mydata)\n",
    "sel=CSSSelector('#content > div:nth-child(3) \\\n",
    "> div._tracklist_mytrack.tracklist_table._searchTrack \\\n",
    "> table > tbody > tr:nth-child(2) > td.name > a.title')\n",
    "results=sel(html)"
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
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "그녀가 보내준 벚꽃편지\n"
     ]
    }
   ],
   "source": [
    "for result in results:\n",
    "    print result.text_content()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "import requests\n",
    "keyword='벚꽃'\n",
    "r = requests.get(\"http://music.naver.com/search/search.nhn?query=\"+keyword+\"&x=0&y=0\")\n",
    "\n",
    "_html=lxml.html.fromstring(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "151981"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(lxml.html.tostring(_html))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lxml.cssselect import CSSSelector\n",
    "\n",
    "sel=CSSSelector('table[summary] > tbody > ._tracklist_move > .name > a.title')\n",
    "nodes=sel(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(nodes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "그녀가 보내준 벚꽃편지\n",
      "벗꽃 사진\n",
      "벚꽃놀이\n",
      "벚꽃\n",
      "サクラ色 (Sakura Iro) (벚꽃 색) - Sony 사이버 샷 CM송\n",
      "벚꽃\n",
      "Sakura (벚꽃)\n",
      "벚꽃 (MR 트랙)\n",
      "벚꽃 (Feat. 제인제이, 진정민)\n",
      "벚꽃 (꽃이 지다...)\n",
      "벚꽃 (Inst.)\n",
      "Sakura (벚꽃) (DenpO115 동일본 에이어 CM 송)\n",
      "벚꽃 (Inst.)\n",
      "Cherry Blossom (벚꽃)\n",
      "벗꽃 버스 여행\n"
     ]
    }
   ],
   "source": [
    "for node in nodes:\n",
    "    print node.text_content()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 곡명, 아티스트, 앨범 모두 가져오기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<tr class=\"_tracklist_move {TRACK_TYPE}\" style=\"display:none;\" trackdata=\"{TRACK_DATA}\">\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"chk\"><input type=\"checkbox\" title=\"&#49440;&#53469;\" class=\"_chkbox_item input_chk {TRACK_CHECK_NCLICKS}\"> </td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"order\">{TRACK_NUM}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"name\">\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{PLAY_TOGGLE}\r\n",
      "\t\t\t\t\t\t\t\t{ADD_TOGGLE}\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t<span class=\"_ico_title ico_title\"><img height=\"18\" width=\"23\" alt=\"TITLE\" src=\"http://static.naver.net/nmusic/201008/blank.gif\"></span>\r\n",
      "\t\t\t\t\t\t\t\t<span class=\"_ico_19 ico19\"><img height=\"18\" width=\"13\" src=\"http://static.naver.net/nmusic/201008/blank.gif\"></span>\r\n",
      "\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{TRACK_SONG_NAME}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t<td class=\"_artist artist {NO_ELL}\">\r\n",
      "\r\n",
      "\r\n",
      "                                   {ARTIST}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "                            <td class=\"album\">\r\n",
      "                                {ALBUM}\r\n",
      "                            </td>\r\n",
      "                        \r\n",
      "                        \r\n",
      "                        \t<td class=\"like\">\r\n",
      "\t\t\t\t\t\t\t\t<div class=\"u_likeit_list_module\">\r\n",
      "\t\t\t\t\t\t\t\t\t<a href=\"javascript:void(0)\" title=\"&#51339;&#50500;&#50836;\" class=\"u_likeit_list_btn u_type_img NPI=a:favo,r:1,i:\" data-sid=\"MUSIC\" data-did=\"MUSIC\" data-cid=\"TRACK_\" data-likeit=\"0\"><span class=\"u_ico\"></span><em class=\"u_txt\"></em><em class=\"u_cnt\"></em></a>\r\n",
      "\t\t\t\t\t\t\t\t</div>\r\n",
      "                        \t</td>\r\n",
      "                        \r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"video\">{MUSIC_VIDEO}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"lyric\">{LYRIC}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"get\">{SCRAP_ROW}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"radio\">{RADIO}</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t<td class=\"buy\">\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t{MP3_BUY_LAYER_BTN}\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t<div style=\"display:none;\" class=\"_buy_layer buy_layer\">\r\n",
      "\t\t\t\t\t\t\t\t\t<ul>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{MP3_BUY_LIST}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{MUSIC_SPRING}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{BELL_SOUND}</li>\r\n",
      "\t\t\t\t\t\t\t\t\t<li>{CONNECTION_SOUND}</li>\r\n",
      "\r\n",
      "\t\t\t\t\t\t\t\t\t</ul>\r\n",
      "\t\t\t\t\t\t\t\t\t<span class=\"bg\"></span>\r\n",
      "\t\t\t\t\t\t\t\t</div>\r\n",
      "\t\t\t\t\t\t\t</td>\r\n",
      "\t\t\t\t\t\t\r\n",
      "\r\n",
      "\t\t\t\t\t\t\r\n",
      "\t\t\t\t\t\t\t</tr>\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\r\n",
      "\t\n"
     ]
    }
   ],
   "source": [
    "from lxml.cssselect import CSSSelector\n",
    "\n",
    "sel=CSSSelector('table[summary] > tbody > ._tracklist_move')\n",
    "nodes=sel(_html)\n",
    "print lxml.html.tostring(nodes[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_selName=CSSSelector('.name > a.title')\n",
    "_selArtist=CSSSelector('._artist.artist')\n",
    "_selAlbum=CSSSelector('.album > a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_name=_selName(nodes[1])\n",
    "_artist=_selArtist(nodes[1])\n",
    "_album=_selAlbum(nodes[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "그녀가 보내준 벚꽃편지\n",
      "벚꽃\n",
      "벚꽃 여행 2\n"
     ]
    }
   ],
   "source": [
    "print _name[0].text_content()\n",
    "print _artist[0].text_content().strip() # .strip() : 공백제거\n",
    "print _album[0].text_content()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "벚꽃 --- 그녀가 보내준 벚꽃편지 --- 벚꽃 여행 2\n",
      "벚꽃 --- 벗꽃 사진 --- 벗꽃 여행\n",
      "벚꽃 --- 벚꽃놀이 --- 벚꽃 여행 2\n",
      "블랙아웃(Black Out) --- 벚꽃 --- 벚꽃\n",
      "Angela Aki --- サクラ色 (Sakura Iro) (벚꽃 색) - Sony 사이버 샷 CM송 --- Today\n",
      "화이트 피아노 --- 벚꽃 --- 2집 화이트 피아노가 전하는 따뜻한 뉴에이지 정규 2집\n",
      "PBC 소년소녀합창단 --- Sakura (벚꽃) --- Voices Of Peace\n",
      "미누(곰돌이) --- 벚꽃 (MR 트랙) --- 곰돌이 MR집\n",
      "홍창우 --- 벚꽃 (Feat. 제인제이, 진정민) --- 夢\n",
      "아몬드와 땅콩들(허은진, 김준희, 김세라, 임미란) --- 벚꽃 (꽃이 지다...) --- 벚꽃 (꽃이 지다...)\n",
      "이소정 --- 벚꽃 (Inst.) --- 님마중 (New Ver.)\n",
      "Ikimonogakari --- Sakura (벚꽃) (DenpO115 동일본 에이어 CM 송) --- 1집 Sakurasakumachi Monogatari (벚꽃 피는 거리이야기)\n",
      "블랙아웃(Black Out) --- 벚꽃 (Inst.) --- 벚꽃\n",
      "강신주 --- Cherry Blossom (벚꽃) --- 나의 노래\n",
      "벚꽃 --- 벗꽃 버스 여행 --- 벗꽃 여행\n"
     ]
    }
   ],
   "source": [
    "for node in nodes:\n",
    "    _name=_selName(node)\n",
    "    _artist=_selArtist(node)\n",
    "    _album=_selAlbum(node)\n",
    "    if _name:\n",
    "        print _artist[0].text_content().strip(),\n",
    "        print \"---\",\n",
    "        print _name[0].text_content(),\n",
    "        print \"---\",\n",
    "        print _album[0].text_content()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
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
