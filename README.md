# automation_testing_bdd_practicesoftwaretesting
https://practicesoftwaretesting.com/#/ --- testare automata BDD


I chose to test the TOOLSHOP DEMO website, which is a website specifically designed for automated testing. I've tested the functionality of the main page (sorting products by price), the login page (creating an account, checking the various error messages when trying to login with wrong credentials, logging in and out) and I've checked if an item can be bought from the main page.

LANGUAGE, IDE, BOOKSTORES
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
