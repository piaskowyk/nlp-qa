import json
from os import listdir
from os.path import isfile, join

output = []

questions = None
with open('question/czywiesz.json', 'r') as json_file:
    for line in json_file:
        questions = json.loads(line)

answers = None
with open('question/ans1.json', 'r', encoding="utf8") as json_file:
    for line in json_file:
        answers = json.loads(line)
with open('question/ans2.json', 'r', encoding="utf8") as json_file:
    for line in json_file:
        answers.update(json.loads(line).items())

csv_content = ""
csv_dict = {}
path = 'question/wiki/'
csv_file_names = [f for f in listdir(path) if isfile(join(path, f))]
for csv_file_name in csv_file_names:
    with open(path + csv_file_name, 'r', encoding="utf8") as csv_file:
        csv_content += csv_file.read()
csv_content = csv_content.replace('../czywieszze/cwz/', '')
for csv_line in csv_content.split('\n'):
    parsed_line = csv_line.split('\t')
    if len(parsed_line) != 2:
        continue
    csv_dict[parsed_line[0].replace('\\', '/')] = parsed_line[1]
csv_path_set = list(csv_dict.keys())

for question_id, question in questions.items():
    answer = answers.get(question_id)
    if not answer:
        continue
    if len(answer) == 0:
        continue
    answer = answer[0]
    csv_name = answer[1].replace('%23', '#')
    if not (csv_name in csv_path_set):
        continue
    answer_text = ' '.join([ans[1] for ans in answer[3]])
    if not answer_text:
        answer_text = csv_dict[csv_name]
    output.append((question, answer_text))

source = '\n'.join([q for q, a in output])
target = '\n'.join([a for q, a in output])
with open('source.txt', 'w', encoding="utf8") as outfile:
    outfile.write(source)
with open('target.txt', 'w', encoding="utf8") as outfile:
    outfile.write(target)

# path = 'question/wiki/'
# want = [f for f in listdir(path) if isfile(join(path, f))]
# to_remove = []
# path = './wiki_csv/'
# all = [f for f in listdir(path) if isfile(join(path, f))]
# for item in all:
#     if item in want:
#         continue
#     to_remove.append(item)
# print('rm ' + ' '.join(to_remove))
