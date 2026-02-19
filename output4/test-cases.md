# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-02-19T21:37:33.296672

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 111 |

### By Type

| Type | Count |
|------|-------|
| Positive | 26 |
| Negative | 66 |
| Edge Case | 19 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 27 |
| Medium | 64 |
| Low | 20 |

### Post-Verification Coverage

| Metric | Count |
|--------|-------|
| Tests Needing Verification | 7 |
| Full Coverage | 3 |
| Partial Coverage | 2 |
| No Coverage | 2 |

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 7 |
| Automated Steps | 12 |
| Manual Steps | 4 |
| Automation Rate | 75.0% |

---

## Test Cases

### Login

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login with username | None | 1. Enter a valid username<br>2. Enter a valid password<br>3. Click the Log In button | User is taken to their account dashboard | High |
| LOGIN-002 | Successful login with email | None | 1. Enter a valid email<br>2. Enter a valid password<br>3. Click the Log In button | User is taken to their account dashboard | High |
| LOGIN-008 | Login page elements display correctly | None | 1. Verify the presence of the username or email field<br>2. Verify the presence of the password field<br>3. Verify the presence of the Log In button<br>4. Verify the presence of the Forgot login info? link<br>5. Verify the presence of the Register link | All elements are displayed correctly on the login page | Low |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-003 | Invalid credentials | None | 1. Enter an invalid username or email<br>2. Enter an invalid password<br>3. Click the Log In button | Error is shown if credentials do not match | High |
| LOGIN-004 | Username field empty | None | 1. Leave the username field empty<br>2. Enter a valid password<br>3. Click the Log In button | Error is shown indicating missing username | Medium |
| LOGIN-005 | Email field empty | None | 1. Leave the email field empty<br>2. Enter a valid password<br>3. Click the Log In button | Error is shown indicating missing email | Medium |
| LOGIN-006 | Password field empty | None | 1. Enter a valid username or email<br>2. Leave the password field empty<br>3. Click the Log In button | Error is shown indicating missing password | Medium |
| LOGIN-007 | Fields remain populated on error | None | 1. Enter an invalid username or email<br>2. Enter an invalid password<br>3. Click the Log In button | Both input fields remain populated on error | Medium |

---

### Forgot Password

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-001 | Successful recovery with valid customer details | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Recovery details displayed | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-002 | No matching record found | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN that does not match any record<br>8. Click on Find My Login Info button | Error displayed indicating no matching record found | High |
| FORPAS-003 | First Name field empty | None | 1. Leave First Name field empty<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating First Name is required | Medium |
| FORPAS-004 | Last Name field empty | None | 1. Enter valid first name<br>2. Leave Last Name field empty<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating Last Name is required | Medium |
| FORPAS-005 | Address field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Leave Address field empty<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating Address is required | Medium |
| FORPAS-006 | City field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Leave City field empty<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating City is required | Medium |
| FORPAS-007 | State field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Leave State field empty<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating State is required | Medium |
| FORPAS-008 | Zip Code field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Leave Zip Code field empty<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Error displayed indicating Zip Code is required | Medium |
| FORPAS-009 | SSN field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Enter valid state<br>6. Enter valid zip code<br>7. Leave SSN field empty<br>8. Click on Find My Login Info button | Error displayed indicating SSN is required | Medium |

---

