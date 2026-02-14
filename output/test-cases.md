# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2026-02-03T02:32:27.572067

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 88 |

### By Type

| Type | Count |
|------|-------|
| Positive | 22 |
| Negative | 60 |
| Edge Case | 6 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 22 |
| Medium | 59 |
| Low | 7 |

### Post-Verification Coverage

| Metric | Count |
|--------|-------|
| Tests Needing Verification | 8 |
| Full Coverage | 1 |
| Partial Coverage | 3 |
| No Coverage | 4 |

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 8 |
| Automated Steps | 4 |
| Manual Steps | 7 |
| Automation Rate | 36.4% |

---

## Test Cases

### Login

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login with username | None | 1. Enter a valid username<br>2. Enter a valid password<br>3. Click the Log In button | User is taken to their account dashboard | High |
| LOGIN-002 | Successful login with email | None | 1. Enter a valid email<br>2. Enter a valid password<br>3. Click the Log In button | User is taken to their account dashboard | High |
| LOGIN-007 | Login form elements displayed correctly | None | 1. Verify the presence of the username or email field<br>2. Verify the presence of the password field<br>3. Verify the presence of the Log In button<br>4. Verify the presence of the Forgot login info? link<br>5. Verify the presence of the Register link | All login form elements are displayed correctly | Low |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-003 | Invalid credentials | None | 1. Enter an invalid username or email<br>2. Enter an invalid password<br>3. Click the Log In button | Error is shown indicating credentials do not match | High |
| LOGIN-004 | Username field empty | None | 1. Leave the username field empty<br>2. Enter a valid password<br>3. Click the Log In button | Error is shown indicating missing username | Medium |
| LOGIN-005 | Password field empty | None | 1. Enter a valid username<br>2. Leave the password field empty<br>3. Click the Log In button | Error is shown indicating missing password | Medium |
| LOGIN-006 | Fields remain populated after failed login | None | 1. Enter an invalid username or email<br>2. Enter an invalid password<br>3. Click the Log In button | Both input fields remain populated with the entered data | Medium |

---

### Forgot Password

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-001 | Successful recovery with all valid details | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Recovery details displayed | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-002 | First Name field empty | None | 1. Leave the First Name field empty<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating First Name is required | Medium |
| FORPAS-003 | Last Name field empty | None | 1. Enter a valid first name<br>2. Leave the Last Name field empty<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating Last Name is required | Medium |
| FORPAS-004 | Address field empty | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Leave the Address field empty<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating Address is required | Medium |
| FORPAS-005 | City field empty | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Leave the City field empty<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating City is required | Medium |
| FORPAS-006 | State field empty | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Leave the State field empty<br>6. Enter a valid zip code<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating State is required | Medium |
| FORPAS-007 | Zip Code field empty | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Leave the Zip Code field empty<br>7. Enter a valid SSN<br>8. Click on the Find My Login Info button | Error displayed indicating Zip Code is required | Medium |
| FORPAS-008 | SSN field empty | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Leave the SSN field empty<br>8. Click on the Find My Login Info button | Error displayed indicating SSN is required | Medium |
| FORPAS-009 | No matching record found | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Enter a valid state<br>6. Enter a valid zip code<br>7. Enter a valid SSN with no matching record<br>8. Click on the Find My Login Info button | Error displayed indicating no matching record found | Medium |

---

