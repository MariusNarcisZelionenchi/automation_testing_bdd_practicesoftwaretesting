@account_feature
Feature: Check the functionality of the <<Account Page>>

  @register_using_faker @register_login_addtocart
  Scenario: Register new account using faker
    Given I am on the <<Home>> page and I navigate to <<Sign In>> page
    When I click on the <<Register Your Account>> button
    Then The <<Register>> page loads
    When I input a fake <<First Name>>
    When I input a fake <<Last Name>>
    When I input "0101200" as <<DateOfBirth>>
    When I input a fake <<Address>>
    When I input a fake <<Postal Code>>
    When I input a fake <<City>>
    When I input a fake <<State>>
    When I input "Romania" as <<Country>>
    When I input a fake <<Phone>>
    When I input a fake <<Email Address>>
    When I input a fake <<Password>>
    When I click on the <<Register>> button
    Then The <<Sign In>> page loads

  @valid_login_using_faker @register_login_addtocart
  Scenario: Check that a registered user can login
    Given I am on the <<Sign In>> page
    When I insert the fake registered email and the fake registered password
    When I click the <<Login>> button
    Then The <<Account>> page loads

  @add_item_in_cart @register_login_addtocart
  Scenario: Check that you can add a product in the shopping cart
    Given I am on the <<Account>> page
    When I click on the <<Logo>>
    When I click on the <<Search>> field, I type in "Sander" and I click the <<Search>> button
    When I click on the 2nd product
    When I click on the <<Add to cart>> button
    Then <<The product being added to the shopping card>> message is displayed
    Then The number of products is displayed on the shopping cart
    Then The number of products is correct
    When I click on the <<Shopping Cart>>
    When I click on the quantity, delete the amount, increase the amount by 1 and hit enter
    Then New <<Total Unit Price>> is 2 times the <<Unit Price>>

  @buy
  Scenario: Check that I can buy a product
     Given I am on the <<Account>> page
     When I click on the <<Shopping Cart>>
     When I click on <<Proceed to checkout>> 1st button
     When I click on <<Proceed to checkout>> 2nd button
     When I click on <<Proceed to checkout>> 3rd button
     Then Payment method is requested
     When I select "Bank Transfer" as desired payment method
     Then The confirmation message "Payment was successful" is displayed
     When I click the <<Confirm>> button
     Then The invoice message is displayed

  @logout
  Scenario: Check if a user is logged in and sign him out
    Given I am on the <<Home>> page and I navigate to <<Sign In>> page
    When I insert the fake registered email and the fake registered password
    When I click the <<Login>> button
    When I check if a user is logged in
    When I sign the user out
    Then The <<Sign In>> button is displayed