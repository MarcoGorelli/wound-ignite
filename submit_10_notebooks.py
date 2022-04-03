import subprocess
import time

with open('notebooks/kernel-metadata.json') as fd:
    orig_content = fd.read()

F = 999
PORTS = [
    range(0, 10),
    range(10, 20),
    range(20, 23),
]

for i in PORTS[0]:
    new_content = orig_content.replace('f-0-port-0', f'f-{F}-port-{i}')
    with open('notebooks/kernel-metadata.json', 'w') as fd:
        fd.write(new_content)

    with open('notebooks/random-f-and-port-with-cv.ipynb') as fd:
        original_notebook = fd.read()
    new_notebook = original_notebook.replace('THIS_PORT = 0', f'THIS_PORT = {i}')
    new_notebook = new_notebook.replace('THIS_F = 0', f'THIS_F = {F}')
    with open('notebooks/random-f-and-port-with-cv.ipynb', 'w') as fd:
        fd.write(new_notebook)

    subprocess.run(['kaggle', 'kernels', 'push', '-p', 'notebooks'])
    time.sleep(2)
    with open('notebooks/kernel-metadata.json', 'w') as fd:
        fd.write(orig_content)
    with open('notebooks/random-f-and-port-with-cv.ipynb', 'w') as fd:
        fd.write(original_notebook)
