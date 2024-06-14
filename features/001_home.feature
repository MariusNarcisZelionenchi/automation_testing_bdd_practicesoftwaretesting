@home_feature
Feature: Test the functionality if the <<Home>> page

  Background:
    Given I am on the <<Home>> page

  Scenario: Check if I can sort certain products by price and adjust the price range
    When I select "Hammer" category
    When I select "Saw" category
    When I select "Tool Belts" category
    When I click the <<Sort By>> arrow and I click the 3rd option
    Then The products are reordered
#    When I click on the max price and drag it until the new max price is 15
#    Then The page displays only products with a price < 15