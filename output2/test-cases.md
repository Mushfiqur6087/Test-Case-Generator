# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-01-06T06:24:40.285749

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 108 |

### By Type

| Type | Count |
|------|-------|
| Positive | 32 |
| Negative | 55 |
| Edge Case | 21 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 28 |
| Medium | 62 |
| Low | 18 |

### Verification Coverage

| Metric | Count |
|--------|-------|
| Positive Tests | 32 |
| Tests that Write State | 20 |
| Tests that Read State | 27 |
| Tests with Verification Links | 14 |
| Tests with Pre-Verification Steps | 20 |
| Tests with Post-Verification Steps | 20 |

**State Categories:**

- **Written:** loan_status, transaction_history, account_list, account_balance, user_profile, search_results, session_status
- **Read:** loan_status, transaction_history, account_list, account_balance, user_profile, search_results, session_status, transfer_details

---

## Test Cases

### Login

#### Functional Tests

**LOGIN-001** - Successful login using valid username

- **Priority:** High
- **Preconditions:** A registered account exists with a valid username and password

- **Reads State:** user_profile
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Verify the user is currently on the Login page
2. Confirm that no active session exists (no 'Logout' or 'Dashboard' links visible)

**Test Steps:**
1. Enter a valid username into the 'username' field
2. Enter the correct password into the 'Password' field
3. Click the 'Log In' button

**Post-Verification Steps:**
1. Verify the URL has changed to the account dashboard
2. Confirm the presence of a 'Logout' button or user-specific greeting
3. Verify session cookies are present in the browser

**Expected Result:** The user is redirected to the account dashboard

---

**LOGIN-002** - Successful login using valid email address

- **Priority:** High
- **Preconditions:** A registered account exists with a valid email and password

- **Reads State:** user_profile
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Verify the user is currently on the Login page
2. Confirm that no active session exists

**Test Steps:**
1. Enter a valid email address into the 'username' field
2. Enter the correct password into the 'Password' field
3. Click the 'Log In' button

**Post-Verification Steps:**
1. Verify the URL has changed to the account dashboard
2. Confirm the dashboard displays information relevant to the account associated with the email
3. Verify session_status is updated to 'Authenticated'

**Expected Result:** The user is redirected to the account dashboard

---

**LOGIN-004** - Correction of credentials after initial failure

- **Priority:** Medium
- **Preconditions:** A registered account exists

- **Reads State:** user_profile
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Verify the user is on the Login page
2. Confirm no active session exists
3. Note the initial state of the login form (empty fields)

**Test Steps:**
1. Enter an incorrect password for a valid username
2. Click the 'Log In' button
3. Observe the error message
4. Clear the 'Password' field and enter the correct password
5. Click the 'Log In' button

**Post-Verification Steps:**
1. Verify that the error message from the first attempt is no longer visible
2. Verify the URL has changed to the account dashboard after the second attempt
3. Confirm session_status is 'Authenticated'

**Expected Result:** The user is successfully redirected to the account dashboard after the second attempt

---

**LOGIN-005** - Verify navigation to Forgot Login Info page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click the 'Forgot login info?' link

**Expected Result:** The browser navigates away from the login page to the password recovery workflow

---

**LOGIN-006** - Verify navigation to Registration page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click the 'Register' button

**Expected Result:** The browser navigates away from the login page to the account registration workflow

---

#### Negative Tests

**LOGIN-003** - Login failure with invalid credentials

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter an unregistered username into the 'username' field
2. Enter a random string into the 'Password' field
3. Click the 'Log In' button

**Expected Result:** An error message is displayed and the input fields remain populated with the entered values

---

**LOGIN-007** - Login failure with empty fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Clear the 'username' field
2. Clear the 'Password' field
3. Click the 'Log In' button

**Expected Result:** An error message is displayed indicating that fields are required

---

#### Boundary/Edge Case Tests

**LOGIN-008** - Login with special characters in username

- **Priority:** Low
- **Preconditions:** An account exists with special characters in the username (e.g., user+test@domain.com)

**Test Steps:**
1. Enter the username containing special characters into the 'username' field
2. Enter the correct password into the 'Password' field
3. Click the 'Log In' button

**Expected Result:** The user is redirected to the account dashboard

---

---

### Forgot Password

#### Functional Tests

**FORPAS-001** - Successful customer lookup with valid details

- **Priority:** High
- **Preconditions:** A valid customer record exists in the system matching the input data

- **Reads State:** user_profile

**Test Steps:**
1. Enter a valid first name into the 'First Name' field
2. Enter a valid last name into the 'Last Name' field
3. Enter a valid street address into the 'Address' field
4. Enter a valid city into the 'City' field
5. Select a valid state from the 'State' dropdown
6. Enter a valid 5-digit zip code into the 'Zip Code' field
7. Enter a valid social security number into the 'SSN' field
8. Click the 'Find My Login Info' button

**Expected Result:** The page displays the appropriate recovery details for the matching account

---

#### Negative Tests

**FORPAS-002** - Error message displayed when no matching record is found

- **Priority:** High
- **Preconditions:** No customer record exists with the provided combination of details

**Test Steps:**
1. Enter 'NonExistent' into the 'First Name' field
2. Enter 'User' into the 'Last Name' field
3. Enter '999 Unknown St' into the 'Address' field
4. Enter 'Anytown' into the 'City' field
5. Select 'CA' from the 'State' dropdown
6. Enter '00000' into the 'Zip Code' field
7. Enter '000-00-0000' into the 'SSN' field
8. Click the 'Find My Login Info' button

**Expected Result:** The page displays an error message indicating that no matching record was found

