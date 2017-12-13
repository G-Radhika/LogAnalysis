Place your catalog project in this directory.

Be sure to include a complete README file containing information on the 


Purpose of the project: {You've been hired onto a team working on a newspaper site.
The user-facing newspaper site frontend itself, and the database behind it, 
are already built and running. You've been asked to build an internal reporting tool
that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. 
The log has a database row for each time a reader loaded a web page. Using that information, 
your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. 
It won't take any input from the user. Instead, it will connect to that database, 
use SQL queries to analyze the log data, and print out the answers to some questions.}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
YOUR JOB IS TO FIND
1.What are the most popular three articles of all time? 
2.Who are the most popular article authors of all time? 
3.On which days did more than 1% of requests lead to errors?

newsdata.sql is the database file. Which contains THREE tables.
authors:
      name       |        bio                  | id
-----------------+-------------------------------------------

articles:
 author | title |slug | lead |body |  time | id
---------------------------+-------------------------------+----

log:
   path  | ip | method | status | time |   id
----------------------------+------------+--------+-

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
the steps needed to build the run-time environment:
This project is built on the vagrant virtual machine. After installing vagrant goto vagrant directory located in Fullstack directory.
1. /Fullstack(master) $ => here vagrant exe is located
2. /Fullstack(master) $ vagrant init ->initializes the VM
3. /Fullstack(master) $ vagrant up ->Boots the VM
4. /Fullstack(master) $ vagrant ssh ->Gets you into vagrant shell
5. vagrant@vagrant:~$
6. vagrant@vagrant:~$ cd /vagrant
7. vagrant@vagrant:/vagrant$ ls
	catalog  catalog.zip  forum  project2  tournament  Vagrantfile
8. vagrant@vagrant:/vagrant$ cd catalog
9. vagrant@vagrant:/vagrant/catalog$ ls
	catlog.py  README.txt  test.py
10.vagrant@vagrant:/vagrant/catalog$ python catalog.py => executes your file. ****execute the Python code*****
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

load the newsdata.sql file into the news database:
Download the newsdata.sql file and keep it in vagrant directory.

Follow the above steps till STEP 9.
9. vagrant@vagrant:/vagrant/catalog$ psql => This will lead you to psql environment where you can type psql queries and see the results directly. NO python required.
10.vagrant@vagrant:/vagrant/catalog$ psql
psql (9.5.9)
Type "help" for help.

vagrant=> psql -d news -f newsdata.sql => imports the data 
vagrant=> \c news => connects to the news database
vagrant=> \dt => gets details about the tables in the database

ctrl+z will get you out of psql prompt