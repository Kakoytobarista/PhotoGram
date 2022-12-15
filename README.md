# PhotoGram
Something like Instagram, but better.

___

### Technologies:
Python==3.8, Django==3.1.7, djangorestframework==3.14.0, HTML/CSS/JS, SqLite, Filters,
Docker.

### How to run project:
#### Install Docker the first if you are don't have.
1. Give permissions to bash file
```
chmod u+x start_project.bash
```
2. Run bash file with docker:
```
./start_project.bash
```


______

### Credentials:

admin:
* login: admin
* password: qwe123!@#


anton:
* login: anton
* password: qwe123!@#

Names of users in system:
* Aslan
* Anton
* Vlad
* Andrey

_______
#### All data inside, so you need just start project.

Some things:
### I didn't have time to do a better implementation of autocomplete, but I decided to describe it here. 
In general, to optimize the database, it makes sense to make one query, 
cache it and push it into the NoSQL database, and from there 
add the field to the autocomplete. This will reduce the load 
on the database and is easy to implement since key value db.

PS: transactions in app for transactions, just for 
make you sure that I know what is it transactions in db.
