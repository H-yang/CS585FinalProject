# FinalProject
CS585 final project : Web Browser Compatability Checker</br>
</br>
Requirements:</br>
To run this, you will need to load the files into your Eclipse.</br>
Required library: Selenium api for Java. (http://www.seleniumhq.org/download/)</br>
Have driver file. You can dowloand from the above link </br>
Specify driver file location in the program </br>

This project can help you to compare the browser compatability by images captured from different browsers. The approach of this project is quite simple and understandable, it will connect to the url then fetch all the url links of current page, the grab two parts of all html pages then compare these images.</br>

[How does this work?]</br></br>
1. The program goes to the link you specified. </br>
2. Gather the links of this page. </br>
3. Visit all the links.</br>
4. Grab two parts of html page:</br>
   (a) top area</br>
   (b) some specified location (you can edit this and make the program scroll to more locations).</br>
5. Store images (by the html file name)</br>
6. Run ImgCompare.py</br>
7. View results in folder "cmp"</br>

Results:
The solid color is image from Chrome, FireFox has lighter color so that you can compare them:</br>
![alt tag](https://raw.githubusercontent.com/H-yang/FinalProject/master/585Proj/cmp/contact-scroll.png-diff.png)

ImgCompare.py also combine the results so you can still compare by your eyes:</br>
![alt tag](https://raw.githubusercontent.com/H-yang/FinalProject/master/585Proj/cmp/contact-scroll.png.png)

Note: I thought the ImgCompare failed when resolution is changed, however it does not. it still did right things.</br>
![alt tag](http://i.imgur.com/SS8xUz6.png)
