# README
code environment
equipment background
software limitation
speed# README.md
-Environment Setting
+ git --version
+ git config --global user.name 'Aaron'
+ git config --global user.email 'ruuu9311@gmail.com'
+ git init
#browse to check a folder existed call .git

- Test File Building
+ create a new file. #README.md and write something.
+ save (ctrl + s)
+ git add .
+ git commit -m 'init README.md'
+ git status #check untracked file or folder
+ git log --oneline

- push local Git to cloud GitHub
+ browse GitHub
+ login GitHub
+ Create new repository
+ copy the instruction*3 and paste to VS code terminal
+ execute

#SELCT
SELECT id,name FROM product_info
WHERE id ='2';

#INSERT
INSERT INTO"main"."product_info"
("name","version","remark")
VALUES('Laptop','ASUS','I LUV ASUS')

#UPDATE
UPDATE product_info
SET NAME = 'IPHONE',version='18.3'
WHERE id=1;

#DELETE
SELECT * FROM product_info
WHERE ID='3';