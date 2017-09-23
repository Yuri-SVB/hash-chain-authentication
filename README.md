# hash-chain-authentication
Proof of concept of Authentication by Computation of Hash Chain

Suppose Alice wants to send Bob a SRVB public-key. How can she know for sure that the key Bob gets is actually the same that she sent, and not a forged key made by Eve (a so called 'middle man')? This means to authenticate the key, and we have a new way to do that: Suppose Alice...

1. Concatenates a video of herself to her SRVB public-key;
2. Takes the hash of it;
3. Calculates hundred of trillions of iterations of that hash;
4. Every, say, billion of iterations, she registers the resulting digest, while traking the correspondent number of iteration of each one;

The resulting trail of registered digest is a computation that is considerably difficult to produce, and **necessarily serial**. But it is **embarassingly parallel to verify**. In order to do that, one just has to assign the verification of the path from each registered digest to the next to one different thread.

If it takes Alice, say, one hour to compute such a hash chain and she, then sends the video-and-key concatenation together with this hash chain to Bob, then, he can be sure that, within a certain window of time proportional to Alice's computational time, that package could only have been produced by her. The rationel is that in order for Eve to forge the package, she would have had not only to substitute Alice's key by hers own, but also to recalculate the entire hash chain. Now, since this computation is inescapably serial, *Eve's hash chain calculation time would necessarily equal or greater than the number of iterations divided by the speed of hash calculation of the single fasted hash calculator existent, **regardless of how much hardware Eve had***, precisely becaue of the inherently serial character of the hash chain computation. Thus, if this world's single fastest hash calculator is, say, sixty times faster than Alice's, Bob can **know for sure** that the package he receives is indeed the same sent by Alice, provided it arrives within **one minute** after the indicated sending time, because, within this one minute gap, Eve do not have enough time to forge the complete package (again, **regardless of how much hardware she has**).

In order to run this prototype, have a file in the working directory named video.avi and another named key.dat. They can have whatever content, but necessarily these names.
