import hashlib
import time
from functools import partial
from multiprocessing import Pool

MILESTONE = 100000
N_MILESTONES = 100

def sha512sum(filename1, filename2):
    d = hashlib.sha512()
    with open(filename1, mode='rb') as f:
        for buf in iter(partial(f.read, 512), b''):
            d.update(buf)
    with open(filename2, mode='rb') as f:
        for buf in iter(partial(f.read, 512), b''):
            d.update(buf)
    return d

def hash_link(digest):
    h = hashlib.sha512(digest).digest()
    for i in range(MILESTONE):
        h = hashlib.sha512(h).digest()
    return h

def verify(k):
    h = k[0]
    final = k[1]
    index = k[2]
    for i in range(MILESTONE):
        h = hashlib.sha512(h).digest()
    if h == final:
        return "Okay!"
    else:
        return "ERROR!"

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

print("Verifying hash chain...")

t0 = time.time()
with Pool() as p:
    args = []
    for i in range(1,len(hashes)):
        args.append((hashes[i-1], hashes[i], i,))
    print(p.map(verify, args))

t1 = time.time()
print("...Done! Elapsed time: ", t1 - t0)
