# FinalProject
CS585 final project ver2

(You can still use ver1 which is done with python, however, you can only grab the top area of the html page. Since your web page can be long, only grab the top area to compare is not enough.)

This project can help you to compare the browser compatability by images captured from different browsers. The approach of this project is quite simple and understandable, it will connect to the url then fetch all the url links of current page, the grab two parts of all html pages then compare these images.

[[How does this work?]]
1. The program goes to the link you specified.
2. Gather the links of this page.
3. Visit all the links.
4. Grab two parts of html page: (a) top area (b) some specified location (you can edit this and make the program scroll to more locations).
5. Store images (by the html file name)
6. Run ImgCompare.py
7. View results in folder "cmp"

