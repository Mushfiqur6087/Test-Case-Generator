# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-01-23T09:48:49.739829

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 112 |

### By Type

| Type | Count |
|------|-------|
| Positive | 28 |
| Negative | 59 |
| Edge Case | 25 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 75 |
| Medium | 12 |
| Low | 25 |

---

## Test Cases

### Login

#### Functional Tests

**LOGIN-001** - Successful login with valid username and password

- **Priority:** High
- **Preconditions:** User has a registered account with valid credentials

**Test Steps:**
1. Enter a valid username in the username field
2. Enter a valid password in the password field
3. Click on the Log In button

**Expected Result:** User is redirected to the account dashboard

---

**LOGIN-002** - Successful login with valid email and password

- **Priority:** High
- **Preconditions:** User has a registered account with valid credentials

**Test Steps:**
1. Enter a valid email address in the username field
2. Enter a valid password in the password field
3. Click on the Log In button

**Expected Result:** User is redirected to the account dashboard

---

#### Negative Tests

**LOGIN-003** - Error message displayed for empty username

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the username field empty
2. Enter a valid password in the password field
3. Click on the Log In button

**Expected Result:** Error message is displayed indicating that both fields must be populated

---

**LOGIN-004** - Error message displayed for empty password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid username in the username field
2. Leave the password field empty
3. Click on the Log In button

**Expected Result:** Error message is displayed indicating that both fields must be populated

---

**LOGIN-005** - Error message displayed for invalid credentials

- **Priority:** Medium
- **Preconditions:** User has an account but uses incorrect credentials

**Test Steps:**
1. Enter an invalid username in the username field
2. Enter an invalid password in the password field
3. Click on the Log In button

**Expected Result:** Error message is displayed indicating invalid credentials, input fields remain populated

---

**LOGIN-006** - Error message displayed for partially filled fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid username in the username field
2. Leave the password field empty
3. Click on the Log In button

**Expected Result:** Error message is displayed indicating that both fields must be populated

---

#### Boundary/Edge Case Tests

**LOGIN-007** - Login attempt with special characters in username and password

- **Priority:** Low
- **Preconditions:** User has a registered account with valid credentials

**Test Steps:**
1. Enter a valid username with special characters in the username field
2. Enter a valid password with special characters in the password field
3. Click on the Log In button

**Expected Result:** User is redirected to the account dashboard

---

**LOGIN-008** - Login attempt with maximum length username and password

- **Priority:** Low
- **Preconditions:** User has a registered account with valid credentials

**Test Steps:**
1. Enter a username at maximum length in the username field
2. Enter a password at maximum length in the password field
3. Click on the Log In button

**Expected Result:** User is redirected to the account dashboard

---

---

### Forgot Password

#### Functional Tests

**FORPAS-001** - Submit with all fields filled correctly

- **Priority:** High
- **Preconditions:** All fields are filled with valid information

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid SSN
8. Click on 'Find My Login Info' button

**Expected Result:** The page displays the appropriate recovery details

---

#### Negative Tests

**FORPAS-002** - Submit with one field left blank

- **Priority:** High
- **Preconditions:** All fields are filled except one

**Test Steps:**
1. Enter a valid first name
2. Leave last name blank
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid SSN
8. Click on 'Find My Login Info' button

**Expected Result:** The page prompts the user to complete the blank field

---

**FORPAS-003** - Submit with all fields left blank

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave all fields blank
2. Click on 'Find My Login Info' button

**Expected Result:** The page prompts the user to complete all fields

---

**FORPAS-004** - Submit with non-matching information

- **Priority:** High
- **Preconditions:** All fields are filled with non-matching information

**Test Steps:**
1. Enter a valid first name that does not match any record
2. Enter a valid last name that does not match any record
3. Enter a valid address that does not match any record
4. Enter a valid city that does not match any record
5. Select a valid state that does not match any record
6. Enter a valid zip code that does not match any record
7. Enter a valid SSN that does not match any record
8. Click on 'Find My Login Info' button

**Expected Result:** The page displays an error indicating no matching record found

---

#### Boundary/Edge Case Tests

**FORPAS-005** - Submit with maximum length inputs

- **Priority:** Low
- **Preconditions:** All fields are filled with maximum length valid information

