Use python 3 for the project

1. Then install virtualenv using pip3

`sudo pip3 install virtualenv`


2. Create a virtual environment

`virtualenv venv`


3. Active your virtual environment:

`source venv/bin/activate`


4. go inside the venv 
   cd venv


5. install postgre
`sudo apt-get install postgresql postgresql-contrib`


6 . Switch over to the postgres account on your server
`sudo -i -u postgres`
    access a Postgres promp
`psql`


7. cd inside the config folder
   cd config
   create symlink
   `ln -sf local.py __init__.py`

8. install Requirements
`pip install -r app/requirements/requirements.dev.txt`    

9. To run it open CORS Free chrome or any other browser