### Register

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-001 | Successful registration with valid data | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Enter a valid SSN<br>9. Enter a valid username<br>10. Enter a valid password<br>11. Enter the same password in Confirm Password<br>12. Click the Register button | Account is created and user is logged in | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-002 | First Name field empty | None | 1. Leave the First Name field empty<br>2. Enter valid data in all other fields<br>3. Click the Register button | Error message displayed indicating First Name is required | Medium |
| REGIST-003 | Last Name field empty | None | 1. Enter a valid first name<br>2. Leave the Last Name field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating Last Name is required | Medium |
| REGIST-004 | Address field empty | None | 1. Enter valid data in First Name and Last Name fields<br>2. Leave the Address field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating Address is required | Medium |
| REGIST-005 | City field empty | None | 1. Enter valid data in First Name, Last Name, and Address fields<br>2. Leave the City field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating City is required | Medium |
| REGIST-006 | State field empty | None | 1. Enter valid data in First Name, Last Name, Address, and City fields<br>2. Leave the State field unselected<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating State is required | Medium |
| REGIST-007 | Zip Code field empty | None | 1. Enter valid data in First Name, Last Name, Address, City, and State fields<br>2. Leave the Zip Code field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating Zip Code is required | Medium |
| REGIST-008 | Phone Number field empty | None | 1. Enter valid data in First Name, Last Name, Address, City, State, and Zip Code fields<br>2. Leave the Phone Number field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating Phone Number is required | Medium |
| REGIST-009 | SSN field empty | None | 1. Enter valid data in First Name, Last Name, Address, City, State, Zip Code, and Phone Number fields<br>2. Leave the SSN field empty<br>3. Enter valid data in all other fields<br>4. Click the Register button | Error message displayed indicating SSN is required | Medium |
| REGIST-010 | Username field empty | None | 1. Enter valid data in all fields except Username<br>2. Leave the Username field empty<br>3. Click the Register button | Error message displayed indicating Username is required | Medium |
| REGIST-011 | Password field empty | None | 1. Enter valid data in all fields except Password<br>2. Leave the Password field empty<br>3. Click the Register button | Error message displayed indicating Password is required | Medium |
| REGIST-012 | Confirm Password field empty | None | 1. Enter valid data in all fields except Confirm Password<br>2. Leave the Confirm Password field empty<br>3. Click the Register button | Error message displayed indicating Confirm Password is required | Medium |
| REGIST-013 | Password and Confirm Password mismatch | None | 1. Enter valid data in all fields<br>2. Enter a valid password<br>3. Enter a different password in Confirm Password<br>4. Click the Register button | Error message displayed indicating passwords do not match | Medium |
| REGIST-014 | Duplicate username | A user account with the same username already exists | 1. Enter valid data in all fields<br>2. Enter a username that is already in use<br>3. Click the Register button | Error message displayed indicating username is already taken | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-015 | Maximum length handling for First Name | None | 1. Enter a maximum length string in First Name<br>2. Enter valid data in all other fields<br>3. Click the Register button | Account is created and user is logged in | Low |
| REGIST-016 | Maximum length handling for Last Name | None | 1. Enter a maximum length string in Last Name<br>2. Enter valid data in all other fields<br>3. Click the Register button | Account is created and user is logged in | Low |
| REGIST-017 | Maximum length handling for Address | None | 1. Enter a maximum length string in Address<br>2. Enter valid data in all other fields<br>3. Click the Register button | Account is created and user is logged in | Low |
| REGIST-018 | Maximum length handling for City | None | 1. Enter a maximum length string in City<br>2. Enter valid data in all other fields<br>3. Click the Register button | Account is created and user is logged in | Low |
| REGIST-019 | Maximum length handling for Username | None | 1. Enter a maximum length string in Username<br>2. Enter valid data in all other fields<br>3. Click the Register button | Account is created and user is logged in | Low |

---

### Open New Account

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Open new Checking account with valid funding source | User is on the Open New Account page | 1. Select 'Checking' as account type<br>2. Select a valid funding source with sufficient funds<br>3. Click on 'Open New Account' button | New Checking account is created, $100.00 is deducted from the funding source, and a unique account number is generated | High |
| ONA-002 | Open new Savings account with valid funding source | User is on the Open New Account page | 1. Select 'Savings' as account type<br>2. Select a valid funding source with sufficient funds<br>3. Click on 'Open New Account' button | New Savings account is created, $100.00 is deducted from the funding source, and a unique account number is generated | High |
| ONA-003 | Verify new account appears in account overview | User has successfully opened a new account | 1. Navigate to the account overview page | The newly created account is visible in the account overview | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-004 | Account type field empty | User is on the Open New Account page | 1. Leave the account type field empty<br>2. Select a valid funding source with sufficient funds<br>3. Click on 'Open New Account' button | An error message is displayed indicating that the account type is required | Medium |
| ONA-005 | Funding source field empty | User is on the Open New Account page | 1. Select 'Checking' as account type<br>2. Leave the funding source field empty<br>3. Click on 'Open New Account' button | An error message is displayed indicating that the funding source is required | Medium |
| ONA-006 | Opening deposit less than $100.00 | User is on the Open New Account page | 1. Select 'Checking' as account type<br>2. Select a valid funding source with insufficient funds<br>3. Click on 'Open New Account' button | An error message is displayed indicating that the opening deposit must be $100.00 | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-007 | Opening deposit exactly $100.00 | User is on the Open New Account page | 1. Select 'Checking' as account type<br>2. Select a valid funding source with exactly $100.00 available<br>3. Click on 'Open New Account' button | New account is created, $100.00 is deducted from the funding source, and a unique account number is generated | Low |