---

**FORPAS-003** - Validation error when First Name is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'First Name' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'First Name' field

---

**FORPAS-004** - Validation error when Last Name is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'Last Name' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'Last Name' field

---

**FORPAS-005** - Validation error when Address is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'Address' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'Address' field

---

**FORPAS-006** - Validation error when City is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'City' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'City' field

---

**FORPAS-007** - Validation error when Zip Code is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'Zip Code' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'Zip Code' field

---

**FORPAS-008** - Validation error when SSN is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'SSN' field empty
2. Fill all other required fields with valid data
3. Click the 'Find My Login Info' button

**Expected Result:** A validation prompt appears requesting the user to complete the 'SSN' field

---

#### Boundary/Edge Case Tests

**FORPAS-009** - Customer lookup with special characters in name fields

- **Priority:** Low
- **Preconditions:** A customer record exists with a hyphenated name (e.g., Jane Smith-Doe)

**Test Steps:**
1. Enter 'Jane' into the 'First Name' field
2. Enter 'Smith-Doe' into the 'Last Name' field
3. Fill all other address and SSN fields with matching valid data
4. Click the 'Find My Login Info' button

**Expected Result:** The page successfully finds the record and displays recovery details

---

---

### Register

#### Functional Tests

**REGIST-001** - Successful login with valid credentials

- **Priority:** High
- **Preconditions:** A user account exists with valid username and password

- **Reads State:** user_profile
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Verify the user is currently on the Login page
2. Confirm that no active session exists (e.g., no 'Logout' button or 'Dashboard' link is visible)

**Test Steps:**
1. Enter a valid username into the Username field
2. Enter the correct password into the Password field
3. Click the Log In button

**Post-Verification Steps:**
1. Verify the URL has changed to the account dashboard
2. Confirm the presence of a 'Logout' button or user-specific greeting
3. Check that the session cookie or token is present in the browser storage

**Expected Result:** The user is successfully authenticated and redirected to their account dashboard

---

**REGIST-002** - Successful account registration with all valid fields

- **Priority:** High
- **Preconditions:** The registration form is loaded and empty

- **Writes State:** user_profile, session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGIN-004, LOGOUT-001, REQLOA-001, UPDPRO-001, LOGOUT-003, LOGIN-002, ONA-003, LOGIN-001, FORPAS-001, LOGOUT-002, ONA-001, REGIST-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to the Registration page
2. Verify that the email/username intended for registration does not already exist in the system (if searchable)

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple St' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'IL' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '555-0199' into the Phone # field
8. Enter '999-00-1111' into the SSN field
9. Enter 'johndoe_unique' into the Username field
10. Enter 'Password123' into the Password field
11. Enter 'Password123' into the Confirm Password field
12. Click the Register button

**Post-Verification Steps:**
1. Verify the user is redirected to the dashboard or a 'Registration Successful' page
2. Confirm the session_status is active (user is logged in)
3. Navigate to the Profile/Account settings page
4. Verify that the user_profile fields (First Name, Last Name, Address) match the data entered during registration

**Expected Result:** The account is created and the user is automatically redirected to the logged-in state/dashboard.

---

**REGIST-005** - Verify 'Forgot login info?' link functionality

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click the 'Forgot login info?' link

**Expected Result:** The user is redirected to the password recovery or account retrieval page

---

**REGIST-006** - Verify 'Register' link functionality

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click the 'Register' link

**Expected Result:** The user is redirected to the account registration page

---

#### Negative Tests

**REGIST-003** - Login attempt with invalid username

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a non-existent username into the Username field
2. Enter any password into the Password field
3. Click the Log In button

**Expected Result:** The system displays an error message indicating invalid login credentials

---

**REGIST-004** - Login attempt with incorrect password

- **Priority:** High
- **Preconditions:** A user account exists with a valid username

**Test Steps:**
1. Enter a valid username into the Username field
2. Enter an incorrect password into the Password field
3. Click the Log In button

**Expected Result:** The system displays an error message indicating invalid login credentials

---

**REGIST-007** - Login attempt with empty credentials

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Username field empty
2. Leave the Password field empty
3. Click the Log In button

**Expected Result:** The system displays an error message indicating that credentials are required

---

**REGIST-008** - Registration fails when First Name is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the First Name field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that First Name is mandatory and no account is created.

---

**REGIST-009** - Registration fails when Last Name is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Last Name field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Last Name is mandatory and no account is created.

---

**REGIST-010** - Registration fails when Address is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Address field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Address is mandatory and no account is created.

---

**REGIST-011** - Registration fails when City is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the City field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that City is mandatory and no account is created.

---

**REGIST-012** - Registration fails when State is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the State field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that State is mandatory and no account is created.

---

**REGIST-013** - Registration fails when Zip Code is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Zip Code field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Zip Code is mandatory and no account is created.

---

**REGIST-014** - Registration fails when Phone # is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Phone # field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Phone # is mandatory and no account is created.

---

**REGIST-015** - Registration fails when SSN is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the SSN field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that SSN is mandatory and no account is created.

---

**REGIST-016** - Registration fails when Username is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Username field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Username is mandatory and no account is created.

---

**REGIST-017** - Registration fails when Password is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Password field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Password is mandatory and no account is created.

---

**REGIST-018** - Registration fails when Confirm Password is empty

- **Priority:** Medium
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Leave the Confirm Password field empty
2. Fill all other mandatory fields with valid data
3. Click the Register button

**Expected Result:** An error message is displayed indicating that Confirm Password is mandatory and no account is created.

---

#### Boundary/Edge Case Tests

**REGIST-019** - Login with username containing special characters

