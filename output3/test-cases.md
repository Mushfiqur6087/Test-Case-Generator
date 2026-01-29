# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-01-29T19:47:51.486907

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 92 |

### By Type

| Type | Count |
|------|-------|
| Positive | 31 |
| Negative | 38 |
| Edge Case | 23 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 25 |
| Medium | 44 |
| Low | 23 |

### Post-Verification Coverage

| Metric | Count |
|--------|-------|
| Tests Needing Verification | 5 |
| Full Coverage | 2 |
| Partial Coverage | 3 |
| No Coverage | 0 |

#### Coverage Gaps

- The test case checks if the transaction is processed, but it does not explicitly verify the transfer status as successful.
- This test checks for the presence of an account number, which is part of the requirement, but does not verify the balance or the uniqueness of the account number.
- The test case checks for a confirmation message upon successful payment, which partially verifies the requirement. However, it does not explicitly check the payment_status.
- The test case verifies that the balance is displayed in the Account Overview module, but it does not specifically check for a $100 deduction.
- None of the test cases verify the specific requirement of checking both source and destination account balances for a transfer operation. They only verify the presence of balance information in the Account Overview.

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 5 |
| Automated Steps | 6 |
| Manual Steps | 1 |
| Automation Rate | 85.7% |

#### Coverage Distribution

| Coverage Level | Count |
|----------------|-------|
| Full | 2 |
| Partial | 2 |
| Minimal | 1 |
| None | 0 |

---

## Test Cases

### Login

#### Functional Tests

**LOGIN-001** - Successful login with valid username and password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid username
2. Enter a valid password
3. Click the Log In button

**Expected Result:** User is redirected to account dashboard

---

**LOGIN-002** - Successful login with valid email and password

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter a valid email address
2. Enter a valid password
3. Click the Log In button

**Expected Result:** User is redirected to account dashboard

---

#### Negative Tests

**LOGIN-003** - Error message displayed for invalid username

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid username
2. Enter a valid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-004** - Error message displayed for invalid email

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid email address
2. Enter a valid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-005** - Error message displayed for invalid password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid username
2. Enter an invalid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-006** - Error message displayed for both invalid username and password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid username
2. Enter an invalid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-007** - Error message displayed for both invalid email and password

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter an invalid email address
2. Enter an invalid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-008** - Login attempt with empty username and password fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the username field empty
2. Leave the password field empty
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

#### Boundary/Edge Case Tests

**LOGIN-009** - Login attempt with special characters in username

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a username with special characters
2. Enter a valid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

**LOGIN-010** - Login attempt with special characters in email

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter an email address with special characters
2. Enter a valid password
3. Click the Log In button

**Expected Result:** Error message is shown and input fields remain populated

---

---

### Forgot Password

#### Functional Tests

**FORPAS-001** - Successful recovery with valid customer details

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter valid first name
2. Enter valid last name
3. Enter valid address
4. Enter valid city
5. Select valid state
6. Enter valid zip code
7. Enter valid SSN
8. Click on Find My Login Info button

**Expected Result:** Recovery details displayed

---

#### Negative Tests

**FORPAS-002** - Error message displayed for non-matching customer details

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Enter non-matching first name
2. Enter non-matching last name
3. Enter non-matching address
4. Enter non-matching city
5. Select non-matching state
6. Enter non-matching zip code
7. Enter non-matching SSN
8. Click on Find My Login Info button

**Expected Result:** Error message displayed indicating no matching record found

---

**FORPAS-003** - Validation error when submitting with empty fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave all fields empty
2. Click on Find My Login Info button

**Expected Result:** Validation error indicating all fields must be completed

---

**FORPAS-004** - Validation error when submitting with partially filled fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter valid first name
2. Leave last name empty
3. Enter valid address
4. Leave city empty
5. Select valid state
6. Enter valid zip code
7. Leave SSN empty
8. Click on Find My Login Info button

**Expected Result:** Validation error indicating all fields must be completed

---

#### Boundary/Edge Case Tests

**FORPAS-005** - Successful recovery with minimum boundary values

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter minimum valid length first name
2. Enter minimum valid length last name
3. Enter minimum valid length address
4. Enter minimum valid length city
5. Select valid state
6. Enter minimum valid length zip code
7. Enter minimum valid length SSN
8. Click on Find My Login Info button

