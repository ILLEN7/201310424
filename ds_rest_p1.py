<<<<<<< HEAD
import os
KEY="7146554555766c66353971696e757a"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM

import requests
data=requests.get(url)

=======
import os
KEY="7146554555766c66353971696e757a"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM

import requests
data=requests.get(url)

>>>>>>> 40ac7c3792f2f0f252517c80568beb0f64e0b55a
print data.text