**Test Steps:**
1. Enter a valid first name at maximum length
2. Enter a valid last name at maximum length
3. Enter a valid address at maximum length
4. Enter a valid city at maximum length
5. Select a valid state
6. Enter a valid zip code at maximum length
7. Enter a valid SSN at maximum length
8. Click on 'Find My Login Info' button

**Expected Result:** The page displays the appropriate recovery details

---

**FORPAS-006** - Submit with special characters in fields

- **Priority:** Low
- **Preconditions:** All fields are filled with valid information including special characters

**Test Steps:**
1. Enter a valid first name with special characters
2. Enter a valid last name with special characters
3. Enter a valid address with special characters
4. Enter a valid city with special characters
5. Select a valid state
6. Enter a valid zip code with special characters
7. Enter a valid SSN with special characters
8. Click on 'Find My Login Info' button

**Expected Result:** The page displays the appropriate recovery details

---

---

### Register

#### Functional Tests

**REGIST-001** - Successful account registration

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** User account is created and user is automatically logged in

---

#### Negative Tests

**REGIST-002** - Registration with missing first name

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the first name field empty
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating first name is mandatory

---

**REGIST-003** - Registration with missing last name

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Leave the last name field empty
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating last name is mandatory

---

**REGIST-004** - Registration with missing address

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Leave the address field empty
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating address is mandatory

---

**REGIST-005** - Registration with missing city

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Leave the city field empty
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating city is mandatory

---

**REGIST-006** - Registration with missing state

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Leave the state field empty
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating state is mandatory

---

**REGIST-007** - Registration with missing zip code

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Leave the zip code field empty
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating zip code is mandatory

---

**REGIST-008** - Registration with missing phone number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Leave the phone number field empty
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating phone number is mandatory

---

**REGIST-009** - Registration with missing SSN

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Leave the SSN field empty
9. Enter a valid username
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating SSN is mandatory

---

**REGIST-010** - Registration with missing username

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Leave the username field empty
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating username is mandatory

---

**REGIST-011** - Registration with missing password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Leave the password field empty
11. Confirm the valid password
12. Click the Register button

**Expected Result:** Error message indicating password is mandatory

---

**REGIST-012** - Registration with missing confirm password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Leave the confirm password field empty
12. Click the Register button

**Expected Result:** Error message indicating confirm password is mandatory

---

**REGIST-013** - Registration with mismatched passwords

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a valid username
10. Enter a valid password
11. Enter a different password in confirm password
12. Click the Register button

**Expected Result:** Error message indicating passwords do not match

---

#### Boundary/Edge Case Tests

**REGIST-014** - Registration with special characters in username

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Enter a valid SSN
9. Enter a username with special characters
10. Enter a valid password
11. Confirm the valid password
12. Click the Register button

**Expected Result:** User account is created and user is automatically logged in

---

**REGIST-015** - Registration with maximum length inputs

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid first name with maximum length
2. Enter a valid last name with maximum length
3. Enter a valid address with maximum length
4. Enter a valid city with maximum length
5. Select a valid state
6. Enter a valid zip code with maximum length
7. Enter a valid phone number with maximum length
8. Enter a valid SSN with maximum length
9. Enter a valid username with maximum length
10. Enter a valid password with maximum length
11. Confirm the valid password with maximum length
12. Click the Register button

**Expected Result:** User account is created and user is automatically logged in

---

---

### Open New Account

#### Functional Tests

**ONA-001** - Open New Account with valid account type and funding source

- **Priority:** High
- **Preconditions:** User is logged in and has a valid funding source account

**Test Steps:**
1. Click on 'Open New Account' button
2. Select 'Savings' as the account type
3. Select an existing account as the funding source
4. Enter the required opening deposit amount
5. Click on 'Open New Account' button

**Expected Result:** A new account is created, $100.00 is deducted from the funding source, and a unique account number is generated

---

#### Negative Tests

**ONA-002** - Open New Account without selecting a funding source

- **Priority:** High
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Click on 'Open New Account' button
2. Select 'Checking' as the account type
3. Leave funding source unselected
4. Enter the required opening deposit amount
5. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that a funding source must be selected

---

**ONA-003** - Open New Account with insufficient opening deposit

- **Priority:** High
- **Preconditions:** User is logged in and has a valid funding source account

**Test Steps:**
1. Click on 'Open New Account' button
2. Select 'Savings' as the account type
3. Select an existing account as the funding source
4. Enter an amount less than $100.00 as the opening deposit
5. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that the opening deposit must be $100.00