**Expected Result:** Recovery details displayed

---

**FORPAS-006** - Successful recovery with maximum boundary values

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter maximum valid length first name
2. Enter maximum valid length last name
3. Enter maximum valid length address
4. Enter maximum valid length city
5. Select valid state
6. Enter maximum valid length zip code
7. Enter maximum valid length SSN
8. Click on Find My Login Info button

**Expected Result:** Recovery details displayed

---

**FORPAS-007** - Error message displayed for special characters in fields

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters in first name
2. Enter special characters in last name
3. Enter special characters in address
4. Enter special characters in city
5. Select valid state
6. Enter special characters in zip code
7. Enter special characters in SSN
8. Click on Find My Login Info button

**Expected Result:** Error message displayed indicating invalid input

---

---

### Register

#### Functional Tests

**REGIST-001** - Register new account with valid details

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Click on the Register link
2. Enter a valid first name
3. Enter a valid last name
4. Enter a valid address
5. Enter a valid city
6. Select a valid state from the dropdown
7. Enter a valid zip code
8. Enter a valid phone number
9. Enter a valid SSN
10. Enter a valid username
11. Enter a valid password
12. Enter the same password in Confirm Password
13. Click on the Register button

**Expected Result:** System creates the new account and automatically logs the user in

---

#### Negative Tests

**REGIST-002** - Attempt registration with missing first name

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on the Register link
2. Leave the first name field empty
3. Enter a valid last name
4. Enter a valid address
5. Enter a valid city
6. Select a valid state from the dropdown
7. Enter a valid zip code
8. Enter a valid phone number
9. Enter a valid SSN
10. Enter a valid username
11. Enter a valid password
12. Enter the same password in Confirm Password
13. Click on the Register button

**Expected Result:** System displays an error message indicating that the first name is required

---

**REGIST-003** - Attempt registration with mismatched passwords

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on the Register link
2. Enter a valid first name
3. Enter a valid last name
4. Enter a valid address
5. Enter a valid city
6. Select a valid state from the dropdown
7. Enter a valid zip code
8. Enter a valid phone number
9. Enter a valid SSN
10. Enter a valid username
11. Enter a valid password
12. Enter a different password in Confirm Password
13. Click on the Register button

**Expected Result:** System displays an error message indicating that the passwords do not match

---

#### Boundary/Edge Case Tests

**REGIST-004** - Attempt registration with special characters in username

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Click on the Register link
2. Enter a valid first name
3. Enter a valid last name
4. Enter a valid address
5. Enter a valid city
6. Select a valid state from the dropdown
7. Enter a valid zip code
8. Enter a valid phone number
9. Enter a valid SSN
10. Enter a username with special characters
11. Enter a valid password
12. Enter the same password in Confirm Password
13. Click on the Register button

**Expected Result:** System displays an error message indicating that special characters are not allowed in the username

---

**REGIST-005** - Attempt registration with maximum length for each field

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Click on the Register link
2. Enter a first name with maximum allowed characters
3. Enter a last name with maximum allowed characters
4. Enter an address with maximum allowed characters
5. Enter a city with maximum allowed characters
6. Select a valid state from the dropdown
7. Enter a zip code with maximum allowed characters
8. Enter a phone number with maximum allowed characters
9. Enter an SSN with maximum allowed characters
10. Enter a username with maximum allowed characters
11. Enter a password with maximum allowed characters
12. Enter the same password in Confirm Password
13. Click on the Register button

**Expected Result:** System creates the new account and automatically logs the user in

---

---

### Open New Account

#### Functional Tests

**ONA-001** - Successfully open a new account with valid inputs

- **Priority:** High
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Select a valid account type
2. Select a valid funding source with sufficient balance
3. Click on Open New Account button

**Expected Result:** A new account is opened, $100.00 is deducted from the selected source account, credited to the new account, and a unique account number is generated

**Post-Verification Required:** ✓ (partial coverage)

| Verification | Status | Matched Test | Note |
|--------------|--------|--------------|------|
| Verify the new account appears in the ac... | ⚠ partial | ACCOVE-003 | Run this test after creating a new account to veri |
| Verify the source account balance is red... | ⚠ partial | ACCOVE-004 | Run this test after the action to verify the balan |

