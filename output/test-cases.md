# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2025-12-25T19:25:43.771727

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 98 |

### By Type

| Type | Count |
|------|-------|
| Positive | 29 |
| Negative | 47 |
| Edge Case | 22 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 32 |
| Medium | 48 |
| Low | 18 |

---

## Test Cases

### Login

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login using valid username | A registered account exists with a valid username and password | 1. Enter a valid username into the username field 2. Enter the correct password into the password field 3. Click the Log In button | The user is redirected to the account dashboard | High |
| LOGIN-002 | Successful login using valid email address | A registered account exists with a valid email and password | 1. Enter a valid email address into the username field 2. Enter the correct password into the password field 3. Click the Log In button | The user is redirected to the account dashboard | High |
| LOGIN-005 | Login recovery after authentication error | A registered account exists | 1. Enter a valid username into the username field 2. Enter an incorrect password into the password field 3. Click the Log In button 4. Clear the password field and enter the correct password 5. Click the Log In button | The user is redirected to the account dashboard after the second login attempt | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-003 | Login failure with unregistered username | None | 1. Enter a non-existent username into the username field 2. Enter any password into the password field 3. Click the Log In button | An error message is displayed and both input fields remain populated with the entered values | High |
| LOGIN-004 | Login failure with incorrect password | A registered account exists | 1. Enter a valid username into the username field 2. Enter an incorrect password into the password field 3. Click the Log In button | An error message is displayed and both input fields remain populated with the entered values | High |
| LOGIN-006 | Login attempt with empty credentials | None | 1. Leave the username field empty 2. Leave the password field empty 3. Click the Log In button | An error message is displayed indicating that credentials do not match or are required | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Login with special characters in username | An account exists with special characters in the username | 1. Enter the username containing special characters into the username field 2. Enter the correct password into the password field 3. Click the Log In button | The user is redirected to the account dashboard | Low |

---

### Forgot Password

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-001 | Successful customer lookup with valid details | A valid user record exists in the system matching the input criteria | 1. Enter a valid First Name into the First Name field 2. Enter a valid Last Name into the Last Name field 3. Enter a valid Address into the Address field 4. Enter a valid City into the City field 5. Select a valid State from the State dropdown 6. Enter a valid Zip Code into the Zip Code field 7. Enter a valid SSN into the SSN field 8. Click the 'Find My Login Info' button | The page displays the appropriate recovery details for the matching record | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-002 | Error message displayed when no matching record is found | No user record exists in the system matching the input criteria | 1. Enter 'NonExistent' into the First Name field 2. Enter 'User' into the Last Name field 3. Enter '999 Unknown St' into the Address field 4. Enter 'Nowhere' into the City field 5. Select a State from the State dropdown 6. Enter '00000' into the Zip Code field 7. Enter '000-00-0000' into the SSN field 8. Click the 'Find My Login Info' button | The page displays an error message indicating no matching record was found | High |
| FORPAS-003 | Validation error when First Name is left blank | None | 1. Leave the First Name field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the First Name field before the form can be submitted | Medium |
| FORPAS-004 | Validation error when Last Name is left blank | None | 1. Leave the Last Name field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the Last Name field before the form can be submitted | Medium |
| FORPAS-005 | Validation error when Address is left blank | None | 1. Leave the Address field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the Address field before the form can be submitted | Medium |
| FORPAS-006 | Validation error when City is left blank | None | 1. Leave the City field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the City field before the form can be submitted | Medium |
| FORPAS-007 | Validation error when Zip Code is left blank | None | 1. Leave the Zip Code field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the Zip Code field before the form can be submitted | Medium |
| FORPAS-008 | Validation error when SSN is left blank | None | 1. Leave the SSN field empty 2. Fill in all other required fields with valid data 3. Click the 'Find My Login Info' button | The user is prompted to complete the SSN field before the form can be submitted | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-009 | Successful lookup with hyphenated Last Name and special characters in Address | A user record exists with a hyphenated last name and an apartment number in the address | 1. Enter 'Jane' into the First Name field 2. Enter 'Smith-Doe' into the Last Name field 3. Enter '123 Main St. #4B' into the Address field 4. Enter 'New York' into the City field 5. Select 'NY' from the State dropdown 6. Enter '10001' into the Zip Code field 7. Enter a valid SSN into the SSN field 8. Click the 'Find My Login Info' button | The page successfully matches the record and displays the recovery details | Low |

