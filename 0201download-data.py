import os, time 
import tarfile 
from six.moves import urllib

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml2/master/" 
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path) 
    tgz_path = os.path.join(housing_path, "housing.tgz") 
    urllib.request.urlretrieve(housing_url, tgz_path) 
    housing_tgz = tarfile.open(tgz_path) 
    housing_tgz.extractall(path=housing_path) 
    housing_tgz.close()

if __name__ == '__main__':
    time1=time.time()
    #print(HOUSING_PATH)
    fetch_housing_data()
    time2 = time.time()
    print('OK!')
    print('Time Used: ' + str(time2 - time1) + 's')