- **Priority:** Low
- **Preconditions:** A user account exists with a username containing special characters (e.g., user_name@123)

**Test Steps:**
1. Enter the username with special characters into the Username field
2. Enter the correct password into the Password field
3. Click the Log In button

**Expected Result:** The user is successfully authenticated and logged into the account

---

**REGIST-020** - Registration with special characters in fields

- **Priority:** Low
- **Preconditions:** The registration form is loaded

**Test Steps:**
1. Enter 'J0hn-Baptiste' into the First Name field
2. Enter 'O'Reilly' into the Last Name field
3. Enter '123/B @ Apt!' into the Address field
4. Enter 'St. Louis' into the City field
5. Enter 'MO' into the State field
6. Enter '63101-1234' into the Zip Code field
7. Enter '+1(555)000' into the Phone # field
8. Enter 'AAA-GG-SSSS' into the SSN field
9. Enter 'user_@.123' into the Username field
10. Enter 'P@ssword!' into the Password field
11. Enter 'P@ssword!' into the Confirm Password field
12. Click the Register button

**Expected Result:** The account is successfully created and the user is logged in, as no format constraints are imposed.

---

---

### Open New Account

#### Functional Tests

**ONA-001** - Successfully open a new Savings account with valid funding

- **Priority:** High
- **Preconditions:** User is on the Open New Account page with at least one existing account containing $100.00 or more

- **Reads State:** session_status, account_list
- **Writes State:** account_list, account_balance, transaction_history
- **Verified By:** BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-002, FINTRA-006, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note the current number of accounts in the account_list
3. Note the current balance of the funding source account

**Test Steps:**
1. Select 'Savings' from the account type dropdown
2. Select an existing account from the funding source dropdown
3. Click the 'Open New Account' button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify a new Savings account exists in the account_list
3. Verify the funding source account balance has decreased by $100.00
4. Click on the new account and verify the initial balance is $100.00

**Expected Result:** A new Savings account is created with a unique account number and a $100.00 balance, deducted from the source account.

---

**ONA-002** - Successfully open a new Checking account with valid funding

- **Priority:** High
- **Preconditions:** User is on the Open New Account page with at least one existing account containing $100.00 or more

- **Reads State:** session_status, account_list
- **Writes State:** account_list, account_balance, transaction_history
- **Verified By:** BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-001, FINTRA-006, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note the current number of accounts in the account_list
3. Note the current balance of the funding source account

**Test Steps:**
1. Select 'Checking' from the account type dropdown
2. Select an existing account from the funding source dropdown
3. Click the 'Open New Account' button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify a new Checking account exists in the account_list
3. Verify the funding source account balance has decreased by $100.00
4. Click on the new account and verify the initial balance is $100.00

**Expected Result:** A new Checking account is created with a unique account number and a $100.00 balance, deducted from the source account.

---

**ONA-003** - Verify transaction integrity after account creation

- **Priority:** High
- **Preconditions:** User is on the Open New Account page with a known balance in the source account

- **Reads State:** session_status, account_list, account_balance, transaction_history
- **Writes State:** account_list, account_balance, transaction_history
- **Verified By:** BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-001, ONA-002, FINTRA-006, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note the current balance of the funding source account
3. Click on the funding source account and note the latest entry in transaction_history

**Test Steps:**
1. Select 'Savings' from the account type dropdown
2. Select an existing account from the funding source dropdown
3. Click the 'Open New Account' button
4. Navigate to the account details of the source account

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify the funding source account balance is exactly $100.00 less than the initial note
3. Click on the funding source account
4. Verify a new debit transaction of $100.00 appears in the transaction_history

**Expected Result:** The source account shows a debit transaction of exactly $100.00 and the balance is updated accordingly.

---

#### Negative Tests

**ONA-004** - Attempt to open account with insufficient funds in source account

- **Priority:** High
- **Preconditions:** User is on the Open New Account page and selects a source account with a balance less than $100.00

**Test Steps:**
1. Select 'Savings' from the account type dropdown
2. Select the source account with insufficient funds
3. Click the 'Open New Account' button

**Expected Result:** The system displays an error message indicating insufficient funds and does not create a new account.

---

**ONA-005** - Attempt to open account without selecting an account type

- **Priority:** Medium
- **Preconditions:** User is on the Open New Account page

**Test Steps:**
1. Leave the account type selection empty
2. Select an existing account from the funding source dropdown
3. Click the 'Open New Account' button

**Expected Result:** The system displays a validation error requiring an account type selection.

---

**ONA-006** - Attempt to open account without selecting a funding source

- **Priority:** Medium
- **Preconditions:** User is on the Open New Account page

**Test Steps:**
1. Select 'Checking' from the account type dropdown
2. Leave the funding source selection empty
3. Click the 'Open New Account' button

**Expected Result:** The system displays a validation error requiring a funding source selection.

---

#### Boundary/Edge Case Tests

**ONA-007** - Verify unique account number generation for consecutive requests

- **Priority:** Medium
- **Preconditions:** User is on the Open New Account page

**Test Steps:**
1. Open a new Savings account
2. Note the generated account number
3. Open a second Savings account using the same funding source
4. Note the second generated account number

**Expected Result:** The system generates two different, unique account numbers for both new accounts.

---

---

### Account Overview

#### Functional Tests

**ACCOVE-001** - Verify Account Overview page layout and heading

- **Priority:** High
- **Preconditions:** User is logged into the application

- **Reads State:** session_status

**Test Steps:**
1. Observe the main content area heading
2. Check the sidebar navigation menu for the active state
3. Verify the presence of the account summary table