---

**ONA-004** - Open New Account with invalid funding source

- **Priority:** High
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Click on 'Open New Account' button
2. Select 'Savings' as the account type
3. Select a non-existing account as the funding source
4. Enter the required opening deposit amount
5. Click on 'Open New Account' button

**Expected Result:** An error message is displayed indicating that the selected funding source is invalid

---

#### Boundary/Edge Case Tests

**ONA-005** - Open New Account with special characters in account type

- **Priority:** Low
- **Preconditions:** User is logged in and has a valid funding source account

**Test Steps:**
1. Click on 'Open New Account' button
2. Select an account type with special characters
3. Select an existing account as the funding source
4. Enter the required opening deposit amount
5. Click on 'Open New Account' button

**Expected Result:** The system processes the request and creates a new account with the specified account type

---

**ONA-006** - Open New Account with maximum length account type

- **Priority:** Low
- **Preconditions:** User is logged in and has a valid funding source account

**Test Steps:**
1. Click on 'Open New Account' button
2. Select an account type with maximum allowed length
3. Select an existing account as the funding source
4. Enter the required opening deposit amount
5. Click on 'Open New Account' button

**Expected Result:** The system processes the request and creates a new account with the specified account type

---

---

### Account Overview

#### Functional Tests

**ACCOVE-001** - Verify Account Services sidebar is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Account Services sidebar
2. Verify that the sidebar is visible
3. Check that all actions are listed in the sidebar

**Expected Result:** Account Services sidebar is displayed with all actions listed

---

**ACCOVE-002** - Verify Open New Account action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Open New Account action in the Account Services sidebar
2. Verify that the Open New Account action is clickable

**Expected Result:** Open New Account action is available and clickable

---

**ACCOVE-003** - Verify Accounts Overview action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Accounts Overview action in the Account Services sidebar
2. Verify that the Accounts Overview action is clickable

**Expected Result:** Accounts Overview action is available and clickable

---

**ACCOVE-004** - Verify Transfer Funds action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Transfer Funds action in the Account Services sidebar
2. Verify that the Transfer Funds action is clickable

**Expected Result:** Transfer Funds action is available and clickable

---

**ACCOVE-005** - Verify Bill Pay action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Bill Pay action in the Account Services sidebar
2. Verify that the Bill Pay action is clickable

**Expected Result:** Bill Pay action is available and clickable

---

**ACCOVE-006** - Verify Find Transactions action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Find Transactions action in the Account Services sidebar
2. Verify that the Find Transactions action is clickable

**Expected Result:** Find Transactions action is available and clickable

---

**ACCOVE-007** - Verify Update Contact Info action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Update Contact Info action in the Account Services sidebar
2. Verify that the Update Contact Info action is clickable

**Expected Result:** Update Contact Info action is available and clickable

---

**ACCOVE-008** - Verify Request Loan action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Request Loan action in the Account Services sidebar
2. Verify that the Request Loan action is clickable

**Expected Result:** Request Loan action is available and clickable

---

**ACCOVE-009** - Verify Log Out action is available

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Log Out action in the Account Services sidebar
2. Verify that the Log Out action is clickable

**Expected Result:** Log Out action is available and clickable

---

**ACCOVE-010** - Verify account number is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the account number element
2. Verify that the account number is visible

**Expected Result:** Account number is displayed

---

**ACCOVE-011** - Verify Balance is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Balance element
2. Verify that the Balance is visible

**Expected Result:** Balance is displayed

---

**ACCOVE-012** - Verify Available Amount is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the Available Amount element
2. Verify that the Available Amount is visible

**Expected Result:** Available Amount is displayed

---

**ACCOVE-013** - Verify combined total balance is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the combined total balance element
2. Verify that the combined total balance is visible

**Expected Result:** Combined total balance is displayed

---

---

### Transfer Funds

#### Functional Tests

**TRAFUN-001** - Transfer funds with valid details

- **Priority:** High
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount in the Amount field
2. Select a valid account number from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Funds are successfully transferred and a confirmation message is displayed

---

#### Negative Tests

**TRAFUN-002** - Transfer funds with zero amount

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter '0' in the Amount field
2. Select a valid account number from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Error message is displayed indicating that the amount must be greater than zero

---

**TRAFUN-003** - Transfer funds with negative amount

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a negative amount in the Amount field
2. Select a valid account number from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Error message is displayed indicating that the amount must be greater than zero