---

### Register

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-001 | Successful login with valid credentials | User has an existing account with valid username and password | 1. Enter a valid username into the Username field 2. Enter the corresponding valid password into the Password field 3. Click the Log In button | The user is successfully authenticated and granted access to their account. | High |
| REGIST-002 | Successful account registration with all valid fields | The registration form is loaded and empty | 1. Enter 'John' into the First Name field 2. Enter 'Doe' into the Last Name field 3. Enter '123 Maple St' into the Address field 4. Enter 'Springfield' into the City field 5. Enter 'IL' into the State field 6. Enter '62704' into the Zip Code field 7. Enter '555-0199' into the Phone # field 8. Enter '999-00-1234' into the SSN field 9. Enter 'johndoe_test' into the Username field 10. Enter 'Password123!' into the Password field 11. Enter 'Password123!' into the Confirm Password field 12. Click the Register button | The account is created and the user is automatically logged into the system | High |
| REGIST-006 | Verify Forgot login info link functionality | None | 1. Click the 'Forgot login info?' link | The user is redirected to the account recovery or password reset page. | Medium |
| REGIST-007 | Verify Register link functionality | None | 1. Click the 'Register' link | The user is redirected to the account registration page. | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-003 | Login failure with invalid username | None | 1. Enter a non-existent username into the Username field 2. Enter any password into the Password field 3. Click the Log In button | The system denies access and displays an authentication error message. | High |
| REGIST-004 | Login failure with incorrect password | User has an existing account | 1. Enter a valid username into the Username field 2. Enter an incorrect password into the Password field 3. Click the Log In button | The system denies access and displays an authentication error message. | High |
| REGIST-005 | Registration failure when Password and Confirm Password do not match | The registration form is loaded | 1. Fill all personal information fields with valid data 2. Enter 'User123' into the Username field 3. Enter 'Secret123' into the Password field 4. Enter 'Different456' into the Confirm Password field 5. Click the Register button | The system displays an error message indicating passwords do not match and does not create the account | High |
| REGIST-008 | Login failure with empty fields | None | 1. Leave the Username field empty 2. Leave the Password field empty 3. Click the Log In button | The system prevents submission or displays a validation message indicating fields are required. | Medium |
| REGIST-009 | Registration failure when mandatory First Name is empty | The registration form is loaded | 1. Leave the First Name field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating First Name is mandatory and does not create the account | Medium |
| REGIST-010 | Registration failure when mandatory SSN is empty | The registration form is loaded | 1. Leave the SSN field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating SSN is mandatory and does not create the account | Medium |
| REGIST-011 | Registration failure when all fields are left empty | The registration form is loaded | 1. Click the Register button without entering any data | The system displays validation errors for all mandatory fields and does not create the account | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-012 | Login with special characters in username | User has an account where the username contains special characters | 1. Enter the username containing special characters into the Username field 2. Enter the valid password into the Password field 3. Click the Log In button | The user is successfully authenticated and granted access to their account. | Low |
| REGIST-013 | Registration with special characters in name and address fields | The registration form is loaded | 1. Enter 'O'Connor-Smith' into the First Name field 2. Enter 'Doe-Ray' into the Last Name field 3. Enter 'Apt #4, 50/50 St.' into the Address field 4. Fill all other mandatory fields with valid data 5. Click the Register button | The account is successfully created and the user is automatically logged in | Low |
| REGIST-014 | Registration with long alphanumeric strings in all fields | The registration form is loaded | 1. Enter a 50-character string into the First Name field 2. Enter a 50-character string into the Last Name field 3. Enter a 100-character string into the Address field 4. Fill all other mandatory fields with valid data 5. Click the Register button | The account is successfully created and the user is automatically logged in | Low |

---