**Expected Result:** The main content area displays the heading 'Accounts Overview' and the 'Accounts Overview' link in the sidebar is highlighted.

---

**ACCOVE-002** - Verify account summary table columns and data population

- **Priority:** High
- **Preconditions:** User has one or more active accounts

- **Reads State:** account_list, account_balance

**Test Steps:**
1. Locate the account summary table
2. Verify the table headers
3. Check that each row contains data for Account, Balance, and Available Amount

**Expected Result:** The table displays columns for Account, Balance, and Available Amount with data populated for every account owned by the customer.

---

**ACCOVE-003** - Verify total balance calculation logic

- **Priority:** High
- **Preconditions:** User has multiple accounts with varying balances

- **Reads State:** account_balance

**Test Steps:**
1. Sum the values in the 'Balance' column for all account rows
2. Locate the 'Total Balance' value at the bottom of the table
3. Compare the calculated sum with the displayed total

**Expected Result:** The displayed total balance matches the mathematical sum of all individual account balances.

---

**ACCOVE-004** - Verify currency formatting for balances

- **Priority:** Medium
- **Preconditions:** User has accounts with non-zero balances

- **Reads State:** account_balance

**Test Steps:**
1. Examine the 'Balance' and 'Available Amount' values in the table
2. Examine the 'Total Balance' value

**Expected Result:** All balance values are formatted as currency (e.g., including dollar signs and two decimal places).

---

#### Boundary/Edge Case Tests

**ACCOVE-005** - Verify display for a customer with a single account

- **Priority:** Medium
- **Preconditions:** User has exactly one account

**Test Steps:**
1. Count the number of account rows in the table
2. Verify the total balance row

**Expected Result:** The table shows exactly one account row and the total balance matches that single account's balance.

---

**ACCOVE-006** - Verify display for a customer with zero accounts

- **Priority:** Medium
- **Preconditions:** User has no open accounts

**Test Steps:**
1. Observe the account summary table area
2. Check for the total balance row

**Expected Result:** The table shows no account rows and the total balance is displayed as $0.00.

---

---

### Transfer Funds

#### Functional Tests

**TRAFUN-001** - Successful fund transfer between two valid accounts

- **Priority:** High
- **Preconditions:** User is on the Transfer Funds page with at least two accounts available

- **Reads State:** session_status, account_list, account_balance, transfer_details
- **Writes State:** account_balance, transaction_history
- **Verified By:** BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Record the current balance of the source account
3. Record the current balance of the destination account
4. Navigate to Transaction History for both accounts and note the most recent entries

**Test Steps:**
1. Enter a valid numeric value in the Amount field
2. Select an account from the From account number dropdown
3. Select a different account from the To account number dropdown
4. Click the Transfer button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify source account balance has decreased by the transfer amount
3. Verify destination account balance has increased by the transfer amount
4. Navigate to Transaction History and verify a new entry exists for the transfer with correct amount and date

**Expected Result:** The system processes the transaction and displays a success confirmation

---

#### Negative Tests

**TRAFUN-002** - Transfer fails when Amount field is empty

- **Priority:** Medium
- **Preconditions:** User is on the Transfer Funds page

**Test Steps:**
1. Leave the Amount field empty
2. Select an account from the From account number dropdown
3. Select an account from the To account number dropdown
4. Click the Transfer button

**Expected Result:** The system prevents the transfer and displays a validation error for the Amount field

---

**TRAFUN-003** - Transfer fails when From account is not selected

- **Priority:** Medium
- **Preconditions:** User is on the Transfer Funds page

**Test Steps:**
1. Enter a valid numeric value in the Amount field
2. Leave the From account number dropdown at its default/unselected state
3. Select an account from the To account number dropdown
4. Click the Transfer button

**Expected Result:** The system prevents the transfer and displays a validation error for the From account selection

---

**TRAFUN-004** - Transfer fails when To account is not selected

- **Priority:** Medium
- **Preconditions:** User is on the Transfer Funds page

**Test Steps:**
1. Enter a valid numeric value in the Amount field
2. Select an account from the From account number dropdown
3. Leave the To account number dropdown at its default/unselected state
4. Click the Transfer button

**Expected Result:** The system prevents the transfer and displays a validation error for the To account selection

---

#### Boundary/Edge Case Tests

**TRAFUN-005** - Transfer with minimum valid amount

- **Priority:** Low
- **Preconditions:** User is on the Transfer Funds page

**Test Steps:**
1. Enter '0.01' in the Amount field
2. Select an account from the From account number dropdown
3. Select an account from the To account number dropdown
4. Click the Transfer button

**Expected Result:** The system processes the transaction for the minimum amount successfully

---

**TRAFUN-006** - Transfer between the same From and To account

- **Priority:** Low
- **Preconditions:** User is on the Transfer Funds page

**Test Steps:**
1. Enter a valid numeric value in the Amount field
2. Select Account A from the From account number dropdown
3. Select Account A from the To account number dropdown
4. Click the Transfer button

**Expected Result:** The system either processes the transfer or displays a business rule validation error regarding identical accounts

---

---

### Bill Payments

#### Functional Tests

**BILPAY-001** - Successful bill payment with all valid fields

- **Priority:** High
- **Preconditions:** User is on the Bill Payment form with a valid balance in the source account

- **Reads State:** session_status, account_list, account_balance
- **Writes State:** account_balance, transaction_history
- **Verified By:** ACCOVE-002, FINTRA-003, REQLOA-001, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Record the current balance of the source account
3. Navigate to Transaction History
4. Note the most recent transaction entry

