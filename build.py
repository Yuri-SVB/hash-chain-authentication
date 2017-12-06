import hashlib
import time
from functools import partial
from multiprocessing import Pool

MILESTONE = 1000000
N_MILESTONES = 10

def sha512sum(filename1, filename2):
    d = hashlib.sha512()
    with open(filename1, mode='rb') as f:
        for buf in iter(partial(f.read, 512), b''):
            d.update(buf)
    with open(filename2, mode='rb') as f:
        for buf in iter(partial(f.read, 512), b''):
            d.update(buf)
    return d

def hash_link(input):
    # digest = hashlib.sha512(input).digest()
    digest = input
    for i in range(MILESTONE):
        digest = hashlib.sha512(digest).digest()
    return digest

hashes = []

print("Creating hash chain...")

t0 = time.time()

h = sha512sum('video.avi', 'key.dat').digest()
print("Initial:", h)
hashes.append(h)
for i in range(N_MILESTONES):
    h = hash_link(h)
    hashes.append(h)
    print("Milestone ", i, ": ", h, sep="")

t1 = time.time()
print("...Done! Elapsed time: ", t1 - t0)

with open('hash_chain', 'w') as HC_file:
    HC_file.write(str(hashes))
    # for i in hashes:
    #     HC_file.write(i)
    #     HC_file.write('\n')
    HC_file.close()
