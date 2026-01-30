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

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 5 |
| Automated Steps | 6 |
| Manual Steps | 1 |
| Automation Rate | 85.7% |

---

## Test Cases

### Login

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login with valid username and password | None | 1. Enter a valid username<br>2. Enter a valid password<br>3. Click the Log In button | User is redirected to account dashboard | High |
| LOGIN-002 | Successful login with valid email and password | None | 1. Enter a valid email address<br>2. Enter a valid password<br>3. Click the Log In button | User is redirected to account dashboard | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-003 | Error message displayed for invalid username | None | 1. Enter an invalid username<br>2. Enter a valid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |
| LOGIN-004 | Error message displayed for invalid email | None | 1. Enter an invalid email address<br>2. Enter a valid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |
| LOGIN-005 | Error message displayed for invalid password | None | 1. Enter a valid username<br>2. Enter an invalid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |
| LOGIN-006 | Error message displayed for both invalid username and password | None | 1. Enter an invalid username<br>2. Enter an invalid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |
| LOGIN-007 | Error message displayed for both invalid email and password | None | 1. Enter an invalid email address<br>2. Enter an invalid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |
| LOGIN-008 | Login attempt with empty username and password fields | None | 1. Leave the username field empty<br>2. Leave the password field empty<br>3. Click the Log In button | Error message is shown and input fields remain populated | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-009 | Login attempt with special characters in username | None | 1. Enter a username with special characters<br>2. Enter a valid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Low |
| LOGIN-010 | Login attempt with special characters in email | None | 1. Enter an email address with special characters<br>2. Enter a valid password<br>3. Click the Log In button | Error message is shown and input fields remain populated | Low |

---

### Forgot Password

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-001 | Successful recovery with valid customer details | None | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid address<br>4. Enter valid city<br>5. Select valid state<br>6. Enter valid zip code<br>7. Enter valid SSN<br>8. Click on Find My Login Info button | Recovery details displayed | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-002 | Error message displayed for non-matching customer details | None | 1. Enter non-matching first name<br>2. Enter non-matching last name<br>3. Enter non-matching address<br>4. Enter non-matching city<br>5. Select non-matching state<br>6. Enter non-matching zip code<br>7. Enter non-matching SSN<br>8. Click on Find My Login Info button | Error message displayed indicating no matching record found | High |
| FORPAS-003 | Validation error when submitting with empty fields | None | 1. Leave all fields empty<br>2. Click on Find My Login Info button | Validation error indicating all fields must be completed | Medium |
| FORPAS-004 | Validation error when submitting with partially filled fields | None | 1. Enter valid first name<br>2. Leave last name empty<br>3. Enter valid address<br>4. Leave city empty<br>5. Select valid state<br>6. Enter valid zip code<br>7. Leave SSN empty<br>8. Click on Find My Login Info button | Validation error indicating all fields must be completed | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-005 | Successful recovery with minimum boundary values | None | 1. Enter minimum valid length first name<br>2. Enter minimum valid length last name<br>3. Enter minimum valid length address<br>4. Enter minimum valid length city<br>5. Select valid state<br>6. Enter minimum valid length zip code<br>7. Enter minimum valid length SSN<br>8. Click on Find My Login Info button | Recovery details displayed | Low |
| FORPAS-006 | Successful recovery with maximum boundary values | None | 1. Enter maximum valid length first name<br>2. Enter maximum valid length last name<br>3. Enter maximum valid length address<br>4. Enter maximum valid length city<br>5. Select valid state<br>6. Enter maximum valid length zip code<br>7. Enter maximum valid length SSN<br>8. Click on Find My Login Info button | Recovery details displayed | Low |
| FORPAS-007 | Error message displayed for special characters in fields | None | 1. Enter special characters in first name<br>2. Enter special characters in last name<br>3. Enter special characters in address<br>4. Enter special characters in city<br>5. Select valid state<br>6. Enter special characters in zip code<br>7. Enter special characters in SSN<br>8. Click on Find My Login Info button | Error message displayed indicating invalid input | Low |

---