**Test Steps:**
1. Enter 'John Doe' into the Payee Name field
2. Enter '123 Maple St' into the Address field
3. Enter 'Springfield' into the City field
4. Enter 'IL' into the State field
5. Enter '62704' into the Zip Code field
6. Enter '555-0199' into the Phone number field
7. Enter '987654321' into the Account number field
8. Enter '987654321' into the Verify Account number field
9. Enter '150.00' into the Amount field
10. Select a valid account from the From account number dropdown
11. Click the Send Payment button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify the source account balance has decreased by the payment amount
3. Navigate to Transaction History
4. Verify a new entry exists for the payment to 'John Doe'
5. Confirm the transaction details match the payment amount and date

**Expected Result:** A confirmation message appears indicating the successful transfer

---

#### Negative Tests

**BILPAY-002** - Error validation when required fields are empty

- **Priority:** High
- **Preconditions:** User is on the Bill Payment form

**Test Steps:**
1. Leave all input fields empty
2. Click the Send Payment button

**Expected Result:** Validation error messages are displayed for all required fields

---

**BILPAY-003** - Error validation when Account Numbers do not match

- **Priority:** Medium
- **Preconditions:** User is on the Bill Payment form

**Test Steps:**
1. Enter 'John Doe' into the Payee Name field
2. Enter '123 Maple St' into the Address field
3. Enter 'Springfield' into the City field
4. Enter 'IL' into the State field
5. Enter '62704' into the Zip Code field
6. Enter '555-0199' into the Phone number field
7. Enter '12345' into the Account number field
8. Enter '67890' into the Verify Account number field
9. Enter '50.00' into the Amount field
10. Select a valid account from the From account number dropdown
11. Click the Send Payment button

**Expected Result:** An error message is displayed stating that the account numbers do not match

---

**BILPAY-004** - Validation for non-numeric Amount input

- **Priority:** Medium
- **Preconditions:** User is on the Bill Payment form

**Test Steps:**
1. Enter 'John Doe' into the Payee Name field
2. Enter '123 Maple St' into the Address field
3. Enter 'Springfield' into the City field
4. Enter 'IL' into the State field
5. Enter '62704' into the Zip Code field
6. Enter '555-0199' into the Phone number field
7. Enter '987654321' into the Account number field
8. Enter '987654321' into the Verify Account number field
9. Enter 'abc' into the Amount field
10. Select a valid account from the From account number dropdown
11. Click the Send Payment button

**Expected Result:** An error message is displayed indicating the amount must be a valid number

---

#### Boundary/Edge Case Tests

**BILPAY-005** - Successful payment with special characters in Payee Name

- **Priority:** Low
- **Preconditions:** User is on the Bill Payment form

**Test Steps:**
1. Enter 'O'Malley & Sons-Corp.' into the Payee Name field
2. Enter '123 Maple St' into the Address field
3. Enter 'Springfield' into the City field
4. Enter 'IL' into the State field
5. Enter '62704' into the Zip Code field
6. Enter '555-0199' into the Phone number field
7. Enter '987654321' into the Account number field
8. Enter '987654321' into the Verify Account number field
9. Enter '10.00' into the Amount field
10. Select a valid account from the From account number dropdown
11. Click the Send Payment button

**Expected Result:** A confirmation message appears indicating the successful transfer

---

**BILPAY-006** - Validation for minimum valid amount

- **Priority:** Low
- **Preconditions:** User is on the Bill Payment form

**Test Steps:**
1. Enter 'John Doe' into the Payee Name field
2. Enter '123 Maple St' into the Address field
3. Enter 'Springfield' into the City field
4. Enter 'IL' into the State field
5. Enter '62704' into the Zip Code field
6. Enter '555-0199' into the Phone number field
7. Enter '987654321' into the Account number field
8. Enter '987654321' into the Verify Account number field
9. Enter '0.01' into the Amount field
10. Select a valid account from the From account number dropdown
11. Click the Send Payment button

**Expected Result:** A confirmation message appears indicating the successful transfer

---

---

### Find Transaction

#### Functional Tests

**FINTRA-001** - Search by valid Transaction ID and Account

- **Priority:** High
- **Preconditions:** A valid Transaction ID exists for the selected account

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a valid transaction identifier into the 'Transaction ID' input field
3. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify the Transaction ID in the results matches the input ID
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays the matching Transaction ID, Date, Description, and Amount.

---

**FINTRA-002** - Search transactions with valid date and account

- **Priority:** High
- **Preconditions:** The Find Transactions page is loaded and at least one transaction exists for the selected date.

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a valid date in 'MM-DD-YYYY' format into the Date input field
3. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify all displayed transactions have a date matching the input date
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays matching transactions with Transaction ID, Date, Description, and Amount.

---

**FINTRA-003** - Search transactions with valid date range and account

- **Priority:** High
- **Preconditions:** The Find Transactions page is loaded and at least one account exists with transactions.

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Enter '01-01-2023' into the 'From' date input field
3. Enter '01-31-2023' into the 'To' date input field
4. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify all displayed transaction dates fall between 01-01-2023 and 01-31-2023
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays matching transactions with Transaction ID, Date, Description, and Amount columns.

---

**FINTRA-004** - Search for transaction with valid amount

- **Priority:** High
- **Preconditions:** At least one transaction exists for the selected account with a specific amount

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a valid numeric value in the 'Amount' input field within the 'Find by Amount' panel
3. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify all displayed transactions have an amount matching the input value
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays transactions matching the entered amount with columns for Transaction ID, Date, Description, and Amount.

---

**FINTRA-005** - Search for amount with decimal places

