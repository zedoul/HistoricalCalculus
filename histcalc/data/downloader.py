import os
import urllib
from datasets import datasets

for _, data in datasets.iteritems():
    source = data["url"]
    target = data["file"]
    if False == os.path.isfile(target):
        print "downloading... " + target
        urllib.urlretrieve(source, target)
