# FinalProject
CS585 final project ver2

(You can still use ver1 which is done with python, however, you can only grab the top area of the html page. Since your web page can be long, only grab the top area to compare is not enough.)

This project can help you to compare the browser compatability by images captured from different browsers. The approach of this project is quite simple and understandable, it will connect to the url then fetch all the url links of current page, the grab two parts of all html pages then compare these images.

[[How does this work?]]
1. The program goes to the link you specified. </br>
2. Gather the links of this page. </br>
3. Visit all the links.</br>
4. Grab two parts of html page: (a) top area (b) some specified location (you can edit this and make the program scroll to more locations).</br>
5. Store images (by the html file name)</br>
6. Run ImgCompare.py</br>
7. View results in folder "cmp"</br>

Results:
The solid color is image from Chrome, FireFox has lighter color so that you can compare them:</br>
<img>https://raw.githubusercontent.com/H-yang/FinalProject/master/585Proj/cmp/contact-scroll.png-diff.png</img>

ImgCompare.py also combine the results so you can still compare by your eyes:</br>
<img>https://raw.githubusercontent.com/H-yang/FinalProject/master/585Proj/cmp/contact-scroll.png.png</img>