- **Priority:** High
- **Preconditions:** A transaction exists with a decimal value (e.g., 100.50)

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter '100.50' in the 'Amount' input field
3. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify the amount column shows exactly '100.50' for the returned records
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays the transaction matching the exact decimal amount '100.50'.

---

**FINTRA-006** - Search transactions for a single day range

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

- **Reads State:** account_list, transaction_history
- **Writes State:** search_results

**Pre-Verification Steps:**
1. Navigate to the Find Transactions page
2. Verify the results table is empty or hidden before search

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Enter '05-15-2023' into the 'From' date input field
3. Enter '05-15-2023' into the 'To' date input field
4. Click the 'Find Transactions' button

**Post-Verification Steps:**
1. Verify the results table is now visible
2. Verify all displayed transactions have the date 05-15-2023
3. Verify the Account column matches the selected account

**Expected Result:** The results table displays transactions specifically occurring on 05-15-2023.

---

**FINTRA-007** - View Search Results

- **Priority:** Medium
- **Preconditions:** User is logged in

- **Reads State:** search_results

**Test Steps:**
1. Navigate to the search results section
2. Verify search results is displayed correctly
3. Note the current values for verification purposes

**Expected Result:** The search results is displayed with correct current values

---

#### Negative Tests

**FINTRA-008** - Search with empty Transaction ID field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Clear any text from the 'Transaction ID' input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Transaction ID field indicating it is required.

---

**FINTRA-009** - Search without selecting an account

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'Select an account' dropdown at its default/empty state
2. Enter a valid transaction identifier into the 'Transaction ID' input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the account dropdown indicating it is required.

---

**FINTRA-010** - Search with empty account selection

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Leave the 'Select an account' dropdown unselected
2. Enter a valid date in 'MM-DD-YYYY' format into the Date input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the account dropdown indicating the field is required.

---

**FINTRA-011** - Search with empty date field

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Leave the Date input field empty
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Date input field indicating the field is required.

---

**FINTRA-012** - Search with invalid date format

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a date in 'YYYY-MM-DD' format into the Date input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Date input field indicating the format must be MM-DD-YYYY.

---

**FINTRA-013** - Search with non-numeric characters in date field

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter 'AA-BB-CCCC' into the Date input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Date input field indicating the input is invalid.

---

**FINTRA-014** - Validation error when account is not selected

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Leave the 'Select an account' dropdown at its default empty state
2. Enter '01-01-2023' into the 'From' date input field
3. Enter '01-31-2023' into the 'To' date input field
4. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the account dropdown indicating the field is required.

---

**FINTRA-015** - Validation error when date fields are empty

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Leave the 'From' and 'To' date input fields empty
3. Click the 'Find Transactions' button

**Expected Result:** Inline validation messages appear next to the date fields indicating they are required.

---

**FINTRA-016** - Validation error for incorrect date format

- **Priority:** Medium
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Enter '2023/01/01' into the 'From' date input field
3. Enter '2023/01/31' into the 'To' date input field
4. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears indicating that dates must be in MM-DD-YYYY format.

---

**FINTRA-017** - Search with empty account selection

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the 'Select an account' dropdown unselected
2. Enter a valid numeric value in the 'Amount' input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the account dropdown indicating the field is required.

---

**FINTRA-018** - Search with empty amount field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Leave the 'Amount' input field empty
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Amount input field indicating the field is required.

---

**FINTRA-019** - Search with non-numeric characters in amount field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter 'abc' into the 'Amount' input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the Amount input field indicating the input is invalid.

---

**FINTRA-020** - Validation error for alpha characters in date fields

- **Priority:** Low
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Enter 'Jan-01-2023' into the 'From' date input field
3. Enter 'Jan-31-2023' into the 'To' date input field
4. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears indicating the input is invalid or must follow the MM-DD-YYYY format.

---

#### Boundary/Edge Case Tests

**FINTRA-021** - Search with non-existent Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a non-existent or random string into the 'Transaction ID' input field
3. Click the 'Find Transactions' button

**Expected Result:** The results table is empty or displays a 'no results found' message.

---

**FINTRA-022** - Search with special characters in Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter special characters like '@#$%^&*' into the 'Transaction ID' input field
3. Click the 'Find Transactions' button

**Expected Result:** The system displays an inline validation message for invalid input or returns no results in the table.

---

**FINTRA-023** - Search for a date with no matching transactions

- **Priority:** Low
- **Preconditions:** The Find Transactions page is loaded and no transactions exist for the chosen date.

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter a valid date in 'MM-DD-YYYY' format that has no records
3. Click the 'Find Transactions' button

**Expected Result:** The results table is empty or displays a message indicating no transactions were found.

---

**FINTRA-024** - Search using a leap year date

- **Priority:** Low
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter '02-29-2024' into the Date input field
3. Click the 'Find Transactions' button

**Expected Result:** The search executes successfully and returns results or an empty table without validation errors.

---

**FINTRA-025** - Search with date range where no transactions exist

- **Priority:** Low
- **Preconditions:** The Find Transactions page is loaded.

**Test Steps:**
1. Select a valid account from the 'Select an account' dropdown
2. Enter '01-01-1900' into the 'From' date input field
3. Enter '01-01-1900' into the 'To' date input field
4. Click the 'Find Transactions' button

**Expected Result:** The results table is empty or displays a message indicating no transactions were found for the selected criteria.

---

**FINTRA-026** - Search for amount that returns no results

- **Priority:** Low
- **Preconditions:** No transactions exist with the amount '999999.99'

**Test Steps:**
1. Select an account from the 'Select an account' dropdown
2. Enter '999999.99' in the 'Amount' input field
3. Click the 'Find Transactions' button