### Register

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-001 | Register new account with valid details | None | 1. Click on the Register link<br>2. Enter a valid first name<br>3. Enter a valid last name<br>4. Enter a valid address<br>5. Enter a valid city<br>6. Select a valid state from the dropdown<br>7. Enter a valid zip code<br>8. Enter a valid phone number<br>9. Enter a valid SSN<br>10. Enter a valid username<br>11. Enter a valid password<br>12. Enter the same password in Confirm Password<br>13. Click on the Register button | System creates the new account and automatically logs the user in | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-002 | Attempt registration with missing first name | None | 1. Click on the Register link<br>2. Leave the first name field empty<br>3. Enter a valid last name<br>4. Enter a valid address<br>5. Enter a valid city<br>6. Select a valid state from the dropdown<br>7. Enter a valid zip code<br>8. Enter a valid phone number<br>9. Enter a valid SSN<br>10. Enter a valid username<br>11. Enter a valid password<br>12. Enter the same password in Confirm Password<br>13. Click on the Register button | System displays an error message indicating that the first name is required | Medium |
| REGIST-003 | Attempt registration with mismatched passwords | None | 1. Click on the Register link<br>2. Enter a valid first name<br>3. Enter a valid last name<br>4. Enter a valid address<br>5. Enter a valid city<br>6. Select a valid state from the dropdown<br>7. Enter a valid zip code<br>8. Enter a valid phone number<br>9. Enter a valid SSN<br>10. Enter a valid username<br>11. Enter a valid password<br>12. Enter a different password in Confirm Password<br>13. Click on the Register button | System displays an error message indicating that the passwords do not match | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-004 | Attempt registration with special characters in username | None | 1. Click on the Register link<br>2. Enter a valid first name<br>3. Enter a valid last name<br>4. Enter a valid address<br>5. Enter a valid city<br>6. Select a valid state from the dropdown<br>7. Enter a valid zip code<br>8. Enter a valid phone number<br>9. Enter a valid SSN<br>10. Enter a username with special characters<br>11. Enter a valid password<br>12. Enter the same password in Confirm Password<br>13. Click on the Register button | System displays an error message indicating that special characters are not allowed in the username | Low |
| REGIST-005 | Attempt registration with maximum length for each field | None | 1. Click on the Register link<br>2. Enter a first name with maximum allowed characters<br>3. Enter a last name with maximum allowed characters<br>4. Enter an address with maximum allowed characters<br>5. Enter a city with maximum allowed characters<br>6. Select a valid state from the dropdown<br>7. Enter a zip code with maximum allowed characters<br>8. Enter a phone number with maximum allowed characters<br>9. Enter an SSN with maximum allowed characters<br>10. Enter a username with maximum allowed characters<br>11. Enter a password with maximum allowed characters<br>12. Enter the same password in Confirm Password<br>13. Click on the Register button | System creates the new account and automatically logs the user in | Low |

---

### Open New Account

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Successfully open a new account with valid inputs | User is logged in and on the Open New Account page | 1. Select a valid account type<br>2. Select a valid funding source with sufficient balance<br>3. Click on Open New Account button | A new account is opened, $100.00 is deducted from the selected source account, credited to the new account, and a unique account number is generated | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-002 | Attempt to open a new account with insufficient funds | User is logged in and on the Open New Account page | 1. Select a valid account type<br>2. Select a funding source with less than $100.00 balance<br>3. Click on Open New Account button | An error message is displayed indicating insufficient funds | Medium |
| ONA-003 | Attempt to open a new account without selecting an account type | User is logged in and on the Open New Account page | 1. Leave the account type unselected<br>2. Select a valid funding source with sufficient balance<br>3. Click on Open New Account button | An error message is displayed indicating that account type selection is required | Medium |
| ONA-004 | Attempt to open a new account without selecting a funding source | User is logged in and on the Open New Account page | 1. Select a valid account type<br>2. Leave the funding source unselected<br>3. Click on Open New Account button | An error message is displayed indicating that funding source selection is required | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-005 | Open a new account with exactly $100.00 balance in the funding source | User is logged in and on the Open New Account page | 1. Select a valid account type<br>2. Select a funding source with exactly $100.00 balance<br>3. Click on Open New Account button | A new account is opened, $100.00 is deducted from the selected source account, credited to the new account, and a unique account number is generated | Low |

---

