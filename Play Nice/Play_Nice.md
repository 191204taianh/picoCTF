Play Nice
=====================================================

## Info
* Difficulty: Hard
* Category: Cryptography
* Hint
    * none
* Description
    * Not all ancient ciphers were so bad... The flag is not in standard format.
    * [playfair.py](playfair.py)

```
nc mercury.picoctf.net 6057
```

## Start 
```
Here is the alphabet: meiktp6yh4wxruavj9no13fb8d027c5glzsq
Here is the encrypted message: y7bcvefqecwfste224508y1ufb21ld
What is the plaintext message? 
```

Using [Playfair decoder](https://planetcalc.com/7751/) with these alphabet and encrypted message to find the plaintext:<br>
--> Plaintext: `hfdnlultdxdlkmeyofsf`<br>
--> Flag: `2e71b99fd3d07af3808f8dff2652ae0e`