**Expected Result:** The results table is empty or displays a message indicating no transactions were found.

---

---

### Update Profile

#### Functional Tests

**UPDPRO-001** - Successful profile update with all valid fields

- **Priority:** High
- **Preconditions:** The Update Profile page is loaded with existing user data

- **Reads State:** user_profile
- **Writes State:** user_profile
- **Verified By:** LOGIN-004, LOGOUT-003, LOGIN-002, LOGIN-001, FORPAS-001, REGIST-001

**Pre-Verification Steps:**
1. Navigate to the Profile page
2. Record the current values for First Name, Last Name, and Address

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Post-Verification Steps:**
1. Verify the confirmation message is displayed
2. Refresh the Profile page
3. Verify First Name is 'John'
4. Verify Last Name is 'Doe'
5. Verify Address is '123 Maple Street'

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

#### Negative Tests

**UPDPRO-002** - Validation error when First Name is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Clear the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that First Name is required

---

**UPDPRO-003** - Validation error when Last Name is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Clear the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that Last Name is required

---

**UPDPRO-004** - Validation error when Address is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Clear the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that Address is required

---

**UPDPRO-005** - Validation error when City is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Clear the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that City is required

---

**UPDPRO-006** - Validation error when State is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Clear the State field
6. Enter '62704' into the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that State is required

---

**UPDPRO-007** - Validation error when Zip Code is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Clear the Zip Code field
7. Enter '5550123456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that Zip Code is required

---

**UPDPRO-008** - Validation error when Phone number is empty

- **Priority:** Medium
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'John' into the First Name field
2. Enter 'Doe' into the Last Name field
3. Enter '123 Maple Street' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'Illinois' into the State field
6. Enter '62704' into the Zip Code field
7. Clear the Phone number field
8. Click the Update Profile button

**Expected Result:** A validation error message appears indicating that Phone number is required

---

#### Boundary/Edge Case Tests

**UPDPRO-009** - Profile update with special characters in name fields

- **Priority:** Low
- **Preconditions:** The Update Profile page is loaded

**Test Steps:**
1. Enter 'Jean-Luc' into the First Name field
2. Enter "O'Connor" into the Last Name field
3. Enter '123 Maple St.' into the Address field
4. Enter 'Springfield' into the City field
5. Enter 'IL' into the State field
6. Enter '62704-1234' into the Zip Code field
7. Enter '555-012-3456' into the Phone number field
8. Click the Update Profile button

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

---

### Request Loan

#### Functional Tests

**REQLOA-001** - Successful loan application with all valid fields

- **Priority:** High
- **Preconditions:** User is on the Request Loan page with a valid account balance

- **Reads State:** session_status, account_list, account_balance
- **Writes State:** loan_status, account_balance, transaction_history
- **Verified By:** BILPAY-001, ACCOVE-002, FINTRA-003, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Record the current balance of the selected 'From' account
3. Navigate to Loan History or Transaction History
4. Note the current number of records and existing loan statuses

**Test Steps:**
1. Enter a valid numeric value in the Loan Amount field
2. Enter a valid numeric value in the Down Payment field
3. Select a valid account from the From account number dropdown
4. Click the Apply Now button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify the 'From' account balance has been updated (reflecting down payment or loan disbursement)
3. Navigate to Transaction History
4. Verify a new entry exists for the loan application/disbursement
5. Navigate to Loan Status page
6. Verify the new loan appears with a status of 'Approved'

**Expected Result:** The loan application is successfully processed and approved

---

**REQLOA-002** - View Loan Status

- **Priority:** Medium
- **Preconditions:** User is logged in

- **Reads State:** loan_status

**Test Steps:**
1. Navigate to the loan status section
2. Verify loan status is displayed correctly
3. Note the current values for verification purposes

**Expected Result:** The loan status is displayed with correct current values

---

#### Negative Tests

**REQLOA-003** - Loan application fails when Loan Amount is blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Loan Amount field empty
2. Enter a valid numeric value in the Down Payment field
3. Select a valid account from the From account number dropdown
4. Click the Apply Now button

**Expected Result:** The process is not completed and a validation error for Loan Amount is displayed

---

**REQLOA-004** - Loan application fails when Down Payment is blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid numeric value in the Loan Amount field
2. Leave the Down Payment field empty
3. Select a valid account from the From account number dropdown
4. Click the Apply Now button

**Expected Result:** The process is not completed and a validation error for Down Payment is displayed

---

**REQLOA-005** - Loan application fails when From account number is not selected

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid numeric value in the Loan Amount field
2. Enter a valid numeric value in the Down Payment field
3. Ensure no account is selected in the From account number field
4. Click the Apply Now button

**Expected Result:** The process is not completed and a validation error for From account number is displayed

---

#### Boundary/Edge Case Tests

**REQLOA-006** - Loan application with minimum valid numeric values

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter '1' in the Loan Amount field
2. Enter '0' in the Down Payment field
3. Select a valid account from the From account number dropdown
4. Click the Apply Now button

**Expected Result:** The loan application is processed successfully

---

**REQLOA-007** - Loan application with large numeric values

- **Priority:** Low
- **Preconditions:** User has a high credit limit or balance

**Test Steps:**
1. Enter '9999999' in the Loan Amount field
2. Enter '1000000' in the Down Payment field
3. Select a valid account from the From account number dropdown
4. Click the Apply Now button

**Expected Result:** The loan application is processed and the system handles the large values correctly

---

---

### Logout

#### Functional Tests

**LOGOUT-001** - Successful logout from the application