---

### Account Overview

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-001 | Verify Account Services sidebar displays all options | None | 1. Check if the sidebar titled 'Account Services' is visible<br>2. Verify the presence of 'Open New Account' option<br>3. Verify the presence of 'Accounts Overview' option<br>4. Verify the presence of 'Transfer Funds' option<br>5. Verify the presence of 'Bill Pay' option<br>6. Verify the presence of 'Find Transactions' option<br>7. Verify the presence of 'Update Contact Info' option<br>8. Verify the presence of 'Request Loan' option<br>9. Verify the presence of 'Log Out' option | All specified options are visible in the sidebar | High |
| ACCOVE-002 | Verify account number is displayed | User is logged in | 1. Check if the account number is displayed on the page | Account number is visible | High |
| ACCOVE-003 | Verify current balance is displayed | User is logged in | 1. Check if the current balance is displayed on the page | Current balance is visible | High |
| ACCOVE-004 | Verify available amount is displayed | User is logged in | 1. Check if the available amount is displayed on the page | Available amount is visible | High |
| ACCOVE-005 | Verify combined total balance is displayed | User is logged in | 1. Check if the combined total balance is displayed on the page | Combined total balance is visible | High |

---

### Transfer Funds

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-001 | Successful transfer between accounts | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From' account number<br>3. Select a valid 'To' account number<br>4. Click on the Transfer button | Transaction is processed successfully | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-002 | Amount field empty | User is logged in and on the Transfer Funds page | 1. Leave the Amount field empty<br>2. Select a valid 'From' account number<br>3. Select a valid 'To' account number<br>4. Click on the Transfer button | Error message is displayed indicating that the Amount is required | Medium |
| TRAFUN-003 | From account number field empty | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Leave the 'From' account number field empty<br>3. Select a valid 'To' account number<br>4. Click on the Transfer button | Error message is displayed indicating that the 'From' account number is required | Medium |
| TRAFUN-004 | To account number field empty | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From' account number<br>3. Leave the 'To' account number field empty<br>4. Click on the Transfer button | Error message is displayed indicating that the 'To' account number is required | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-005 | Exact boundary amount transfer | User is logged in and on the Transfer Funds page | 1. Enter an amount exactly at the boundary limit<br>2. Select a valid 'From' account number<br>3. Select a valid 'To' account number<br>4. Click on the Transfer button | Transaction is processed successfully | Low |
| TRAFUN-006 | Amount just below boundary limit | User is logged in and on the Transfer Funds page | 1. Enter an amount just below the boundary limit<br>2. Select a valid 'From' account number<br>3. Select a valid 'To' account number<br>4. Click on the Transfer button | Transaction is processed successfully | Low |

---

