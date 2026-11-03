Feature: Order Transaction
  Tests related to order transactions


  Scenario Outline: Verify order success details message shown in details page
    Given place the item order with <username> and <password>
    And user is on landing page
    When I login to portal with <username> and <password>
    And navigate to orders page
    And select the orderId
    Then order message is successfully displayed
    Examples:
      | username                    | password        |
      | patnaikabinash07@gmail.com  | Abichinu@#12345 |