- **Priority:** High
- **Preconditions:** User is currently logged into the application and on a page where the logout function is visible

- **Reads State:** session_status
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Verify the user is currently logged in
2. Confirm access to a restricted dashboard or account page
3. Note the presence of the 'Logout' button

**Test Steps:**
1. Click on the logout function element

**Post-Verification Steps:**
1. Verify redirection to the login page URL
2. Confirm the 'Logout' button is no longer visible
3. Attempt to navigate back to a restricted URL and verify access is denied/redirected to login

**Expected Result:** The user is redirected to the login page and the session is terminated.

---

**LOGOUT-002** - Verify session invalidation after logout

- **Priority:** High
- **Preconditions:** User has successfully clicked the logout function and is redirected to the login page

- **Reads State:** session_status

**Test Steps:**
1. Click the browser back button

**Expected Result:** The user is not granted access to the previous authenticated page and remains on the login page or is redirected back to it.

---

**LOGOUT-003** - Verify removal of sensitive account data from the UI

- **Priority:** Medium
- **Preconditions:** User is currently logged into the application

- **Reads State:** session_status, user_profile
- **Writes State:** session_status
- **Verified By:** BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to the dashboard or profile page
2. Identify and note specific sensitive data displayed (e.g., username, account ID)
3. Verify the session is active

**Test Steps:**
1. Click on the logout function element
2. Inspect the login page for any persistent user-specific data (e.g., username, profile name, or account ID)

**Post-Verification Steps:**
1. Verify the login page is displayed
2. Inspect the login page DOM and UI for the previously noted sensitive data
3. Confirm that username fields or welcome messages are empty or reset to default state

**Expected Result:** No sensitive account information or previous session data is visible on the login page.

---

#### Boundary/Edge Case Tests

**LOGOUT-004** - Verify logout functionality when multiple tabs are open

- **Priority:** Medium
- **Preconditions:** User is logged into the application in two separate browser tabs

**Test Steps:**
1. Click on the logout function element in the first tab
2. Switch to the second tab and refresh the page

**Expected Result:** The second tab redirects the user to the login page, confirming the session was cleared globally.

---

---

## Verification Chain

This section shows which test cases verify the results of other tests.

| Test ID | Test Name | Writes State | Verified By |
|---------|-----------|--------------|-------------|
| LOGIN-001 | Successful login using valid username | session_status | BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |
| LOGIN-002 | Successful login using valid email address | session_status | BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |
| LOGIN-004 | Correction of credentials after initial failure | session_status | BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |
| REGIST-001 | Successful login with valid credentials | session_status | BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |
| REGIST-002 | Successful account registration with all valid fields | user_profile, session_status | BILPAY-001, ACCOVE-001, LOGIN-004, LOGOUT-001, REQLOA-001, UPDPRO-001, LOGOUT-003, LOGIN-002, ONA-003, LOGIN-001, FORPAS-001, LOGOUT-002, ONA-001, REGIST-001, ONA-002, TRAFUN-001 |
| ONA-001 | Successfully open a new Savings account with valid funding | account_list, account_balance, transaction_history | BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-002, FINTRA-006, TRAFUN-001 |
| ONA-002 | Successfully open a new Checking account with valid funding | account_list, account_balance, transaction_history | BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-001, FINTRA-006, TRAFUN-001 |
| ONA-003 | Verify transaction integrity after account creation | account_list, account_balance, transaction_history | BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, FINTRA-001, ACCOVE-003, FINTRA-004, FINTRA-005, ACCOVE-004, FINTRA-002, ONA-001, ONA-002, FINTRA-006, TRAFUN-001 |
| TRAFUN-001 | Successful fund transfer between two valid accounts | account_balance, transaction_history | BILPAY-001, ACCOVE-002, FINTRA-003, REQLOA-001, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006 |
| BILPAY-001 | Successful bill payment with all valid fields | account_balance, transaction_history | ACCOVE-002, FINTRA-003, REQLOA-001, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006, TRAFUN-001 |
| UPDPRO-001 | Successful profile update with all valid fields | user_profile | LOGIN-004, LOGOUT-003, LOGIN-002, LOGIN-001, FORPAS-001, REGIST-001 |
| REQLOA-001 | Successful loan application with all valid fields | loan_status, account_balance, transaction_history | BILPAY-001, ACCOVE-002, FINTRA-003, ACCOVE-003, FINTRA-001, FINTRA-004, ONA-003, FINTRA-005, ACCOVE-004, FINTRA-002, FINTRA-006, TRAFUN-001 |
| LOGOUT-001 | Successful logout from the application | session_status | BILPAY-001, ACCOVE-001, REQLOA-001, LOGOUT-003, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |
| LOGOUT-003 | Verify removal of sensitive account data from the UI | session_status | BILPAY-001, ACCOVE-001, LOGOUT-001, REQLOA-001, ONA-003, LOGOUT-002, ONA-001, ONA-002, TRAFUN-001 |

## Navigation Graph

![Navigation Graph](output2/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /index.htm | No | 8 |
| Forgot Password | /lookup.htm | No | 9 |
| Register | /register.htm | No | 20 |
| Open New Account | /openaccount.htm | Yes | 7 |
| Account Overview | /overview.htm | Yes | 6 |
| Transfer Funds | /transfer.htm | Yes | 6 |
| Bill Payments | /billpay.htm | Yes | 6 |
| Find Transaction | /findtrans.htm | Yes | 26 |
| Update Profile | /updateprofile.htm | Yes | 9 |
| Request Loan | /requestloan.htm | Yes | 7 |
| Logout | /logout.htm | Yes | 4 |
