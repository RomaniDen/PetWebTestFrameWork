# PetWebTestFrameWork (work in progress...)

This is a pet project for portfolio created by RomaniDen, a Python AQA. <br>
The project is written in Python using Selenium, pytest and Page Object Pattern. It includes integration with TestRail.<br>
The product to be tested was picked randomly: exist.ua web application.<br>

# Getting Started
Prerequisites<br>
Before you can run the tests, you will need to have the following installed on your machine:<br>

Python 3.6+ <br>
pip <br>
Installation <br>
Clone the repository: git clone https://github.com/RomaniDen/PetWebTestFrameWork.git <br>
Navigate to the project directory: cd PetWebTestFrameWork <br>
Install the required dependencies: pip install -r requirements.txt 

# Configuration
You will need to create the testrail.cfg file with your own credentials for TestRail. 

[API]
url = 'testrail URL'<br>
email = 'testrail email'<br>
password = 'testrail API'<br>

[TESTRUN]
assignedto_id = 1 <br>
project_id = 1 <br>
suite_id = 1 <br>
milestone_id = 3 <br>
plan_id = 11 <br>
run_id = 12 <br>
description = 'Test description' <br>

[TESTCASE]
custom_comment = 'Test run with 1 script'

# Running the tests
To run the tests, simply execute the following command in the terminal:<br>
pytest --testrail --tr-config=testrail.cfg<br>

OR run the run_tests.sh

