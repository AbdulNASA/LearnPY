from urllib import request
#contacturl = r'C:\Users\Dr Abd Al-Rahman\Downloads\contacts.csv'

def download(csvurl):
   # response = request.urlopen(csvurl)
 #   csv = response.read()
  #  csvstr = str(csv)
    lines = csvurl.split("\\n")
  #  desturl = r'goog.csv'
    fx = open(csvurl, 'r')
   # for line in lines:
   #     fx.write(line + "\n")
    fx.close()
download(contacturl)


#It doesn't work'