@home_feature
Feature: Test the functionality if the <<Home>> page

  Background:
    Given I am on the <<Home>> page

  @contact
  Scenario: Use the contact form and upload a file
    When I click the <<Contact>> button
    When I insert "Johnny" as first name, "Mnemonic" as last name and "J_M@pharmakom.org" as email
    When I select a subject
    When I insert "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..." as message
    When I choose a file to upload
    When I click <<Send>>
    Then The "Thanks for your message! We will contact you shortly." message is displayed

  @sort
  Scenario: Check if I can sort certain products by price and adjust the price range
    When I select "Hammer" category
    When I select "Saw" category
    When I select "Tool Belts" category
    When I click the <<Sort By>> arrow and I click the 3rd option
    Then The products are reordered
    When I click on the max price and drag it to the left
    Then The page displays only products with a price lower than the new max price