---

**TRAFUN-004** - Transfer funds with invalid From account number

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount in the Amount field
2. Select an invalid account number from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Error message is displayed indicating that the From account number is invalid

---

**TRAFUN-005** - Transfer funds with invalid To account number

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount in the Amount field
2. Select a valid account number from the From account number dropdown
3. Select an invalid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Error message is displayed indicating that the To account number is invalid

---

#### Boundary/Edge Case Tests

**TRAFUN-006** - Transfer funds with maximum allowable amount

- **Priority:** Low
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter the maximum allowable amount in the Amount field
2. Select a valid account number from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Funds are successfully transferred and a confirmation message is displayed

---

**TRAFUN-007** - Transfer funds with special characters in account numbers

- **Priority:** Low
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount in the Amount field
2. Select an account number containing special characters from the From account number dropdown
3. Select a valid account number from the To account number dropdown
4. Click on the Transfer button

**Expected Result:** Error message is displayed indicating that the From account number contains invalid characters

---

---

### Bill Payments

#### Functional Tests

**BILPAY-001** - Successful payment submission with all fields completed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Confirmation message appears upon successful transfer

---

#### Negative Tests

**BILPAY-002** - Error message for missing payee name

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the payee name field empty
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the payee name is required

---

**BILPAY-003** - Error message for missing address

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Leave the address field empty
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the address is required

---

**BILPAY-004** - Error message for missing city

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Leave the city field empty
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the city is required

---

**BILPAY-005** - Error message for missing state

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Leave the state field empty
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the state is required

---

**BILPAY-006** - Error message for missing zip code

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Leave the zip code field empty
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the zip code is required

---

**BILPAY-007** - Error message for missing phone number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Leave the phone number field empty
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the phone number is required

---

**BILPAY-008** - Error message for missing account number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Leave the account number field empty
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the account number is required

---

**BILPAY-009** - Error message for mismatched account numbers

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a different verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the account numbers do not match

---

**BILPAY-010** - Error message for missing amount

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Leave the amount field empty
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the amount is required

---

**BILPAY-011** - Error message for missing from account number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Leave the from account number field empty
11. Click on the Send Payment button

**Expected Result:** Error message indicates that the from account number is required

---

#### Boundary/Edge Case Tests

**BILPAY-012** - Edge case for maximum length of payee name

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name at maximum length
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Confirmation message appears upon successful transfer

---

**BILPAY-013** - Edge case for special characters in address

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address with special characters
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a matching valid verify account number
9. Enter a valid amount
10. Select a valid from account number
11. Click on the Send Payment button

**Expected Result:** Confirmation message appears upon successful transfer

---

---

### Find Transaction

#### Functional Tests

**FINTRA-001** - Search for transaction with valid Transaction ID

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid Transaction ID in the input field
2. Click on the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table

---

**FINTRA-002** - Search for transactions with a valid date

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Enter a valid date in MM-DD-YYYY format
3. Click on the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table

---

**FINTRA-003** - Search for transactions with valid date range

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid start date in MM-DD-YYYY format in the date range input field
2. Enter a valid end date in MM-DD-YYYY format in the date range input field
3. Click the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table

---

**FINTRA-004** - Search for transactions with a valid amount

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for 'Find by Amount'
2. Enter a valid transaction amount into the input field
3. Click the 'Find Transactions' button

**Expected Result:** Matching transactions are displayed in the results table

---

#### Negative Tests

**FINTRA-005** - Search for transaction with empty Transaction ID

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the Transaction ID input field empty
2. Click on the Find Transactions button

**Expected Result:** Inline validation message appears next to the input field indicating that the field is required

---

**FINTRA-006** - Search for transaction with invalid Transaction ID format

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid Transaction ID format in the input field
2. Click on the Find Transactions button

**Expected Result:** Inline validation message appears next to the input field indicating that the input is invalid

---

**FINTRA-007** - Attempt to search without entering a date

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Leave the input field empty
3. Click on the Find Transactions button

**Expected Result:** An inline validation message appears next to the field indicating that the date is required

---

**FINTRA-008** - Attempt to search with an invalid date format

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Enter an invalid date format
3. Click on the Find Transactions button

**Expected Result:** An inline validation message appears next to the field indicating that the date format is invalid

---

**FINTRA-009** - Attempt to search with empty date range fields

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave the start date input field empty
2. Leave the end date input field empty
3. Click the Find Transactions button

