Feature: Login Test

  Scenario: Check if login - success
    Given Chrome browser
    And Gmail login page
    When we write login emaildotestowaniapawel and click login button
    And we write password pawel321 and click login button
    Then we will login

  Scenario: Check if login - wrong password
    Given Chrome browser
    And Gmail login page
    When we write login emaildotestowaniapawel and click login button
    And we write password pawel123 and click login button
    Then we will not login

  Scenario: Check if login - wrong login
    Given Chrome browser
    And Gmail login page
    When we write login emailtestowaniapawel and click login button
    Then we will not login

  Scenario: Check if login - empty password
    Given Chrome browser
    And Gmail login page
    When we write login emaildotestowaniapawel and click login button
    And click login button on password page
    Then we will not login

  Scenario: Check if login - empty login
    Given Chrome browser
    And Gmail login page
    When click login button on login page
    Then we will not login