### Open New Account

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Successfully open a new Savings account with valid funding | User is on the Open New Account page with an existing account containing at least $100.00 | 1. Select 'Savings' from the account type dropdown 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button | A new Savings account is created with a unique account number and a $100.00 balance, deducted from the source account. | High |
| ONA-002 | Successfully open a new Checking account with valid funding | User is on the Open New Account page with an existing account containing at least $100.00 | 1. Select 'Checking' from the account type dropdown 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button | A new Checking account is created with a unique account number and a $100.00 balance, deducted from the source account. | High |
| ONA-003 | Verify transaction integrity of the $100.00 opening deposit | User is on the Open New Account page with a known balance in the source account | 1. Select 'Savings' from the account type dropdown 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button 4. Navigate to the account summary or transaction history | The source account shows a debit of exactly $100.00 and the new account shows a credit of exactly $100.00. | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-004 | Attempt to open account with insufficient funds in source account | User is on the Open New Account page with an existing account containing less than $100.00 | 1. Select 'Savings' from the account type dropdown 2. Select the existing account with insufficient funds from the funding source dropdown 3. Click the 'Open New Account' button | System displays an error message indicating insufficient funds and does not create a new account. | High |
| ONA-005 | Attempt to open account without selecting a funding source | User is on the Open New Account page | 1. Select 'Checking' from the account type dropdown 2. Leave the funding source dropdown unselected 3. Click the 'Open New Account' button | System displays a validation error requiring a funding source selection. | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-006 | Attempt to open account with exactly $100.00 in source account | User is on the Open New Account page with an existing account containing exactly $100.00 | 1. Select 'Savings' from the account type dropdown 2. Select the existing account with exactly $100.00 from the funding source dropdown 3. Click the 'Open New Account' button | The account is successfully created and the source account balance is reduced to $0.00. | Medium |

---

### Account Overview

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-001 | Verify Account Services sidebar links are present | User is logged in and viewing the Accounts Overview page | 1. Locate the 'Account Services' sidebar 2. Check for the presence of 'Open New Account' link 3. Check for the presence of 'Accounts Overview' link 4. Check for the presence of 'Transfer Funds' link 5. Check for the presence of 'Bill Pay' link 6. Check for the presence of 'Find Transactions' link 7. Check for the presence of 'Update Contact Info' link 8. Check for the presence of 'Request Loan' link 9. Check for the presence of 'Log Out' link | All specified links are visible within the Account Services sidebar | High |
| ACCOVE-002 | Verify Accounts Overview table structure and heading | User has at least one active account | 1. Verify the main content area heading is 'Accounts Overview' 2. Locate the accounts table 3. Verify table headers include 'Account', 'Balance', and 'Available Amount' | The page displays the correct heading and a table with columns for Account, Balance, and Available Amount | High |
| ACCOVE-003 | Verify account row data accuracy | User has multiple accounts with existing balances | 1. Identify each row in the accounts table 2. Verify each row contains a clickable Account number 3. Verify each row displays a Balance value 4. Verify each row displays an Available Amount value | Every account owned by the customer is listed with its specific number, balance, and available amount | High |
| ACCOVE-004 | Verify total balance calculation | User has multiple accounts with varying balances | 1. Sum the values in the 'Balance' column for all account rows 2. Locate the 'Total' row at the bottom of the table 3. Compare the calculated sum with the value displayed in the Total row | The Total row displays the correct combined sum of all account balances | High |
| ACCOVE-005 | Verify Accounts Overview is highlighted in sidebar | User is on the Accounts Overview page | 1. Locate the 'Accounts Overview' link in the sidebar 2. Inspect the CSS properties or class of the 'Accounts Overview' link | The 'Accounts Overview' link is visually highlighted or marked as active compared to other sidebar links | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-006 | Verify display for customer with a single account | User has exactly one account | 1. Count the number of account rows in the table 2. Check the Total balance value | The table shows one account row and the Total balance matches that single account's balance | Medium |

---

### Transfer Funds

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-001 | Successful fund transfer with valid inputs | User has at least two accounts with available balances | 1. Enter a valid numeric value in the Amount field 2. Select an account from the From account number dropdown 3. Select a different account from the To account number dropdown 4. Click the Transfer button | The system processes the transaction and displays a success confirmation | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-002 | Transfer fails when Amount field is empty | None | 1. Leave the Amount field empty 2. Select an account from the From account number dropdown 3. Select an account from the To account number dropdown 4. Click the Transfer button | The system prevents the transfer and displays a validation error for the Amount field | Medium |
| TRAFUN-003 | Transfer fails when From account is not selected | None | 1. Enter a valid numeric value in the Amount field 2. Ensure no account is selected in the From account number dropdown 3. Select an account from the To account number dropdown 4. Click the Transfer button | The system prevents the transfer and displays a validation error for the From account selection | Medium |
| TRAFUN-004 | Transfer fails when To account is not selected | None | 1. Enter a valid numeric value in the Amount field 2. Select an account from the From account number dropdown 3. Ensure no account is selected in the To account number dropdown 4. Click the Transfer button | The system prevents the transfer and displays a validation error for the To account selection | Medium |
| TRAFUN-005 | Transfer fails with non-numeric amount input | None | 1. Enter 'ABC' in the Amount field 2. Select an account from the From account number dropdown 3. Select an account from the To account number dropdown 4. Click the Transfer button | The system prevents the transfer and displays an invalid format error for the Amount field | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-006 | Transfer with minimum valid amount | User has at least two accounts with available balances | 1. Enter '0.01' in the Amount field 2. Select an account from the From account number dropdown 3. Select a different account from the To account number dropdown 4. Click the Transfer button | The system processes the transaction for the minimum amount successfully | Low |

