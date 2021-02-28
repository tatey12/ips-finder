import random
import hashlib
import requests
import glob
import os
import imghdr
import __main__
import time
downfolder = os.getcwd()
suffixes = ["_d", "s", ""]

urlformat = "https://i.imgur.com/{0}{1}.png"
monopolyhash = "dc92ae81dc8dd00bfc340c9779e64d3ef8941ea4b9edfc621c805012c687bb42"
removedhash = "9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9"
deletedatshit = glob.glob('*.*')
for i in deletedatshit:
  if i == __file__:
    print('Skipping current script.')
  else:
    os.remove(i)
def rand(byte):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  if byte == 5:
    byter = 5
  elif byte == 7:
    byter = 7
  return ''.join(random.choice(letters) for i in range(byte))

def genurls(byte, amount, urlsuffix):
  global failures
  global passes
  failures = 0
  passes = 0
  monopolies = 0
  imgururls = []
 
  if not urlsuffix in suffixes:
    print('Not a valid URL suffix, using "_d"')
    urlsuffix = '_d'
  try:
    while True:
      time.sleep(int(os.environ["WAIT"]))
      randerps = rand(byte)
      url2 = urlformat.format(randerps,urlsuffix)
      r = requests.get(url2)
      if hashlib.sha256(r.content).hexdigest() == removedhash:
        failures += 1
        print("FAIL for " + str(url2) + " Total " + str(failures) + " failures.")
      else:
        passes += 1
        print("PASS for " + str(url2) + " Total " + str(passes) + " passes.")
        discord = requests.post(os.environ["imgur"],data={"content":str(url2)})
        discord2 = requests.post(os.environ["secondary_imgur"],data={"content":str(url2)})
        time.sleep(.75)
      if hashlib.sha256(r.content).hexdigest() ==  monopolyhash:
        monopolies += 1
        print("And it is Monopoly #" + str(monopolies) + " !")
        discord = requests.post(os.environ["monopoly"],data={"content":str(url2)})
        imgururls.append(url2)
    return imgururls
  except Exception as e:
    print('Error.', str(e))
def downloadurls(listor):
  print('Downloading urls.')
  for i in range(len(listor)):
   
    try:
      r = requests.get(listor[i])
      filetype = imghdr.what(None, h=r.content)
      if filetype == None:
        print('Filetype unidentifiable, using png')
        filetype = 'png'
      with open(str(i) + '.' + filetype, 'wb') as image:
        image.write(r.content)
        
    except Exception as e:
      print('Error downloading image url', str(i), str(e))

urls = genurls(5, 90000, '')
print('Info:', str(failures), 'failures, ' + str(passes) + ' passes.')
print(urls)
