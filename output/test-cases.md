# Parabank Functional Overview

**Base URL:** https://parabank.parasoft.com/parabank/index.htm
**Generated:** 2025-12-25T18:56:34.051829

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 43 |

### By Type

| Type | Count |
|------|-------|
| Positive | 10 |
| Negative | 27 |
| Edge Case | 6 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 18 |
| Medium | 20 |
| Low | 5 |

---

## Test Cases

### Login

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-001 | Successful login using valid username | User has a registered account with a valid username | 1. Enter valid username into the username field 2. Enter valid password into the password field 3. Click the Log In button | User is redirected to the account dashboard | High |
| LOGIN-002 | Successful login using valid email address | User has a registered account with a valid email address | 1. Enter valid email address into the username field 2. Enter valid password into the password field 3. Click the Log In button | User is redirected to the account dashboard | High |
| LOGIN-005 | Retry login after authentication error | User has a registered account | 1. Enter an incorrect password into the password field 2. Click the Log In button 3. Clear the password field 4. Enter the correct password into the password field 5. Click the Log In button | User is successfully redirected to the account dashboard after the second attempt | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-003 | Login failure with unregistered credentials | None | 1. Enter an unregistered username into the username field 2. Enter any password into the password field 3. Click the Log In button | An error message is displayed and the input fields remain populated with the entered values | High |
| LOGIN-004 | Login failure with incorrect password | User has a registered account | 1. Enter a valid registered username into the username field 2. Enter an incorrect password into the password field 3. Click the Log In button | An error message is displayed and the input fields remain populated with the entered values | High |
| LOGIN-006 | Login attempt with empty fields | None | 1. Leave username and password fields empty 2. Click the Log In button | An error message is displayed indicating that credentials are required | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| LOGIN-007 | Login with special characters in username | User has a registered account containing special characters in the username | 1. Enter username containing special characters (e.g., user!@#) into the username field 2. Enter valid password into the password field 3. Click the Log In button | User is redirected to the account dashboard | Low |

---

### Forgot Password

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-001 | Successful customer lookup with valid details | A registered customer record exists in the system | 1. Enter a valid First Name into the First Name field 2. Enter a valid Last Name into the Last Name field 3. Enter a valid Address into the Address field 4. Enter a valid City into the City field 5. Select a valid State from the State dropdown 6. Enter a valid Zip Code into the Zip Code field 7. Enter a valid SSN into the SSN field 8. Click the Find My Login Info button | The page displays the appropriate recovery details for the matching record | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-002 | Error message displayed when no matching record is found | No customer record exists with the provided details | 1. Enter non-existent First Name into the First Name field 2. Enter non-existent Last Name into the Last Name field 3. Enter non-existent Address into the Address field 4. Enter non-existent City into the City field 5. Select any State from the State dropdown 6. Enter a non-existent Zip Code into the Zip Code field 7. Enter a non-existent SSN into the SSN field 8. Click the Find My Login Info button | The page displays an error message indicating no matching record was found | High |
| FORPAS-003 | Validation error when First Name is left blank | None | 1. Leave the First Name field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the First Name field | Medium |
| FORPAS-004 | Validation error when Last Name is left blank | None | 1. Leave the Last Name field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the Last Name field | Medium |
| FORPAS-005 | Validation error when Address is left blank | None | 1. Leave the Address field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the Address field | Medium |
| FORPAS-006 | Validation error when City is left blank | None | 1. Leave the City field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the City field | Medium |
| FORPAS-007 | Validation error when Zip Code is left blank | None | 1. Leave the Zip Code field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the Zip Code field | Medium |
| FORPAS-008 | Validation error when SSN is left blank | None | 1. Leave the SSN field empty 2. Fill all other required fields with valid data 3. Click the Find My Login Info button | A prompt appears requesting the user to complete the SSN field | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| FORPAS-009 | Customer lookup with special characters in name fields | A record exists with special characters in the name (e.g., O'Connor) | 1. Enter 'O'Connor' into the Last Name field 2. Fill all other fields with matching valid data 3. Click the Find My Login Info button | The page successfully finds and displays the recovery details for the record | Low |

---

### Register

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-001 | Successful login with valid credentials | User has an existing account with a valid username and password | 1. Enter a valid username into the Username field 2. Enter the corresponding valid password into the Password field 3. Click the Log In button | The user is successfully authenticated and granted access to their account | High |
| REGIST-002 | Successful account registration with all valid fields | The registration form is loaded and the user is not logged in | 1. Enter 'John' into the First Name field 2. Enter 'Doe' into the Last Name field 3. Enter '123 Maple Street' into the Address field 4. Enter 'Springfield' into the City field 5. Enter 'Illinois' into the State field 6. Enter '62704' into the Zip Code field 7. Enter '555-0199' into the Phone # field 8. Enter '999-00-1111' into the SSN field 9. Enter 'johndoe_unique' into the Username field 10. Enter 'Password123!' into the Password field 11. Enter 'Password123!' into the Confirm Password field 12. Click the Register button | The account is created and the user is automatically redirected to the logged-in state/dashboard | High |
| REGIST-010 | Verify navigation to Forgot Login Info page | None | 1. Click the 'Forgot login info?' link | The user is redirected to the password recovery or account assistance page | Medium |
| REGIST-011 | Verify navigation to Register page | None | 1. Click the 'Register' link | The user is redirected to the account registration page | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-003 | Login failure with empty username | None | 1. Leave the Username field empty 2. Enter a valid password into the Password field 3. Click the Log In button | The system prevents login and displays a validation error indicating the username is mandatory | High |
| REGIST-004 | Login failure with empty password | None | 1. Enter a valid username into the Username field 2. Leave the Password field empty 3. Click the Log In button | The system prevents login and displays a validation error indicating the password is mandatory | High |
| REGIST-005 | Registration fails when First Name is empty | The registration form is loaded | 1. Leave the First Name field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating First Name is mandatory and no account is created | High |
| REGIST-006 | Registration fails when Last Name is empty | The registration form is loaded | 1. Leave the Last Name field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Last Name is mandatory and no account is created | High |
| REGIST-007 | Registration fails when Username is empty | The registration form is loaded | 1. Leave the Username field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Username is mandatory | High |
| REGIST-008 | Registration fails when Password is empty | The registration form is loaded | 1. Leave the Password field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Password is mandatory | High |
| REGIST-009 | Registration fails when Confirm Password is empty | The registration form is loaded | 1. Leave the Confirm Password field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Confirm Password is mandatory | High |
| REGIST-012 | Login failure with both fields empty | None | 1. Leave the Username field empty 2. Leave the Password field empty 3. Click the Log In button | The system prevents login and displays validation errors for both mandatory fields | Medium |
| REGIST-013 | Registration fails when Address is empty | The registration form is loaded | 1. Leave the Address field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Address is mandatory | Medium |
| REGIST-014 | Registration fails when City is empty | The registration form is loaded | 1. Leave the City field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating City is mandatory | Medium |
| REGIST-015 | Registration fails when State is empty | The registration form is loaded | 1. Leave the State field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating State is mandatory | Medium |
| REGIST-016 | Registration fails when Zip Code is empty | The registration form is loaded | 1. Leave the Zip Code field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Zip Code is mandatory | Medium |
| REGIST-017 | Registration fails when Phone # is empty | The registration form is loaded | 1. Leave the Phone # field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating Phone # is mandatory | Medium |
| REGIST-018 | Registration fails when SSN is empty | The registration form is loaded | 1. Leave the SSN field empty 2. Fill all other mandatory fields with valid data 3. Click the Register button | The system displays a validation error indicating SSN is mandatory | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| REGIST-019 | Login with special characters in username and password | An account exists where the username and password contain special characters (e.g., !@#$%^&*) | 1. Enter the username containing special characters into the Username field 2. Enter the password containing special characters into the Password field 3. Click the Log In button | The user is successfully authenticated and granted access to their account | Low |
| REGIST-020 | Registration with special characters in name and address fields | The registration form is loaded | 1. Enter 'O'Connor-Smith' into the Last Name field 2. Enter 'Apt #4, 1/2 St.' into the Address field 3. Fill all other mandatory fields with valid data 4. Click the Register button | The system successfully creates the account and logs the user in | Low |
| REGIST-021 | Registration with very long strings in mandatory fields | The registration form is loaded | 1. Enter a 100-character string into the First Name field 2. Enter a 100-character string into the Username field 3. Fill all other mandatory fields with valid data 4. Click the Register button | The system successfully creates the account and logs the user in | Low |

---

### Open New Account

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-001 | Open New Savings Account with valid funding source | User is on the Open New Account page and has at least one existing account with a balance of $100.00 or more | 1. Select 'Savings' from the account type dropdown 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button | A new savings account is created with a unique account number and a $100.00 credit, while the source account is debited $100.00 | High |
| ONA-002 | Open New Checking Account with valid funding source | User is on the Open New Account page and has at least one existing account with a balance of $100.00 or more | 1. Select 'Checking' from the account type dropdown 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button | A new checking account is created with a unique account number and a $100.00 credit, while the source account is debited $100.00 | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-003 | Attempt to open account with insufficient funds in source account | User is on the Open New Account page and selects a source account with a balance less than $100.00 | 1. Select 'Savings' from the account type dropdown 2. Select the account with insufficient funds from the funding source dropdown 3. Click the 'Open New Account' button | The system displays an error message stating that the required opening deposit of $100.00 is not available in the selected source account | High |
| ONA-004 | Attempt to open account without selecting an account type | User is on the Open New Account page | 1. Leave the account type dropdown unselected 2. Select an existing account from the funding source dropdown 3. Click the 'Open New Account' button | The system displays a validation error indicating that an account type must be selected | Medium |
| ONA-005 | Attempt to open account without selecting a funding source | User is on the Open New Account page | 1. Select 'Savings' from the account type dropdown 2. Leave the funding source dropdown unselected 3. Click the 'Open New Account' button | The system displays a validation error indicating that a funding source must be selected | Medium |

#### Boundary/Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| ONA-006 | Verify unique account number generation for consecutive requests | User is on the Open New Account page and has sufficient funds for multiple accounts | 1. Open a Savings account using a valid funding source 2. Return to the Open New Account page 3. Open a second Savings account using the same funding source | Two different unique account numbers are generated for the two new accounts | Medium |

---

## Navigation Graph

![Navigation Graph](output/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| Login | /index.htm | No | 7 |
| Forgot Password | /lookup.htm | No | 9 |
| Register | /register.htm | No | 21 |
| Open New Account | /openaccount.htm | Yes | 6 |
| Account Overview | /overview.htm | Yes | 0 |
| Transfer Funds | /transfer.htm | Yes | 0 |
| Bill Payments | /billpay.htm | Yes | 0 |
| Find Transaction | /findtrans.htm | Yes | 0 |
| Update Profile | /updateprofile.htm | Yes | 0 |
| Request Loan | /requestloan.htm | Yes | 0 |
| Logout | /logout.htm | Yes | 0 |