**Coverage Gaps:**
- ⚠ This test checks for the presence of an account number, which is part of the requirement, but does not verify the balance or the uniqueness of the account number.
- ⚠ The test case verifies that the balance is displayed in the Account Overview module, but it does not specifically check for a $100 deduction.


---

#### Negative Tests

**ONA-002** - Attempt to open a new account with insufficient funds

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Select a valid account type
2. Select a funding source with less than $100.00 balance
3. Click on Open New Account button

**Expected Result:** An error message is displayed indicating insufficient funds

---

**ONA-003** - Attempt to open a new account without selecting an account type

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Leave the account type unselected
2. Select a valid funding source with sufficient balance
3. Click on Open New Account button

**Expected Result:** An error message is displayed indicating that account type selection is required

---

**ONA-004** - Attempt to open a new account without selecting a funding source

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Select a valid account type
2. Leave the funding source unselected
3. Click on Open New Account button

**Expected Result:** An error message is displayed indicating that funding source selection is required

---

#### Boundary/Edge Case Tests

**ONA-005** - Open a new account with exactly $100.00 balance in the funding source

- **Priority:** Low
- **Preconditions:** User is logged in and on the Open New Account page

**Test Steps:**
1. Select a valid account type
2. Select a funding source with exactly $100.00 balance
3. Click on Open New Account button

**Expected Result:** A new account is opened, $100.00 is deducted from the selected source account, credited to the new account, and a unique account number is generated

---

---

### Account Overview

#### Functional Tests

**ACCOVE-001** - Verify Account Services sidebar is displayed

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if the Account Services sidebar is visible on the page

**Expected Result:** Account Services sidebar is displayed

---

**ACCOVE-002** - Verify all actions are listed in Account Services sidebar

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if all actions (Open New Account, Accounts Overview, Transfer Funds, Bill Pay, Find Transactions, Update Contact Info, Request Loan, Log Out) are listed in the Account Services sidebar

**Expected Result:** All actions are listed in the Account Services sidebar

---

**ACCOVE-003** - Verify Accounts Overview displays account number

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if the Accounts Overview section displays the account number

**Expected Result:** Account number is displayed in the Accounts Overview section

---

**ACCOVE-004** - Verify Accounts Overview displays Balance

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if the Accounts Overview section displays the Balance

**Expected Result:** Balance is displayed in the Accounts Overview section

---

**ACCOVE-005** - Verify Accounts Overview displays Available Amount

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if the Accounts Overview section displays the Available Amount

**Expected Result:** Available Amount is displayed in the Accounts Overview section

---

**ACCOVE-006** - Verify Accounts Overview displays combined total balance

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Check if the Accounts Overview section displays the combined total balance

**Expected Result:** Combined total balance is displayed in the Accounts Overview section

---

**ACCOVE-007** - Verify clicking 'Log Out' logs the user out

- **Priority:** High
- **Preconditions:** None

**Test Steps:**
1. Click on 'Log Out' in the Account Services sidebar

**Expected Result:** User is logged out and redirected to the login page

---

**ACCOVE-008** - Verify clicking 'Open New Account' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Open New Account' in the Account Services sidebar

**Expected Result:** User is navigated to the Open New Account page

---

**ACCOVE-009** - Verify clicking 'Transfer Funds' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Transfer Funds' in the Account Services sidebar

**Expected Result:** User is navigated to the Transfer Funds page

---

**ACCOVE-010** - Verify clicking 'Bill Pay' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Bill Pay' in the Account Services sidebar

**Expected Result:** User is navigated to the Bill Pay page

---

**ACCOVE-011** - Verify clicking 'Find Transactions' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Find Transactions' in the Account Services sidebar

**Expected Result:** User is navigated to the Find Transactions page

---

**ACCOVE-012** - Verify clicking 'Update Contact Info' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Update Contact Info' in the Account Services sidebar

**Expected Result:** User is navigated to the Update Contact Info page

---

**ACCOVE-013** - Verify clicking 'Request Loan' navigates to the correct page

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Click on 'Request Loan' in the Account Services sidebar

**Expected Result:** User is navigated to the Request Loan page

---

---

### Transfer Funds

