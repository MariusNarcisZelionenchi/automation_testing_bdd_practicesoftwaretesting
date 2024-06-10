@account_feature
Feature: Check the functionality of the <<Account Page>>

  Scenario: Login with the new created user
    Given I am on the <<Home>> page and I navigate to <<Sign In>> page
    When I insert the registered email and the registered password
    When I click the <<Login>> button
    Then The <<Account>> page loads

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
     Then New <<Total Unit Price>> is "2" times the <<Unit Price>>
     When I click on <<Proceed to checkout>> 1st button
     When I click on <<Proceed to checkout>> 2nd button
     When I click on <<Proceed to checkout>> 3rd button
     Then Payment method is requested

#   Scenario Outline: Check that all payment methods work
#     When click pe dropdown
#     When click pe "<Bank Transfer>"
#     Then <<Bank Name>>, <<Account Name>> and <<Account number>> appear
#     When I insert the bank name "Banca"
#     When I insert the account name "Cont"
#     When I insert the account number "010101010101010101"
#     When I click the <<Confirm>> button
#     Then The confirmation message is displayed
#     Then The message reads "Payment was successful"
#     When I click the <<Confirm>> button
#     Then The invoice message is displayed
#     Then The cart is empty
