# Evergreen

To Run Server Locally:
1. Install Python 3.8
2. Create Virtual Environments https://docs.python.org/3/tutorial/venv.html  
    python3 -m venv <venv_name>  
    <venv_name>\Scripts\activate
3. requirements.txt is located at server/requirements.txt  
    cd server/   
    pip install -r requirements.txt  
4. Run django server:  
    python manage.py runserver  
5. Manage database manually:  
    url: http://127.0.0.1:8000/admin/  
    username: root  
    password: root  
6. Get requests for all the tests on a given day for a given test center:  
    url: http://127.0.0.1:8000/tests/test_list?test_center=<test_center_id\>&date=\<date\>  