#### Functional Tests

**TRAFUN-001** - Transfer funds with valid inputs

- **Priority:** High
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is processed

**Post-Verification Required:** ✓ (partial coverage)

| Verification | Status | Matched Test | Note |
|--------------|--------|--------------|------|
| Verify the transfer status is successful... | ⚠ partial | TRAFUN-006 | Run this test and verify if the transfer status is |
| Verify the source and destination accoun... | ✗ not_found | - | None of the test cases verify the specific require |

**Coverage Gaps:**
- ⚠ The test case checks if the transaction is processed, but it does not explicitly verify the transfer status as successful.
- ⚠ None of the test cases verify the specific requirement of checking both source and destination account balances for a transfer operation. They only verify the presence of balance information in the Account Overview.


---

#### Negative Tests

**TRAFUN-002** - Transfer funds with zero amount

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter zero as the amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is not processed and an error message is displayed

---

**TRAFUN-003** - Transfer funds with negative amount

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a negative amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is not processed and an error message is displayed

---

**TRAFUN-004** - Transfer funds with non-numeric amount

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a non-numeric value as the amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is not processed and an error message is displayed

---

**TRAFUN-005** - Transfer funds with same 'From' and 'To' account numbers

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter a valid amount
2. Select the same account for both 'From account number' and 'To account number'
3. Click on 'Transfer' button

**Expected Result:** Transaction is not processed and an error message is displayed

---

#### Boundary/Edge Case Tests

**TRAFUN-006** - Transfer funds with maximum allowable amount

- **Priority:** Low
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter the maximum allowable amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is processed

---

**TRAFUN-007** - Transfer funds with minimum allowable amount

- **Priority:** Low
- **Preconditions:** User is logged in and on the Transfer Funds page

**Test Steps:**
1. Enter the minimum allowable amount
2. Select a valid 'From account number'
3. Select a valid 'To account number'
4. Click on 'Transfer' button

**Expected Result:** Transaction is processed

---

---

### Bill Payments

#### Functional Tests

**BILPAY-001** - Successfully send payment with all valid inputs

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
8. Re-enter the valid account number for verification
9. Enter a valid amount
10. Select a valid from account number
11. Click on Send Payment

**Expected Result:** A confirmation message appears upon successful transfer

**Post-Verification Required:** ✓ (partial coverage)

| Verification | Status | Matched Test | Note |
|--------------|--------|--------------|------|
| Verify the payment status is successful... | ⚠ partial | BILPAY-005 | Run this test to verify that a confirmation messag |

**Coverage Gaps:**
- ⚠ The test case checks for a confirmation message upon successful payment, which partially verifies the requirement. However, it does not explicitly check the payment_status.


---

#### Negative Tests

**BILPAY-002** - Fail to send payment with mismatched account numbers

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter a valid phone number
7. Enter a valid account number
8. Enter a different account number for verification
9. Enter a valid amount
10. Select a valid from account number
11. Click on Send Payment

**Expected Result:** An error message appears indicating account numbers do not match

---

**BILPAY-003** - Fail to send payment with invalid phone number format

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid payee name
2. Enter a valid address
3. Enter a valid city
4. Select a valid state
5. Enter a valid zip code
6. Enter an invalid phone number format
7. Enter a valid account number
8. Re-enter the valid account number for verification
9. Enter a valid amount
10. Select a valid from account number
11. Click on Send Payment

**Expected Result:** An error message appears indicating invalid phone number format

---

**BILPAY-004** - Fail to send payment with empty required fields

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the payee name empty
2. Leave the address empty
3. Leave the city empty
4. Leave the state unselected
5. Leave the zip code empty
6. Leave the phone number empty
7. Leave the account number empty
8. Leave the verify account number empty
9. Leave the amount empty
10. Leave the from account number unselected
11. Click on Send Payment

**Expected Result:** An error message appears indicating required fields are missing

---

#### Boundary/Edge Case Tests

**BILPAY-005** - Successfully send payment with maximum length inputs

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter a payee name with maximum allowed characters
2. Enter an address with maximum allowed characters
3. Enter a city with maximum allowed characters
4. Select a valid state
5. Enter a zip code with maximum allowed characters
6. Enter a phone number with maximum allowed characters
7. Enter an account number with maximum allowed characters
8. Re-enter the account number with maximum allowed characters for verification
9. Enter the maximum allowed amount
10. Select a valid from account number
11. Click on Send Payment