### Bill Payments

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-001 | Successful payment with all valid inputs | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Re-enter the same valid Account number in Verify Account number<br>9. Enter a valid Amount<br>10. Select a valid From account number from the dropdown<br>11. Click on Send Payment | Confirmation message appears upon successful transfer | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-002 | Payee Name field empty | None | 1. Leave the Payee Name field empty<br>2. Enter valid data in all other fields<br>3. Click on Send Payment | Error message indicating Payee Name is required | Medium |
| BILPAY-003 | Address field empty | None | 1. Enter a valid Payee Name<br>2. Leave the Address field empty<br>3. Enter valid data in all other fields<br>4. Click on Send Payment | Error message indicating Address is required | Medium |
| BILPAY-004 | City field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Leave the City field empty<br>4. Enter valid data in all other fields<br>5. Click on Send Payment | Error message indicating City is required | Medium |
| BILPAY-005 | State field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Leave the State field empty<br>5. Enter valid data in all other fields<br>6. Click on Send Payment | Error message indicating State is required | Medium |
| BILPAY-006 | Zip Code field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Leave the Zip Code field empty<br>6. Enter valid data in all other fields<br>7. Click on Send Payment | Error message indicating Zip Code is required | Medium |
| BILPAY-007 | Phone number field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Leave the Phone number field empty<br>7. Enter valid data in all other fields<br>8. Click on Send Payment | Error message indicating Phone number is required | Medium |
| BILPAY-008 | Account number field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Leave the Account number field empty<br>8. Enter valid data in all other fields<br>9. Click on Send Payment | Error message indicating Account number is required | Medium |
| BILPAY-009 | Verify Account number field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Leave the Verify Account number field empty<br>9. Enter valid data in all other fields<br>10. Click on Send Payment | Error message indicating Verify Account number is required | Medium |
| BILPAY-010 | Amount field empty | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Re-enter the same valid Account number in Verify Account number<br>9. Leave the Amount field empty<br>10. Select a valid From account number from the dropdown<br>11. Click on Send Payment | Error message indicating Amount is required | Medium |
| BILPAY-011 | Account number mismatch | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Enter a different Account number in Verify Account number<br>9. Enter a valid Amount<br>10. Select a valid From account number from the dropdown<br>11. Click on Send Payment | Error message indicating Account numbers do not match | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-012 | Amount exactly at boundary value | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Re-enter the same valid Account number in Verify Account number<br>9. Enter an Amount exactly at the boundary value<br>10. Select a valid From account number from the dropdown<br>11. Click on Send Payment | Confirmation message appears upon successful transfer | Low |
| BILPAY-013 | Amount just below boundary value | None | 1. Enter a valid Payee Name<br>2. Enter a valid Address<br>3. Enter a valid City<br>4. Enter a valid State<br>5. Enter a valid Zip Code<br>6. Enter a valid Phone number<br>7. Enter a valid Account number<br>8. Re-enter the same valid Account number in Verify Account number<br>9. Enter an Amount just below the boundary value<br>10. Select a valid From account number from the dropdown<br>11. Click on Send Payment | Confirmation message appears upon successful transfer | Low |

---