**Expected Result:** Inline validation messages appear next to both fields indicating they are required

---

**FINTRA-010** - Attempt to search with invalid date format

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid start date format in the date range input field
2. Enter an invalid end date format in the date range input field
3. Click the Find Transactions button

**Expected Result:** Inline validation messages appear next to both fields indicating the format is incorrect

---

**FINTRA-011** - Search for transactions with start date greater than end date

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid start date that is later than the end date in MM-DD-YYYY format in the date range input field
2. Enter a valid end date in MM-DD-YYYY format in the date range input field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears indicating that the start date must be before the end date

---

**FINTRA-012** - Attempt to search with an empty amount field

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for 'Find by Amount'
2. Leave the input field empty
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the field indicating that the amount is required

---

**FINTRA-013** - Search for transactions with a date containing special characters

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Enter a date with special characters
3. Click on the Find Transactions button

**Expected Result:** An inline validation message appears next to the field indicating that the date format is invalid

---

**FINTRA-014** - Attempt to search with an invalid amount format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for 'Find by Amount'
2. Enter an invalid amount format into the input field (e.g., letters or special characters)
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the field indicating that the input is invalid

---

#### Boundary/Edge Case Tests

**FINTRA-015** - Search for transaction with special characters in Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters in the Transaction ID input field
2. Click on the Find Transactions button

**Expected Result:** Inline validation message appears next to the input field indicating that the input is invalid

---

**FINTRA-016** - Search for transaction with maximum length Transaction ID

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a Transaction ID that reaches the maximum allowed length in the input field
2. Click on the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table if the input is valid

---

**FINTRA-017** - Search for transactions with a date in the future

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Enter a future date in MM-DD-YYYY format
3. Click on the Find Transactions button

**Expected Result:** No transactions are displayed, or a message indicating no transactions found appears

---

**FINTRA-018** - Search for transactions with a date at the boundary of valid input

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for date
2. Enter a date that is the earliest valid date in MM-DD-YYYY format
3. Click on the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table or a message indicating no transactions found appears

---

**FINTRA-019** - Search for transactions with special characters in date fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a start date with special characters in the date range input field
2. Enter an end date with special characters in the date range input field
3. Click the Find Transactions button

**Expected Result:** Inline validation messages appear next to both fields indicating the format is incorrect

---

**FINTRA-020** - Search for transactions with maximum length date input

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a start date with the maximum allowed length in MM-DD-YYYY format in the date range input field
2. Enter an end date with the maximum allowed length in MM-DD-YYYY format in the date range input field
3. Click the Find Transactions button

**Expected Result:** Matching transactions are displayed in the results table

---

**FINTRA-021** - Search for transactions with a negative amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for 'Find by Amount'
2. Enter a negative transaction amount into the input field
3. Click the 'Find Transactions' button

**Expected Result:** An inline validation message appears next to the field indicating that the amount must be positive

---

**FINTRA-022** - Search for transactions with a very large amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Locate the input field for 'Find by Amount'
2. Enter a very large transaction amount into the input field
3. Click the 'Find Transactions' button

**Expected Result:** Matching transactions are displayed in the results table if valid, or an inline validation message if not

---

---

### Update Profile

#### Functional Tests

**UPDPRO-001** - Update profile with valid information

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Confirmation message is shown upon successful submission

---

#### Negative Tests

**UPDPRO-002** - Attempt to update profile with missing first name

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Leave the first name field empty
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the first name is required is displayed

---

**UPDPRO-003** - Attempt to update profile with missing last name

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Leave the last name field empty
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the last name is required is displayed

---

**UPDPRO-004** - Attempt to update profile with missing address

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Leave the address field empty
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the address is required is displayed

---

**UPDPRO-005** - Attempt to update profile with missing city

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Leave the city field empty
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the city is required is displayed

---

**UPDPRO-006** - Attempt to update profile with missing state

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Leave the state field empty
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the state is required is displayed

---

**UPDPRO-007** - Attempt to update profile with missing zip code

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Leave the zip code field empty
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the zip code is required is displayed

---

**UPDPRO-008** - Attempt to update profile with missing phone number

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Leave the phone number field empty
8. Click on the Update Profile button

**Expected Result:** Error message indicating that the phone number is required is displayed

---

#### Boundary/Edge Case Tests

**UPDPRO-009** - Update profile with special characters in first name

