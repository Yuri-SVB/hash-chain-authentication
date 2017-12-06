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

with open('hash_chain', 'r') as HC_file:
	line = HC_file.readline()
	print(line)
	hashes = eval(line)
	print(hashes)
	HC_file.close()

print("Verifying hash chain...")

t0 = time.time()
with Pool() as p:
    args = []
    for i in range(1,len(hashes)):
        args.append((hashes[i-1], hashes[i], i,))
    print(p.map(verify, args))

t1 = time.time()
print("...Done! Elapsed time: ", t1 - t0)