### Find Transaction

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-001 | Find transaction by valid Transaction ID and valid Account | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid Transaction ID in the Find by Transaction ID input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-002 | Find transactions by valid date for Checking account | User is logged in and on the Find Transaction page | 1. Select 'Checking' from the Account dropdown<br>2. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-003 | Find transactions by valid date for Savings account | User is logged in and on the Find Transaction page | 1. Select 'Savings' from the Account dropdown<br>2. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-004 | Find transactions with valid date range and account selected | None | 1. Select an account from the Account dropdown<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |
| FINTRA-005 | Find transactions by amount with valid account and amount | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid amount in the Find by Amount input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-006 | Account field empty | None | 1. Leave the Account dropdown unselected<br>2. Enter a valid Transaction ID in the Find by Transaction ID input<br>3. Click the Find Transactions button | Inline validation message appears next to the Account dropdown | Medium |
| FINTRA-007 | Transaction ID field empty | None | 1. Select a valid account from the Account dropdown<br>2. Leave the Find by Transaction ID input empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Transaction ID input | Medium |
| FINTRA-008 | Invalid Transaction ID format | None | 1. Select a valid account from the Account dropdown<br>2. Enter an invalid format in the Find by Transaction ID input<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Transaction ID input | Medium |
| FINTRA-009 | Account dropdown field empty | User is logged in and on the Find Transaction page | 1. Leave the Account dropdown unselected<br>2. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>3. Click the Find Transactions button | Inline validation message appears next to the Account dropdown indicating it is required | Medium |
| FINTRA-010 | Find by Date input field empty | User is logged in and on the Find Transaction page | 1. Select an account from the Account dropdown<br>2. Leave the Find by Date input empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Date input indicating it is required | Medium |
| FINTRA-011 | Invalid date format in Find by Date input | User is logged in and on the Find Transaction page | 1. Select an account from the Account dropdown<br>2. Enter an invalid date format in the Find by Date input<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Date input indicating the correct format is MM-DD-YYYY | Medium |
| FINTRA-012 | Account dropdown field empty | None | 1. Leave the Account dropdown unselected<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | Inline validation message appears next to the Account dropdown | Medium |
| FINTRA-013 | Start date field empty | None | 1. Select an account from the Account dropdown<br>2. Leave the start date field empty<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | Inline validation message appears next to the start date field | Medium |
| FINTRA-014 | End date field empty | None | 1. Select an account from the Account dropdown<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Leave the end date field empty<br>4. Click the Find Transactions button | Inline validation message appears next to the end date field | Medium |
| FINTRA-015 | Invalid start date format | None | 1. Select an account from the Account dropdown<br>2. Enter an invalid start date format<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | Inline validation message appears next to the start date field | Medium |
| FINTRA-016 | Invalid end date format | None | 1. Select an account from the Account dropdown<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Enter an invalid end date format<br>4. Click the Find Transactions button | Inline validation message appears next to the end date field | Medium |
| FINTRA-017 | Account field empty | None | 1. Leave the Account dropdown unselected<br>2. Enter a valid amount in the Find by Amount input<br>3. Click the Find Transactions button | Inline validation message appears next to the Account dropdown for empty input | Medium |
| FINTRA-018 | Find by Amount field empty | None | 1. Select a valid account from the Account dropdown<br>2. Leave the Find by Amount input empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Amount input for empty input | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-019 | Find transaction with maximum length Transaction ID | None | 1. Select a valid account from the Account dropdown<br>2. Enter a Transaction ID with maximum allowed length in the Find by Transaction ID input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-020 | Find transactions with future date | User is logged in and on the Find Transaction page | 1. Select an account from the Account dropdown<br>2. Enter a future date in MM-DD-YYYY format in the Find by Date input<br>3. Click the Find Transactions button | System returns no transactions and displays a message indicating no transactions found for the selected date | Low |
| FINTRA-021 | Same start and end date | None | 1. Select an account from the Account dropdown<br>2. Enter the same date for both start and end date in MM-DD-YYYY format<br>3. Click the Find Transactions button | System returns matching transactions for the specified date in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-022 | Future date range | None | 1. Select an account from the Account dropdown<br>2. Enter a future start date in MM-DD-YYYY format<br>3. Enter a future end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | System returns no transactions and displays an appropriate message indicating no transactions found | Low |
| FINTRA-023 | Find transactions by amount with maximum length amount | None | 1. Select a valid account from the Account dropdown<br>2. Enter a maximum length valid amount in the Find by Amount input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-024 | Find transactions by amount with amount just below boundary | None | 1. Select a valid account from the Account dropdown<br>2. Enter an amount just below the boundary in the Find by Amount input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-025 | Find transactions by amount with exact boundary amount | None | 1. Select a valid account from the Account dropdown<br>2. Enter an exact boundary amount in the Find by Amount input<br>3. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |

---

### Update Profile

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-001 | Successful profile update with all valid inputs | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Confirmation message is shown upon successful submission | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-002 | First Name field empty | User is on the Update Profile page | 1. Leave First Name field empty<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating First Name is required | Medium |
| UPDPRO-003 | Last Name field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Leave Last Name field empty<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Last Name is required | Medium |
| UPDPRO-004 | Address field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Leave Address field empty<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Address is required | Medium |
| UPDPRO-005 | City field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Leave City field empty<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating City is required | Medium |
| UPDPRO-006 | State field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Leave State field unselected<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating State is required | Medium |
| UPDPRO-007 | Zip Code field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Leave Zip Code field empty<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Zip Code is required | Medium |
| UPDPRO-008 | Phone number field empty | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Leave Phone number field empty<br>8. Click on Update Profile button | Error message indicating Phone number is required | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-009 | Maximum length for First Name | User is on the Update Profile page | 1. Enter maximum length valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Confirmation message is shown upon successful submission | Low |
| UPDPRO-010 | Maximum length for Last Name | User is on the Update Profile page | 1. Enter valid first name<br>2. Enter maximum length valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Confirmation message is shown upon successful submission | Low |

---