---

### Bill Payments

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-001 | Successful payment submission with all valid fields | User is on the Send Payment page with a funded account available | 1. Enter 'John Doe' into the Payee Name field 2. Enter '123 Maple St' into the Address field 3. Enter 'Springfield' into the City field 4. Enter 'IL' into the State field 5. Enter '62704' into the Zip Code field 6. Enter '5551234567' into the Phone number field 7. Enter '987654321' into the Account number field 8. Enter '987654321' into the Verify Account number field 9. Enter '150.00' into the Amount field 10. Select the first available account from the From account number dropdown 11. Click the Send Payment button | A confirmation message appears indicating the transfer was successful | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-002 | Error validation when required fields are left empty | User is on the Send Payment page | 1. Leave all input fields empty 2. Click the Send Payment button | Validation errors are displayed for all required fields and no confirmation message appears | High |
| BILPAY-003 | Error validation when Account Number and Verify Account Number do not match | User is on the Send Payment page | 1. Enter 'John Doe' into the Payee Name field 2. Enter '123 Maple St' into the Address field 3. Enter 'Springfield' into the City field 4. Enter 'IL' into the State field 5. Enter '62704' into the Zip Code field 6. Enter '5551234567' into the Phone number field 7. Enter '12345' into the Account number field 8. Enter '54321' into the Verify Account number field 9. Enter '10.00' into the Amount field 10. Select an account from the From account number dropdown 11. Click the Send Payment button | An error message is displayed indicating that the account numbers do not match | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-004 | Payment submission with special characters in Payee Name | User is on the Send Payment page | 1. Enter 'O'Reilly-Smith & Co.' into the Payee Name field 2. Enter '123 Maple St' into the Address field 3. Enter 'Springfield' into the City field 4. Enter 'IL' into the State field 5. Enter '62704' into the Zip Code field 6. Enter '5551234567' into the Phone number field 7. Enter '987654321' into the Account number field 8. Enter '987654321' into the Verify Account number field 9. Enter '5.00' into the Amount field 10. Select an account from the From account number dropdown 11. Click the Send Payment button | A confirmation message appears indicating the transfer was successful | Low |
| BILPAY-005 | Verify Zip Code field accepts alphanumeric characters | User is on the Send Payment page | 1. Enter 'Jane Doe' into the Payee Name field 2. Enter '456 Oak Ave' into the Address field 3. Enter 'Toronto' into the City field 4. Enter 'ON' into the State field 5. Enter 'M5H 2N2' into the Zip Code field 6. Enter '5559876543' into the Phone number field 7. Enter '112233' into the Account number field 8. Enter '112233' into the Verify Account number field 9. Enter '25.50' into the Amount field 10. Select an account from the From account number dropdown 11. Click the Send Payment button | A confirmation message appears indicating the transfer was successful | Low |

---