### Register

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-001 | Successful registration with all valid inputs | None | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Enter a valid SSN<br>9. Enter a valid username<br>10. Enter a valid password<br>11. Enter the same password in Confirm Password<br>12. Click the Register button | Account is created and user is logged in | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-002 | First Name field empty | None | 1. Leave the First Name field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating First Name is required | Medium |
| REGIST-003 | Last Name field empty | None | 1. Leave the Last Name field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Last Name is required | Medium |
| REGIST-004 | Address field empty | None | 1. Leave the Address field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Address is required | Medium |
| REGIST-005 | City field empty | None | 1. Leave the City field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating City is required | Medium |
| REGIST-006 | State field empty | None | 1. Leave the State field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating State is required | Medium |
| REGIST-007 | Zip Code field empty | None | 1. Leave the Zip Code field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Zip Code is required | Medium |
| REGIST-008 | Phone Number field empty | None | 1. Leave the Phone Number field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Phone Number is required | Medium |
| REGIST-009 | SSN field empty | None | 1. Leave the SSN field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating SSN is required | Medium |
| REGIST-010 | Username field empty | None | 1. Leave the Username field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Username is required | Medium |
| REGIST-011 | Password field empty | None | 1. Leave the Password field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Password is required | Medium |
| REGIST-012 | Confirm Password field empty | None | 1. Leave the Confirm Password field empty<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating Confirm Password is required | Medium |
| REGIST-013 | Password and Confirm Password mismatch | None | 1. Enter a valid password<br>2. Enter a different password in Confirm Password<br>3. Enter valid data for all other fields<br>4. Click the Register button | Error message indicating passwords do not match | Medium |
| REGIST-014 | Duplicate username | Username already exists in the system | 1. Enter a username that already exists<br>2. Enter valid data for all other fields<br>3. Click the Register button | Error message indicating username is already taken | Medium |

---

### Open New Account

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Open new checking account with valid funding source | User is authenticated and on the Open New Account page | 1. Select 'Checking' as the account type<br>2. Select a valid funding source with sufficient balance<br>3. Click 'Open New Account' | New checking account is created, $100.00 is deducted from the funding source, and a unique account number is generated | High |
| ONA-002 | Open new savings account with valid funding source | User is authenticated and on the Open New Account page | 1. Select 'Savings' as the account type<br>2. Select a valid funding source with sufficient balance<br>3. Click 'Open New Account' | New savings account is created, $100.00 is deducted from the funding source, and a unique account number is generated | High |
| ONA-003 | Verify new account is visible in account overview after creation | User has successfully opened a new account | 1. Navigate to the account overview page<br>2. Verify the new account is listed with the correct account type and balance | New account is visible in the account overview with the correct details | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-004 | Open new account with account type field empty | User is authenticated and on the Open New Account page | 1. Leave the account type field empty<br>2. Select a valid funding source with sufficient balance<br>3. Click 'Open New Account' | Error message is displayed indicating that the account type is required | Medium |
| ONA-005 | Open new account with funding source field empty | User is authenticated and on the Open New Account page | 1. Select a valid account type<br>2. Leave the funding source field empty<br>3. Click 'Open New Account' | Error message is displayed indicating that the funding source is required | Medium |
| ONA-006 | Open new account with insufficient funds in funding source | User is authenticated and on the Open New Account page | 1. Select a valid account type<br>2. Select a funding source with less than $100.00 balance<br>3. Click 'Open New Account' | Error message is displayed indicating insufficient funds in the funding source | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-007 | Open new account with exactly $100 in funding source | User is authenticated and on the Open New Account page | 1. Select a valid account type<br>2. Select a funding source with exactly $100.00 balance<br>3. Click 'Open New Account' | New account is created, $100.00 is deducted from the funding source, and a unique account number is generated | Low |

---

### Account Overview

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-001 | Verify all actions are listed in the Account Services sidebar | None | 1. Locate the Account Services sidebar<br>2. Verify the presence of 'Open New Account'<br>3. Verify the presence of 'Accounts Overview'<br>4. Verify the presence of 'Transfer Funds'<br>5. Verify the presence of 'Bill Pay'<br>6. Verify the presence of 'Find Transactions'<br>7. Verify the presence of 'Update Contact Info'<br>8. Verify the presence of 'Request Loan'<br>9. Verify the presence of 'Log Out' | All actions are listed in the Account Services sidebar | High |
| ACCOVE-002 | Verify account number is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the account number is displayed | Account number is displayed in the Accounts Overview | High |
| ACCOVE-003 | Verify balance is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the balance is displayed | Balance is displayed in the Accounts Overview | High |
| ACCOVE-004 | Verify available amount is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the available amount is displayed | Available amount is displayed in the Accounts Overview | High |
| ACCOVE-005 | Verify combined total balance is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the combined total balance is displayed | Combined total balance is displayed in the Accounts Overview | High |