### Request Loan

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-001 | Apply for a loan with all fields correctly filled | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click the Apply Now button | Loan is approved | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-002 | Loan Amount field empty | None | 1. Leave the loan amount field empty<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click the Apply Now button | Process is not completed | Medium |
| REQLOA-003 | Down Payment field empty | None | 1. Enter a valid loan amount<br>2. Leave the down payment field empty<br>3. Select a valid from account number<br>4. Click the Apply Now button | Process is not completed | Medium |
| REQLOA-004 | From account number field empty | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Leave the from account number field empty<br>4. Click the Apply Now button | Process is not completed | Medium |
| REQLOA-005 | Internal error occurs during loan application | Simulate an internal error | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click the Apply Now button | Process is not completed | Medium |

---

### Logout

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Successful logout | User is logged in | 1. Click on the logout button | User session ends, sensitive data is cleared, and user is returned to the login page | High |
| LOGOUT-002 | Verify session ends after logout | User is logged in | 1. Click on the logout button<br>2. Attempt to access a protected page | Access to the protected page is denied, indicating the session has ended | High |
| LOGOUT-003 | Verify sensitive data is cleared after logout | User is logged in | 1. Click on the logout button<br>2. Check for any residual sensitive data in session storage | No sensitive data is found in session storage | High |
| LOGOUT-004 | Verify redirection to login page after logout | User is logged in | 1. Click on the logout button | User is redirected to the login page | High |

---

## Post-Verification Details

This section shows verification requirements for tests that modify application state.
Tests using the **before/after** strategy require running a verification test BEFORE
and AFTER the action to compare values.

### ONA-001: Open new Checking account with valid funding source

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_opening

**1. Verify the new Checking account appears in the account overview**

- **Status:** ❌ not_found
- **Strategy:** ▶️ After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All test cases operate on the correct module but do not access or confirm the presence of a new Checking account.
- **Manual Step:** Manually check the account overview to ensure the new Checking account is listed.

**2. Verify $100.00 is deducted from the funding source**

- **Status:** ✅ found
- **Strategy:** 🔄 Before/After
- **Matched Test:** ACCOVE-003 (Verify current balance is displayed)
- **Confidence:** 100%
- **Before Action:** Record the balance of the funding source account before the action
- **After Action:** Compare the balance and confirm it decreased by $100.00
- **Execution Note:** Use this test to observe the current balance before and after the action. The execution strategy will handle the comparison.

**⚠️ Coverage Gaps:**
- All test cases operate on the correct module but do not access or confirm the presence of a new Checking account.

#### 📋 Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Open New Account to Account Overview to record baseline data

**2. [PRE-VERIFY] 📸 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 and RECORD the current values before the action

**3. [NAVIGATE] 🧭** Navigate to Open New Account
   > Return to Open New Account to execute the action

**4. [ACTION] ⚡ ONA-001** — Open new Checking account with valid funding source
   > Run ONA-001 — this is the state-changing action being verified

**5. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Open New Account to Account Overview to verify the change

**6. [POST-VERIFY] 🔍 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with ACCOVE-003 → ACTION: Execute ONA-001 → POST: Verify with ACCOVE-003 (compare against baseline) → Manual verification needed for 1 item(s)

**⚠️ Manual Verification Required:**
- Verify the new Checking account appears in the account overview
  - Suggested: Manually check the account overview to ensure the new Checking account is listed.

---

### ONA-002: Open new Savings account with valid funding source

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_opening

**1. Verify the new Savings account appears in the account overview**

- **Status:** ❌ not_found
- **Strategy:** ▶️ After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases confirm the presence of a new Savings account in the account overview.
- **Manual Step:** Manually check the account overview page to ensure the new Savings account is listed.

**2. Verify $100.00 is deducted from the funding source**

- **Status:** ✅ found
- **Strategy:** 🔄 Before/After
- **Matched Test:** ACCOVE-003 (Verify current balance is displayed)
- **Confidence:** 100%
- **Before Action:** Record the balance of the funding source account before the action
- **After Action:** Compare the balance and confirm it decreased by $100.00
- **Execution Note:** Use this test to display the current balance of the funding source account before and after the action. The before_after execution strategy will handle the comparison to confirm the $100.00 deduction.

