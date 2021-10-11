Note: It is developed only for Windows operating system.

To run this program you will have to follow step by step:

1. This project is required a python programming language and python version is 3.6+. So you will have to download it from https://www.python.org/downloads/source/ and install it.

2. Then You will need a Postman tool to connect this program for sending and retrieving API data. Download it from https://www.postman.com/downloads/ and install it.

3. To check python version you have to use cmd(command line interface). Go to search programs or files then enter type cmd you will see command line windows box.
Enter command line type: python --version. If python version is shown up then it is already installed. Here example picture is given below:


![cmd](https://user-images.githubusercontent.com/53641071/130817465-79e4c71d-e046-410e-8151-b56fcb7d8a0e.png)

4. You have to check pip(python package manager) version which is recommended to use python framework or third party library to run this project.

![pip](https://user-images.githubusercontent.com/53641071/130818576-0667ff88-8478-4eff-b619-f390ede8cd32.png)

5. You have to create python virtual environment. This purpose is to create an isolated environment for Python projects. Enter type 'pip install virtualenv' in cmd.

![env](https://user-images.githubusercontent.com/53641071/130819998-a2229af4-876d-48bb-8318-b68b37ab1923.png)

To make environment this project. Type 'python -m venv newsenv' in cmd. It should be like

![pip](https://user-images.githubusercontent.com/53641071/130821212-a29faa16-3580-431e-ab39-508f629d0d43.png)


Activate this python environment. I will show this picture

![pip](https://user-images.githubusercontent.com/53641071/130822133-bad6cc13-ff7c-4e3f-9fa8-302b7cfc05d6.png)

You will see from above picture from last line in cmd that is actiavted.

6. Create a folder named  'Longevityin' in your choice directory. Go to web browser Download zip file from https://github.com/safinmnabi/longevity inside directory when you create folder named.

![testtask](https://user-images.githubusercontent.com/53641071/134121419-c5795f58-a782-43ba-ba4f-a83b37a46b22.png)


7. Then unzip this file and run manage.py in CMD tool when python environment is activated. Here is picture

![testtask](https://user-images.githubusercontent.com/53641071/134122890-865bd3fe-cecf-4726-9594-4468d5425e34.png)

8. Go to http://127.0.0.1:8000/ you will see template does not exist then it is fine because it is developed only API server. We have to use Postman tool for exchanging data from this server. Go to Postman when you installed it.


![testtask](https://user-images.githubusercontent.com/53641071/134125173-b7d6ff4a-4317-4181-8c6f-51570315f552.png)

This is a postman tool.

9. it has two parameters which are weight and blood_pressure from our API server to send user or B2B to get recommendation data. So, go to Postman tool. Select POST method and enter url address http://127.0.0.1:8000/update/1. Below picture will help you to understand

![testtask](https://user-images.githubusercontent.com/53641071/134127312-a7ef8e31-2f28-4fdd-ab75-643a64e297e6.png)

When to use weight parameter, if user has less than 49 Kg, it will retrieve to get recommendation data. Similarly, User has more than 50 Kg which is perfect health so will not retrieve data.

When to use blood_pressure parameter, if user's blood pressure has 120/80mmHg or higher. Then it is considered risks as has high blood pressure will get risks data from Postman tool. You will see "BPF": 2 from Postman output result. BPF means blood pressure factor.

BPF 0: when user's blood pressure has 90/60mmHg or lower as low bllod pressure

BPF 1: when user's blood pressure has 90/60mmHg higher and 120/80mmHg lower as Ideal or Normal Pressure

Note: It is first task is completed out of 5 tasks and It is sample/test task for reviewer board. i will carry on remaining of tasks until further notice from reviewer board.  