**Expected Result:** A confirmation message appears upon successful transfer

---

---

### Find Transaction

#### Functional Tests

**FINTRA-001** - Search transactions with valid Transaction ID

- **Priority:** High
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a valid Transaction ID in the input field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-002** - Search transactions with valid date and account

- **Priority:** High
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a valid date in MM-DD-YYYY format in the Find by Date field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-003** - Search transactions with valid date range and account

- **Priority:** High
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Enter a valid start date in MM-DD-YYYY format
3. Enter a valid end date in MM-DD-YYYY format
4. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-004** - Search transactions with valid amount

- **Priority:** High
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a valid amount in the Find by Amount field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

#### Negative Tests

**FINTRA-005** - Attempt search with empty Transaction ID

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Leave the Transaction ID input field empty
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Transaction ID field

---

**FINTRA-006** - Attempt search with empty account selection

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Leave the account dropdown unselected
2. Enter a valid Transaction ID in the input field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the account dropdown

---

**FINTRA-007** - Search transactions with empty date field

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Leave the Find by Date field empty
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Date field

---

**FINTRA-008** - Search transactions with invalid date format

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter an invalid date format in the Find by Date field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Date field

---

**FINTRA-009** - Attempt search with empty date fields

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Leave the start date field empty
3. Leave the end date field empty
4. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the date fields

---

**FINTRA-010** - Attempt search with invalid date format

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Enter an invalid start date format
3. Enter an invalid end date format
4. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the date fields

---

**FINTRA-011** - Attempt search with only start date filled

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Enter a valid start date in MM-DD-YYYY format
3. Leave the end date field empty
4. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the end date field

---

**FINTRA-012** - Attempt search with only end date filled

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Leave the start date field empty
3. Enter a valid end date in MM-DD-YYYY format
4. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the start date field

---

**FINTRA-013** - Search transactions with empty amount field

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Leave the Find by Amount field empty
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Amount field

---

**FINTRA-014** - Search transactions with non-numeric amount

- **Priority:** Medium
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter non-numeric characters in the Find by Amount field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Amount field

---

#### Boundary/Edge Case Tests

**FINTRA-015** - Search transactions with special characters in Transaction ID

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a Transaction ID containing special characters in the input field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Transaction ID field

---

**FINTRA-016** - Search transactions with maximum length Transaction ID

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a Transaction ID with maximum allowed length in the input field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-017** - Search transactions with special characters in date field

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter special characters in the Find by Date field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Date field

---

**FINTRA-018** - Search transactions with boundary date value

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter a boundary date value in MM-DD-YYYY format in the Find by Date field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-019** - Search transactions with date range at boundary values

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select a valid account from the dropdown
2. Enter the earliest possible valid start date in MM-DD-YYYY format
3. Enter the latest possible valid end date in MM-DD-YYYY format
4. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

**FINTRA-020** - Search transactions with special characters in amount

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter special characters in the Find by Amount field
3. Click the Find Transactions button

**Expected Result:** Inline validation message appears next to the Find by Amount field

---

**FINTRA-021** - Search transactions with maximum allowable amount

- **Priority:** Low
- **Preconditions:** User is on the Find Transactions page

**Test Steps:**
1. Select an account from the dropdown
2. Enter the maximum allowable amount in the Find by Amount field
3. Click the Find Transactions button

**Expected Result:** System returns matching transactions in a results table

---

---

### Update Profile

#### Functional Tests

**UPDPRO-001** - Update profile with valid data

- **Priority:** High
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state from the dropdown
6. Enter a valid zip code
7. Enter a valid phone number
8. Click the Update Profile button

**Expected Result:** A confirmation message is shown upon successful submission

**Post-Verification Required:** ✓ (full coverage)

| Verification | Status | Matched Test | Note |
|--------------|--------|--------------|------|
| Verify the profile update status is succ... | ✓ found | UPDPRO-004 | Run this test after updating the profile to verify |


---

#### Negative Tests