**⚠️ Coverage Gaps:**
- None of the test cases confirm the presence of a new Savings account in the account overview.

#### 📋 Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Open New Account to Account Overview to record baseline data

**2. [PRE-VERIFY] 📸 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 and RECORD the current values before the action

**3. [NAVIGATE] 🧭** Navigate to Open New Account
   > Return to Open New Account to execute the action

**4. [ACTION] ⚡ ONA-002** — Open new Savings account with valid funding source
   > Run ONA-002 — this is the state-changing action being verified

**5. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Open New Account to Account Overview to verify the change

**6. [POST-VERIFY] 🔍 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with ACCOVE-003 → ACTION: Execute ONA-002 → POST: Verify with ACCOVE-003 (compare against baseline) → Manual verification needed for 1 item(s)

**⚠️ Manual Verification Required:**
- Verify the new Savings account appears in the account overview
  - Suggested: Manually check the account overview page to ensure the new Savings account is listed.

---

### ONA-003: Verify new account appears in account overview

**Coverage:** ❌ None
**Modifies State:** new_account_opening

**1. Verify the newly created account is visible in the account overview**

- **Status:** ❌ not_found
- **Strategy:** ▶️ After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases confirm the existence of a newly created account in the account overview.
- **Manual Step:** Manually check the account overview page to ensure the newly created account is listed.

**⚠️ Coverage Gaps:**
- None of the test cases confirm the existence of a newly created account in the account overview.

#### 📋 Execution Plan

**1. [ACTION] ⚡ ONA-003** — Verify new account appears in account overview
   > Run ONA-003 — this is the state-changing action being verified

**Notes:** Execute ONA-003 → Manual verification needed for 1 item(s)

**⚠️ Manual Verification Required:**
- Verify the newly created account is visible in the account overview
  - Suggested: Manually check the account overview page to ensure the newly created account is listed.

---

### TRAFUN-001: Successful transfer between accounts

**Coverage:** ✅ Full
**Modifies State:** fund_transfer

**1. Verify the source account balance decreased by the transferred amount**

- **Status:** ✅ found
- **Strategy:** 🔄 Before/After
- **Matched Test:** ACCOVE-003 (Verify current balance is displayed)
- **Confidence:** 90%
- **Before Action:** Record the balance of the source account before the action
- **After Action:** Compare the balance and confirm it decreased by the transferred amount
- **Execution Note:** Use this test to display the current balance of the source account before and after the transfer.

**2. Verify the destination account balance increased by the transferred amount**

- **Status:** ✅ found
- **Strategy:** 🔄 Before/After
- **Matched Test:** ACCOVE-003 (Verify current balance is displayed)
- **Confidence:** 90%
- **Before Action:** Record the balance of the destination account before the action
- **After Action:** Compare the balance and confirm it increased by the transferred amount
- **Execution Note:** This test can be used to verify the destination account balance by displaying the current balance. It will be executed before and after the transfer to observe any changes.

#### 📋 Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Transfer Funds to Account Overview to record baseline data

**2. [PRE-VERIFY] 📸 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 and RECORD the current values before the action

**3. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Transfer Funds to Account Overview to record baseline data

**4. [PRE-VERIFY] 📸 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 and RECORD the current values before the action

**5. [NAVIGATE] 🧭** Navigate to Transfer Funds
   > Return to Transfer Funds to execute the action

**6. [ACTION] ⚡ TRAFUN-001** — Successful transfer between accounts
   > Run TRAFUN-001 — this is the state-changing action being verified

**7. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Transfer Funds to Account Overview to verify the change

**8. [POST-VERIFY] 🔍 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**9. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Transfer Funds to Account Overview to verify the change

**10. [POST-VERIFY] 🔍 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with ACCOVE-003, ACCOVE-003 → ACTION: Execute TRAFUN-001 → POST: Verify with ACCOVE-003, ACCOVE-003 (compare against baseline)

---

### BILPAY-001: Successful payment with all valid inputs

**Coverage:** ✅ Full
**Modifies State:** bill_payment

**1. Verify a confirmation message appears upon successful payment**