### Account Overview

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-001 | Verify Account Services sidebar is displayed | None | 1. Check if the Account Services sidebar is visible on the page | Account Services sidebar is displayed | High |
| ACCOVE-002 | Verify all actions are listed in Account Services sidebar | None | 1. Check if all actions (Open New Account, Accounts Overview, Transfer Funds, Bill Pay, Find Transactions, Update Contact Info, Request Loan, Log Out) are listed in the Account Services sidebar | All actions are listed in the Account Services sidebar | High |
| ACCOVE-003 | Verify Accounts Overview displays account number | None | 1. Check if the Accounts Overview section displays the account number | Account number is displayed in the Accounts Overview section | High |
| ACCOVE-004 | Verify Accounts Overview displays Balance | None | 1. Check if the Accounts Overview section displays the Balance | Balance is displayed in the Accounts Overview section | High |
| ACCOVE-005 | Verify Accounts Overview displays Available Amount | None | 1. Check if the Accounts Overview section displays the Available Amount | Available Amount is displayed in the Accounts Overview section | High |
| ACCOVE-006 | Verify Accounts Overview displays combined total balance | None | 1. Check if the Accounts Overview section displays the combined total balance | Combined total balance is displayed in the Accounts Overview section | High |
| ACCOVE-007 | Verify clicking 'Log Out' logs the user out | None | 1. Click on 'Log Out' in the Account Services sidebar | User is logged out and redirected to the login page | High |
| ACCOVE-008 | Verify clicking 'Open New Account' navigates to the correct page | None | 1. Click on 'Open New Account' in the Account Services sidebar | User is navigated to the Open New Account page | Medium |
| ACCOVE-009 | Verify clicking 'Transfer Funds' navigates to the correct page | None | 1. Click on 'Transfer Funds' in the Account Services sidebar | User is navigated to the Transfer Funds page | Medium |
| ACCOVE-010 | Verify clicking 'Bill Pay' navigates to the correct page | None | 1. Click on 'Bill Pay' in the Account Services sidebar | User is navigated to the Bill Pay page | Medium |
| ACCOVE-011 | Verify clicking 'Find Transactions' navigates to the correct page | None | 1. Click on 'Find Transactions' in the Account Services sidebar | User is navigated to the Find Transactions page | Medium |
| ACCOVE-012 | Verify clicking 'Update Contact Info' navigates to the correct page | None | 1. Click on 'Update Contact Info' in the Account Services sidebar | User is navigated to the Update Contact Info page | Medium |
| ACCOVE-013 | Verify clicking 'Request Loan' navigates to the correct page | None | 1. Click on 'Request Loan' in the Account Services sidebar | User is navigated to the Request Loan page | Medium |

---

### Transfer Funds

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-001 | Transfer funds with valid inputs | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is processed | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-002 | Transfer funds with zero amount | User is logged in and on the Transfer Funds page | 1. Enter zero as the amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is not processed and an error message is displayed | Medium |
| TRAFUN-003 | Transfer funds with negative amount | User is logged in and on the Transfer Funds page | 1. Enter a negative amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is not processed and an error message is displayed | Medium |
| TRAFUN-004 | Transfer funds with non-numeric amount | User is logged in and on the Transfer Funds page | 1. Enter a non-numeric value as the amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is not processed and an error message is displayed | Medium |
| TRAFUN-005 | Transfer funds with same 'From' and 'To' account numbers | User is logged in and on the Transfer Funds page | 1. Enter a valid amount<br>2. Select the same account for both 'From account number' and 'To account number'<br>3. Click on 'Transfer' button | Transaction is not processed and an error message is displayed | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-006 | Transfer funds with maximum allowable amount | User is logged in and on the Transfer Funds page | 1. Enter the maximum allowable amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is processed | Low |
| TRAFUN-007 | Transfer funds with minimum allowable amount | User is logged in and on the Transfer Funds page | 1. Enter the minimum allowable amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is processed | Low |

---