**UPDPRO-002** - Update profile with empty first name

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Leave the first name field empty
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state from the dropdown
6. Enter a valid zip code
7. Enter a valid phone number
8. Click the Update Profile button

**Expected Result:** An error message is displayed indicating the first name is required

---

**UPDPRO-003** - Update profile with invalid phone number format

- **Priority:** Medium
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state from the dropdown
6. Enter a valid zip code
7. Enter an invalid phone number format
8. Click the Update Profile button

**Expected Result:** An error message is displayed indicating the phone number format is invalid

---

#### Boundary/Edge Case Tests

**UPDPRO-004** - Update profile with maximum length first name

- **Priority:** Low
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a first name with maximum allowed characters
2. Enter a valid last name
3. Enter a valid address
4. Enter a valid city
5. Select a valid state from the dropdown
6. Enter a valid zip code
7. Enter a valid phone number
8. Click the Update Profile button

**Expected Result:** A confirmation message is shown upon successful submission

---

**UPDPRO-005** - Update profile with special characters in address

- **Priority:** Low
- **Preconditions:** User is logged in and on the Update Profile page

**Test Steps:**
1. Enter a valid first name
2. Enter a valid last name
3. Enter an address with special characters
4. Enter a valid city
5. Select a valid state from the dropdown
6. Enter a valid zip code
7. Enter a valid phone number
8. Click the Update Profile button

**Expected Result:** A confirmation message is shown upon successful submission

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
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Loan is approved

**Post-Verification Required:** ✓ (full coverage)

| Verification | Status | Matched Test | Note |
|--------------|--------|--------------|------|
| Verify the loan application status is ap... | ✓ found | REQLOA-006 | Run this test after the action to verify the loan  |


---

#### Negative Tests

**REQLOA-002** - Attempt to apply for a loan with loan amount field left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the loan amount field blank
2. Enter a valid down payment
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Process is not completed

---

**REQLOA-003** - Attempt to apply for a loan with down payment field left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid loan amount
2. Leave the down payment field blank
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Process is not completed

---

**REQLOA-004** - Attempt to apply for a loan with from account number field left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Enter a valid loan amount
2. Enter a valid down payment
3. Leave the from account number field blank
4. Click on Apply Now button

**Expected Result:** Process is not completed

---

**REQLOA-005** - Attempt to apply for a loan with all fields left blank

- **Priority:** Medium
- **Preconditions:** None

**Test Steps:**
1. Leave the loan amount field blank
2. Leave the down payment field blank
3. Leave the from account number field blank
4. Click on Apply Now button

**Expected Result:** Process is not completed

---

#### Boundary/Edge Case Tests

**REQLOA-006** - Apply for a loan with maximum valid loan amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter the maximum valid loan amount
2. Enter a valid down payment
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Loan is approved

---

**REQLOA-007** - Apply for a loan with minimum valid loan amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter the minimum valid loan amount
2. Enter a valid down payment
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Loan is approved

---

**REQLOA-008** - Apply for a loan with special characters in loan amount

- **Priority:** Low
- **Preconditions:** None

**Test Steps:**
1. Enter special characters in the loan amount field
2. Enter a valid down payment
3. Select a valid from account number
4. Click on Apply Now button

**Expected Result:** Process is not completed

---

---

### Logout

#### Functional Tests

**LOGOUT-001** - Successful Logout

- **Priority:** High
- **Preconditions:** User is logged in

**Test Steps:**
1. Click on the logout button

**Expected Result:** User session ends, sensitive data is cleared, and user is returned to the login page

---

**LOGOUT-002** - Logout Session Termination

- **Priority:** High
- **Preconditions:** User is logged in

**Test Steps:**
1. Click on the logout button
2. Attempt to access a protected page

**Expected Result:** Access to the protected page is denied and user is redirected to the login page

---

**LOGOUT-003** - Logout Data Clearance

- **Priority:** High
- **Preconditions:** User is logged in and has sensitive data in session

**Test Steps:**
1. Click on the logout button
2. Check for the presence of sensitive data in session storage

**Expected Result:** Sensitive data is cleared from session storage

---

**LOGOUT-004** - Logout Redirect to Login Page

- **Priority:** High
- **Preconditions:** User is logged in

**Test Steps:**
1. Click on the logout button

**Expected Result:** User is redirected to the login page

