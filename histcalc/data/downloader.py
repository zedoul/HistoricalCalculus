import urllib
from data import datasets

for key, data in datasets.iteritems():
    source = data["url"]
    target = data["file"]
    print "downloading... " + target
    urllib.urlretrieve(source, target)