### Bill Payments

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-001 | Successfully send payment with all valid inputs | None | 1. Enter a valid payee name<br>2. Enter a valid address<br>3. Enter a valid city<br>4. Select a valid state<br>5. Enter a valid zip code<br>6. Enter a valid phone number<br>7. Enter a valid account number<br>8. Re-enter the valid account number for verification<br>9. Enter a valid amount<br>10. Select a valid from account number<br>11. Click on Send Payment | A confirmation message appears upon successful transfer | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-002 | Fail to send payment with mismatched account numbers | None | 1. Enter a valid payee name<br>2. Enter a valid address<br>3. Enter a valid city<br>4. Select a valid state<br>5. Enter a valid zip code<br>6. Enter a valid phone number<br>7. Enter a valid account number<br>8. Enter a different account number for verification<br>9. Enter a valid amount<br>10. Select a valid from account number<br>11. Click on Send Payment | An error message appears indicating account numbers do not match | Medium |
| BILPAY-003 | Fail to send payment with invalid phone number format | None | 1. Enter a valid payee name<br>2. Enter a valid address<br>3. Enter a valid city<br>4. Select a valid state<br>5. Enter a valid zip code<br>6. Enter an invalid phone number format<br>7. Enter a valid account number<br>8. Re-enter the valid account number for verification<br>9. Enter a valid amount<br>10. Select a valid from account number<br>11. Click on Send Payment | An error message appears indicating invalid phone number format | Medium |
| BILPAY-004 | Fail to send payment with empty required fields | None | 1. Leave the payee name empty<br>2. Leave the address empty<br>3. Leave the city empty<br>4. Leave the state unselected<br>5. Leave the zip code empty<br>6. Leave the phone number empty<br>7. Leave the account number empty<br>8. Leave the verify account number empty<br>9. Leave the amount empty<br>10. Leave the from account number unselected<br>11. Click on Send Payment | An error message appears indicating required fields are missing | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-005 | Successfully send payment with maximum length inputs | None | 1. Enter a payee name with maximum allowed characters<br>2. Enter an address with maximum allowed characters<br>3. Enter a city with maximum allowed characters<br>4. Select a valid state<br>5. Enter a zip code with maximum allowed characters<br>6. Enter a phone number with maximum allowed characters<br>7. Enter an account number with maximum allowed characters<br>8. Re-enter the account number with maximum allowed characters for verification<br>9. Enter the maximum allowed amount<br>10. Select a valid from account number<br>11. Click on Send Payment | A confirmation message appears upon successful transfer | Low |

---

### Find Transaction

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-001 | Search transactions with valid Transaction ID | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a valid Transaction ID in the input field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | High |
| FINTRA-002 | Search transactions with valid date and account | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a valid date in MM-DD-YYYY format in the Find by Date field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | High |
| FINTRA-003 | Search transactions with valid date range and account | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | System returns matching transactions in a results table | High |
| FINTRA-004 | Search transactions with valid amount | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a valid amount in the Find by Amount field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-005 | Attempt search with empty Transaction ID | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Leave the Transaction ID input field empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Transaction ID field | Medium |
| FINTRA-006 | Attempt search with empty account selection | User is on the Find Transactions page | 1. Leave the account dropdown unselected<br>2. Enter a valid Transaction ID in the input field<br>3. Click the Find Transactions button | Inline validation message appears next to the account dropdown | Medium |
| FINTRA-007 | Search transactions with empty date field | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Leave the Find by Date field empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Date field | Medium |
| FINTRA-008 | Search transactions with invalid date format | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter an invalid date format in the Find by Date field<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Date field | Medium |
| FINTRA-009 | Attempt search with empty date fields | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Leave the start date field empty<br>3. Leave the end date field empty<br>4. Click the Find Transactions button | Inline validation message appears next to the date fields | Medium |
| FINTRA-010 | Attempt search with invalid date format | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Enter an invalid start date format<br>3. Enter an invalid end date format<br>4. Click the Find Transactions button | Inline validation message appears next to the date fields | Medium |
| FINTRA-011 | Attempt search with only start date filled | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Enter a valid start date in MM-DD-YYYY format<br>3. Leave the end date field empty<br>4. Click the Find Transactions button | Inline validation message appears next to the end date field | Medium |
| FINTRA-012 | Attempt search with only end date filled | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Leave the start date field empty<br>3. Enter a valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | Inline validation message appears next to the start date field | Medium |
| FINTRA-013 | Search transactions with empty amount field | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Leave the Find by Amount field empty<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Amount field | Medium |
| FINTRA-014 | Search transactions with non-numeric amount | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter non-numeric characters in the Find by Amount field<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Amount field | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FINTRA-015 | Search transactions with special characters in Transaction ID | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a Transaction ID containing special characters in the input field<br>3. Click the Find Transactions button | Inline validation message appears next to the Transaction ID field | Low |
| FINTRA-016 | Search transactions with maximum length Transaction ID | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a Transaction ID with maximum allowed length in the input field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | Low |
| FINTRA-017 | Search transactions with special characters in date field | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter special characters in the Find by Date field<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Date field | Low |
| FINTRA-018 | Search transactions with boundary date value | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter a boundary date value in MM-DD-YYYY format in the Find by Date field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | Low |
| FINTRA-019 | Search transactions with date range at boundary values | User is on the Find Transactions page | 1. Select a valid account from the dropdown<br>2. Enter the earliest possible valid start date in MM-DD-YYYY format<br>3. Enter the latest possible valid end date in MM-DD-YYYY format<br>4. Click the Find Transactions button | System returns matching transactions in a results table | Low |
| FINTRA-020 | Search transactions with special characters in amount | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter special characters in the Find by Amount field<br>3. Click the Find Transactions button | Inline validation message appears next to the Find by Amount field | Low |
| FINTRA-021 | Search transactions with maximum allowable amount | User is on the Find Transactions page | 1. Select an account from the dropdown<br>2. Enter the maximum allowable amount in the Find by Amount field<br>3. Click the Find Transactions button | System returns matching transactions in a results table | Low |