### Find Transaction

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-001 | Search for transaction with valid Transaction ID | A transaction with ID 'TXN12345' exists for the selected account | 1. Select an account from the Account dropdown 2. Enter 'TXN12345' into the Transaction ID input field 3. Click the Find Transactions button | The results table displays the matching transaction showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-002 | Search for transactions with valid single date | The user is on the Find Transaction page with existing transaction data for the selected date | 1. Select an account from the Account dropdown 2. Enter a valid date in 'MM-DD-YYYY' format into the Find by Date field 3. Click the Find Transactions button | The results table displays transactions matching the selected date with Transaction ID, Date, Description, and Amount columns | High |
| FINTRA-003 | Successful search by valid date range | User is on the Find Transaction page with existing transactions in the system | 1. Select an account from the Account dropdown 2. Enter '01-01-2023' into the Start Date field 3. Enter '01-31-2023' into the End Date field 4. Click the 'Find Transactions' button | A results table is displayed showing Transaction ID, Date, Description, and Amount for all transactions within the specified range. | High |
| FINTRA-004 | Search for transaction with valid amount and account | At least one transaction exists for the selected account with a specific amount | 1. Select a valid account from the 'Account' dropdown 2. Enter a valid numeric value in the 'Find by Amount' field 3. Click the 'Find Transactions' button | The results table displays matching transactions showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-005 | Search for transaction with amount containing decimals | A transaction exists with a decimal value (e.g., 100.50) | 1. Select a valid account from the 'Account' dropdown 2. Enter a decimal value (e.g., '100.50') in the 'Find by Amount' field 3. Click the 'Find Transactions' button | The results table displays the transaction matching the exact decimal amount | High |
| FINTRA-007 | Search with single day date range | User is on the Find Transaction page | 1. Select an account from the Account dropdown 2. Enter '05-15-2023' into the Start Date field 3. Enter '05-15-2023' into the End Date field 4. Click the 'Find Transactions' button | The system returns transactions that occurred specifically on 05-15-2023 in the results table. | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-006 | Validation error on empty required fields | User is on the Find Transaction page | 1. Leave the Account, Start Date, and End Date fields empty 2. Click the 'Find Transactions' button | Inline validation messages appear next to the Account, Start Date, and End Date fields indicating they are required. | High |
| FINTRA-008 | Search with empty Account field | None | 1. Leave the Account dropdown unselected 2. Enter 'TXN12345' into the Transaction ID input field 3. Click the Find Transactions button | An inline validation message appears next to the Account field indicating it is required | Medium |
| FINTRA-009 | Search with empty Transaction ID field | None | 1. Select an account from the Account dropdown 2. Clear any text from the Transaction ID input field 3. Click the Find Transactions button | An inline validation message appears next to the Transaction ID field indicating it is required | Medium |
| FINTRA-010 | Search with empty Account field | None | 1. Leave the Account dropdown unselected 2. Enter a valid date in 'MM-DD-YYYY' format into the Find by Date field 3. Click the Find Transactions button | An inline validation message appears next to the Account field indicating it is required | Medium |
| FINTRA-011 | Search with empty Date field | None | 1. Select an account from the Account dropdown 2. Leave the Find by Date field empty 3. Click the Find Transactions button | An inline validation message appears next to the Find by Date field indicating it is required | Medium |
| FINTRA-012 | Search with invalid date format | None | 1. Select an account from the Account dropdown 2. Enter a date in 'YYYY-MM-DD' format into the Find by Date field 3. Click the Find Transactions button | An inline validation message appears next to the Find by Date field indicating the format must be MM-DD-YYYY | Medium |
| FINTRA-013 | Search with non-numeric characters in date field | None | 1. Select an account from the Account dropdown 2. Enter 'AA-BB-CCCC' into the Find by Date field 3. Click the Find Transactions button | An inline validation message appears next to the Find by Date field indicating an invalid date format | Medium |
| FINTRA-014 | Validation error for invalid date format | User is on the Find Transaction page | 1. Select an account from the Account dropdown 2. Enter '2023/01/01' into the Start Date field 3. Enter '2023/01/31' into the End Date field 4. Click the 'Find Transactions' button | Inline validation messages appear next to the date fields indicating the required MM-DD-YYYY format. | Medium |
| FINTRA-015 | Validation error for non-numeric date characters | User is on the Find Transaction page | 1. Select an account from the Account dropdown 2. Enter 'Jan-01-2023' into the Start Date field 3. Enter 'Jan-31-2023' into the End Date field 4. Click the 'Find Transactions' button | Inline validation messages appear next to the date fields indicating the input is invalid. | Medium |
| FINTRA-016 | Validation error when Account is not selected | None | 1. Leave the 'Account' dropdown unselected or at its default empty state 2. Enter a valid numeric value in the 'Find by Amount' field 3. Click the 'Find Transactions' button | An inline validation message appears next to the Account field indicating it is required | Medium |
| FINTRA-017 | Validation error when Amount field is empty | None | 1. Select a valid account from the 'Account' dropdown 2. Leave the 'Find by Amount' field empty 3. Click the 'Find Transactions' button | An inline validation message appears next to the Find by Amount field indicating it is required | Medium |
| FINTRA-018 | Validation error for non-numeric input in Amount field | None | 1. Select a valid account from the 'Account' dropdown 2. Enter non-numeric characters (e.g., 'abc') in the 'Find by Amount' field 3. Click the 'Find Transactions' button | An inline validation message appears next to the Find by Amount field indicating invalid input | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-019 | Search with non-existent Transaction ID | None | 1. Select an account from the Account dropdown 2. Enter 'NON_EXISTENT_999' into the Transaction ID input field 3. Click the Find Transactions button | The results table is empty or displays a message indicating no transactions were found | Medium |
| FINTRA-020 | Search with Transaction ID containing special characters | A transaction with ID 'TXN-@#$123' exists for the selected account | 1. Select an account from the Account dropdown 2. Enter 'TXN-@#$123' into the Transaction ID input field 3. Click the Find Transactions button | The results table displays the matching transaction with the special character ID | Low |
| FINTRA-021 | Search for a date with no matching transactions | The user is on the Find Transaction page and selects a date known to have no transaction history | 1. Select an account from the Account dropdown 2. Enter a valid date in 'MM-DD-YYYY' format that has no records 3. Click the Find Transactions button | The results table is empty or displays a message indicating no transactions were found for the selected date | Low |
| FINTRA-022 | Search with date range containing no transactions | User is on the Find Transaction page | 1. Select an account from the Account dropdown 2. Enter '01-01-1900' into the Start Date field 3. Enter '01-01-1901' into the End Date field 4. Click the 'Find Transactions' button | The system indicates that no transactions were found for the selected criteria (e.g., an empty table or a 'no results' message). | Low |
| FINTRA-023 | Search with leap year date | User is on the Find Transaction page | 1. Select an account from the Account dropdown 2. Enter '02-29-2024' into the Start Date field 3. Enter '02-29-2024' into the End Date field 4. Click the 'Find Transactions' button | The system accepts the valid leap year date and returns matching transactions in the results table. | Low |
| FINTRA-024 | Search for an amount that has no matching transactions | No transactions exist for the selected account with the amount '999999.99' | 1. Select a valid account from the 'Account' dropdown 2. Enter '999999.99' in the 'Find by Amount' field 3. Click the 'Find Transactions' button | The system indicates no matching transactions were found, and the results table remains empty or hidden | Low |
| FINTRA-025 | Search using a zero amount | None | 1. Select a valid account from the 'Account' dropdown 2. Enter '0' in the 'Find by Amount' field 3. Click the 'Find Transactions' button | The system processes the request and either returns matching $0.00 transactions or shows no results if none exist | Low |

