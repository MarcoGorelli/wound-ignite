# kaggle kernels list -m --sort-by dateRun --page-size 100 -p 1| awk '{print $1}' | xclip -sel clip
import re

with open('cv-results/kernels_list.txt') as fd:
    content = fd.read().splitlines()

content = [i[len('code/marcogorelli/'):] for i in content]
content = [i for i in content if re.search(r'^f-\d+-port-\d+$', i)]
for i in content:
    print(f'"marcogorelli/{i}",')