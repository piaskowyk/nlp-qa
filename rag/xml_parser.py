import os
from bs4 import BeautifulSoup

main_path = './../czywieszze/cwz/'

part_size = 128
part = 2
print("Part size:", part_size, "dirs")

dirs = os.listdir(main_path)
print("Total parts: ", len(dirs) / part_size)

if not os.path.exists('logs'):
	os.mkdir('logs')
if not os.path.exists('wiki_csv'):
	os.mkdir('wiki_csv')

cur_dirs = dirs[part*part_size : (part+1)*part_size]

with open("logs/parser.log", "a", encoding='utf-8') as log:
	log.write("START part " + str(part) +  " dirs " + str(cur_dirs) + '\n' )

print("Current part: ", part)
print("DIRS ", cur_dirs)

for dir in cur_dirs:
	print("START DIR " + dir)
	with open("wiki_csv/wiki_" + dir + ".csv", "w", encoding='utf-8') as output:
		for root, d, files in os.walk(main_path + dir):
			for name in files:
				path = os.path.join(root, name)
				title = os.path.join(root, name)[2:]
				with open(path, encoding="utf-8") as f:
					xml = BeautifulSoup(f.read(), features="html.parser")
					text = ' '.join([chunk.text for chunk in xml.cesana.chunklist.findAll("chunk")])
				output.write(title + '\t' + text + '\n')
		print("END DIR " + dir)

with open("logs/parser.log", "a", encoding='utf-8') as log:
	log.write("END part: " + str(part) + '\n' )