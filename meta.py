import subprocess

infoDict = {}  # Creating the dict to get the metadata tags
# for linux user
exifToolPath = '/usr/bin/exiftool'
imgPath = '/path/to/image'

''' use Exif tool to get the metadata '''
process = subprocess.Popen([exifToolPath, imgPath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           universal_newlines=True)
''' get the tags in dict '''
for tag in process.stdout:
    line = tag.strip().split(':')
    infoDict[line[0].strip()] = line[-1].strip()

for k, v in infoDict.items():
    print(k, ':', v)
