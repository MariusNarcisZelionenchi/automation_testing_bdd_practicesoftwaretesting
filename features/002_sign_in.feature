@sign_in_feature
Feature: Test the functionality of the <<Sign In>> page

  Background:
    Given I am on the <<Home>> page and I navigate to <<Sign In>> page

  @register
  Scenario: Register a new account
    When I click on the <<Register Your Account>> button
    Then The <<Register>> page loads
    When I fill in the required info
    Then The <<Sign In>> page loads

  @invalid_login
  Scenario Outline: Check that you cannot login when providing invalid credentials
    Then I cannot login with the "<email>" and "<password>" into the account and i receive "<email_err>" error
#    Then Clear input
    Examples:
      | email            | password | email_err                                                                   |
      | blank            | pass1    | Email is required                                                           |
      | no_email         | pass2    | Email format is invalid                                                     |
      | registered_email | pass3    | Invalid email or password                                                   |
      | registered_email | pass4    | Account locked, too many failed attempts. Please contact the administrator. |


  @credentials_error
  Scenario: Check that "Invalid email or password" message appears when an unregistered email is inserted
    When I insert "wrong_email@email.com" in the email field
    When I insert "password" in the password field
    When I click the <<Login>> button
    Then The credentials error message appears. The credentials error message is "Invalid email or password"
#    Then Clear input

  @password_length
  Scenario: Check that "Password length is invalid" message appears when the length of the password is less than 3 character
    When I insert "some_email@email.com" in the email field and a 1 or 2 characters password in the password field
    When I click the <<Login>> button
    Then The password error message appears. The password error message is "Password length is invalid"
#    Then Clear input

  @skip @register_using_parameters
  Scenario: Register new account using parameters
    When I click on the <<Register Your Account>> button
    Then The <<Register>> page loads
    When I input "Prenume" as <<First Name>>
    When I input "Nume" as <<Last Name>>
    When I input "0101200" as <<DateOfBirth>>
    When I input "adresa" as <<Address>>
    When I input "0123456" as <<Postal Code>>
    When I input "Oras" as <<City>>
    When I input "Judet" as <<State>>
    When I input "Romania" as <<Country>>
    When I input "0123456789" as <<Phone>>
    When I input the <<Email Address>>
    When I input the <<Password>>
    When I click on the <<Register>> button
    Then The <<Sign In>> page loads

  @skip @register_using_faker
  Scenario: Register new account using faker
    When I click on the <<Register Your Account>> button
    Then The <<Register>> page loads
    When I input a random <<First Name>>
    When I input a random <<Last Name>>
    When I input "0101200" as <<DateOfBirth>>
    When I input a random <<Address>>
    When I input a random <<Postal Code>>
    When I input a random <<City>>
    When I input a random <<State>>
    When I input "Romania" as <<Country>>
    When I input a random <<Phone>>
    When I input a random <<Email Address>>
    When I input a random <<Password>>
    When I click on the <<Register>> button
    Then The <<Sign In>> page loads

  @valid_login
  Scenario: Check that a registered user can login
    When I insert the registered email and the registered password
    When I click the <<Login>> button
    Then The <<Account>> page loads

 @skip @valid_login_using_faker
  Scenario: Check that a registered user can login
    When I insert the fake registered email and the fake registered password
    When I click the <<Login>> button
    Then The <<Account>> page loads