- **Status:** ✅ found
- **Strategy:** ▶️ After Only
- **Matched Test:** BILPAY-012 (Amount exactly at boundary value)
- **Confidence:** 100%
- **Execution Note:** This test can be used to verify the confirmation message appears upon successful payment.

**2. Verify the balance of the paying account decreased by the payment amount**

- **Status:** ✅ found
- **Strategy:** 🔄 Before/After
- **Matched Test:** ACCOVE-003 (Verify current balance is displayed)
- **Confidence:** 100%
- **Before Action:** Record the balance of the paying account before the action
- **After Action:** Compare the balance and confirm it decreased by the payment amount
- **Execution Note:** Use this test to observe the current balance before and after the payment action. The execution strategy will handle the comparison.

#### 📋 Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Bill Payments to Account Overview to record baseline data

**2. [PRE-VERIFY] 📸 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 and RECORD the current values before the action

**3. [NAVIGATE] 🧭** Navigate to Bill Payments
   > Return to Bill Payments to execute the action

**4. [ACTION] ⚡ BILPAY-001** — Successful payment with all valid inputs
   > Run BILPAY-001 — this is the state-changing action being verified

**5. [POST-VERIFY] 🔍 BILPAY-012** — Amount exactly at boundary value
   > This test can be used to verify the confirmation message appears upon successful payment.

**6. [NAVIGATE] 🧭** Navigate to Account Overview
   > Navigate from Bill Payments to Account Overview to verify the change

**7. [POST-VERIFY] 🔍 ACCOVE-003** — Verify current balance is displayed
   > Run ACCOVE-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with ACCOVE-003 → ACTION: Execute BILPAY-001 → POST: Verify with BILPAY-012, ACCOVE-003 (compare against baseline)

---

### UPDPRO-001: Successful profile update with all valid inputs

**Coverage:** ✅ Full
**Modifies State:** profile_modification

**1. Verify a confirmation message is shown upon successful profile update**

- **Status:** ✅ found
- **Strategy:** ▶️ After Only
- **Matched Test:** UPDPRO-009 (Maximum length for First Name)
- **Confidence:** 90%
- **Execution Note:** This test can be used to verify the confirmation message upon successful profile update.

#### 📋 Execution Plan

**1. [ACTION] ⚡ UPDPRO-001** — Successful profile update with all valid inputs
   > Run UPDPRO-001 — this is the state-changing action being verified

**2. [POST-VERIFY] 🔍 UPDPRO-009** — Maximum length for First Name
   > This test can be used to verify the confirmation message upon successful profile update.

**Notes:** Execute UPDPRO-001 → then verify with UPDPRO-009

---

### REQLOA-001: Apply for a loan with all fields correctly filled

**Coverage:** ❌ None
**Modifies State:** loan_application

**1. Verify the loan application is approved**

- **Status:** ❌ not_found
- **Strategy:** ▶️ After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on scenarios where the loan application process is not completed due to errors or missing information. None of them confirm the loan approval status.
- **Manual Step:** After applying for the loan, manually check the loan application status to ensure it shows 'approved'.

**⚠️ Coverage Gaps:**
- All candidate test cases focus on scenarios where the loan application process is not completed due to errors or missing information. None of them confirm the loan approval status.

#### 📋 Execution Plan

**1. [ACTION] ⚡ REQLOA-001** — Apply for a loan with all fields correctly filled
   > Run REQLOA-001 — this is the state-changing action being verified

**Notes:** Execute REQLOA-001 → Manual verification needed for 1 item(s)

**⚠️ Manual Verification Required:**
- Verify the loan application is approved
  - Suggested: After applying for the loan, manually check the loan application status to ensure it shows 'approved'.

---

## Navigation Graph

![Navigation Graph](output4/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /login | No | 8 |
| Forgot Password | /forgot-password | No | 9 |
| Register | /register | No | 19 |
| Open New Account | /open-new-account | Yes | 7 |
| Account Overview | /account-overview | Yes | 5 |
| Transfer Funds | /transfer-funds | Yes | 6 |
| Bill Payments | /bill-payments | Yes | 13 |
| Find Transaction | /find-transaction | Yes | 25 |
| Update Profile | /update-profile | Yes | 10 |
| Request Loan | /request-loan | Yes | 5 |
| Logout | /logout | Yes | 4 |
