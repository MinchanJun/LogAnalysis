# Logs Analysis Project
Python code that shows the analyis of data sql in a deeper level. For a security purpose, I am not able to push news database since I didn't build it.

# Background
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

# Learn your skills
### 1. Udacity Links
[Joining tables](https://classroom.udacity.com/courses/ud197/lessons/3415228765/concepts/33932188550923)
[The select ...where statement](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287000923)
[Select clauses](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287080923)
[Writing code with DB-API](https://classroom.udacity.com/courses/ud197/lessons/3483858580/concepts/35153985360923)
[Views](https://classroom.udacity.com/courses/ud197/lessons/3490418600/concepts/35140186650923)

### 2. PostgreSQL Documentation

[The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
[SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
[Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)

# Getting Started
This project makes use of the same Linux-based virtual machine (VM).

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

### Use a terminal
You'll be loading this python file using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [here](vagrantup.com). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

For a security purpose, I did not add any class materials.

### Start the virtual machine
From your terminal, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

### To load database

    psql -d news -f newsdata.sql

1.  psql — the PostgreSQL command line program
2. -d news — connect to the database named news which has been set up for you
3. -f newsdata.sql — run the SQL statements in the file newsdata.sql

### What is going to be reported?
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    Example:
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

    Example:
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

    Example:
July 29, 2016 — 2.5% errors

### To run news.py file properly
1. This query has to be run before you run this file.

        CREATE VIEW total_status AS
        SELECT TO_CHAR(time, 'FMMonth DD,YYYY') AS t, COUNT(status) AS num
        FROM log
        GROUP BY t;

        CREATE VIEW errors AS
        SELECT TO_CHAR(time, 'FMMonth DD,YYYY') AS t, COUNT(status) AS num
        FROM log
        WHERE status != '200 OK'
        GROUP BY t;

    First query counts all the status in log and displayed in an order by dates. Second query counts all the error status in log and displayed in an order by dates Make sure these two queries are executed before you run this file. This is necessary for question 3 to have output. If you made a mistake, please drop those queries again re-run it.

        drop view if exists total_status;
        drop view if exists errors;

### Run
    python news.py
Once you run this file, you will see a text file that is generated from news.py. Open the file and check the result of execution of queries.

## Authors
Minchan Jun

## License
