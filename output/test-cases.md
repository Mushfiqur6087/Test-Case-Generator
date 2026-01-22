# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-01-22T18:33:45.118566

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 122 |

### By Type

| Type | Count |
|------|-------|
| Positive | 25 |
| Negative | 59 |
| Edge Case | 38 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 33 |
| Medium | 51 |
| Low | 38 |

### Verification Coverage

| Metric | Count |
|--------|-------|
| Positive Tests | 25 |
| Tests that Write State | 18 |
| Tests that Read State | 24 |
| Tests with Verification Links | 17 |
| Tests with Pre-Verification Steps | 18 |
| Tests with Post-Verification Steps | 18 |

**State Categories:**

- **Written:** bill_payment_details, account_list, account_balance, transfer_details, transaction_history, session_status, loan_status, transaction_search_results, user_profile
- **Read:** bill_payment_details, account_list, account_balance, transfer_details, transaction_history, loan_status, transaction_search_results, payee_list, registration_data, user_profile, session_status

---

## Test Cases

### Login

#### Functional Tests

**LOGIN-001** - Login with valid username and password

- **Priority:** High
- **Preconditions:** None

- **Reads State:** registration_data
- **Writes State:** session_status
- **Verified By:** ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, LOGOUT-003

**Pre-Verification Steps:**
1. Navigate to the login page
2. Verify the session_status is not active (user is logged out)

**Test Steps:**
1. Enter a valid username in the Username field
2. Enter the correct password in the Password field
3. Click the Log In button

**Post-Verification Steps:**
1. Verify the session_status is active (user is logged in)
2. Verify user is redirected to the account dashboard

**Expected Result:** User is redirected to the account dashboard

---

**LOGIN-002** - Login with valid email and password

- **Priority:** High
- **Preconditions:** None

- **Reads State:** registration_data
- **Writes State:** session_status
- **Verified By:** ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, LOGOUT-003

**Pre-Verification Steps:**
1. Navigate to the login page
2. Verify the session_status is not active (user is logged out)

**Test Steps:**
1. Enter a valid email in the Email field
2. Enter the correct password in the Password field
3. Click the Log In button

**Post-Verification Steps:**
1. Verify the session_status is active (user is logged in)
2. Verify user is redirected to the account dashboard

**Expected Result:** User is redirected to the account dashboard

---

#### Negative Tests

**LOGIN-003** - Login with invalid username and password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid username in the Username field
2. Enter an incorrect password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

**LOGIN-004** - Login with invalid email and password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid email in the Email field
2. Enter an incorrect password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

**LOGIN-005** - Login with empty username and password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Username field empty
2. Leave the Password field empty
3. Click the Log In button

**Expected Result:** Error message is displayed indicating required fields, and input fields remain empty

---

**LOGIN-006** - Login with empty email and password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Email field empty
2. Leave the Password field empty
3. Click the Log In button

**Expected Result:** Error message is displayed indicating required fields, and input fields remain empty

---

**LOGIN-007** - Login with valid username and incorrect password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid username in the Username field
2. Enter an incorrect password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

**LOGIN-008** - Login with valid email and incorrect password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid email in the Email field
2. Enter an incorrect password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

#### Boundary/Edge Case Tests

