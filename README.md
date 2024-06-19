# automation_testing_bdd_practicesoftwaretesting
https://practicesoftwaretesting.com/#/ --- testare automata BDD


I chose to test the TOOLSHOP DEMO website, which is a website specifically designed for automated testing. I've tested the functionality of the main page (sorting products by price), the login page (creating an account, checking the various error messages when trying to login with wrong credentials, logging in and out) and I've checked if an item can be bought from the main page.

LANGUAGE, IDE, LIBRARIES

As IDE I used PyCharm which accepts the Python language. As libraries I used random, time, faker, selenium, string, pynput, webdriver, behave to automate the interaction with the website. The "Python Packages" section of PyCharm can be accessed to install these libraries. After adding the name of the desired library in the field, I pressed the "Install" button. (or the cmd terminal, using the "pip instal" command)

THE IMPORTANCE OF AUTOMATED TESTING

Automated testing plays a crucial role in enhancing software development efficiency. It offers advantages such as increased speed, reproducibility, broader coverage, reusability, seamless integration with agile methodologies, and early identification of defects. These benefits collectively contribute to maintaining software quality consistently throughout the development process.

THE CHOSEN METHODOLOGY

The software development approach known as Behavior-Driven Development (BDD) emphasizes team collaboration and articulating the application's behavior using a straightforward language like Gherkin. I opted for BDD to enhance communication among developers, testers, and stakeholders, enabling the creation of automated tests that accurately represent stakeholder-specified behavior. This choice brings benefits such as improved communication clarity, easily comprehensible and current tests, and alignment between requirements and implementation. BDD fosters teamwork and ensures that development efforts concentrate on delivering valuable functionalities that align with user expectations.

USE OF THE PROJECT

To begin working on the project, start by cloning it from GitHub. Access the project repository, click on the green "Code" button, copy the provided link, navigate to the desired folder on your computer, open Git Bash, and enter the command "git clone" followed by the copied link. Press "Enter" to clone the project successfully. Once cloned, you can open the project in PyCharm. To execute tests, use the command "behave -f html -o report.html" in the terminal. To view the test report, simply open the "report.html" file in a web browser.

STRUCTURE OF THE PROJECT

The project is structured with multiple files and directories. Within the "browser" file, settings for Chrome, window maximization, and a default 1-second delay can be found. The "environment" directory outlines the structure of the tested pages. The overall structure comprises three directories: "features," "pages," and "steps." Test scenarios, written in Gherkin syntax, are located in the "features" directory. General methods for actions like clicking, element locating, and typing are defined in basepage.py. The "pages" directory contains locators and specific methods for the test scenarios. Functions defined in Gherkin syntax are present in the "steps" directory. This organized structure facilitates automated test code management.

SCREENSHOTS (CODE):

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/108276b2-a9bc-4efc-aa4f-5b0e69e0b935)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/bcf0eb6f-30dd-47ee-9d26-7231ec89ae35)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/ae7cc031-3399-469f-99fc-8bbf6658cc2e)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/b54d6f49-0eaa-4483-ad0b-bf26ff44e890)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/54afa35d-c4f7-4fa3-9cae-df67c44afe6c)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/b378c8bb-f990-4ba1-8285-4415a424eec7)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/daa71222-6293-49f7-8d32-d7e962f68d64)

SCREENSHOTS (STEPS):

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/29347492-9857-465f-8144-bbe7b61d291f)


SCENARIOS:

Use the contact form and upload a file

Check if I can sort certain products by price and adjust the price range

Register a new account

Check that a registered user can login

Check that you cannot login when providing invalid credentials

Check that "Password length is invalid" message appears when the length of the password is less than 3 character

Check that you can add a product in the shopping cart

Check that I can buy a product

Check if a user is logged in and sign him out

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/7aa331d8-8916-4a2d-b58c-007de738fb47)

![image](https://github.com/MariusNarcisZelionenchi/automation_testing_bdd_practicesoftwaretesting/assets/123659805/e6f7c32a-c9a4-4a96-9eab-aeddb939bc1d)