---

### Transfer Funds

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-001 | Successful fund transfer between accounts | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button | Transaction is processed successfully | High |
| TRAFUN-002 | Verify account balance update after transfer | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button<br>5. Verify the balance of the 'From account' is reduced by the transfer amount<br>6. Verify the balance of the 'To account' is increased by the transfer amount | Balances are updated correctly after the transfer | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-003 | Amount field empty | User is logged in and on the Transfer Funds page | 1. Leave the 'Amount' field empty<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button | An error message is displayed indicating that the amount is required | Medium |
| TRAFUN-004 | From account number field empty | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Leave the 'From account number' field empty<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button | An error message is displayed indicating that the from account number is required | Medium |
| TRAFUN-005 | To account number field empty | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From account number'<br>3. Leave the 'To account number' field empty<br>4. Click the 'Transfer' button | An error message is displayed indicating that the to account number is required | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-006 | Transfer amount exactly at boundary value | User is logged in and on the Transfer Funds page | 1. Enter an amount exactly at the boundary value<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button | Transaction is processed successfully | Low |
| TRAFUN-007 | Transfer amount just below boundary value | User is logged in and on the Transfer Funds page | 1. Enter an amount just below the boundary value<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click the 'Transfer' button | Transaction is processed successfully | Low |

---

### Bill Payments

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-001 | Successful payment with all valid inputs | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Confirmation message appears upon successful transfer | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-002 | Payee Name field empty | None | 1. Leave Payee Name empty<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Payee Name is required | Medium |
| BILPAY-003 | Address field empty | None | 1. Enter valid Payee Name<br>2. Leave Address empty<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Address is required | Medium |
| BILPAY-004 | City field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Leave City empty<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating City is required | Medium |
| BILPAY-005 | State field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Leave State empty<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating State is required | Medium |
| BILPAY-006 | Zip Code field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Leave Zip Code empty<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Zip Code is required | Medium |
| BILPAY-007 | Phone number field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Leave Phone number empty<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Phone number is required | Medium |
| BILPAY-008 | Account number field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Leave Account number empty<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Account number is required | Medium |
| BILPAY-009 | Verify Account number field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Leave Verify Account number empty<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Verify Account number is required | Medium |
| BILPAY-010 | Amount field empty | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Leave Amount empty<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Amount is required | Medium |
| BILPAY-011 | From account number not selected | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Re-enter valid Account number for verification<br>9. Enter valid Amount<br>10. Do not select From account number<br>11. Click on Send Payment | Error message indicating From account number is required | Medium |
| BILPAY-012 | Account number mismatch | None | 1. Enter valid Payee Name<br>2. Enter valid Address<br>3. Enter valid City<br>4. Enter valid State<br>5. Enter valid Zip Code<br>6. Enter valid Phone number<br>7. Enter valid Account number<br>8. Enter a different Account number for verification<br>9. Enter valid Amount<br>10. Select valid From account number from dropdown<br>11. Click on Send Payment | Error message indicating Account numbers do not match | Medium |

---

### Find Transaction

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-001 | Find transactions with all valid inputs | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-002 | Account dropdown field empty | None | 1. Leave the Account dropdown empty<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Account dropdown | Medium |
| FINTRA-003 | Find by Transaction ID input field empty | None | 1. Select a valid account from the Account dropdown<br>2. Leave the Find by Transaction ID input empty<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Transaction ID input | Medium |
| FINTRA-004 | Find by Date input field empty | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Leave the Find by Date input empty<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Date input | Medium |
| FINTRA-005 | Find by Date Range input field empty | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Leave the Find by Date Range input empty<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Date Range input | Medium |
| FINTRA-006 | Find by Amount input field empty | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Leave the Find by Amount input empty<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Amount input | Medium |
| FINTRA-007 | Invalid date format in Find by Date input | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter an invalid date format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Date input | Medium |
| FINTRA-008 | Invalid date format in Find by Date Range input | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter an invalid date format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | Inline validation message appears next to the Find by Date Range input | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-009 | Exact boundary value for amount | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter an exact boundary amount value in the Find by Amount input<br>6. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-010 | Just below boundary value for amount | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter an amount just below the boundary value in the Find by Amount input<br>6. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |
| FINTRA-011 | Same start and end date in Find by Date Range input | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter the same start and end date in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | Low |

