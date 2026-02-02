# ParaBank Test Cases

**Website URL:** https://parabank.parasoft.com/parabank/index.htm
**Test Suite Version:** 1.0

---

## Table of Contents
1. [Login](#1-login)
2. [Forgot Password](#2-forgot-password)
3. [Registration](#3-registration)
4. [Open New Account](#4-open-new-account)
5. [Account Overview](#5-account-overview)
6. [Transfer Funds](#6-transfer-funds)
7. [Bill Pay](#7-bill-pay)
8. [Find Transactions](#8-find-transactions)
9. [Update Profile](#9-update-profile)
10. [Request Loan](#10-request-loan)
11. [Logout](#11-logout)

---

## 1. Login

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Valid login with username | Registered user exists | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click "Log In" | User is redirected to Accounts Overview page | High |
| LOGIN-002 | Valid login with email | Registered user exists | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click "Log In" | User is redirected to Accounts Overview page | High |
| LOGIN-003 | Login page elements displayed | None | 1. Navigate to login page | Username field, Password field, Log In button, "Forgot login info?" link, and "Register" link are visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-004 | Invalid username | None | 1. Navigate to login page<br>2. Enter invalid username<br>3. Enter any password<br>4. Click "Log In" | Error message displayed, user remains on login page, fields remain populated | High |
| LOGIN-005 | Invalid password | Registered user exists | 1. Navigate to login page<br>2. Enter valid username<br>3. Enter incorrect password<br>4. Click "Log In" | Error message displayed, user remains on login page | High |
| LOGIN-006 | Empty username | None | 1. Navigate to login page<br>2. Leave username empty<br>3. Enter password<br>4. Click "Log In" | Error message displayed | High |
| LOGIN-007 | Empty password | None | 1. Navigate to login page<br>2. Enter username<br>3. Leave password empty<br>4. Click "Log In" | Error message displayed | High |
| LOGIN-008 | Both fields empty | None | 1. Navigate to login page<br>2. Leave both fields empty<br>3. Click "Log In" | Error message displayed | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-009 | Maximum length username | None | 1. Enter username at max character limit<br>2. Enter valid password<br>3. Click "Log In" | System handles appropriately (accepts or truncates) | Low |
| LOGIN-010 | Maximum length password | None | 1. Enter valid username<br>2. Enter password at max character limit<br>3. Click "Log In" | System handles appropriately | Low |

---

## 2. Forgot Password

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-001 | Successful password recovery | Registered user exists | 1. Click "Forgot login info?"<br>2. Fill all required fields (First Name, Last Name, Address, City, State, Zip Code, SSN)<br>3. Click "Find My Login Info" | Recovery details displayed | High |
| FP-002 | Page elements displayed | None | 1. Navigate to Forgot Login Info page | Customer Lookup form with all fields visible | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-003 | No matching record | None | 1. Fill form with non-existent user data<br>2. Click "Find My Login Info" | Error message: no matching record found | High |
| FP-004 | First Name empty | None | 1. Leave First Name empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for First Name field | High |
| FP-005 | Last Name empty | None | 1. Fill First Name, leave Last Name empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for Last Name field | High |
| FP-006 | Address empty | None | 1. Leave Address empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for Address field | High |
| FP-007 | City empty | None | 1. Leave City empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for City field | High |
| FP-008 | State empty | None | 1. Leave State empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for State field | High |
| FP-009 | Zip Code empty | None | 1. Leave Zip Code empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for Zip Code field | High |
| FP-010 | SSN empty | None | 1. Leave SSN empty<br>2. Fill other fields<br>3. Click "Find My Login Info" | Validation error for SSN field | High |
| FP-011 | All fields empty | None | 1. Leave all fields empty<br>2. Click "Find My Login Info" | Validation errors for all required fields | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FP-012 | Partial SSN match | Registered user exists | 1. Enter correct data with partially incorrect SSN<br>2. Submit form | No matching record found | Medium |
| FP-013 | Case sensitivity - Name | Registered user exists | 1. Enter name with different case<br>2. Submit form | Verify if search is case-sensitive | Low |

---

## 3. Registration

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-001 | Successful registration | None | 1. Click "Register"<br>2. Fill all 11 fields<br>3. Click "Register" | Account created, user auto-logged in | High |
| REG-002 | Registration form displayed | None | 1. Navigate to registration page | All 11 fields visible: First Name, Last Name, Address, City, State, Zip Code, Phone #, SSN, Username, Password, Confirm Password | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REG-003 | First Name empty | None | 1. Leave First Name empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-004 | Last Name empty | None | 1. Leave Last Name empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-005 | Address empty | None | 1. Leave Address empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-006 | City empty | None | 1. Leave City empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-007 | State empty | None | 1. Leave State empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-008 | Zip Code empty | None | 1. Leave Zip Code empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-009 | Phone empty | None | 1. Leave Phone # empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-010 | SSN empty | None | 1. Leave SSN empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-011 | Username empty | None | 1. Leave Username empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-012 | Password empty | None | 1. Leave Password empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-013 | Confirm Password empty | None | 1. Leave Confirm Password empty<br>2. Fill other fields<br>3. Click Register | Validation error | High |
| REG-014 | Password mismatch | None | 1. Fill all fields<br>2. Enter different values for Password and Confirm Password<br>3. Click Register | Validation error: passwords do not match | High |
| REG-015 | Duplicate username | User with username exists | 1. Fill all fields<br>2. Use existing username<br>3. Click Register | Error: username already exists | High |

---

## 4. Open New Account

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Open Checking account | User logged in, has account with >= $100 | 1. Navigate to Open New Account<br>2. Select "Checking"<br>3. Select funding source account<br>4. Click "Open New Account" | New Checking account created, $100 deducted from source, unique account number generated | High |
| ONA-002 | Open Savings account | User logged in, has account with >= $100 | 1. Navigate to Open New Account<br>2. Select "Savings"<br>3. Select funding source account<br>4. Click "Open New Account" | New Savings account created, $100 deducted from source | High |
| ONA-003 | Success message displayed | ONA-001 completed | After account creation | Success message with new account number displayed | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-004 | Insufficient funds | User logged in, account balance < $100 | 1. Select account type<br>2. Select low-balance account as funding source<br>3. Click "Open New Account" | Error: insufficient funds | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-005 | Exactly $100 balance | Account has exactly $100 | 1. Open new account with this funding source | Account created, source balance becomes $0 | Medium |
| ONA-006 | Just under $100 | Account has $99.99 | 1. Open new account with this funding source | Error: insufficient funds | Medium |

---

## 5. Account Overview

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| AO-001 | Display all accounts | User logged in with multiple accounts | 1. Navigate to Accounts Overview | All accounts displayed with Account Number, Balance, Available Amount | High |
| AO-002 | Total balance calculation | User logged in with multiple accounts | 1. View Accounts Overview | Total balance at bottom equals sum of all account balances | High |
| AO-003 | Account number clickable | User logged in | 1. Click on an account number | Navigates to account details (or expected behavior) | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| AO-004 | No accounts | New user with no accounts | 1. Navigate to Accounts Overview | Appropriate message or empty state displayed | Medium |

---

## 6. Transfer Funds

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TF-001 | Successful transfer | User logged in, multiple accounts, sufficient funds | 1. Navigate to Transfer Funds<br>2. Enter amount<br>3. Select "From" account<br>4. Select "To" account<br>5. Click "Transfer" | Transfer processed, success message displayed | High |
| TF-002 | Balance updated after transfer | TF-001 completed | 1. View Accounts Overview | Source account debited, destination account credited | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TF-003 | Insufficient funds | User logged in | 1. Enter amount greater than source balance<br>2. Submit transfer | Error: insufficient funds | High |
| TF-004 | Same source and destination | User logged in | 1. Select same account for From and To<br>2. Submit transfer | Error or prevented from selecting same account | High |
| TF-005 | Empty amount | User logged in | 1. Leave amount empty<br>2. Submit transfer | Validation error | High |
| TF-006 | Zero amount | User logged in | 1. Enter 0 as amount<br>2. Submit transfer | Validation error or handled gracefully | Medium |
| TF-007 | Negative amount | User logged in | 1. Enter negative amount<br>2. Submit transfer | Validation error | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| TF-008 | Transfer exact balance | Account with known balance | 1. Transfer entire account balance | Transfer succeeds, source balance = $0 | Medium |
| TF-009 | Minimum transfer amount | User logged in | 1. Transfer $0.01 | Transfer succeeds or minimum amount error | Low |
| TF-010 | Large transfer amount | Account with high balance | 1. Transfer maximum allowed amount | System handles appropriately | Low |

---

## 7. Bill Pay

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BP-001 | Successful bill payment | User logged in, sufficient funds | 1. Navigate to Bill Pay<br>2. Fill all fields: Payee Name, Address, City, State, Zip Code, Phone, Account number, Verify Account number, Amount<br>3. Select source account<br>4. Click "Send Payment" | Payment processed, confirmation message displayed | High |
| BP-002 | Balance deducted | BP-001 completed | 1. View Accounts Overview | Source account balance reduced by payment amount | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BP-003 | Payee Name empty | User logged in | 1. Leave Payee Name empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-004 | Address empty | User logged in | 1. Leave Address empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-005 | City empty | User logged in | 1. Leave City empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-006 | State empty | User logged in | 1. Leave State empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-007 | Zip Code empty | User logged in | 1. Leave Zip Code empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-008 | Phone empty | User logged in | 1. Leave Phone empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-009 | Account number empty | User logged in | 1. Leave Account number empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-010 | Verify Account number empty | User logged in | 1. Leave Verify Account number empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-011 | Account numbers mismatch | User logged in | 1. Enter different values for Account and Verify Account<br>2. Submit | Validation error: account numbers do not match | High |
| BP-012 | Amount empty | User logged in | 1. Leave Amount empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| BP-013 | Insufficient funds | User logged in | 1. Enter amount greater than account balance<br>2. Submit | Error: insufficient funds | High |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| BP-014 | Minimum payment | User logged in | 1. Enter $0.01 as amount<br>2. Submit | Payment processed or minimum amount error | Low |
| BP-015 | Pay entire balance | User logged in | 1. Enter exact account balance as amount | Payment processed, balance = $0 | Medium |

---

## 8. Find Transactions

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FT-001 | Find by Transaction ID | User logged in, transactions exist | 1. Navigate to Find Transactions<br>2. Select account<br>3. Enter Transaction ID<br>4. Click "Find Transactions" | Matching transaction displayed | High |
| FT-002 | Find by Date | User logged in, transactions exist | 1. Select account<br>2. Enter date (MM-DD-YYYY)<br>3. Click "Find Transactions" | Transactions from that date displayed | High |
| FT-003 | Find by Date Range | User logged in, transactions exist | 1. Select account<br>2. Enter start and end dates<br>3. Click "Find Transactions" | Transactions within range displayed | High |
| FT-004 | Find by Amount | User logged in, transactions exist | 1. Select account<br>2. Enter amount<br>3. Click "Find Transactions" | Transactions matching amount displayed | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FT-005 | Invalid Transaction ID | User logged in | 1. Enter non-existent Transaction ID<br>2. Submit | No results or appropriate message | High |
| FT-006 | Empty Transaction ID | User logged in | 1. Leave Transaction ID empty<br>2. Submit | Validation error | High |
| FT-007 | Invalid date format | User logged in | 1. Enter date in wrong format (not MM-DD-YYYY)<br>2. Submit | Validation error | High |
| FT-008 | Empty date fields | User logged in | 1. Leave date fields empty<br>2. Submit | Validation error | High |
| FT-009 | End date before start date | User logged in | 1. Enter end date earlier than start date<br>2. Submit | Validation error or no results | Medium |
| FT-010 | Empty amount | User logged in | 1. Leave amount empty<br>2. Submit | Validation error | High |
| FT-011 | No matching transactions | User logged in | 1. Search with criteria that has no matches | "No transactions found" message | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FT-012 | Same start and end date | User logged in | 1. Enter same date for start and end | Transactions for that single day | Low |
| FT-013 | Future date | User logged in | 1. Enter future date<br>2. Submit | No results or appropriate handling | Low |

---

## 9. Update Profile

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UP-001 | Successful profile update | User logged in | 1. Navigate to Update Profile<br>2. Modify any field<br>3. Click "Update Profile" | Confirmation message displayed | High |
| UP-002 | Pre-populated fields | User logged in | 1. Navigate to Update Profile | All fields pre-filled with current user data | High |
| UP-003 | Update First Name | User logged in | 1. Change First Name<br>2. Submit | First Name updated successfully | Medium |
| UP-004 | Update Last Name | User logged in | 1. Change Last Name<br>2. Submit | Last Name updated successfully | Medium |
| UP-005 | Update Address | User logged in | 1. Change Address<br>2. Submit | Address updated successfully | Medium |
| UP-006 | Update City | User logged in | 1. Change City<br>2. Submit | City updated successfully | Medium |
| UP-007 | Update State | User logged in | 1. Change State<br>2. Submit | State updated successfully | Medium |
| UP-008 | Update Zip Code | User logged in | 1. Change Zip Code<br>2. Submit | Zip Code updated successfully | Medium |
| UP-009 | Update Phone | User logged in | 1. Change Phone number<br>2. Submit | Phone updated successfully | Medium |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| UP-010 | First Name empty | User logged in | 1. Clear First Name<br>2. Submit | Validation error | High |
| UP-011 | Last Name empty | User logged in | 1. Clear Last Name<br>2. Submit | Validation error | High |
| UP-012 | Address empty | User logged in | 1. Clear Address<br>2. Submit | Validation error | High |
| UP-013 | City empty | User logged in | 1. Clear City<br>2. Submit | Validation error | High |
| UP-014 | State empty | User logged in | 1. Clear State<br>2. Submit | Validation error | High |
| UP-015 | Zip Code empty | User logged in | 1. Clear Zip Code<br>2. Submit | Validation error | High |
| UP-016 | Phone empty | User logged in | 1. Clear Phone<br>2. Submit | Validation error | High |

---

## 10. Request Loan

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| RL-001 | Successful loan application | User logged in | 1. Navigate to Request Loan<br>2. Enter Loan Amount<br>3. Enter Down Payment<br>4. Select account<br>5. Click "Apply Now" | Loan approved, success message displayed | High |
| RL-002 | Loan account created | RL-001 completed | 1. View Accounts Overview | New loan account visible | High |

### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| RL-003 | Loan Amount empty | User logged in | 1. Leave Loan Amount empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| RL-004 | Down Payment empty | User logged in | 1. Leave Down Payment empty<br>2. Fill other fields<br>3. Submit | Validation error | High |
| RL-005 | No account selected | User logged in | 1. Fill amounts<br>2. Don't select account<br>3. Submit | Validation error | High |
| RL-006 | Zero loan amount | User logged in | 1. Enter 0 for Loan Amount<br>2. Submit | Validation error | Medium |
| RL-007 | Negative loan amount | User logged in | 1. Enter negative Loan Amount<br>2. Submit | Validation error | Medium |

### Boundary Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| RL-008 | Down payment equals loan | User logged in | 1. Enter same value for Loan and Down Payment | System handles appropriately | Low |
| RL-009 | Down payment exceeds loan | User logged in | 1. Enter Down Payment > Loan Amount | Validation error or handled gracefully | Low |
| RL-010 | Minimum loan amount | User logged in | 1. Enter smallest possible loan amount | Loan processed or minimum error | Low |

---

## 11. Logout

### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LO-001 | Successful logout | User logged in | 1. Click "Log Out" in left menu | User redirected to login page | High |
| LO-002 | Session cleared | LO-001 completed | 1. Try to access protected page directly | Redirected to login or access denied | High |
| LO-003 | Back button after logout | LO-001 completed | 1. Click browser back button | Cannot access account data (session ended) | High |

---

## Test Summary

| Module | Total Tests | High Priority | Medium Priority | Low Priority |
|--------|-------------|---------------|-----------------|--------------|
| Login | 10 | 7 | 1 | 2 |
| Forgot Password | 13 | 10 | 2 | 1 |
| Registration | 15 | 14 | 1 | 0 |
| Open New Account | 6 | 4 | 2 | 0 |
| Account Overview | 4 | 2 | 2 | 0 |
| Transfer Funds | 10 | 5 | 2 | 3 |
| Bill Pay | 15 | 13 | 2 | 0 |
| Find Transactions | 13 | 8 | 2 | 3 |
| Update Profile | 16 | 14 | 2 | 0 |
| Request Loan | 10 | 6 | 2 | 2 |
| Logout | 3 | 3 | 0 | 0 |
| **TOTAL** | **115** | **86** | **18** | **11** |