---

**LOGOUT-005** - Logout Button Visibility

- **Priority:** Medium
- **Preconditions:** User is logged in

**Test Steps:**
1. Verify the visibility of the logout button

**Expected Result:** Logout button is visible

---

#### Negative Tests

**LOGOUT-006** - Logout Without Active Session

- **Priority:** Medium
- **Preconditions:** User is not logged in

**Test Steps:**
1. Attempt to click on the logout button

**Expected Result:** No action is performed and user remains on the current page

---

---

## Execution Plans

This section shows the recommended test execution sequence for each test case that requires post-verification.

### ONA-001: Successfully open a new account with valid inputs

**Coverage:** ⚠ Partial

**Verification Sequence:**

1. 🔄 **ACCOVE-003** - Verify Accounts Overview displays account number
   - *Purpose:* Verify the new account appears in the account summary
   - *Note:* Run this test after creating a new account to verify the account number appears in the Account Overview.
   - *Confidence:* 70%

2. 🔄 **ACCOVE-004** - Verify Accounts Overview displays Balance
   - *Purpose:* Verify the source account balance is reduced by $100.00
   - *Note:* Run this test after the action to verify the balance is displayed, but it does not check for the $100 deduction.
   - *Confidence:* 60%

**Quick Reference:** After executing ONA-001, run: ACCOVE-003 → ACCOVE-004

---

### TRAFUN-001: Transfer funds with valid inputs

**Coverage:** ⚠ Minimal

**Verification Sequence:**

1. 🔄 **TRAFUN-006** - Transfer funds with maximum allowable amount
   - *Purpose:* Verify the transfer status is successful
   - *Note:* Run this test and verify if the transfer status is marked as successful after processing.
   - *Confidence:* 60%

**Manual Verification Required:**

- ⚠ Verify the source and destination account balances are updated correctly
  - *Suggested:* Manually perform a transfer and check the source and destination account balances in the Account Overview to ensure they reflect the transfer amount correctly.
  - *Reason:* None of the test cases verify the specific requirement of checking both source and destination account balances for a transfer operation. They only verify the presence of balance information in the Account Overview.

**Quick Reference:** After executing TRAFUN-001, run: TRAFUN-006; Manual verification needed for 1 item(s)

---

### BILPAY-001: Successfully send payment with all valid inputs

**Coverage:** ⚠ Partial

**Verification Sequence:**

1. 🔄 **BILPAY-005** - Successfully send payment with maximum length inputs
   - *Purpose:* Verify the payment status is successful
   - *Note:* Run this test to verify that a confirmation message appears, indicating a successful payment.
   - *Confidence:* 70%

**Quick Reference:** After executing BILPAY-001, run: BILPAY-005

---

### UPDPRO-001: Update profile with valid data

**Coverage:** ✓ Full

**Verification Sequence:**

1. ▶️ **UPDPRO-004** - Update profile with maximum length first name
   - *Purpose:* Verify the profile update status is successful
   - *Note:* Run this test after updating the profile to verify the confirmation message is displayed.
   - *Confidence:* 90%

**Quick Reference:** After executing UPDPRO-001, run: UPDPRO-004

---

### REQLOA-001: Apply for a loan with all fields filled correctly

**Coverage:** ✓ Full

**Verification Sequence:**

1. ▶️ **REQLOA-006** - Apply for a loan with maximum valid loan amount
   - *Purpose:* Verify the loan application status is approved
   - *Note:* Run this test after the action to verify the loan application status is marked as approved.
   - *Confidence:* 90%

**Quick Reference:** After executing REQLOA-001, run: REQLOA-006

---

## Navigation Graph

![Navigation Graph](output3/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /login | No | 10 |
| Forgot Password | /forgot-password | No | 7 |
| Register | /register | No | 5 |
| Open New Account | /open-new-account | Yes | 5 |
| Account Overview | /account-overview | Yes | 13 |
| Transfer Funds | /transfer-funds | Yes | 7 |
| Bill Payments | /bill-payments | Yes | 5 |
| Find Transaction | /find-transaction | Yes | 21 |
| Update Profile | /update-profile | Yes | 5 |
| Request Loan | /request-loan | Yes | 8 |
| Logout | /logout | Yes | 6 |