---

### Update Profile

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-001 | Update profile with all valid fields | The Update Profile page is loaded with existing user data | 1. Enter 'John' into the First Name field 2. Enter 'Doe' into the Last Name field 3. Enter '123 Maple Street' into the Address field 4. Enter 'Springfield' into the City field 5. Enter 'Illinois' into the State field 6. Enter '62704' into the Zip Code field 7. Enter '555-0199' into the Phone number field 8. Click the Update Profile button | A confirmation message is displayed indicating the profile was successfully updated | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-002 | Submit form with empty First Name | The Update Profile page is loaded | 1. Clear the First Name field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that First Name is required | Medium |
| UPDPRO-003 | Submit form with empty Last Name | The Update Profile page is loaded | 1. Clear the Last Name field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that Last Name is required | Medium |
| UPDPRO-004 | Submit form with empty Address | The Update Profile page is loaded | 1. Clear the Address field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that Address is required | Medium |
| UPDPRO-005 | Submit form with empty City | The Update Profile page is loaded | 1. Clear the City field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that City is required | Medium |
| UPDPRO-006 | Submit form with empty State | The Update Profile page is loaded | 1. Clear the State field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that State is required | Medium |
| UPDPRO-007 | Submit form with empty Zip Code | The Update Profile page is loaded | 1. Clear the Zip Code field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that Zip Code is required | Medium |
| UPDPRO-008 | Submit form with empty Phone number | The Update Profile page is loaded | 1. Clear the Phone number field 2. Fill all other required fields with valid data 3. Click the Update Profile button | An error message is displayed indicating that Phone number is required | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-009 | Update profile using special characters in Name fields | The Update Profile page is loaded | 1. Enter 'Jean-Luc' into the First Name field 2. Enter 'O'Reilly' into the Last Name field 3. Fill all other required fields with valid data 4. Click the Update Profile button | A confirmation message is displayed indicating the profile was successfully updated | Low |
| UPDPRO-010 | Update profile with alphanumeric Zip Code | The Update Profile page is loaded | 1. Enter 'K1A 0B1' into the Zip Code field 2. Fill all other required fields with valid data 3. Click the Update Profile button | A confirmation message is displayed indicating the profile was successfully updated | Low |

