import glob

files = glob.glob('dataset/czywieszze/czywieszki2.0/wiki/**/*.xml', recursive=True)
print(files[:10])

# import xml.etree.ElementTree as ET

# root = ET.fromstring(xml)
# for item in root[0]:
#   print(item.text)