**LOGIN-009** - Login with special characters in username

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a username containing special characters (e.g., @#$%) in the Username field
2. Enter a valid password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

**LOGIN-010** - Login with special characters in email

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter an email containing special characters (e.g., test@#$.com) in the Email field
2. Enter a valid password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, and input fields remain populated

---

**LOGIN-011** - Login with maximum character length in username

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a username with the maximum allowed characters (e.g., 255 characters) in the Username field
2. Enter a valid password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed if credentials are invalid, and input fields remain populated

---

**LOGIN-012** - Login with maximum character length in email

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter an email with the maximum allowed characters (e.g., 255 characters) in the Email field
2. Enter a valid password in the Password field
3. Click the Log In button

**Expected Result:** Error message is displayed if credentials are invalid, and input fields remain populated

---

---

### Forgot Password

#### Functional Tests

**FORPAS-001** - Submit valid Customer Lookup form with matching record

- **Priority:** High
- **Preconditions:** None

- **Reads State:** user_profile

**Test Steps:**
1. Enter a valid First Name in the First Name field
2. Enter a valid Last Name in the Last Name field
3. Enter a valid Address in the Address field
4. Enter a valid City in the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code in the Zip Code field
7. Enter a valid SSN in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** Recovery details are displayed for the matching record

---

#### Negative Tests

**FORPAS-002** - Submit Customer Lookup form with no matching record

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid First Name in the First Name field
2. Enter a valid Last Name in the Last Name field
3. Enter a valid Address in the Address field
4. Enter a valid City in the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code in the Zip Code field
7. Enter a valid SSN in the SSN field that does not match any record
8. Click the 'Find My Login Info' button

**Expected Result:** An error message is displayed indicating no matching record was found

---

**FORPAS-003** - Submit Customer Lookup form with all fields empty

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave all fields empty
2. Click the 'Find My Login Info' button

**Expected Result:** An error message is displayed indicating that all fields are required

---

**FORPAS-004** - Submit Customer Lookup form with missing First Name

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the First Name field empty
2. Enter a valid Last Name in the Last Name field
3. Enter a valid Address in the Address field
4. Enter a valid City in the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code in the Zip Code field
7. Enter a valid SSN in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** An error message is displayed indicating that the First Name field is required

---

**FORPAS-005** - Submit Customer Lookup form with invalid Zip Code format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid First Name in the First Name field
2. Enter a valid Last Name in the Last Name field
3. Enter a valid Address in the Address field
4. Enter a valid City in the City field
5. Select a valid State from the State dropdown
6. Enter an invalid Zip Code (e.g., 'ABCDE') in the Zip Code field
7. Enter a valid SSN in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** An error message is displayed indicating that the Zip Code format is invalid

---

#### Boundary/Edge Case Tests

**FORPAS-006** - Submit Customer Lookup form with special characters in First Name

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters (e.g., '@#$%') in the First Name field
2. Enter a valid Last Name in the Last Name field
3. Enter a valid Address in the Address field
4. Enter a valid City in the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code in the Zip Code field
7. Enter a valid SSN in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** An error message is displayed indicating that the First Name field contains invalid characters

---

**FORPAS-007** - Submit Customer Lookup form with maximum character length in all fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter the maximum allowed characters in the First Name field
2. Enter the maximum allowed characters in the Last Name field
3. Enter the maximum allowed characters in the Address field
4. Enter the maximum allowed characters in the City field
5. Select a valid State from the State dropdown
6. Enter the maximum allowed characters in the Zip Code field
7. Enter the maximum allowed characters in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** The system processes the form successfully if the inputs are valid

---

**FORPAS-008** - Submit Customer Lookup form with leading and trailing spaces in all fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid First Name with leading and trailing spaces in the First Name field
2. Enter a valid Last Name with leading and trailing spaces in the Last Name field
3. Enter a valid Address with leading and trailing spaces in the Address field
4. Enter a valid City with leading and trailing spaces in the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code with leading and trailing spaces in the Zip Code field
7. Enter a valid SSN with leading and trailing spaces in the SSN field
8. Click the 'Find My Login Info' button

**Expected Result:** The system trims the spaces and processes the form successfully if the inputs are valid

---

---

### Register

#### Functional Tests

**REGIST-001** - Successful registration with valid inputs

- **Priority:** High
- **Preconditions:** None

- **Reads State:** registration_data
- **Writes State:** user_profile, session_status
- **Verified By:** ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, FORPAS-001, UPDPRO-001, LOGOUT-003

**Pre-Verification Steps:**
1. Navigate to Profile/Settings
2. Note current profile values
3. Verify user is logged out initially

**Test Steps:**
1. Enter a valid First Name into the First Name field
2. Enter a valid Last Name into the Last Name field
3. Enter a valid Address into the Address field
4. Enter a valid City into the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code into the Zip Code field
7. Enter a valid Phone Number into the Phone # field
8. Enter a valid SSN into the SSN field
9. Enter a valid Username into the Username field
10. Enter a valid Password into the Password field
11. Re-enter the same valid Password into the Confirm Password field
12. Click the Register button

**Post-Verification Steps:**
1. Navigate to Profile/Settings
2. Verify updated values are displayed
3. Verify user session state changed as expected

**Expected Result:** The account is successfully created, and the user is automatically logged in.

---

#### Negative Tests

**REGIST-002** - Registration fails when a mandatory field is left empty

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the First Name field empty
2. Enter valid inputs for all other fields
3. Click the Register button

**Expected Result:** An error message is displayed indicating that the First Name field is required, and the account is not created.

---

**REGIST-003** - Registration fails when Password and Confirm Password do not match

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter valid inputs into all fields except the Password and Confirm Password fields
2. Enter a valid Password into the Password field
3. Enter a different value into the Confirm Password field
4. Click the Register button

**Expected Result:** An error message is displayed indicating that the Password and Confirm Password fields must match, and the account is not created.

---

**REGIST-004** - Registration fails when SSN field is left empty

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the SSN field empty
2. Enter valid inputs for all other fields
3. Click the Register button

**Expected Result:** An error message is displayed indicating that the SSN field is required, and the account is not created.

---

**REGIST-005** - Registration fails when all fields are left empty

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave all fields empty
2. Click the Register button

**Expected Result:** An error message is displayed indicating that all fields are required, and the account is not created.

---

**REGIST-006** - Registration fails when Password field is left empty

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter valid inputs into all fields except the Password field
2. Leave the Password field empty
3. Click the Register button

**Expected Result:** An error message is displayed indicating that the Password field is required, and the account is not created.

---

**REGIST-007** - Registration fails when invalid Zip Code is entered

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter valid inputs into all fields except the Zip Code field
2. Enter an invalid value (e.g., alphabetic characters) into the Zip Code field
3. Click the Register button

**Expected Result:** An error message is displayed indicating that the Zip Code field must contain a valid value, and the account is not created.

---

#### Boundary/Edge Case Tests

**REGIST-008** - Successful registration with edge case values for fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid First Name with special characters (e.g., O'Connor) into the First Name field
2. Enter a valid Last Name with special characters (e.g., Smith-Jones) into the Last Name field
3. Enter a valid Address with special characters (e.g., Apt #5) into the Address field
4. Enter a valid City with special characters (e.g., St. Louis) into the City field
5. Select a valid State from the State dropdown
6. Enter a valid Zip Code with leading zeros (e.g., 01234) into the Zip Code field
7. Enter a valid Phone Number with dashes (e.g., 123-456-7890) into the Phone # field
8. Enter a valid SSN with dashes (e.g., 123-45-6789) into the SSN field
9. Enter a valid Username with mixed case and numbers (e.g., User123) into the Username field
10. Enter a valid Password with special characters (e.g., P@ssw0rd!) into the Password field
11. Re-enter the same valid Password into the Confirm Password field
12. Click the Register button

**Expected Result:** The account is successfully created, and the user is automatically logged in.

---

---

### Open New Account

#### Functional Tests

**ONA-001** - Open a new account with valid account type and funding source

- **Priority:** High
- **Preconditions:** None

- **Reads State:** account_list, account_balance
- **Writes State:** account_list, account_balance, transaction_history
- **Verified By:** BILPAY-001, FINTRA-003, FINTRA-007, REQLOA-001, ACCOVE-003, ACCOVE-001, FINTRA-005, ACCOVE-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note current number of accounts
3. Navigate to Accounts Overview
4. Note current account balance(s)
5. Navigate to Transaction History
6. Note current transaction count

**Test Steps:**
1. Click on 'Open New Account' button
2. Select a valid account type from the dropdown
3. Select a valid funding source from the dropdown
4. Click on 'Open New Account' button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify account list updated
3. Navigate to Accounts Overview
4. Verify balance reflects the change
5. Navigate to Transaction History
6. Verify new transaction appears

**Expected Result:** A new account is created with a unique account number, $100.00 is debited from the funding source, and $100.00 is credited to the new account

---

#### Negative Tests

**ONA-002** - Attempt to open a new account without selecting an account type

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' button
2. Leave the account type dropdown unselected
3. Select a valid funding source from the dropdown
4. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that account type must be selected

---

**ONA-003** - Attempt to open a new account without selecting a funding source

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' button
2. Select a valid account type from the dropdown
3. Leave the funding source dropdown unselected
4. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that a funding source must be selected

---

**ONA-004** - Attempt to open a new account with insufficient funds in the funding source

- **Priority:** Medium
- **Preconditions:** Funding source account has less than $100.00 balance

**Test Steps:**
1. Click on 'Open New Account' button
2. Select a valid account type from the dropdown
3. Select a funding source with insufficient funds from the dropdown
4. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating insufficient funds in the funding source

---

**ONA-005** - Attempt to open a new account with empty funding source and account type

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' button
2. Leave both the account type and funding source dropdowns unselected
3. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that both account type and funding source must be selected

---

#### Boundary/Edge Case Tests

**ONA-006** - Open a new account with boundary value of $100.00 in funding source

- **Priority:** Low
- **Preconditions:** Funding source account has exactly $100.00 balance

**Test Steps:**
1. Click on 'Open New Account' button
2. Select a valid account type from the dropdown
3. Select a funding source with exactly $100.00 balance from the dropdown
4. Click on 'Open New Account' button

**Expected Result:** A new account is created with a unique account number, $100.00 is debited from the funding source, and $100.00 is credited to the new account

---

**ONA-007** - Open a new account with special characters in account type name

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' button
2. Select an account type with special characters (e.g., 'Savings@123') from the dropdown
3. Select a valid funding source from the dropdown
4. Click on 'Open New Account' button

**Expected Result:** A new account is created with a unique account number, $100.00 is debited from the funding source, and $100.00 is credited to the new account

---

**ONA-008** - Open a new account with maximum length account type name

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' button
2. Select an account type with the maximum allowed length (e.g., 50 characters) from the dropdown
3. Select a valid funding source from the dropdown
4. Click on 'Open New Account' button

**Expected Result:** A new account is created with a unique account number, $100.00 is debited from the funding source, and $100.00 is credited to the new account

---

---

### Account Overview

#### Functional Tests

**ACCOVE-001** - Verify the presence of all Account Services options in the sidebar

- **Priority:** High
- **Preconditions:** None

- **Reads State:** account_list

**Test Steps:**
1. Locate the left sidebar titled 'Account Services'.
2. Verify the presence of the following options: Open New Account, Accounts Overview, Transfer Funds, Bill Pay, Find Transactions, Update Contact Info, Request Loan, Log Out.

**Expected Result:** All listed options are visible in the 'Account Services' sidebar.

---

**ACCOVE-002** - Verify the Accounts Overview heading is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the 'Accounts Overview' heading on the page.

**Expected Result:** The 'Accounts Overview' heading is displayed on the page.

---

**ACCOVE-003** - Verify account details are displayed correctly

- **Priority:** High
- **Preconditions:** None

- **Reads State:** account_balance, account_list

**Test Steps:**
1. Locate the account details section.
2. Verify the presence of the following elements: Account number, Balance, Available Amount, Combined total balance.

**Expected Result:** All account details are displayed correctly.

---

**ACCOVE-004** - Verify the Combined total balance is calculated correctly

- **Priority:** High
- **Preconditions:** At least two accounts are displayed with balances.

- **Reads State:** account_balance

**Test Steps:**
1. Locate the individual account balances.
2. Locate the Combined total balance.
3. Verify that the Combined total balance equals the sum of the individual account balances.

**Expected Result:** The Combined total balance is correctly calculated as the sum of individual account balances.

---

**ACCOVE-005** - Verify the sidebar option 'Open New Account' is clickable

- **Priority:** Medium
- **Preconditions:** None

- **Reads State:** account_list

**Test Steps:**
1. Locate the 'Open New Account' option in the sidebar.
2. Click on the 'Open New Account' option.

**Expected Result:** The 'Open New Account' option is clickable and responds to user interaction.

---

**ACCOVE-006** - Verify the sidebar option 'Log Out' is clickable

- **Priority:** Medium
- **Preconditions:** None

- **Reads State:** session_status

**Test Steps:**
1. Locate the 'Log Out' option in the sidebar.
2. Click on the 'Log Out' option.

**Expected Result:** The 'Log Out' option is clickable and responds to user interaction.

---

#### Boundary/Edge Case Tests

**ACCOVE-007** - Verify the page handles no accounts gracefully

- **Priority:** Low
- **Preconditions:** User has no accounts associated with their profile.

**Test Steps:**
1. Check the account details section.
2. Verify the message displayed when no accounts are available.

**Expected Result:** A user-friendly message is displayed indicating no accounts are available.

---

**ACCOVE-008** - Verify the page handles a large number of accounts gracefully

- **Priority:** Low
- **Preconditions:** User has a large number of accounts associated with their profile.

**Test Steps:**
1. Check the account details section.
2. Verify that all accounts are displayed without layout issues or performance degradation.

**Expected Result:** All accounts are displayed correctly without layout issues or performance degradation.

---

**ACCOVE-009** - Verify special characters in account names are displayed correctly

- **Priority:** Low
- **Preconditions:** User has accounts with special characters in their names.

**Test Steps:**
1. Locate the account names in the account details section.
2. Verify that special characters in account names are displayed correctly.

**Expected Result:** Special characters in account names are displayed correctly without encoding or rendering issues.

---

---

### Transfer Funds

#### Functional Tests

**TRAFUN-001** - Successful fund transfer with valid inputs

- **Priority:** High
- **Preconditions:** None

- **Reads State:** account_balance, account_list, transfer_details
- **Writes State:** account_balance, transaction_history, transfer_details
- **Verified By:** ONA-001, BILPAY-001, FINTRA-003, FINTRA-007, ACCOVE-003, FINTRA-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note current account balance(s)
3. Navigate to Transaction History
4. Note current transaction count

**Test Steps:**
1. Enter a valid amount (e.g., 100) in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify balance reflects the change
3. Navigate to Transaction History
4. Verify new transaction appears

**Expected Result:** Funds are successfully transferred, and a confirmation message is displayed

---

#### Negative Tests

**TRAFUN-002** - Transfer fails when Amount field is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Amount field blank
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the Amount field is required

---

**TRAFUN-003** - Transfer fails when From account number is not selected

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid amount (e.g., 100) in the Amount field
2. Leave the From account number field unselected
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the From account number is required

---

**TRAFUN-004** - Transfer fails when To account number is not selected

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid amount (e.g., 100) in the Amount field
2. Select a valid From account number from the dropdown
3. Leave the To account number field unselected
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the To account number is required

---

**TRAFUN-005** - Transfer fails when Amount is zero

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter 0 in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the Amount must be greater than zero

---

**TRAFUN-006** - Transfer fails when Amount is a negative value

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a negative value (e.g., -100) in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the Amount must be a positive value

---

**TRAFUN-007** - Transfer fails when From and To account numbers are the same

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid amount (e.g., 100) in the Amount field
2. Select the same account number for both From and To account fields
3. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the From and To account numbers cannot be the same

---

**TRAFUN-008** - Transfer fails when Amount exceeds available balance

- **Priority:** Medium
- **Preconditions:** Ensure the From account has a balance less than the entered Amount

**Test Steps:**
1. Enter an amount greater than the available balance (e.g., 1000 when balance is 500) in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating insufficient balance

---

#### Boundary/Edge Case Tests

**TRAFUN-009** - Transfer fails when Amount contains special characters

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid value with special characters (e.g., $100) in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** An error message is displayed indicating that the Amount must be a numeric value

---

**TRAFUN-010** - Transfer succeeds with maximum allowable Amount

- **Priority:** Low
- **Preconditions:** Ensure the From account has a balance equal to or greater than the maximum allowable Amount

**Test Steps:**
1. Enter the maximum allowable Amount (e.g., 100000) in the Amount field
2. Select a valid From account number from the dropdown
3. Select a valid To account number from the dropdown
4. Click on the Transfer button

**Expected Result:** Funds are successfully transferred, and a confirmation message is displayed

---

---

### Bill Payments

#### Functional Tests

**BILPAY-001** - Successful payment with valid inputs

- **Priority:** High
- **Preconditions:** None

- **Reads State:** session_status, account_balance, payee_list, bill_payment_details
- **Writes State:** account_balance, transaction_history, bill_payment_details
- **Verified By:** ONA-001, FINTRA-003, FINTRA-007, ACCOVE-003, FINTRA-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001, TRAFUN-001

**Pre-Verification Steps:**
1. Navigate to Accounts Overview
2. Note current account balance(s)
3. Navigate to Transaction History
4. Note current transaction count

**Test Steps:**
1. Enter a valid Payee Name
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter a valid 10-digit Phone Number
7. Enter a valid Account Number
8. Re-enter the same Account Number in the Verify Account Number field
9. Enter a valid payment Amount greater than zero
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Post-Verification Steps:**
1. Navigate to Accounts Overview
2. Verify balance reflects the change
3. Navigate to Transaction History
4. Verify new transaction appears

**Expected Result:** A confirmation message appears indicating the payment was successful

---

#### Negative Tests

**BILPAY-002** - Error when Payee Name is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Payee Name field blank
2. Fill out all other fields with valid inputs
3. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Payee Name is required

---

**BILPAY-003** - Error when Address is left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Payee Name
2. Leave the Address field blank
3. Fill out all other fields with valid inputs
4. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Address is required

---

**BILPAY-004** - Error when Zip Code is invalid

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Payee Name
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter an invalid Zip Code (e.g., less than 5 digits or contains letters)
6. Fill out all other fields with valid inputs
7. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Zip Code is invalid

---

**BILPAY-005** - Error when Account Number and Verify Account Number do not match

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Payee Name
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter a valid 10-digit Phone Number
7. Enter a valid Account Number
8. Enter a different Account Number in the Verify Account Number field
9. Enter a valid payment Amount greater than zero
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Account Number and Verify Account Number do not match

---

**BILPAY-006** - Error when Amount is zero

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Payee Name
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter a valid 10-digit Phone Number
7. Enter a valid Account Number
8. Re-enter the same Account Number in the Verify Account Number field
9. Enter '0' in the Amount field
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Amount must be greater than zero

---

**BILPAY-007** - Error when Phone Number is invalid

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Payee Name
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter an invalid Phone Number (e.g., less than 10 digits or contains letters)
7. Enter a valid Account Number
8. Re-enter the same Account Number in the Verify Account Number field
9. Enter a valid payment Amount greater than zero
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that the Phone Number is invalid

---

#### Boundary/Edge Case Tests

**BILPAY-008** - Edge case: Maximum valid input lengths for all fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter the maximum allowed characters in the Payee Name field
2. Enter the maximum allowed characters in the Address field
3. Enter the maximum allowed characters in the City field
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter a valid 10-digit Phone Number
7. Enter the maximum allowed digits in the Account Number field
8. Re-enter the same Account Number in the Verify Account Number field
9. Enter the maximum allowed Amount
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Expected Result:** A confirmation message appears indicating the payment was successful

---

**BILPAY-009** - Edge case: Special characters in Payee Name

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters (e.g., @#$%^&*) in the Payee Name field
2. Enter a valid Address
3. Enter a valid City
4. Select a valid State from the dropdown
5. Enter a valid 5-digit Zip Code
6. Enter a valid 10-digit Phone Number
7. Enter a valid Account Number
8. Re-enter the same Account Number in the Verify Account Number field
9. Enter a valid payment Amount greater than zero
10. Select a valid From Account Number from the dropdown
11. Click the 'Send Payment' button

**Expected Result:** An error message appears indicating that special characters are not allowed in the Payee Name

---

---

### Find Transaction

#### Functional Tests

**FINTRA-001** - Search for transaction with valid Transaction ID

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-004

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter a valid Transaction ID into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transaction is displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-002** - Search for transaction with alphanumeric Transaction ID

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter a valid alphanumeric Transaction ID into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transaction is displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-003** - Search transactions with valid date

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-007, FINTRA-005, FINTRA-006, FINTRA-002, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown
2. Enter a valid date in MM-DD-YYYY format in the Date input field
3. Click the Find Transactions button

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transactions for the entered date are displayed in the results table showing Transaction ID, Date, Description, and Amount

---

**FINTRA-004** - Search transactions with valid date range

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter a valid start date in MM-DD-YYYY format in the Date Range input field.
4. Enter a valid end date in MM-DD-YYYY format in the Date Range input field.
5. Click the 'Find Transactions' button.

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-005** - Search transactions with valid amount

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-002, FINTRA-003, FINTRA-006, FINTRA-007, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter a valid amount (e.g., 100) in the Amount input field.
3. Click the Find Transactions button.

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-006** - Search transactions with decimal amount

- **Priority:** High
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-007, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter a valid decimal amount (e.g., 100.50) in the Amount input field.
3. Click the Find Transactions button.

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-007** - Search transactions with past date having no transactions

- **Priority:** Medium
- **Preconditions:** None

- **Reads State:** transaction_history, transaction_search_results, account_list
- **Writes State:** transaction_search_results
- **Verified By:** FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-002, FINTRA-004, FINTRA-001

**Pre-Verification Steps:**
1. Note initial application state

**Test Steps:**
1. Select an account from the account dropdown
2. Enter a past date in MM-DD-YYYY format that has no transactions in the Date input field
3. Click the Find Transactions button

**Post-Verification Steps:**
1. Verify application state changed as expected

**Expected Result:** No transactions are displayed in the results table, and a message indicating no matching transactions is shown

---

#### Negative Tests

**FINTRA-008** - Attempt search with empty Transaction ID field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Leave the Transaction ID input field empty.
4. Click the 'Find Transactions' button.

**Expected Result:** An inline validation message appears next to the Transaction ID input field indicating that the field is required.

---

**FINTRA-009** - Attempt search with invalid Transaction ID format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter an invalid Transaction ID (e.g., special characters or incorrect format) into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Expected Result:** An inline validation message appears next to the Transaction ID input field indicating that the input format is invalid.

---

**FINTRA-010** - Attempt search with whitespace-only Transaction ID

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter only whitespace characters into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Expected Result:** An inline validation message appears next to the Transaction ID input field indicating that the field is required.

---

**FINTRA-011** - Attempt search without selecting an account

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Do not select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter a valid Transaction ID into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Expected Result:** An inline validation message appears next to the account dropdown indicating that the field is required.

---

**FINTRA-012** - Search transactions with empty date field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown
2. Leave the Date input field empty
3. Click the Find Transactions button

**Expected Result:** An inline validation message appears next to the Date input field indicating that the field is required

---

**FINTRA-013** - Search transactions with invalid date format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown
2. Enter an invalid date format (e.g., DD-MM-YYYY or YYYY/MM/DD) in the Date input field
3. Click the Find Transactions button

**Expected Result:** An inline validation message appears next to the Date input field indicating that the date must be in MM-DD-YYYY format

---

**FINTRA-014** - Search transactions without selecting an account

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the account dropdown unselected
2. Enter a valid date in MM-DD-YYYY format in the Date input field
3. Click the Find Transactions button

**Expected Result:** An inline validation message appears next to the account dropdown indicating that the field is required

---

**FINTRA-015** - Search transactions with empty date range fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Leave both the start date and end date fields empty.
4. Click the 'Find Transactions' button.

**Expected Result:** Inline validation messages appear next to both fields indicating that they are required.

---

**FINTRA-016** - Search transactions with invalid date format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter an invalid date format (e.g., DD-MM-YYYY) in the start date field.
4. Enter an invalid date format (e.g., YYYY-MM-DD) in the end date field.
5. Click the 'Find Transactions' button.

**Expected Result:** Inline validation messages appear next to both fields indicating that the date must be in MM-DD-YYYY format.

---

**FINTRA-017** - Search transactions with start date later than end date

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter a start date that is later than the end date in MM-DD-YYYY format.
4. Click the 'Find Transactions' button.

**Expected Result:** Inline validation message appears indicating that the start date cannot be later than the end date.

---

**FINTRA-018** - Search transactions with missing account selection

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the account dropdown unselected.
2. Click on the 'Find by Date Range' option.
3. Enter valid dates in MM-DD-YYYY format in both the start date and end date fields.
4. Click the 'Find Transactions' button.

**Expected Result:** Inline validation message appears indicating that the account selection is required.

---

**FINTRA-019** - Search transactions with empty amount field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Leave the Amount input field empty.
3. Click the Find Transactions button.

**Expected Result:** An inline validation message appears next to the Amount input field indicating the field is required.

---

**FINTRA-020** - Search transactions with invalid characters in amount field

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter invalid characters (e.g., 'abc') in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** An inline validation message appears next to the Amount input field indicating invalid input.

---

**FINTRA-021** - Search transactions with negative amount

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter a negative amount (e.g., -50) in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** An inline validation message appears next to the Amount input field indicating invalid input.

---

**FINTRA-022** - Search transactions without selecting an account

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the account dropdown unselected.
2. Enter a valid amount (e.g., 100) in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** An inline validation message appears next to the account dropdown indicating the field is required.

---

**FINTRA-023** - Search transactions with special characters in amount field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter special characters (e.g., '!@#$') in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** An inline validation message appears next to the Amount input field indicating invalid input.

---

#### Boundary/Edge Case Tests

**FINTRA-024** - Search for transaction with maximum length Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter a Transaction ID with the maximum allowed length into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Expected Result:** Matching transaction is displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-025** - Search for transaction with minimum length Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Transaction ID' option.
3. Enter a Transaction ID with the minimum allowed length into the Transaction ID input field.
4. Click the 'Find Transactions' button.

**Expected Result:** Matching transaction is displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-026** - Search transactions with special characters in date field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown
2. Enter special characters (e.g., ##-##-####) in the Date input field
3. Click the Find Transactions button

**Expected Result:** An inline validation message appears next to the Date input field indicating that the date must be in MM-DD-YYYY format

---

**FINTRA-027** - Search transactions with future date

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown
2. Enter a future date in MM-DD-YYYY format in the Date input field
3. Click the Find Transactions button

**Expected Result:** No transactions are displayed in the results table, and a message indicating no matching transactions is shown

---

**FINTRA-028** - Search transactions with date containing leading or trailing spaces

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown
2. Enter a valid date in MM-DD-YYYY format with leading or trailing spaces in the Date input field
3. Click the Find Transactions button

**Expected Result:** Matching transactions for the entered date are displayed in the results table showing Transaction ID, Date, Description, and Amount

---

**FINTRA-029** - Search transactions with boundary date range

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter the same date in both the start date and end date fields in MM-DD-YYYY format.
4. Click the 'Find Transactions' button.

**Expected Result:** Matching transactions for the specified date are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-030** - Search transactions with special characters in date fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter special characters (e.g., ##-##-####) in the start date field.
4. Enter special characters (e.g., ##-##-####) in the end date field.
5. Click the 'Find Transactions' button.

**Expected Result:** Inline validation messages appear next to both fields indicating that the date must be in MM-DD-YYYY format.

---

**FINTRA-031** - Search transactions with valid leap year date range

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Click on the 'Find by Date Range' option.
3. Enter a valid leap year date (e.g., 02-29-2024) in the start date field.
4. Enter a valid leap year date (e.g., 02-29-2024) in the end date field.
5. Click the 'Find Transactions' button.

**Expected Result:** Matching transactions for the specified leap year date are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-032** - Search transactions with maximum allowed amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter the maximum allowed amount (e.g., 999999999.99) in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-033** - Search transactions with zero amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter zero (0) in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

**FINTRA-034** - Search transactions with leading and trailing spaces in amount field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Select an account from the account dropdown.
2. Enter an amount with leading and trailing spaces (e.g., ' 100 ') in the Amount input field.
3. Click the Find Transactions button.

**Expected Result:** Matching transactions are displayed in the results table showing Transaction ID, Date, Description, and Amount.

---

---

### Update Profile

#### Functional Tests

**UPDPRO-001** - Update profile with valid information

- **Priority:** High
- **Preconditions:** None

- **Reads State:** user_profile
- **Writes State:** user_profile
- **Verified By:** LOGOUT-003, FORPAS-001

**Pre-Verification Steps:**
1. Navigate to Profile/Settings
2. Note current profile values

**Test Steps:**
1. Enter 'John' in the First Name field
2. Enter 'Doe' in the Last Name field
3. Enter '123 Main St' in the Address field
4. Enter 'Springfield' in the City field
5. Select 'Illinois' from the State dropdown
6. Enter '62704' in the Zip Code field
7. Enter '555-123-4567' in the Phone Number field
8. Click the 'Update Profile' button

**Post-Verification Steps:**
1. Navigate to Profile/Settings
2. Verify updated values are displayed

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

#### Negative Tests

**UPDPRO-002** - Attempt to update profile with empty fields

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave all fields empty
2. Click the 'Update Profile' button

**Expected Result:** Error messages are displayed for all required fields indicating they cannot be empty

---

**UPDPRO-003** - Attempt to update profile with invalid phone number format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter 'John' in the First Name field
2. Enter 'Doe' in the Last Name field
3. Enter '123 Main St' in the Address field
4. Enter 'Springfield' in the City field
5. Select 'Illinois' from the State dropdown
6. Enter '62704' in the Zip Code field
7. Enter '12345' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** An error message is displayed indicating the phone number format is invalid

---

**UPDPRO-004** - Attempt to update profile with invalid zip code format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter 'John' in the First Name field
2. Enter 'Doe' in the Last Name field
3. Enter '123 Main St' in the Address field
4. Enter 'Springfield' in the City field
5. Select 'Florida' from the State dropdown
6. Enter 'ABCDE' in the Zip Code field
7. Enter '555-123-4567' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** An error message is displayed indicating the zip code format is invalid

---

**UPDPRO-005** - Attempt to update profile with missing state selection

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter 'John' in the First Name field
2. Enter 'Doe' in the Last Name field
3. Enter '123 Main St' in the Address field
4. Enter 'Springfield' in the City field
5. Leave the State dropdown unselected
6. Enter '62704' in the Zip Code field
7. Enter '555-123-4567' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** An error message is displayed indicating the state field is required

---

#### Boundary/Edge Case Tests

**UPDPRO-006** - Update profile with maximum allowed characters in all fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a 50-character string in the First Name field
2. Enter a 50-character string in the Last Name field
3. Enter a 100-character string in the Address field
4. Enter a 50-character string in the City field
5. Select 'California' from the State dropdown
6. Enter '99999' in the Zip Code field
7. Enter '555-555-5555' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

**UPDPRO-007** - Attempt to update profile with special characters in name fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter 'J@hn!' in the First Name field
2. Enter 'D#e$' in the Last Name field
3. Enter '123 Main St' in the Address field
4. Enter 'Springfield' in the City field
5. Select 'Texas' from the State dropdown
6. Enter '75001' in the Zip Code field
7. Enter '555-987-6543' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

**UPDPRO-008** - Update profile with numeric values in address field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter 'John' in the First Name field
2. Enter 'Doe' in the Last Name field
3. Enter '1234567890' in the Address field
4. Enter 'Springfield' in the City field
5. Select 'Nevada' from the State dropdown
6. Enter '89044' in the Zip Code field
7. Enter '555-123-4567' in the Phone Number field
8. Click the 'Update Profile' button

**Expected Result:** A confirmation message is displayed indicating the profile was successfully updated

---

---

### Request Loan

#### Functional Tests

**REQLOA-001** - Apply for a loan with valid inputs

- **Priority:** High
- **Preconditions:** None

- **Reads State:** account_list, loan_status
- **Writes State:** loan_status

**Pre-Verification Steps:**
1. Navigate to Loan section
2. Note current loan status

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Enter a valid Down Payment (e.g., 1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Post-Verification Steps:**
1. Navigate to Loan section
2. Verify loan status updated

**Expected Result:** Loan application is successfully submitted, and a confirmation message is displayed

---

#### Negative Tests

**REQLOA-002** - Internal error occurs during loan application

- **Priority:** High
- **Preconditions:** Simulate an internal error in the system

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Enter a valid Down Payment (e.g., 1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the loan application could not be processed due to an internal error

---

**REQLOA-003** - Leave Loan Amount field blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the Loan Amount field empty
2. Enter a valid Down Payment (e.g., 1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Loan Amount field is mandatory

---

**REQLOA-004** - Leave Down Payment field blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Leave the Down Payment field empty
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Down Payment field is mandatory

---

**REQLOA-005** - Leave From account number field blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Enter a valid Down Payment (e.g., 1000)
3. Leave the From account number field empty
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the From account number field is mandatory

---

#### Boundary/Edge Case Tests

**REQLOA-006** - Enter zero as Loan Amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter 0 as the Loan Amount
2. Enter a valid Down Payment (e.g., 1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Loan Amount must be greater than zero

---

**REQLOA-007** - Enter negative value as Down Payment

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Enter a negative value as Down Payment (e.g., -1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Down Payment must be a positive value

---

**REQLOA-008** - Enter special characters in Loan Amount field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters (e.g., @#$%) in the Loan Amount field
2. Enter a valid Down Payment (e.g., 1000)
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Loan Amount must be a numeric value

---

**REQLOA-009** - Enter special characters in Down Payment field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Loan Amount (e.g., 5000)
2. Enter special characters (e.g., @#$%) in the Down Payment field
3. Select a valid From account number from the dropdown
4. Click on the 'Apply Now' button

**Expected Result:** An error message is displayed indicating that the Down Payment must be a numeric value

---

---

### Logout

#### Functional Tests

**LOGOUT-001** - Verify successful logout redirects to login page

- **Priority:** High
- **Preconditions:** User is logged in

- **Reads State:** session_status
- **Writes State:** session_status
- **Verified By:** LOGOUT-003, ACCOVE-006, LOGOUT-002, BILPAY-001

**Pre-Verification Steps:**
1. Verify user is logged out initially

**Test Steps:**
1. Click on the 'Logout' button

**Post-Verification Steps:**
1. Verify user session state changed as expected

**Expected Result:** User is redirected to the login page

---

**LOGOUT-002** - Verify session data is cleared after logout

- **Priority:** High
- **Preconditions:** User is logged in

- **Reads State:** session_status
- **Writes State:** session_status
- **Verified By:** LOGOUT-003, ACCOVE-006, LOGOUT-001, BILPAY-001

**Pre-Verification Steps:**
1. Verify user is logged out initially

**Test Steps:**
1. Click on the 'Logout' button
2. Attempt to access a page that requires authentication

**Post-Verification Steps:**
1. Verify user session state changed as expected

**Expected Result:** Access to the page is denied, and the user is redirected to the login page

---

**LOGOUT-003** - Verify no account information is accessible after logout

- **Priority:** High
- **Preconditions:** User is logged in

- **Reads State:** session_status, user_profile
- **Writes State:** session_status
- **Verified By:** ACCOVE-006, LOGOUT-001, LOGOUT-002, BILPAY-001

**Pre-Verification Steps:**
1. Verify user is logged out initially

**Test Steps:**
1. Click on the 'Logout' button
2. Inspect browser storage (cookies, local storage, session storage) for any user-related data

**Post-Verification Steps:**
1. Verify user session state changed as expected

**Expected Result:** No account information or sensitive data is present in the browser storage

---

#### Negative Tests

**LOGOUT-004** - Verify logout functionality when session has already expired

- **Priority:** Medium
- **Preconditions:** User session has expired

**Test Steps:**
1. Click on the 'Logout' button

**Expected Result:** User is redirected to the login page without errors

---

**LOGOUT-005** - Verify logout functionality when user is not logged in

- **Priority:** Medium
- **Preconditions:** User is not logged in

**Test Steps:**
1. Click on the 'Logout' button

**Expected Result:** No action is performed, and the user remains on the current page or is redirected to the login page

---

#### Boundary/Edge Case Tests

**LOGOUT-006** - Verify logout button is functional when clicked multiple times

- **Priority:** Medium
- **Preconditions:** User is logged in

**Test Steps:**
1. Click on the 'Logout' button multiple times in quick succession

**Expected Result:** User is logged out successfully and redirected to the login page without errors

---

**LOGOUT-007** - Verify logout functionality when browser cookies are disabled

- **Priority:** Low
- **Preconditions:** User is logged in and browser cookies are disabled

**Test Steps:**
1. Click on the 'Logout' button

**Expected Result:** User is redirected to the login page, and no sensitive data remains accessible

---

---

## Verification Chain

This section shows which test cases verify the results of other tests.

| Test ID | Test Name | Writes State | Verified By |
|---------|-----------|--------------|-------------|
| LOGIN-001 | Login with valid username and password | session_status | ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, LOGOUT-003 |
| LOGIN-002 | Login with valid email and password | session_status | ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, LOGOUT-003 |
| REGIST-001 | Successful registration with valid inputs | user_profile, session_status | ACCOVE-006, BILPAY-001, LOGOUT-002, LOGOUT-001, FORPAS-001, UPDPRO-001, LOGOUT-003 |
| ONA-001 | Open a new account with valid account type and funding source | account_list, account_balance, transaction_history | BILPAY-001, FINTRA-003, FINTRA-007, REQLOA-001, ACCOVE-003, ACCOVE-001, FINTRA-005, ACCOVE-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001, TRAFUN-001 |
| TRAFUN-001 | Successful fund transfer with valid inputs | account_balance, transaction_history, transfer_details | ONA-001, BILPAY-001, FINTRA-003, FINTRA-007, ACCOVE-003, FINTRA-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001 |
| BILPAY-001 | Successful payment with valid inputs | account_balance, transaction_history, bill_payment_details | ONA-001, FINTRA-003, FINTRA-007, ACCOVE-003, FINTRA-005, FINTRA-006, ACCOVE-004, FINTRA-002, FINTRA-004, FINTRA-001, TRAFUN-001 |
| FINTRA-001 | Search for transaction with valid Transaction ID | transaction_search_results | FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-004 |
| FINTRA-002 | Search for transaction with alphanumeric Transaction ID | transaction_search_results | FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-004, FINTRA-001 |
| FINTRA-003 | Search transactions with valid date | transaction_search_results | FINTRA-007, FINTRA-005, FINTRA-006, FINTRA-002, FINTRA-004, FINTRA-001 |
| FINTRA-004 | Search transactions with valid date range | transaction_search_results | FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-007, FINTRA-001 |
| FINTRA-005 | Search transactions with valid amount | transaction_search_results | FINTRA-002, FINTRA-003, FINTRA-006, FINTRA-007, FINTRA-004, FINTRA-001 |
| FINTRA-006 | Search transactions with decimal amount | transaction_search_results | FINTRA-002, FINTRA-003, FINTRA-005, FINTRA-007, FINTRA-004, FINTRA-001 |
| FINTRA-007 | Search transactions with past date having no transactions | transaction_search_results | FINTRA-003, FINTRA-005, FINTRA-006, FINTRA-002, FINTRA-004, FINTRA-001 |
| UPDPRO-001 | Update profile with valid information | user_profile | LOGOUT-003, FORPAS-001 |
| LOGOUT-001 | Verify successful logout redirects to login page | session_status | LOGOUT-003, ACCOVE-006, LOGOUT-002, BILPAY-001 |
| LOGOUT-002 | Verify session data is cleared after logout | session_status | LOGOUT-003, ACCOVE-006, LOGOUT-001, BILPAY-001 |
| LOGOUT-003 | Verify no account information is accessible after logout | session_status | ACCOVE-006, LOGOUT-001, LOGOUT-002, BILPAY-001 |

## Navigation Graph

![Navigation Graph](output/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /login | No | 12 |
| Forgot Password | /forgot-password | No | 8 |
| Register | /register | No | 8 |
| Open New Account | /open-new-account | Yes | 8 |
| Account Overview | /accounts-overview | Yes | 9 |
| Transfer Funds | /transfer-funds | Yes | 10 |
| Bill Payments | /bill-payments | Yes | 9 |
| Find Transaction | /find-transaction | Yes | 34 |
| Update Profile | /update-profile | Yes | 8 |
| Request Loan | /request-loan | Yes | 9 |
| Logout | /logout | Yes | 7 |