- **Priority:** Low
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a first name with special characters
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state
6. Enter a valid zip code
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Confirmation message is shown upon successful submission

---

**UPDPRO-010** - Update profile with maximum length values

- **Priority:** Low
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a first name at maximum length
2. Enter a last name at maximum length
3. Enter an address at maximum length
4. Enter a city at maximum length
5. Select a valid state
6. Enter a zip code at maximum length
7. Enter a valid phone number
8. Click on the Update Profile button

**Expected Result:** Confirmation message is shown upon successful submission

---

---

### Request Loan

#### Functional Tests

**REQLOA-001** - Apply for a loan with all fields filled correctly

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid loan amount
2. Enter a valid down payment
3. Enter a valid from account number
4. Click on Apply Now

**Expected Result:** Loan application is successfully submitted and approved

---

#### Negative Tests

**REQLOA-002** - Attempt to apply for a loan with blank loan amount

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Leave loan amount field blank
2. Enter a valid down payment
3. Enter a valid from account number
4. Click on Apply Now

**Expected Result:** Error message is displayed indicating loan amount is mandatory

---

**REQLOA-003** - Attempt to apply for a loan with blank down payment

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid loan amount
2. Leave down payment field blank
3. Enter a valid from account number
4. Click on Apply Now

**Expected Result:** Error message is displayed indicating down payment is mandatory

---

**REQLOA-004** - Attempt to apply for a loan with blank from account number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid loan amount
2. Enter a valid down payment
3. Leave from account number field blank
4. Click on Apply Now

**Expected Result:** Error message is displayed indicating from account number is mandatory

---

#### Boundary/Edge Case Tests

**REQLOA-005** - Apply for a loan with special characters in loan amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a loan amount with special characters
2. Enter a valid down payment
3. Enter a valid from account number
4. Click on Apply Now

**Expected Result:** Error message is displayed indicating loan amount is invalid

---

**REQLOA-006** - Apply for a loan with maximum length of loan amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a loan amount at maximum allowed length
2. Enter a valid down payment
3. Enter a valid from account number
4. Click on Apply Now

**Expected Result:** Loan application is successfully submitted and approved

---

---

### Logout

#### Functional Tests

**LOGOUT-001** - Successful Logout

- **Priority:** High
- **Preconditions:** User is logged into the application

**Test Steps:**
1. Locate and click the logout button

**Expected Result:** User is returned to the login page

---

**LOGOUT-002** - Session Data Cleared After Logout

- **Priority:** High
- **Preconditions:** User is logged into the application

**Test Steps:**
1. Click the logout button
2. Attempt to access a protected page

**Expected Result:** User is redirected to the login page and cannot access the protected page

---

#### Negative Tests

**LOGOUT-003** - Access Account Information After Logout

- **Priority:** High
- **Preconditions:** User is logged into the application

**Test Steps:**
1. Click the logout button
2. Attempt to access account information page

**Expected Result:** Access is denied and user is redirected to the login page

---

**LOGOUT-004** - Session Persistence Check After Logout

- **Priority:** Medium
- **Preconditions:** User is logged into the application

**Test Steps:**
1. Click the logout button
2. Check if session storage or cookies still contain user data

**Expected Result:** No user data remains in session storage or cookies

---

**LOGOUT-005** - Logout Without Prior Login

- **Priority:** Medium
- **Preconditions:** User is not logged into the application

**Test Steps:**
1. Locate and click the logout button

**Expected Result:** No action is performed and user remains on the current page

---

#### Boundary/Edge Case Tests

**LOGOUT-006** - Logout with Special Characters in Session

- **Priority:** Low
- **Preconditions:** User is logged into the application with special characters in session data

**Test Steps:**
1. Click the logout button

**Expected Result:** User is returned to the login page and no session data remains

---

---

## Navigation Graph

![Navigation Graph](output/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /login | No | 8 |
| Forgot Password | /forgot-password | No | 6 |
| Register | /register | No | 15 |
| Open New Account | /open-new-account | Yes | 6 |
| Account Overview | /accounts-overview | Yes | 13 |
| Transfer Funds | /transfer-funds | No | 7 |
| Bill Payments | /bill-pay | No | 13 |
| Find Transaction | /find-transaction | No | 22 |
| Update Profile | /update-profile | Yes | 10 |
| Request Loan | /request-loan | No | 6 |
| Logout | /logout | Yes | 6 |
