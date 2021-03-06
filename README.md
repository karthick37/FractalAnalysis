# FractalAnalysis Assignment
Todo app with React front-end and Django Backend

**Depandancies**
<ul>
  <li>Python3.5 or above</li>
  <li>python3-django</li>
  <li>python3-djangorestframework</li>
  <li>reactjs</li>
</ul>

**How To Run** <br>

Step 1: Git Clone <br>
    <code>git clone git@github.com:karthick37/FractalAnalysis.git</code><br>
  
Step 2: Initialize django server <br>
    <code>python3 manage.py makemigrations</code> <br>
    <code>python3 manage.py migrate</code> <br>
    <code>python3 manage.py runserver 8000</code> <br>
  
Step 3: Initialize React App <br>
    Follow the steps mentioned <a href="https://github.com/karthick37/FractalAnalysis/tree/master/todo_frontend">here</a> <br>
    <code>cd react_frontend</code> <br>
    <code>npm build </code> <br>
    <code>npm start </code> <br>
  
**On Browser** <br>
    FrontEnd: <url>http://localhost:3000</url> <br>
    BackEnd:  <url>http://localhost:8000/api/todo-backend/</url>
 

**Updates Planned**
  <ul>
    <li>Form Validation</li>
    <li>Error Handling</li>
    <li>Edit/Update Tasks with alert modal</li>
    <li>Bucket with multiple users</li>
    <li>UI Change - Convert bootstrap based UI into MaterialUI</li>
    <li>Add Organisation and user roles</li>
    <li>User login within organisation, etc,... </li>
  </ul>
