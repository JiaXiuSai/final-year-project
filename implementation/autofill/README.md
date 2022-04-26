# Autofill Testing Website
![Screenshot of website](../../rpsh88/paper/diagrams/autofill-testing-site.png)
This folder contains all the source code for the autofill testing website. The website is hosted on two different domains using Heroku ([pwmtester1](https://pwmtester1.herokuapp.com) and [pwmtester2](https://pwmtester2.herokuapp.com)). For testing purposes, the website can be run on localhost using the commands:

1. Install [node](https://nodejs.org/en/download/) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) if you haven't already.
2. Download the repository and install all the required packages and their dependencies.
```
npm install 
```
3. Run node to start the server and the web pages will be accessible on https://localhost:3000
```
node .\server.js
```
Note: Edit variable  ```servertype``` in server.js to switch between servers using HTTP, HTTPS with valid cert and HTTPS with invalid cert.

## References
S. Oesch and S. Ruoti, “That was then, this is now: A security evaluation of password generation, storage, and autofill in browser-based password managers,” in 29th USENIX Security Symposium (USENIX Security 20). USENIX Association, Aug. 2020, pp. 2165–2182.