---

### Request Loan

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-001 | Successful loan application with all valid fields | User is on the Request Loan page with a valid account available | 1. Enter a valid numeric value in the Loan Amount field 2. Enter a valid numeric value in the Down Payment field 3. Select a valid account from the From account number dropdown 4. Click the Apply Now button | The loan application is approved and a success message is displayed | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-002 | Loan application fails when Loan Amount is blank | User is on the Request Loan page | 1. Leave the Loan Amount field empty 2. Enter a valid numeric value in the Down Payment field 3. Select a valid account from the From account number dropdown 4. Click the Apply Now button | The process is not completed and a validation error for Loan Amount is displayed | Medium |
| REQLOA-003 | Loan application fails when Down Payment is blank | User is on the Request Loan page | 1. Enter a valid numeric value in the Loan Amount field 2. Leave the Down Payment field empty 3. Select a valid account from the From account number dropdown 4. Click the Apply Now button | The process is not completed and a validation error for Down Payment is displayed | Medium |
| REQLOA-004 | Loan application fails when From account number is not selected | User is on the Request Loan page | 1. Enter a valid numeric value in the Loan Amount field 2. Enter a valid numeric value in the Down Payment field 3. Ensure no account is selected in the From account number dropdown 4. Click the Apply Now button | The process is not completed and a validation error for account selection is displayed | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-005 | Loan application with zero down payment | User is on the Request Loan page | 1. Enter a valid numeric value in the Loan Amount field 2. Enter '0' in the Down Payment field 3. Select a valid account from the From account number dropdown 4. Click the Apply Now button | The application is processed based on the business rules for zero down payment | Low |
| REQLOA-006 | Loan application with minimum valid loan amount | User is on the Request Loan page | 1. Enter '1' in the Loan Amount field 2. Enter '1' in the Down Payment field 3. Select a valid account from the From account number dropdown 4. Click the Apply Now button | The application is processed successfully for the minimum amount | Low |

---

### Logout

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Successful logout from the application | User is currently logged into the application and viewing a page with the logout function available | 1. Click on the logout button/link | The user is redirected to the login page and the session is terminated. | High |
| LOGOUT-002 | Verify session invalidation after logout | User has successfully clicked the logout button and is on the login page | 1. Click the browser's 'Back' button to attempt to return to the previous authenticated page | The user is prevented from viewing authenticated content and is redirected back to the login page or shown an unauthorized message. | High |
| LOGOUT-003 | Verify removal of sensitive account data from the UI | User is logged in and account-specific information (e.g., username, profile pic) is visible | 1. Click on the logout button/link 2. Observe the resulting login page for any cached user-specific data | The login page loads without displaying any previous account information, usernames, or sensitive session data. | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-004 | Verify logout functionality across multiple open tabs | User has the application open in two different browser tabs and is logged in | 1. Click the logout button in Tab 1 2. Switch to Tab 2 3. Refresh the page in Tab 2 | Tab 2 redirects the user to the login page, confirming the session was cleared globally. | Medium |

---

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /index.htm | No | 7 |
| Forgot Password | /lookup.htm | No | 9 |
| Register | /register.htm | No | 14 |
| Open New Account | /openaccount.htm | Yes | 6 |
| Account Overview | /overview.htm | Yes | 6 |
| Transfer Funds | /transfer.htm | Yes | 6 |
| Bill Payments | /billpay.htm | Yes | 5 |
| Find Transaction | /findtrans.htm | Yes | 25 |
| Update Profile | /updateprofile.htm | Yes | 10 |
| Request Loan | /requestloan.htm | Yes | 6 |
| Logout | /logout.htm | Yes | 4 |