---

### Update Profile

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-001 | Update profile with valid data | User is logged in and on the Update Profile page | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Click the Update Profile button | A confirmation message is shown upon successful submission | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-002 | Update profile with empty first name | User is logged in and on the Update Profile page | 1. Leave the first name field empty<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Click the Update Profile button | An error message is displayed indicating the first name is required | Medium |
| UPDPRO-003 | Update profile with invalid phone number format | User is logged in and on the Update Profile page | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter an invalid phone number format<br>8. Click the Update Profile button | An error message is displayed indicating the phone number format is invalid | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-004 | Update profile with maximum length first name | User is logged in and on the Update Profile page | 1. Enter a first name with maximum allowed characters<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Click the Update Profile button | A confirmation message is shown upon successful submission | Low |
| UPDPRO-005 | Update profile with special characters in address | User is logged in and on the Update Profile page | 1. Enter a valid first name<br>2. Enter a valid last name<br>3. Enter an address with special characters<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Click the Update Profile button | A confirmation message is shown upon successful submission | Low |

---

### Request Loan

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-001 | Apply for a loan with all fields filled correctly | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Loan is approved | High |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-002 | Attempt to apply for a loan with loan amount field left blank | None | 1. Leave the loan amount field blank<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Process is not completed | Medium |
| REQLOA-003 | Attempt to apply for a loan with down payment field left blank | None | 1. Enter a valid loan amount<br>2. Leave the down payment field blank<br>3. Select a valid from account number<br>4. Click on Apply Now button | Process is not completed | Medium |
| REQLOA-004 | Attempt to apply for a loan with from account number field left blank | None | 1. Enter a valid loan amount<br>2. Enter a valid down payment<br>3. Leave the from account number field blank<br>4. Click on Apply Now button | Process is not completed | Medium |
| REQLOA-005 | Attempt to apply for a loan with all fields left blank | None | 1. Leave the loan amount field blank<br>2. Leave the down payment field blank<br>3. Leave the from account number field blank<br>4. Click on Apply Now button | Process is not completed | Medium |

#### 🔄 Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-006 | Apply for a loan with maximum valid loan amount | None | 1. Enter the maximum valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Loan is approved | Low |
| REQLOA-007 | Apply for a loan with minimum valid loan amount | None | 1. Enter the minimum valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Loan is approved | Low |
| REQLOA-008 | Apply for a loan with special characters in loan amount | None | 1. Enter special characters in the loan amount field<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Process is not completed | Low |

---

### Logout

#### ✅ Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-001 | Successful Logout | User is logged in | 1. Click on the logout button | User session ends, sensitive data is cleared, and user is returned to the login page | High |
| LOGOUT-002 | Logout Session Termination | User is logged in | 1. Click on the logout button<br>2. Attempt to access a protected page | Access to the protected page is denied and user is redirected to the login page | High |
| LOGOUT-003 | Logout Data Clearance | User is logged in and has sensitive data in session | 1. Click on the logout button<br>2. Check for the presence of sensitive data in session storage | Sensitive data is cleared from session storage | High |
| LOGOUT-004 | Logout Redirect to Login Page | User is logged in | 1. Click on the logout button | User is redirected to the login page | High |
| LOGOUT-005 | Logout Button Visibility | User is logged in | 1. Verify the visibility of the logout button | Logout button is visible | Medium |

#### ❌ Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGOUT-006 | Logout Without Active Session | User is not logged in | 1. Attempt to click on the logout button | No action is performed and user remains on the current page | Medium |

---

## Post-Verification Details

This section shows verification requirements for tests that modify application state.

### ONA-001: Successfully open a new account with valid inputs

**Coverage:** ⚠️ Partial
**Modifies State:** new_account_opening

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the new account appears in the account s... | ⚠️ partial | ACCOVE-003<br>(Verify Accounts Overview di...) | 70% | Run this test after creating a new account to v...<br>This test checks for the presence of an account...<br>**Manual:** Manually verify that the new account ... |
| 2 | Verify the source account balance is reduced by... | ⚠️ partial | ACCOVE-004<br>(Verify Accounts Overview di...) | 60% | Run this test after the action to verify the ba...<br>The test case verifies that the balance is disp...<br>**Manual:** Manually verify that the balance refl... |

