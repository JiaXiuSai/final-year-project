# Security Analysis of Modern Password Managers

This repository contains my final year project submission for Durham University COMP3012 Computer Science Project 2021/22 on the Security Analysis of Modern Password Managers.

[Paper](https://drive.google.com/file/d/1Rz6AZt4TPFb2Z1uldgl_vdtsRUBCVNmY/view?usp=sharing)
[Presentation Slides](https://docs.google.com/presentation/d/18GeDTNGZg78NOmDNWsHa7T00gNHg9ahnM1B27y4eKl4/edit?usp=sharing)  

The rapid growth of today’s internet usage makes online security more important than ever. With passwords being the primary authentication method on the internet, they need to be resilient against malicious attacks to protect the valuable assets of internet users. Password managers are advertised as a solution for users looking for a one-stop solution for their password needs to improve their online security. Security analysis looks at the current software products to find any security vulnerabilities that can be exploited to compromise its users. The objective of this paper is to improve password managers by analysing the state of security in password managers and providing suggestions for improvements based on industry standards. A list of tests was devised from prior academic and non-academic sources on the topic to evaluate the password managers on their three main features; password generation, password storage and password autofill. Analysis and comparison are made based on the results from the tests on seven popular password managers. The results show that improvements have been made since previous security analyses but there still exist some security flaws in today’s password managers. The problems include the lack of setting for common use cases, insecure design choices to vulnerable autofill policies. Based on our results, we identify the current industry stand of password managers, provide recommendations to improve password managers, report crucial vulnerabilities to the developers and showed that password managers improve users’ online security.


| Password Manager |    Version   |
|------------------|:------------:|
| Google Chrome    | 95.0.4638.69 |
| Mozilla Firefox  | 94.0.1       |
| Microsoft Edge   | 95.0.1020.53 |
| LastPass         | 4.84.0       |
| Bitwarden        | 1.54.0       |
| Dashlane         | 6.2142.2     |
| 1Password        | 2.1.4        |

## References
S. Oesch and S. Ruoti, “That was then, this is now: A security evaluation of password generation, storage, and autofill in browser-based password managers” in 29th USENIX Security Symposium (USENIX Security 20). USENIX Association, Aug. 2020, pp. 2165–2182.

B. Hitaj, P. Gasti, G. Ateniese, and F. Perez-Cruz, “Passgan: A deep learning approach for password guessing” 2019.

D. L. Wheeler, “Zxcvbn: Low-budget password strength estimation” in Proceedings of the 25th USENIX Conference on Security Symposium, ser. Sec’16. Usa: USENIX Association, 2016, p. 157–173
