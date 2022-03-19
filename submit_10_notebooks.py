import subprocess
import time

with open('notebooks/kernel-metadata.json') as fd:
    orig_content = fd.read()

for i in range(10):
    new_content = orig_content.replace('random-f-port-and-cv-fork', f'random-f-port-and-cv-fork{i}')
    with open('notebooks/kernel-metadata.json', 'w') as fd:
        fd.write(new_content)

    subprocess.run(['kaggle', 'kernels', 'push', '-p', 'notebooks'])
    time.sleep(2)
    with open('notebooks/kernel-metadata.json', 'w') as fd:
        fd.write(orig_content)
    time.sleep(2)