---

### Update Profile

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-001 | Update profile with all valid details | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Confirmation message is shown upon successful submission | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-002 | First Name field empty | None | 1. Leave First Name field empty<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating First Name is required | Medium |
| UPDPRO-003 | Last Name field empty | None | 1. Enter valid first name<br>2. Leave Last Name field empty<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Last Name is required | Medium |
| UPDPRO-004 | Address field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Leave Address field empty<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Address is required | Medium |
| UPDPRO-005 | City field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Leave City field empty<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating City is required | Medium |
| UPDPRO-006 | State field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Leave State field empty<br>6. Enter valid zip code<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating State is required | Medium |
| UPDPRO-007 | Zip Code field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Leave Zip Code field empty<br>7. Enter valid phone number<br>8. Click on Update Profile button | Error message indicating Zip Code is required | Medium |
| UPDPRO-008 | Phone number field empty | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Leave Phone number field empty<br>8. Click on Update Profile button | Error message indicating Phone number is required | Medium |

---

### Request Loan

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-001 | Apply for loan with all fields correctly filled | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on the Apply Now button | Loan is approved | High |
| REQLOA-002 | Verify form fields are displayed correctly | None | 1. Verify Loan Amount field is displayed<br>2. Verify Down Payment field is displayed<br>3. Verify From account number field is displayed<br>4. Verify Apply Now button is displayed | All form fields and button are displayed correctly | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-003 | Loan Amount field empty | None | 1. Leave the Loan Amount field empty<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on the Apply Now button | Process is not completed | Medium |
| REQLOA-004 | Down Payment field empty | None | 1. Enter a valid loan amount<br>2. Leave the Down Payment field empty<br>3. Select a valid from account number<br>4. Click on the Apply Now button | Process is not completed | Medium |
| REQLOA-005 | From account number field empty | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Leave the From account number field empty<br>4. Click on the Apply Now button | Process is not completed | Medium |
| REQLOA-006 | Internal error during loan application | Simulate an internal error condition | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on the Apply Now button | Process is not completed | Medium |

---

### Logout

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Successful logout returns user to login page | User is logged in | 1. Click on the logout button | User is redirected to the login page | High |
| LOGOUT-002 | Sensitive data cleared from session after logout | User is logged in | 1. Click on the logout button<br>2. Attempt to navigate back to a page that requires login | User is redirected to the login page, indicating session data is cleared | High |

---

## Post-Verification Details

This section shows verification requirements for tests that modify application state.

### ONA-001: Open new checking account with valid funding source

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_creation

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the new checking account is created with... | ⚠️ partial | ACCOVE-002<br>(Verify account number is di...) | 70% | Run this test after creating a new checking acc...<br>The test verifies the presence of an account nu...<br>**Manual:** Manually verify that the new account ... |
| 2 | Verify $100.00 is deducted from the funding source | ❌ not_found | - | - | None of the test cases verify the deduction of ...<br>**Manual:** Manually check the account overview p... |

**⚠️ Coverage Gaps:**
- The test verifies the presence of an account number but does not check for uniqueness.
- None of the test cases verify the deduction of $100.00 from the funding source balance. They only...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-002 | Verify account number is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the account number is displayed | Account number is displayed in the Accounts Overview | High |

---

### ONA-002: Open new savings account with valid funding source

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_creation

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the new savings account is created with ... | ⚠️ partial | ACCOVE-002<br>(Verify account number is di...) | 70% | Run this test after creating a new savings acco...<br>The test case verifies that an account number i...<br>**Manual:** Manually verify that the account numb... |
| 2 | Verify $100.00 is deducted from the funding source | ❌ not_found | - | - | None of the test cases verify the deduction of ...<br>**Manual:** Manually check the funding source bal... |

