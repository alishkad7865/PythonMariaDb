# Installing Wamp server
- If you are using 64 bit Windows machine click on [download-64bit](https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.2.6_x64.exe/download), or else if you are using 32 bit windows machine click on [download-32bit](https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.2.6_x86.exe/download). For more info click on https://www.wampserver.com/en/
- You must have microsoft visual C++ installed into your machine
- Open the downloaded wampserver file, and run it as administration.
- Select the package version you want to install or leave it as default. The packages include php, MariaDb, MySQL, Apache, phpMyAdmin.
- Save the location for wampserver folder or set it as default "C:\wampserver\".
- After the download is complete, Click on Start in task bar and type Wampserver and select the filtered application.
- After it is sucessfully installed into your machine, you can see the Wampserver icon into your toolbar
- Click on that icon and select 'localhost' to view your folders in website
- You can also click on phpMyAdmin from that icon and login as username 'root' and leave password empty and log in
- You can create database and table directly through phpMyAdmin UI or if you prefer command line then click on MariaDb from Wamp server icon in toolbar and it will open command line terminal to write MySQL commands
- For more guidelines on installing Wampserver click on [Youtube link](https://www.youtube.com/watch?v=7gMplrbDZJs)
- For basic MySQL command instriction click on [MySQL basic commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)

#  Install Python
- To install python go to https://www.python.org/downloads/ and install your prefered version for your machine
- After installing Python you might have to install python from Microsoft store if you are on windows machine. If you are using other OS then it's not an issue
- You have to add python bin path to your system administration PATH
- After installation open terminal and type `python` on successful execution exit from python
- type `pip install mariadb` into terminal

# Creating Connection Between Python and MySQL database
- Create new testFile.py with extension py and then copy the python code from '../src/Connection.py' and copy into your file
- Please save the Students.sql file from the repository '.../database/students.sql' 
- Go to phpMyadmin from wamp server log in as root and create a database from left side and name it as 'myDb'
- import the students.sql file into this database
- To create new user in mySQL type following command in MariaDb console:
```
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password123456';
GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost';
FLUSH PRIVILEGES;
```
- Open terminal to project path and type `python testFile.py`
- You might have to make changes to the code if any error sql error is displayed
- The connections should be successful

# Next Steps
- Create or Enhance archecture structure in Backend to connect to API using MVC
- Create simple WebPage page to connect to Backend using API
- Use React or vanilla JS for the front end
- Add security on Backend and Front End 
- Add BFF on front end React JS
