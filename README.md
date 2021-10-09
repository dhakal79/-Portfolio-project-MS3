![Optimum Coagulant dose from jar test](images/jartest.jpg)

# Calculator optimum coagulant dose
Welcome! [IHE Delft](http://un-ihe.org)
## Introduction
Coagulation is a general treatment method to remove suspended fine particles, colour and other constituents from raw water, after adding chemicals (coagulants) and followed by further treatment. Coagulation is often applied in both conventional and advanced water treatment processes for the production of drinking water. 

Theoretical calculation of the optimum coagulant dose is not possible. Therefore, for each raw water experiments are needed. In glass beakers the coagulation process (rapid mixing, flocculation and sedimentation) is performed as shown in Fiure. This bench scale test is the so called “Jar test”. 

The overall aim of this project is to make an app which allows to analyze the google sheet data generated from the lab jar test experiments and calcualte the optimum coagulant dose. The app also allows the users to eneters the some plant operational data to calculate the total coagulant dose needed.

A live website can be found [here](https://dhakal79.github.io/Portfolio-project-MS2/).

![website preview](images/screenshot.jpg)

# Table of Contents
 [1. About the coagulant calculaor app](#coagulant-app)

 [2. How does the app works?](#play-app)

 [3. Features](#features)

 [4. User Expereince (UX) design](#ux)
  - [User Goals:](#user-goals)
  - [User Expectations:](#user-expectations)

 [5. Flow chart](#flow-chart)

 [6.Technologies used](#technologies-used)

 [7.Testing](#testing)

 [8.Bugs](#bugs)

 [9. Deployment](#deployment)

 [10. Acknowledgement](#acknowledgement)

  <a name="coagulant-app"></a>
# 1. About the coagulant calculaor app
  [Go to the top](#table-of-contents)


  <a name="play-app"></a>
# 2. How does the app works?
  [Go to the top](#table-of-contents)

  <a name="features"></a>
# 3. Features
  [Go to the top](#table-of-contents)

   <a name="ux"></a>
# 4. User Expereince (UX) design
  [Go to the top](#table-of-contents)

   <a name="user-goals"></a>
## 4.1 User Goals
  [Go to the top](#table-of-contents)

  <a name ="user-expectations"></a>
## 4.2 User Expectations
  [Go to the top](#table-of-contents)

 <a name="flow-chart"></a>
# 5. Flow Chart
  [Go to the top](#table-of-contents)

 <a name="technologies-used"></a>
# 6. Technologies-used
  [Go to the top](#table-of-contents)

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)) was used as a scripting language for the app development in this project.

* [Lucid Chart](https://www.lucidchart.com/) was used to flow diagram for the app.

* [Github](https://github.com/) was used to create the repository and to store the cproject's code after pushed from Git.
* [Gitpod](https://www.gitpod.io/) was used as the Code Editor for the site
* [PEP8 online](http://pep8online.com/) tool was used for manual testing procedures for code validation.

* [Ami](http://ami.responsivedesign.is/) was used to develop a Mockup screenshot generator
* [Heroku](heroku.com) was used to deploy a final version of the Python Essentials application code.

<a name="testing"></a>
# 7. Testing
  [Go to the top](#table-of-contents)
## PEP8 online validation
  PEP8 online validation tool was used to validate the code to ensure there were no syntax errors or improper code indentation. It passed the test as seen in the screenshot below:
  ![PEP* online validation](images/pep8_online.jpg)
## Mannual testing 
## a) Google sheet
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Google sheet | checked if the data in the google sheet is not a float number except table heading, it gives an error message "Data is not valid ! Please check the data entry".| PASS

## b) User input 
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
User input | checked if the data provided by user is not either integer or float or positive, it gives an error message "Please enter numeric value greater than 0" and "Enter value can't be zero or negative, try again" until the correct input is given| PASS
Update google sheet | checked if the data in google sheet is updated or not based on the users input and app calcualtion| PASS
Update google sheet | checked if the new data in google sheet is updated in the new row or not after each input from the user| PASS

<a name="bugs"></a>
# 8. Bugs
  [Go to the top](#table-of-contents)

 <a name="deployment"></a>
# 9. Deployment
  [Go to the top](#table-of-contents)

  The proejct was deployed to Heroku using the following steps:
- Sign up to Heroku
- 


<a name="acknowledgement"></a>
# 10. Acknowledgement
  [Go to the top](#table-of-contents)


* Inspired from love sandwitch project from the code institute course
* Thanks to my mentor Marcel Mulders for his constructive feedback