**⚠️ Coverage Gaps:**
- The test case verifies that an account number is displayed, but does not specifically check for u...
- None of the test cases verify the deduction of $100.00 from the funding source. They all focus on...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-002 | Verify account number is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the account number is displayed | Account number is displayed in the Accounts Overview | High |

---

### ONA-003: Verify new account is visible in account overview after creation

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_creation

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the new account is visible in the accoun... | ⚠️ partial | ACCOVE-003<br>(Verify balance is displayed...) | 50% | Run this test after creating a new account to v...<br>The test case checks for balance display in the...<br>**Manual:** Manually check the account type in th... |

**⚠️ Coverage Gaps:**
- The test case checks for balance display in the Account Overview, which is part of the requiremen...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-003 | Verify balance is displayed in the Accounts Overview | None | 1. Locate the Accounts Overview section<br>2. Verify the balance is displayed | Balance is displayed in the Accounts Overview | High |

---

### TRAFUN-001: Successful fund transfer between accounts

**Coverage:** ✅ Full
**Modifies State:** fund_transfer

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the transaction is recorded successfully | ✅ found | FINTRA-001<br>(Find transactions with all ...) | 90% | Run this test after the transaction is expected... |

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-001 | Find transactions with all valid inputs | None | 1. Select a valid account from the Account dropdown<br>2. Enter a valid transaction ID in the Find by Transaction ID input<br>3. Enter a valid date in MM-DD-YYYY format in the Find by Date input<br>4. Enter a valid date range in MM-DD-YYYY format in the Find by Date Range input<br>5. Enter a valid amount in the Find by Amount input<br>6. Click the Find Transactions button | System returns matching transactions in a results table showing Transaction ID, Date, Description, and Amount | High |

---

### TRAFUN-002: Verify account balance update after transfer

**Coverage:** ❌ None
**Modifies State:** fund_transfer

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the balance of the 'From account' is red... | ❌ not_found | - | - | None of the test cases verify the reduction of ...<br>**Manual:** After performing a transfer, manually... |
| 2 | Verify the balance of the 'To account' is incre... | ❌ not_found | - | - | None of the test cases verify the increase in b...<br>**Manual:** After performing a transfer, manually... |

**⚠️ Coverage Gaps:**
- None of the test cases verify the reduction of the 'From account' balance by the transfer amount....
- None of the test cases verify the increase in balance of the 'To account' after a transfer. They ...

---

### BILPAY-001: Successful payment with all valid inputs

**Coverage:** ❌ None
**Modifies State:** bill_payment

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the payment confirmation message appears | ❌ not_found | - | - | All candidate test cases focus on error message...<br>**Manual:** After making a payment, manually chec... |

**⚠️ Coverage Gaps:**
- All candidate test cases focus on error messages for empty fields and do not check for a payment ...

---

### UPDPRO-001: Update profile with all valid details

**Coverage:** ❌ None
**Modifies State:** profile_modification

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the profile update confirmation message ... | ❌ not_found | - | - | None of the candidate test cases check for a pr...<br>**Manual:** After updating the profile, manually ... |

**⚠️ Coverage Gaps:**
- None of the candidate test cases check for a profile update confirmation message. They all focus ...

---

### REQLOA-001: Apply for loan with all fields correctly filled

**Coverage:** ❌ None
**Modifies State:** loan_request

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the loan application is approved | ❌ not_found | - | - | None of the test cases verify the loan approval...<br>**Manual:** Manually check the loan application s... |

**⚠️ Coverage Gaps:**
- None of the test cases verify the loan approval status. They either check for errors, form field ...

---

## Navigation Graph

![Navigation Graph](output/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /login | No | 7 |
| Forgot Password | /forgot-password | No | 9 |
| Register | /register | No | 14 |
| Open New Account | /open-new-account | Yes | 7 |
| Account Overview | /account-overview | Yes | 5 |
| Transfer Funds | /transfer-funds | Yes | 7 |
| Bill Payments | /bill-payments | Yes | 12 |
| Find Transaction | /find-transaction | Yes | 11 |
| Update Profile | /update-profile | Yes | 8 |
| Request Loan | /request-loan | Yes | 6 |
| Logout | /logout | Yes | 2 |
