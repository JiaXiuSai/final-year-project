# Password Generation Analysis
This folder contains all the source code for the password generation analysis. 

Folders:
- Collection: Code used for collection of password corpus.
- Information Entropy: Code used for password analysis (Shannon entropy and chi^2 test).
- PassGAN: Code used for deep learning password guessing (PassGAN)
- Password Corpus: Password corpus collected.
- Results: Results from zxcvbn.py in CSV format, sorted by estimated strength, and stats.py.


The models trained using PassGAN can be found on OneDrive [here](https://durhamuniversity-my.sharepoint.com/:f:/g/personal/rpsh88_durham_ac_uk/EgUo4pMuNCdDv-aIE8CMT4MB9DUCt2avD0AeWNN7vGaVjw?e=jgRE0e) (13 GB). A Durham Unversity email is required and please do not hesitate to contact me if there are any difficulties accessing the folder. 

## Installation
1. Install  [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) if you haven't already.
2. Download the repository and download [zxcvbn](https://github.com/dropbox/zxcvbn).
3. Run zxcvbn.py using the command:
```
python zxcvbn.py
```
## References
S. Oesch and S. Ruoti, “That was then, this is now: A security evaluation of password generation, storage, and autofill in browser-based password managers,” in 29th USENIX Security Symposium (USENIX Security 20). USENIX Association, Aug. 2020, pp. 2165–2182.

B. Hitaj, P. Gasti, G. Ateniese, and F. Perez-Cruz, “Passgan: A deep learning approach for password guessing,” 2019.

D. L. Wheeler, “Zxcvbn: Low-budget password strength estimation,” in Proceedings of the 25th USENIX Conference on Security Symposium, ser. Sec’16. Usa: USENIX Association, 2016, p. 157–173

Mutalik, D. Chheda, Z. Shaikh, and D. Toradmalle, “Rockyou,” 2021. [Online]. Available: https://dx.doi.org/10.21227/gzcg-yc1`
