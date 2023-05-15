# git clone to your local folder
## git clone git@github.com:ja841014/python_pretest_be.git

# open terminal and go to your target folder

# run test case
## python3 manage.py test PretestBE 

# run django server
## python3 manage.py runserver


## open the browser and enter http://localhost:3000/ to see the website

## API

# GET api/users
{
    "users": [
        {
            "id": 1,
            "name": "testuser",
            "point": 11
        },
        {
            "id": 3,
            "name": "newuser",
            "point": 0
        },
    ]
}

# POST api/users
{
    'name': 'add'
}
# PUT api/users/points
{
    'id': 9, 'point': 8
}