**⚠️ Coverage Gaps:**
- This test checks for the presence of an account number, which is part of the requirement, but doe...
- The test case verifies that the balance is displayed in the Account Overview module, but it does ...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ACCOVE-004 | Verify Accounts Overview displays Balance | None | 1. Check if the Accounts Overview section displays the Balance | Balance is displayed in the Accounts Overview section | High |
| ACCOVE-003 | Verify Accounts Overview displays account number | None | 1. Check if the Accounts Overview section displays the account number | Account number is displayed in the Accounts Overview section | High |

---

### TRAFUN-001: Transfer funds with valid inputs

**Coverage:** ⚠️ Partial
**Modifies State:** fund_transfer

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the transfer status is successful | ⚠️ partial | TRAFUN-006<br>(Transfer funds with maximum...) | 60% | Run this test and verify if the transfer status...<br>The test case checks if the transaction is proc...<br>**Manual:** After executing the test, manually ch... |
| 2 | Verify the source and destination account balan... | ❌ not_found | - | - | None of the test cases verify the specific requ...<br>**Manual:** Manually perform a transfer and check... |

**⚠️ Coverage Gaps:**
- The test case checks if the transaction is processed, but it does not explicitly verify the trans...
- None of the test cases verify the specific requirement of checking both source and destination ac...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TRAFUN-006 | Transfer funds with maximum allowable amount | User is logged in and on the Transfer Funds page | 1. Enter the maximum allowable amount<br>2. Select a valid 'From account number'<br>3. Select a valid 'To account number'<br>4. Click on 'Transfer' button | Transaction is processed | Low |

---

### BILPAY-001: Successfully send payment with all valid inputs

**Coverage:** ⚠️ Partial
**Modifies State:** bill_payment

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the payment status is successful | ⚠️ partial | BILPAY-005<br>(Successfully send payment w...) | 70% | Run this test to verify that a confirmation mes...<br>The test case checks for a confirmation message...<br>**Manual:** After executing the test, manually ve... |

**⚠️ Coverage Gaps:**
- The test case checks for a confirmation message upon successful payment, which partially verifies...

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BILPAY-005 | Successfully send payment with maximum length inputs | None | 1. Enter a payee name with maximum allowed characters<br>2. Enter an address with maximum allowed characters<br>3. Enter a city with maximum allowed characters<br>4. Select a valid state<br>5. Enter a zip code with maximum allowed characters<br>6. Enter a phone number with maximum allowed characters<br>7. Enter an account number with maximum allowed characters<br>8. Re-enter the account number with maximum allowed characters for verification<br>9. Enter the maximum allowed amount<br>10. Select a valid from account number<br>11. Click on Send Payment | A confirmation message appears upon successful transfer | Low |

---

### UPDPRO-001: Update profile with valid data

**Coverage:** ✅ Full
**Modifies State:** profile_modification

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the profile update status is successful | ✅ found | UPDPRO-004<br>(Update profile with maximum...) | 90% | Run this test after updating the profile to ver... |

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UPDPRO-004 | Update profile with maximum length first name | User is logged in and on the Update Profile page | 1. Enter a first name with maximum allowed characters<br>2. Enter a valid last name<br>3. Enter a valid address<br>4. Enter a valid city<br>5. Select a valid state from the dropdown<br>6. Enter a valid zip code<br>7. Enter a valid phone number<br>8. Click the Update Profile button | A confirmation message is shown upon successful submission | Low |

---

### REQLOA-001: Apply for a loan with all fields filled correctly

**Coverage:** ✅ Full
**Modifies State:** loan_application

| # | Verification Needed | Status | Matched Test | Confidence | Remarks |
|---|---------------------|--------|--------------|------------|---------|
| 1 | Verify the loan application status is approved | ✅ found | REQLOA-006<br>(Apply for a loan with maxim...) | 90% | Run this test after the action to verify the lo... |

#### 📋 Verification Test Cases to Execute

The following test cases should be executed to verify the action:

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REQLOA-006 | Apply for a loan with maximum valid loan amount | None | 1. Enter the maximum valid loan amount<br>2. Enter a valid down payment<br>3. Select a valid from account number<br>4. Click on Apply Now button | Loan is approved | Low |

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
