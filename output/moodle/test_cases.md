# Moodle

**Base URL:** 
**Generated:** 2026-03-04T04:56:31.298045

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 173 |

### By Type

| Type | Count |
|------|-------|
| Positive | 132 |
| Negative | 34 |
| Edge Case | 7 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 66 |
| Medium | 81 |
| Low | 26 |

### Post-Verification Coverage

| Metric | Count |
|--------|-------|
| Tests Needing Verification | 23 |
| Full Coverage | 12 |
| Partial Coverage | 2 |
| No Coverage | 9 |

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 23 |
| Automated Steps | 23 |
| Manual Steps | 12 |
| Automation Rate | 65.7% |

---

## Test Cases

### 1. Login

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1.1.LOG-001 | Successful login with valid username and password | None | 1. Enter a valid username<br>2. Enter a valid password<br>3. Click the Log in button | Redirects to the Dashboard | High |
| 1.1.LOG-006 | Access as a guest | None | 1. Click the Access as a guest button | Access granted as a guest without login | Low |
| 1.1.LOG-007 | Cookies notice button functionality | None | 1. Click the Cookies notice button | Cookies notice is accepted and disappears | Low |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1.1.LOG-002 | Username field empty | None | 1. Leave the Username field empty<br>2. Enter a valid password<br>3. Click the Log in button | Error message appears for empty Username field | Medium |
| 1.1.LOG-003 | Password field empty | None | 1. Enter a valid username<br>2. Leave the Password field empty<br>3. Click the Log in button | Error message appears for empty Password field | Medium |
| 1.1.LOG-004 | Invalid credentials error | None | 1. Enter an invalid username<br>2. Enter an invalid password<br>3. Click the Log in button | Error message appears for invalid credentials | Medium |
| 1.1.LOG-005 | Username field remains populated after error | None | 1. Enter an invalid username<br>2. Enter an invalid password<br>3. Click the Log in button | Username field remains populated for correction | Medium |

---

### 2. Dashboard

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 2.2.DAS-001 | Verify personalized greeting displays correctly | User is logged in | 1. Check the top of the dashboard for the personalized greeting | The greeting displays 'Hi, [Name]!' with a waving hand emoji | High |
| 2.2.DAS-004 | Verify Search field functionality | User is logged in | 1. Enter a search term in the Search field<br>2. Press Enter or click the search icon | Search results relevant to the entered term are displayed | High |
| 2.2.DAS-005 | Verify New event button functionality | User is logged in | 1. Click on the New event button | A form or modal to create a new event is displayed | High |
| 2.2.DAS-006 | Verify Next 7 days dropdown functionality | User is logged in | 1. Click on the Next 7 days dropdown<br>2. Select an option from the dropdown | The selected option is applied and displayed correctly | Medium |
| 2.2.DAS-007 | Verify Sort by dates dropdown functionality | User is logged in | 1. Click on the Sort by dates dropdown<br>2. Select an option from the dropdown | The selected sorting option is applied and displayed correctly | Medium |
| 2.2.DAS-008 | Verify All courses dropdown functionality | User is logged in | 1. Click on the All courses dropdown<br>2. Select a course from the dropdown | The selected course is displayed correctly | Medium |
| 2.2.DAS-009 | Verify Navigation arrows functionality | User is logged in | 1. Click on the navigation arrows | The content navigates to the previous or next section | Medium |
| 2.2.DAS-010 | Verify Full calendar link functionality | User is logged in | 1. Click on the Full calendar link | The full calendar view is displayed | Medium |
| 2.2.DAS-011 | Verify Import or export calendars link functionality | User is logged in | 1. Click on the Import or export calendars link | Options to import or export calendars are displayed | Medium |
| 2.2.DAS-012 | Verify Edit mode toggle functionality | User is logged in | 1. Toggle the Edit mode | The dashboard switches to edit mode, allowing modifications | Medium |
| 2.2.DAS-013 | Verify Reset page to default button functionality | User is logged in | 1. Click on the Reset page to default button | The dashboard resets to its default layout | Medium |
| 2.2.DAS-014 | Verify + Add a block button functionality | User is logged in | 1. Click on the + Add a block button | The Add a block modal is displayed | Medium |
| 2.2.DAS-015 | Verify Three-dot menu functionality | User is logged in | 1. Click on the Three-dot menu | Options related to the block or item are displayed | Medium |
| 2.2.DAS-017 | Verify Add a block modal X button functionality | Add a block modal is open | 1. Click on the X button in the Add a block modal | The Add a block modal is closed | Low |
| 2.2.DAS-018 | Verify Add a block modal Cancel button functionality | Add a block modal is open | 1. Click on the Cancel button in the Add a block modal | The Add a block modal is closed | Low |
| 2.2.DAS-019 | Verify Add a block page Cancel link functionality | User is on the Add a block page | 1. Click on the Cancel link | The user is returned to the previous page or dashboard | Low |
| 2.2.DAS-020 | Verify Move icon functionality | User is in edit mode | 1. Drag and drop a block using the Move icon | The block is moved to the new location | Low |
| 2.2.DAS-002 | Verify Timeline block is visible | User is logged in | 1. Check the main content area for the Timeline block | The Timeline block is visible in the main content area | High |
| 2.2.DAS-003 | Verify Calendar block is visible | User is logged in | 1. Check the main content area for the Calendar block | The Calendar block is visible in the main content area | High |
| 2.2.DAS-016 | Verify No activities require action icon visibility | User is logged in | 1. Check for the No activities require action icon | The icon is visible if no activities require action | Low |

---

### 3. My Courses

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 3.3MC-003 | Verify search functionality in the search field | User is logged in and enrolled in courses | 1. Enter a course name in the search field<br>2. Press Enter or click the search icon | Courses matching the search term are displayed | High |
| 3.3MC-004 | Verify functionality of 'All' dropdown | None | 1. Click on the 'All' dropdown<br>2. Select a different category from the dropdown | Courses are filtered according to the selected category | Medium |
| 3.3MC-005 | Verify sorting functionality by course name | User is logged in and enrolled in multiple courses | 1. Click on the 'Sort by course name' dropdown<br>2. Select an option to sort courses | Courses are sorted according to the selected option | Medium |
| 3.3MC-006 | Verify 'Star this course' option functionality | User is logged in and enrolled in courses | 1. Click on the three-dot menu on a course card<br>2. Select 'Star this course' option | The course is marked as starred | Medium |
| 3.3MC-007 | Verify 'Remove from view' option functionality | User is logged in and enrolled in courses | 1. Click on the three-dot menu on a course card<br>2. Select 'Remove from view' option | The course is removed from the current view | Medium |
| 3.3MC-001 | Verify My Courses page displays with correct headings | User is logged in and enrolled in at least one course | 1. Check for the presence of 'My courses' heading<br>2. Check for the presence of 'Course overview' subheading | 'My courses' heading and 'Course overview' subheading are displayed correctly | High |
| 3.3MC-002 | Verify each course is displayed as a visual card | User is logged in and enrolled in multiple courses | 1. Check that each course is displayed as a visual card<br>2. Verify each card contains a course image, course name link, and category name | All courses are displayed as visual cards with image, name, and category | High |

---

### 4. Course Page

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 4.4CP-010 | Verify Edit mode toggle is available | Course page is loaded | 1. Check for the presence of the Edit mode toggle | Edit mode toggle is available | High |
| 4.4CP-011 | Verify collapsible chevron arrow is functional | Course page is loaded | 1. Click on the collapsible chevron arrow | Sections collapse or expand when the chevron arrow is clicked | Medium |
| 4.4CP-012 | Verify Collapse all link collapses all sections | Course page is loaded | 1. Click on the Collapse all link | All sections are collapsed | Medium |
| 4.4CP-015 | Verify Close button (X) is functional | Course page is loaded | 1. Click on the Close button (X) | Page or modal is closed | Medium |
| 4.4CP-001 | Verify course full name is displayed as heading | Course page is loaded | 1. Check the heading at the top of the page | Course full name is displayed as a heading | High |
| 4.4CP-002 | Verify horizontal navigation bar is displayed | Course page is loaded | 1. Check for the presence of the horizontal navigation bar | Horizontal navigation bar is displayed | High |
| 4.4CP-003 | Verify Course tab is present in navigation bar | Course page is loaded | 1. Check for the Course tab in the navigation bar | Course tab is present in the navigation bar | High |
| 4.4CP-004 | Verify Settings tab is present in navigation bar | Course page is loaded | 1. Check for the Settings tab in the navigation bar | Settings tab is present in the navigation bar | High |
| 4.4CP-005 | Verify Participants tab is present in navigation bar | Course page is loaded | 1. Check for the Participants tab in the navigation bar | Participants tab is present in the navigation bar | High |
| 4.4CP-006 | Verify Grades tab is present in navigation bar | Course page is loaded | 1. Check for the Grades tab in the navigation bar | Grades tab is present in the navigation bar | High |
| 4.4CP-007 | Verify Activities tab is present in navigation bar | Course page is loaded | 1. Check for the Activities tab in the navigation bar | Activities tab is present in the navigation bar | High |
| 4.4CP-008 | Verify More dropdown is present in navigation bar | Course page is loaded | 1. Check for the More dropdown in the navigation bar | More dropdown is present in the navigation bar | High |
| 4.4CP-009 | Verify Competencies tab is present in navigation bar | Course page is loaded | 1. Check for the Competencies tab in the navigation bar | Competencies tab is present in the navigation bar | High |
| 4.4CP-013 | Verify activity icon is displayed next to activity name | Course page is loaded | 1. Check for the activity icon next to each activity name | Activity icon is displayed next to each activity name | Medium |
| 4.4CP-014 | Verify Course Index is displayed | Course page is loaded | 1. Check for the presence of the Course Index | Course Index is displayed | Medium |

---

### 5. Adding Activities (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5.5AA(O-001 | Enable editing mode | None | 1. Click the edit mode toggle | Editing mode is enabled | High |
| 5.5AA(O-002 | Open Activity Chooser | Editing mode is enabled | 1. Click the + button | Activity Chooser modal is displayed | High |
| 5.5AA(O-003 | Select an activity from the Activity Chooser | Activity Chooser modal is open | 1. Select an activity or resource option from the grid | Selected activity or resource is highlighted | High |
| 5.5AA(O-004 | Add selected activity to course | An activity or resource is selected in the Activity Chooser | 1. Click the Add button | Selected activity or resource is added to the course | High |
| 5.5AA(O-005 | Create new assignment with all required fields | None | 1. Enter a valid assignment name<br>2. Enter a valid description<br>3. Select 'Display description on course page' checkbox<br>4. Enter valid activity instructions<br>5. Upload a valid additional file<br>6. Enable 'Allow submissions from' and select a valid date<br>7. Enable 'Due date' and select a valid date<br>8. Enable 'Cut-off date' and select a valid date<br>9. Enable 'Remind me to grade by' and select a valid date<br>10. Select 'Always show description' checkbox<br>11. Select 'Online text' checkbox<br>12. Select 'File submissions' checkbox<br>13. Select a valid option from 'Maximum number of uploaded files' dropdown<br>14. Select a valid option from 'Maximum submission size' dropdown<br>15. Enter valid accepted file types<br>16. Select 'Send content change notification' checkbox<br>17. Click 'Save and return to course' button | Assignment is created and user is returned to the course page | High |
| 5.5AA(O-006 | Create new assignment with 'Save and display' | None | 1. Enter a valid assignment name<br>2. Enter a valid description<br>3. Click 'Save and display' button | Assignment is created and the assignment page is displayed | High |
| 5.5AA(O-008 | Search for an activity using the search field | Activity Chooser modal is open | 1. Enter a search term in the search field<br>2. Verify the search results | Relevant activities or resources are displayed based on the search term | Medium |
| 5.5AA(O-009 | Filter activities by category | Activity Chooser modal is open | 1. Select a category filter<br>2. Verify the filtered results | Activities or resources are filtered by the selected category | Medium |
| 5.5AA(O-010 | Cancel new assignment creation | None | 1. Enter a valid assignment name<br>2. Enter a valid description<br>3. Click 'Cancel' button | No assignment is created and changes are discarded | Medium |
| 5.5AA(O-013 | Verify info button displays additional information | Activity Chooser modal is open | 1. Click the Info button for an activity or resource | Additional information about the activity or resource is displayed | Low |
| 5.5AA(O-014 | Verify star button marks activity as favorite | Activity Chooser modal is open | 1. Click the Star button for an activity or resource | Activity or resource is marked as favorite | Low |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5.5AA(O-007 | Assignment name field empty | None | 1. Leave the assignment name field empty<br>2. Enter a valid description<br>3. Click 'Save and return to course' button | Error message displayed indicating assignment name is required | High |
| 5.5AA(O-011 | Attempt to add activity without selecting any option | Activity Chooser modal is open | 1. Click the Add button without selecting an activity or resource | Error message is displayed indicating no selection was made | Medium |
| 5.5AA(O-012 | Upload file exceeding maximum size | None | 1. Enter a valid assignment name<br>2. Upload a file larger than 100 MB in the additional files upload area<br>3. Click 'Save and return to course' button | Error message displayed indicating file size exceeds the maximum limit | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5.5AA(O-015 | Maximum submission size boundary test | None | 1. Enter a valid assignment name<br>2. Select 'File submissions' checkbox<br>3. Select '100 MB' from 'Maximum submission size' dropdown<br>4. Click 'Save and return to course' button | Assignment is created with maximum submission size set to 100 MB | Low |
| 5.5AA(O-016 | Enable and set same start and end date for submissions | None | 1. Enter a valid assignment name<br>2. Enable 'Allow submissions from' and select a valid date<br>3. Enable 'Due date' and select the same date as 'Allow submissions from'<br>4. Click 'Save and return to course' button | Assignment is created with the same start and end date for submissions | Low |

---

### 6. Course Settings (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6.6CS(O-001 | Save course settings with all required fields filled | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category from the dropdown<br>4. Click the Save and display button | Course settings are saved successfully and displayed | High |
| 6.6CS(O-005 | Verify all dropdowns are displayed correctly | User is on the Course Settings page | 1. Verify the presence of Course visibility dropdown<br>2. Verify the presence of Format dropdown<br>3. Verify the presence of Hidden sections dropdown<br>4. Verify the presence of Course layout dropdown<br>5. Verify the presence of Force language dropdown<br>6. Verify the presence of Number of announcements dropdown<br>7. Verify the presence of Show gradebook to students dropdown<br>8. Verify the presence of Show activity reports dropdown<br>9. Verify the presence of Show activity dates dropdown<br>10. Verify the presence of Maximum upload size dropdown<br>11. Verify the presence of Enable completion tracking dropdown<br>12. Verify the presence of Show activity completion conditions dropdown<br>13. Verify the presence of Group mode dropdown<br>14. Verify the presence of Force group mode dropdown<br>15. Verify the presence of Default grouping dropdown<br>16. Verify the presence of Tags field with search dropdown | All dropdowns and fields are displayed correctly on the page | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6.6CS(O-002 | Course full name field empty | User is on the Course Settings page | 1. Leave the course full name field empty<br>2. Enter a valid course short name<br>3. Select a valid course category from the dropdown<br>4. Click the Save and display button | An error message is displayed indicating that the course full name is required | High |
| 6.6CS(O-003 | Course short name field empty | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Leave the course short name field empty<br>3. Select a valid course category from the dropdown<br>4. Click the Save and display button | An error message is displayed indicating that the course short name is required | High |
| 6.6CS(O-004 | Course category field empty | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Leave the course category field empty<br>4. Click the Save and display button | An error message is displayed indicating that the course category is required | High |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6.6CS(O-006 | Course start date and end date are the same | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category from the dropdown<br>4. Set the course start date and end date to the same date<br>5. Click the Save and display button | Course settings are saved successfully with the same start and end date | Low |
| 6.6CS(O-007 | Course end date set in the past | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category from the dropdown<br>4. Set the course end date to a date in the past<br>5. Click the Save and display button | An error message is displayed indicating that the course end date cannot be in the past | Low |
| 6.6CS(O-008 | Maximum upload size dropdown boundary test | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category from the dropdown<br>4. Select the maximum value from the Maximum upload size dropdown<br>5. Click the Save and display button | Course settings are saved successfully with the maximum upload size set | Low |

---

### 7. Participants

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 7.7.PAR-001 | Enroll a new user using email address | None | 1. Click on the Enrol users button<br>2. Enter a valid email address in the email field<br>3. Select a role from the Roles dropdown<br>4. Click the Enrol button | User is successfully enrolled and appears in the Enrolled users dropdown | High |
| 7.7.PAR-002 | Edit an existing user's role | User is already enrolled in the course | 1. Locate the user in the Enrolled users dropdown<br>2. Click the Edit icon next to the user's name<br>3. Select a new role from the Roles dropdown<br>4. Click the Save button | User's role is updated and reflected in the Roles column | High |
| 7.7.PAR-003 | Remove an enrolled user | User is already enrolled in the course | 1. Locate the user in the Enrolled users dropdown<br>2. Click the Delete icon next to the user's name<br>3. Confirm the deletion | User is removed from the Enrolled users dropdown | High |
| 7.7.PAR-004 | Filter participants by name | None | 1. Select 'Name' from the Match filter system<br>2. Enter a valid name in the input field<br>3. Click the Apply filters button | Displays number of participants found matching the name | High |
| 7.7.PAR-005 | Filter participants by role | None | 1. Select 'Role' from the Match filter system<br>2. Choose a role from the Any dropdown<br>3. Click the Apply filters button | Displays number of participants found with the selected role | High |
| 7.7.PAR-006 | Filter participants by group | None | 1. Select 'Group' from the Match filter system<br>2. Choose a group from the Select dropdown<br>3. Click the Apply filters button | Displays number of participants found in the selected group | High |
| 7.7.PAR-007 | Bulk select participants using checkbox | Participants are listed on the page | 1. Click the checkbox for bulk selection<br>2. Verify all participants are selected | All participants are selected | High |
| 7.7.PAR-008 | Perform bulk action to edit roles on selected participants | Multiple participants are selected | 1. Click 'With selected users...' text<br>2. Select 'Edit roles' from the 'Choose...' dropdown<br>3. Confirm the action | Roles of selected participants are edited successfully | High |
| 7.7.PAR-009 | Perform bulk action to remove selected participants | Multiple participants are selected | 1. Click 'With selected users...' text<br>2. Select 'Remove participants' from the 'Choose...' dropdown<br>3. Confirm the action | Selected participants are removed successfully | High |
| 7.7.PAR-010 | Verify enrolled users dropdown displays correctly | None | 1. Observe the Enrolled users dropdown | Enrolled users dropdown displays all currently enrolled users | Medium |
| 7.7.PAR-011 | Verify role change is reflected in the Roles column | User's role has been edited | 1. Locate the user in the Enrolled users dropdown<br>2. Observe the Roles column | Roles column displays the updated role for the user | Medium |
| 7.7.PAR-012 | Clear filters using Clear filters button | Filters are applied | 1. Click the Clear filters button | All filters are cleared and the full list of participants is displayed | Medium |
| 7.7.PAR-013 | Add multiple filter conditions | None | 1. Select 'Name' from the Match filter system<br>2. Enter a valid name in the input field<br>3. Click the + Add condition link<br>4. Select 'Role' from the Match filter system<br>5. Choose a role from the Any dropdown<br>6. Click the Apply filters button | Displays number of participants found matching both conditions | Medium |
| 7.7.PAR-014 | Remove a filter condition using X button | Multiple filter conditions are applied | 1. Click the X button next to a filter condition | The selected filter condition is removed | Medium |
| 7.7.PAR-015 | Filter participants using alphabetical filter buttons | None | 1. Click on an alphabetical filter button corresponding to a letter<br>2. Click the Apply filters button | Displays number of participants whose names start with the selected letter | Medium |
| 7.7.PAR-016 | Verify 'With selected users...' text is displayed | Participants are listed on the page | 1. Verify the presence of 'With selected users...' text | 'With selected users...' text is displayed | Medium |
| 7.7.PAR-017 | Verify 'Choose...' dropdown is displayed | Participants are listed on the page | 1. Verify the presence of 'Choose...' dropdown | 'Choose...' dropdown is displayed | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 7.7.PAR-018 | Enroll user with empty email field | None | 1. Click on the Enrol users button<br>2. Leave the email field empty<br>3. Select a role from the Roles dropdown<br>4. Click the Enrol button | An error message is displayed indicating the email field is required | Medium |
| 7.7.PAR-019 | Enroll user with empty role selection | None | 1. Click on the Enrol users button<br>2. Enter a valid email address in the email field<br>3. Leave the role selection empty<br>4. Click the Enrol button | An error message is displayed indicating a role must be selected | Medium |
| 7.7.PAR-020 | Enroll user with invalid email format | None | 1. Click on the Enrol users button<br>2. Enter an invalid email format in the email field<br>3. Select a role from the Roles dropdown<br>4. Click the Enrol button | An error message is displayed indicating the email format is invalid | Medium |
| 7.7.PAR-021 | Filter participants with no criteria | None | 1. Click the Apply filters button without selecting any criteria | Displays the full list of participants | Medium |
| 7.7.PAR-022 | Filter participants with invalid name | None | 1. Select 'Name' from the Match filter system<br>2. Enter an invalid name in the input field<br>3. Click the Apply filters button | Displays zero participants found | Medium |
| 7.7.PAR-023 | Filter participants with invalid role | None | 1. Select 'Role' from the Match filter system<br>2. Enter an invalid role in the Any dropdown<br>3. Click the Apply filters button | Displays zero participants found | Medium |
| 7.7.PAR-024 | Filter participants with invalid group | None | 1. Select 'Group' from the Match filter system<br>2. Enter an invalid group in the Select dropdown<br>3. Click the Apply filters button | Displays zero participants found | Medium |
| 7.7.PAR-025 | Attempt to perform bulk action with no participants selected | No participants are selected | 1. Click 'With selected users...' text<br>2. Attempt to select an action from the 'Choose...' dropdown | No action is performed, and an error message is displayed | Medium |
| 7.7.PAR-026 | Attempt to perform bulk action with invalid action selected | Multiple participants are selected | 1. Click 'With selected users...' text<br>2. Select an invalid action from the 'Choose...' dropdown<br>3. Confirm the action | No action is performed, and an error message is displayed | Medium |

---

### 9. Assignment Submissions (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 9.9AS(O-002 | Search users using a valid username | None | 1. Enter a valid username in the Search users field<br>2. Press Enter or click the search icon | Submissions table is filtered to show only the entries related to the searched username | High |
| 9.9AS(O-003 | Search users using a valid email | None | 1. Enter a valid email in the Search users field<br>2. Press Enter or click the search icon | Submissions table is filtered to show only the entries related to the searched email | High |
| 9.9AS(O-004 | Grade a student submission | A student submission is available | 1. Click the Grade button for a specific student submission<br>2. Enter a grade in the grade input field<br>3. Save the grade | The grade is saved and displayed correctly in the Submissions tab | High |
| 9.9AS(O-005 | Verify submission status update after grading | A student submission is graded | 1. Check the Status column for the graded submission | Status is updated to reflect the grading | High |
| 9.9AS(O-007 | Filter submissions by a specific name | None | 1. Select a specific name from the Filter by name dropdown | Submissions table is filtered to show only the entries related to the selected name | Medium |
| 9.9AS(O-008 | Filter submissions by status | None | 1. Select a specific status from the Status filter | Submissions table is filtered to show only the entries with the selected status | Medium |
| 9.9AS(O-009 | Use advanced filter options | None | 1. Click on the Advanced dropdown<br>2. Select various filter options | Submissions table is filtered according to the selected advanced options | Medium |
| 9.9AS(O-010 | Perform an action from the Actions dropdown | None | 1. Select an action from the Actions dropdown<br>2. Confirm the action | The selected action is performed successfully | Medium |
| 9.9AS(O-011 | Access student details via First name / Last name link | None | 1. Click on the First name / Last name link for a specific submission | Student details page is displayed | Medium |
| 9.9AS(O-012 | Verify feedback comments are saved | A student submission is available | 1. Enter feedback comments for a submission<br>2. Save the feedback | Feedback comments are saved and displayed correctly | Medium |
| 9.9AS(O-013 | Verify feedback files are uploaded | A student submission is available | 1. Upload feedback files for a submission<br>2. Save the feedback | Feedback files are uploaded and displayed correctly | Medium |
| 9.9AS(O-014 | Toggle Quick grading option | None | 1. Check the Quick grading checkbox<br>2. Verify the interface changes to allow quick grading | Quick grading interface is enabled | Low |
| 9.9AS(O-015 | Select a submission using the Select checkbox | None | 1. Click the Select checkbox for a specific submission | The submission is selected | Low |
| 9.9AS(O-001 | Verify all elements are displayed on the Submissions tab | None | 1. Check the presence of the Search users field<br>2. Check the presence of the Filter by name dropdown<br>3. Check the presence of the Status filter<br>4. Check the presence of the Advanced dropdown<br>5. Check the presence of the Grade button<br>6. Check the presence of the Quick grading checkbox<br>7. Check the presence of the Actions dropdown<br>8. Check the presence of the Select checkbox<br>9. Check the presence of the First name / Last name link<br>10. Check the presence of the Email address<br>11. Check the presence of the Status<br>12. Check the presence of the Grade<br>13. Check the presence of the Last modified (submission)<br>14. Check the presence of the Online text<br>15. Check the presence of the File submissions<br>16. Check the presence of the Submission comments<br>17. Check the presence of the Last modified (grade)<br>18. Check the presence of the Feedback comments<br>19. Check the presence of the Feedback files<br>20. Check the presence of the Final grade<br>21. Check the presence of the Three-dot menus | All elements are displayed correctly on the Submissions tab | High |
| 9.9AS(O-006 | Verify final grade is displayed correctly | A student submission is graded | 1. Check the Final grade column for the graded submission | Final grade is displayed correctly | High |

---

### 10. Assignment (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 10.1A(V-001 | Submit assignment with online text | Assignment is available for submission | 1. Click on the 'Add submission' button<br>2. Enter valid text in the 'Online text' field<br>3. Click the 'Submit' button | Submission status updates to 'Submitted for grading' | High |
| 10.1A(V-002 | Submit assignment with file upload | Assignment is available for submission | 1. Click on the 'Add submission' button<br>2. Upload a valid file in the 'Upload files' section<br>3. Click the 'Submit' button | Submission status updates to 'Submitted for grading' | High |
| 10.1A(V-003 | Verify submission status updates after submission | Assignment has been submitted | 1. View the submission status | Submission status is 'Submitted for grading' | High |
| 10.1A(V-005 | Edit submission after initial submission | Assignment has been submitted | 1. Click on 'Edit submission'<br>2. Make changes to the submission<br>3. Click the 'Submit' button | Submission status remains 'Submitted for grading' with updated content | Medium |
| 10.1A(V-006 | Remove submission after initial submission | Assignment has been submitted | 1. Click on 'Remove submission'<br>2. Confirm the removal | Submission status updates to 'Not submitted' | Medium |
| 10.1A(V-004 | Verify grade and feedback appear after grading | Assignment has been graded | 1. View the grade<br>2. View the feedback | Grade and feedback are displayed | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 10.1A(V-007 | Submit assignment with empty online text | Assignment is available for submission | 1. Click on the 'Add submission' button<br>2. Leave the 'Online text' field empty<br>3. Click the 'Submit' button | Submission is not accepted and an error message is displayed | Medium |
| 10.1A(V-008 | Submit assignment with no file uploaded | Assignment is available for submission | 1. Click on the 'Add submission' button<br>2. Do not upload any file in the 'Upload files' section<br>3. Click the 'Submit' button | Submission is not accepted and an error message is displayed | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 10.1A(V-009 | Submit assignment with maximum length online text | Assignment is available for submission | 1. Click on the 'Add submission' button<br>2. Enter maximum allowed characters in the 'Online text' field<br>3. Click the 'Submit' button | Submission status updates to 'Submitted for grading' | Low |

---

### 11. Advanced Grading (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 11.1AG(O-001 | Verify dropdown default selection is 'Rubric' | None | 1. Locate the 'Change active grading method to' dropdown<br>2. Check the default selected option | The default selected option is 'Rubric' | High |
| 11.1AG(O-002 | Create new grading form from scratch | None | 1. Click on 'Define new grading form from scratch' card option<br>2. Fill out the necessary fields to create a grading form<br>3. Submit the form | A new grading form is created successfully | High |
| 11.1AG(O-003 | Create new grading form from a template | None | 1. Click on 'Create new grading form from a template' card option<br>2. Select a template from the available options<br>3. Submit the form | A new grading form is created from the selected template successfully | High |
| 11.1AG(O-004 | Verify 'Define new grading form from scratch' option is available | None | 1. Locate the 'Define new grading form from scratch' card option | 'Define new grading form from scratch' option is visible and selectable | Medium |
| 11.1AG(O-005 | Verify 'Create new grading form from a template' option is available | None | 1. Locate the 'Create new grading form from a template' card option | 'Create new grading form from a template' option is visible and selectable | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 11.1AG(O-006 | Verify simple grading method is used when form is invalid | An invalid grading form exists | 1. Attempt to use the grading form with invalid status | The simple grading method is used instead of the invalid form | Medium |
| 11.1AG(O-007 | Verify error message when grading form status is invalid | An invalid grading form exists | 1. Attempt to use the grading form with invalid status | An error message indicating the grading form status is invalid is displayed | Medium |

---

### 12. Gradebook / Grader Report (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 12.1G/GR(-001 | Save changes with valid data in all columns | Grader report is in edit mode | 1. Enter valid data in BUS301 - Case Study Analysis column<br>2. Enter valid data in BUS301 - Business Plan Draft column<br>3. Enter valid data in BUS301 - Final Presentation column<br>4. Enter valid data in r column<br>5. Enter valid data in Course total column<br>6. Click on Save changes button | Changes are saved successfully and reflected in the Gradebook | High |
| 12.1G/GR(-002 | Verify changes are reflected in the Overall average row | Changes have been saved successfully | 1. Observe the Overall average row after saving changes | Overall average row is updated to reflect the changes made | High |
| 12.1G/GR(-008 | Verify Grader report dropdown is functional | None | 1. Click on Grader report dropdown<br>2. Select an option from the dropdown | Selected option is displayed and applied in the Grader report | Low |
| 12.1G/GR(-009 | Verify Search users field is functional | None | 1. Enter a valid user name in the Search users field<br>2. Press Enter or click on the search icon | Search results display the user matching the entered name | Low |
| 12.1G/GR(-010 | Verify Filter by name dropdown is functional | None | 1. Click on Filter by name dropdown<br>2. Select a name from the dropdown | Grader report is filtered to show only the selected name | Low |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 12.1G/GR(-003 | Save changes with empty BUS301 - Case Study Analysis column | Grader report is in edit mode | 1. Leave BUS301 - Case Study Analysis column empty<br>2. Enter valid data in other columns<br>3. Click on Save changes button | Error message displayed indicating BUS301 - Case Study Analysis column cannot be empty | Medium |
| 12.1G/GR(-004 | Save changes with empty BUS301 - Business Plan Draft column | Grader report is in edit mode | 1. Leave BUS301 - Business Plan Draft column empty<br>2. Enter valid data in other columns<br>3. Click on Save changes button | Error message displayed indicating BUS301 - Business Plan Draft column cannot be empty | Medium |
| 12.1G/GR(-005 | Save changes with empty BUS301 - Final Presentation column | Grader report is in edit mode | 1. Leave BUS301 - Final Presentation column empty<br>2. Enter valid data in other columns<br>3. Click on Save changes button | Error message displayed indicating BUS301 - Final Presentation column cannot be empty | Medium |
| 12.1G/GR(-006 | Save changes with empty r column | Grader report is in edit mode | 1. Leave r column empty<br>2. Enter valid data in other columns<br>3. Click on Save changes button | Error message displayed indicating r column cannot be empty | Medium |
| 12.1G/GR(-007 | Save changes with empty Course total column | Grader report is in edit mode | 1. Leave Course total column empty<br>2. Enter valid data in other columns<br>3. Click on Save changes button | Error message displayed indicating Course total column cannot be empty | Medium |

---

### 13. Grades / User Report (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 13.1G/UR(-002 | Verify '(Empty)' is displayed for unsubmitted assignments | Student is logged in and on the Grades page | 1. Locate the Calculated weight column<br>2. Identify any assignments that have not been submitted or graded | The Calculated weight column shows '(Empty)' for unsubmitted or ungraded assignments | High |
| 13.1G/UR(-003 | Verify grade items display correct information | Student is logged in and on the Grades page | 1. Locate each Grade item<br>2. Verify that each Grade item displays Grade, Range, Percentage, Feedback, and Contribution to course total | Each Grade item displays all required information correctly | High |
| 13.1G/UR(-001 | Verify student's own grades are displayed | Student is logged in and on the Grades page | 1. Locate the Grades tab<br>2. Verify the presence of the User report dropdown<br>3. Check that the grades displayed belong to the logged-in student | The grades displayed are only for the logged-in student | High |
| 13.1G/UR(-004 | Verify User report dropdown is present | Student is logged in and on the Grades page | 1. Locate the User report dropdown at the top of the page | User report dropdown is visible and accessible | Medium |
| 13.1G/UR(-005 | Verify AGGREGATION Course total row is displayed | Student is logged in and on the Grades page | 1. Scroll to the bottom of the grades list<br>2. Locate the AGGREGATION Course total row | The AGGREGATION Course total row is visible at the bottom of the grades list | Medium |

---

### 14. Activities (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 14.1A(V-001 | Verify Activities page heading displays correctly | None | 1. Check the page heading at the top of the Activities page | The page heading displays as 'Activities' | High |
| 14.1A(V-005 | Verify each activity displays a name | None | 1. Check each activity in the Assignments, Forums, and Resources sections for a name | Each activity displays a name | High |
| 14.1A(V-006 | Verify each activity displays a due date | None | 1. Check each activity in the Assignments section for a due date | Each activity displays a due date | Medium |
| 14.1A(V-007 | Verify each activity displays a submission status | None | 1. Check each activity in the Assignments section for a submission status | Each activity displays a submission status | Medium |
| 14.1A(V-002 | Verify Assignments section is present on the Activities page | None | 1. Locate the Assignments section on the Activities page | Assignments section is present | High |
| 14.1A(V-003 | Verify Forums section is present on the Activities page | None | 1. Locate the Forums section on the Activities page | Forums section is present | High |
| 14.1A(V-004 | Verify Resources section is present on the Activities page | None | 1. Locate the Resources section on the Activities page | Resources section is present | High |
| 14.1A(V-008 | Verify arrow icon is present for each activity | None | 1. Check each activity for the presence of an arrow icon | Arrow icon is present for each activity | Low |

---

### 15. Profile

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.15.PRO-001 | Update profile with all valid inputs | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Select a valid email visibility option<br>5. Enter a valid MoodleNet profile ID<br>6. Enter a valid city/town<br>7. Select a valid country<br>8. Select a valid timezone<br>9. Enter a valid description in the rich text editor<br>10. Upload a valid image file<br>11. Enter a valid picture description<br>12. Click the Update profile button | Profile is updated successfully with the new information | High |
| 15.15.PRO-002 | Verify profile fields are displayed correctly | User is logged in and on the profile update page | 1. Verify the first name field is displayed<br>2. Verify the last name field is displayed<br>3. Verify the email address field is displayed<br>4. Verify the email visibility dropdown is displayed<br>5. Verify the MoodleNet profile ID field is displayed<br>6. Verify the city/town field is displayed<br>7. Verify the country dropdown is displayed<br>8. Verify the timezone dropdown is displayed<br>9. Verify the description rich text editor is displayed<br>10. Verify the current picture is displayed<br>11. Verify the new picture upload area is displayed<br>12. Verify the picture description field is displayed | All profile fields are displayed correctly | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.15.PRO-003 | First name field empty | User is logged in and on the profile update page | 1. Leave the first name field empty<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Click the Update profile button | An error message is displayed indicating the first name is required | Medium |
| 15.15.PRO-004 | Last name field empty | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Leave the last name field empty<br>3. Enter valid email address<br>4. Click the Update profile button | An error message is displayed indicating the last name is required | Medium |
| 15.15.PRO-005 | Email address field empty | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Leave the email address field empty<br>4. Click the Update profile button | An error message is displayed indicating the email address is required | Medium |
| 15.15.PRO-006 | Upload image file exceeding maximum size | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Upload an image file exceeding 100 MB<br>5. Click the Update profile button | An error message is displayed indicating the file size exceeds the maximum limit | Medium |
| 15.15.PRO-007 | Upload more than one image file | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Upload more than one image file<br>5. Click the Update profile button | An error message is displayed indicating only one file can be uploaded | Medium |
| 15.15.PRO-008 | Upload image file with invalid type | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Upload an image file with an unsupported format<br>5. Click the Update profile button | An error message is displayed indicating the file type is not supported | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.15.PRO-009 | Update profile with maximum length description | User is logged in and on the profile update page | 1. Enter valid first name<br>2. Enter valid last name<br>3. Enter valid email address<br>4. Enter maximum length text in the description rich text editor<br>5. Click the Update profile button | Profile is updated successfully with the maximum length description | Low |

---

### 8. Assignment (Teacher View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 8.8A(V-001 | Verify Grade button is present | None | 1. Check if the Grade button is visible on the page | Grade button is visible | High |
| 8.8A(V-002 | Verify Grading summary section is displayed | None | 1. Check if the Grading summary section is visible on the page | Grading summary section is visible | High |
| 8.8A(V-003 | Verify Participants count is displayed | None | 1. Check if the Participants count is displayed in the Grading summary section | Participants count is displayed | Medium |
| 8.8A(V-004 | Verify Submitted count is displayed | None | 1. Check if the Submitted count is displayed in the Grading summary section | Submitted count is displayed | Medium |
| 8.8A(V-005 | Verify Needs grading count is displayed | None | 1. Check if the Needs grading count is displayed in the Grading summary section | Needs grading count is displayed | Medium |
| 8.8A(V-006 | Verify Time remaining until due date is displayed | None | 1. Check if the Time remaining until due date is displayed | Time remaining until due date is displayed | Medium |
| 8.8A(V-007 | Verify Assignment description text is displayed | None | 1. Check if the Assignment description text is visible on the page | Assignment description text is visible | Medium |
| 8.8A(V-008 | Verify Assignment icon is displayed | None | 1. Check if the Assignment icon is visible on the page | Assignment icon is visible | Low |
| 8.8A(V-009 | Verify Assignment name is displayed | None | 1. Check if the Assignment name is visible on the page | Assignment name is visible | Low |
| 8.8A(V-010 | Verify Breadcrumbs are displayed | None | 1. Check if the Breadcrumbs are visible on the page | Breadcrumbs are visible | Low |
| 8.8A(V-011 | Verify Hidden from students indicator is displayed | None | 1. Check if the Hidden from students indicator is visible on the page | Hidden from students indicator is visible | Low |

---

## Post-Verification Details

This section shows verification requirements for tests that modify application state.
Tests using the **before/after** strategy require running a verification test BEFORE
and AFTER the action to compare values.

### 5.5AA(O-004: Add selected activity to course

**Coverage:** NONE None
**Modifies State:** course_content_modification

**1. Verify the new activity or resource appears in the course content**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on verifying the presence of navigation tabs and do not check the course content for new activities or resources.
- **Manual Step:** Manually navigate to the course page and check the course sections to confirm the new activity or resource is listed.

**2. Verify the new activity appears in the student's activities overview**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Session Switch Required:** Login as a student enrolled in the course
- **Reason:** None of the test cases confirm the presence of a new activity in the student's activities overview.
- **Manual Step:** Manually check the student's activities overview to confirm the new activity is listed.

**Coverage Gaps:**
- All candidate test cases focus on verifying the presence of navigation tabs and do not check the course content for new activities or resources.
- None of the test cases confirm the presence of a new activity in the student's activities overview.

#### Execution Plan

**1. [ACTION] 5.5AA(O-004** -- Add selected activity to course
   > Run 5.5AA(O-004 — this is the state-changing action being verified

**Notes:** Execute 5.5AA(O-004 → Manual verification needed for 2 item(s)

**Manual Verification Required:**
- Verify the new activity or resource appears in the course content
  - Suggested: Manually navigate to the course page and check the course sections to confirm the new activity or resource is listed.
- Verify the new activity appears in the student's activities overview
  - Suggested: Manually check the student's activities overview to confirm the new activity is listed.

---

### 5.5AA(O-005: Create new assignment with all required fields

**Coverage:** NONE None
**Modifies State:** course_content_modification

**1. Verify the new assignment appears in the course content**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or display the course content to verify the presence of a new assignment.
- **Manual Step:** Manually navigate to the Course Page and check the course sections for the new assignment to confirm it is listed in the course content.

**2. Verify the new assignment appears in the student's activities overview**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Session Switch Required:** Login as a student enrolled in the course
- **Reason:** None of the test cases confirm the presence of a new assignment in the activities overview. They focus on due dates, submission statuses, and icons, which are not relevant to confirming the listing of a new assignment.
- **Manual Step:** Manually log in as a student, navigate to the Activities section, and verify the new assignment is listed in the activities overview.

**Coverage Gaps:**
- None of the test cases access or display the course content to verify the presence of a new assignment.
- None of the test cases confirm the presence of a new assignment in the activities overview. They focus on due dates, submission statuses, and icons, which are not relevant to confirming the listing of a new assignment.

#### Execution Plan

**1. [ACTION] 5.5AA(O-005** -- Create new assignment with all required fields
   > Run 5.5AA(O-005 — this is the state-changing action being verified

**Notes:** Execute 5.5AA(O-005 → Manual verification needed for 2 item(s)

**Manual Verification Required:**
- Verify the new assignment appears in the course content
  - Suggested: Manually navigate to the Course Page and check the course sections for the new assignment to confirm it is listed in the course content.
- Verify the new assignment appears in the student's activities overview
  - Suggested: Manually log in as a student, navigate to the Activities section, and verify the new assignment is listed in the activities overview.

---

### 5.5AA(O-006: Create new assignment with 'Save and display'

**Coverage:** NONE None
**Modifies State:** course_content_modification

**1. Verify the new assignment page is displayed with correct details**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases are related to displaying elements like the Course Index, navigation bar, or activity icons, none of which confirm the assignment page details.
- **Manual Step:** Manually navigate to the new assignment page and verify that the assignment details are displayed correctly.

**Coverage Gaps:**
- All candidate test cases are related to displaying elements like the Course Index, navigation bar, or activity icons, none of which confirm the assignment page details.

#### Execution Plan

**1. [ACTION] 5.5AA(O-006** -- Create new assignment with 'Save and display'
   > Run 5.5AA(O-006 — this is the state-changing action being verified

**Notes:** Execute 5.5AA(O-006 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the new assignment page is displayed with correct details
  - Suggested: Manually navigate to the new assignment page and verify that the assignment details are displayed correctly.

---

### 6.6CS(O-001: Save course settings with all required fields filled

**Coverage:** PARTIAL Partial
**Modifies State:** settings_config

**1. Verify the course settings are saved and displayed correctly**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 6.6CS(O-008 (Maximum upload size dropdown boundary test)
- **Confidence:** 50%
- **Execution Note:** This test can verify that the course settings are saved successfully, but it only confirms the maximum upload size setting.
- **Reason:** The test operates on the correct module and confirms that a specific setting (maximum upload size) is saved successfully. However, it does not verify all course settings.
- **Manual Step:** Manually verify that all course settings, not just the maximum upload size, reflect the saved changes on the course settings page.

**Coverage Gaps:**
- The test operates on the correct module and confirms that a specific setting (maximum upload size) is saved successfully. However, it does not verify all course settings.

#### Execution Plan

**1. [ACTION] 6.6CS(O-001** -- Save course settings with all required fields filled
   > Run 6.6CS(O-001 — this is the state-changing action being verified

**2. [POST-VERIFY] 6.6CS(O-008** -- Maximum upload size dropdown boundary test
   > This test can verify that the course settings are saved successfully, but it only confirms the maximum upload size setting.
   > Limitation: The test operates on the correct module and confirms that a specific setting (maximum upload size) is saved successfully. However, it does not verify all course settings.

**Notes:** Execute 6.6CS(O-001 → then verify with 6.6CS(O-008

---

### 7.7.PAR-001: Enroll a new user using email address

**Coverage:** FULL Full
**Modifies State:** enrollment_management

**1. Verify the new user appears in the enrolled users list**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 7.7.PAR-010 (Verify enrolled users dropdown displays correctly)
- **Confidence:** 90%
- **Execution Note:** This test can be used to verify if the new user appears in the enrolled users dropdown, confirming the expected outcome.

#### Execution Plan

**1. [ACTION] 7.7.PAR-001** -- Enroll a new user using email address
   > Run 7.7.PAR-001 — this is the state-changing action being verified

**2. [POST-VERIFY] 7.7.PAR-010** -- Verify enrolled users dropdown displays correctly
   > This test can be used to verify if the new user appears in the enrolled users dropdown, confirming the expected outcome.

**Notes:** Execute 7.7.PAR-001 → then verify with 7.7.PAR-010

---

### 7.7.PAR-002: Edit an existing user's role

**Coverage:** FULL Full
**Modifies State:** enrollment_management

**1. Verify the user's role is updated in the enrolled users list**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 7.7.PAR-011 (Verify role change is reflected in the Roles column)
- **Confidence:** 90%
- **Before Action:** Record the user's current role before the action
- **After Action:** Confirm the user's role is updated to the new role
- **Execution Note:** Use this test to observe the Roles column for the user in the Enrolled users list before and after the action.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 7.7.PAR-011** -- Verify role change is reflected in the Roles column
   > Run 7.7.PAR-011 and RECORD the current values before the action

**2. [ACTION] 7.7.PAR-002** -- Edit an existing user's role
   > Run 7.7.PAR-002 — this is the state-changing action being verified

**3. [POST-VERIFY] 7.7.PAR-011** -- Verify role change is reflected in the Roles column
   > Run 7.7.PAR-011 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 7.7.PAR-011 → ACTION: Execute 7.7.PAR-002 → POST: Verify with 7.7.PAR-011 (compare against baseline)

---

### 7.7.PAR-003: Remove an enrolled user

**Coverage:** FULL Full
**Modifies State:** enrollment_management

**1. Verify the user is removed from the enrolled users list**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 7.7.PAR-011 (Verify role change is reflected in the Roles column)
- **Confidence:** 90%
- **Before Action:** Record the presence of the user in the list before the action
- **After Action:** Confirm the user is no longer present in the list
- **Execution Note:** Use this test to observe the enrolled users list and check the Roles column for the presence of the user before and after the action.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 7.7.PAR-011** -- Verify role change is reflected in the Roles column
   > Run 7.7.PAR-011 and RECORD the current values before the action

**2. [ACTION] 7.7.PAR-003** -- Remove an enrolled user
   > Run 7.7.PAR-003 — this is the state-changing action being verified

**3. [POST-VERIFY] 7.7.PAR-011** -- Verify role change is reflected in the Roles column
   > Run 7.7.PAR-011 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 7.7.PAR-011 → ACTION: Execute 7.7.PAR-003 → POST: Verify with 7.7.PAR-011 (compare against baseline)

---

### 7.7.PAR-008: Perform bulk action to edit roles on selected participants

**Coverage:** NONE None
**Modifies State:** enrollment_management

**1. Verify the roles of selected participants are updated**

- **Status:** MISSING not_found
- **Strategy:** Before/After
- **Matched Test:** -
- **Confidence:** -
- **Before Action:** Record the roles of selected participants before the action
- **After Action:** Confirm the roles are updated to the new roles
- **Reason:** None of the test cases access or display the roles of participants in the enrollment list.
- **Manual Step:** Manually verify the roles of selected participants in the enrollment list before and after the update action.

**Coverage Gaps:**
- None of the test cases access or display the roles of participants in the enrollment list.

#### Execution Plan

**1. [ACTION] 7.7.PAR-008** -- Perform bulk action to edit roles on selected participants
   > Run 7.7.PAR-008 — this is the state-changing action being verified

**Notes:** Execute 7.7.PAR-008 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the roles of selected participants are updated
  - Suggested: Manually verify the roles of selected participants in the enrollment list before and after the update action.

---

### 7.7.PAR-009: Perform bulk action to remove selected participants

**Coverage:** FULL Full
**Modifies State:** enrollment_management

**1. Verify the selected participants are removed from the enrolled users list**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 7.7.PAR-003 (Remove an enrolled user)
- **Confidence:** 100%
- **Before Action:** Record the presence of selected participants in the list before the action
- **After Action:** Confirm the selected participants are no longer present in the list
- **Execution Note:** Use this test to observe the enrolled users list before and after the action to verify the removal of selected participants.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 7.7.PAR-003** -- Remove an enrolled user
   > Run 7.7.PAR-003 and RECORD the current values before the action

**2. [ACTION] 7.7.PAR-009** -- Perform bulk action to remove selected participants
   > Run 7.7.PAR-009 — this is the state-changing action being verified

**3. [POST-VERIFY] 7.7.PAR-003** -- Remove an enrolled user
   > Run 7.7.PAR-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 7.7.PAR-003 → ACTION: Execute 7.7.PAR-009 → POST: Verify with 7.7.PAR-003 (compare against baseline)

---

### 9.9AS(O-004: Grade a student submission

**Coverage:** PARTIAL Partial
**Modifies State:** grading_actions

**1. Verify the grade is saved and displayed correctly in the submissions tab**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 9.9AS(O-006 (Verify final grade is displayed correctly)
- **Confidence:** 90%
- **Execution Note:** This test can be used to verify that the final grade is displayed correctly in the submissions tab after the grade is saved.

**2. Verify the grade appears in the student's grade report**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 13.1G/UR(-001 (Verify student's own grades are displayed)
- **Confidence:** 60%
- **Session Switch Required:** Login as the student who received the grade
- **Execution Note:** This test can verify that grades displayed belong to the logged-in student, but does not specifically confirm the presence of a new grade.
- **Reason:** The test operates on the correct module and confirms grades are displayed for the logged-in student, but it does not specifically confirm the presence of a new grade.
- **Manual Step:** After executing the test, manually verify that the specific new grade is present in the student's grade report.

**3. Verify the grade appears in the teacher's gradebook**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or display the specific data needed to confirm the new grade entry in the gradebook.
- **Manual Step:** Manually check the gradebook to confirm the new grade entry is present and correctly displayed.

**Coverage Gaps:**
- The test operates on the correct module and confirms grades are displayed for the logged-in student, but it does not specifically confirm the presence of a new grade.
- None of the test cases access or display the specific data needed to confirm the new grade entry in the gradebook.

#### Execution Plan

**1. [ACTION] 9.9AS(O-004** -- Grade a student submission
   > Run 9.9AS(O-004 — this is the state-changing action being verified

**2. [POST-VERIFY] 9.9AS(O-006** -- Verify final grade is displayed correctly
   > This test can be used to verify that the final grade is displayed correctly in the submissions tab after the grade is saved.

**3. [NAVIGATE]** Navigate to 13. Grades / User Report (Student View)
   > Navigate from 9. Assignment Submissions (Teacher Only) to 13. Grades / User Report (Student View)

**4. [SESSION]** Switch user session for verification
   > Login as the student who received the grade

**5. [POST-VERIFY] 13.1G/UR(-001** -- Verify student's own grades are displayed
   > This test can verify that grades displayed belong to the logged-in student, but does not specifically confirm the presence of a new grade.
   > Limitation: The test operates on the correct module and confirms grades are displayed for the logged-in student, but it does not specifically confirm the presence of a new grade.

**Notes:** Execute 9.9AS(O-004 → then verify with 9.9AS(O-006, 13.1G/UR(-001 → (requires user session switch) → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the grade appears in the teacher's gradebook
  - Suggested: Manually check the gradebook to confirm the new grade entry is present and correctly displayed.

---

### 9.9AS(O-005: Verify submission status update after grading

**Coverage:** FULL Full
**Modifies State:** grading_actions

**1. Verify the submission status is updated to reflect the grading**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 9.9AS(O-006 (Verify final grade is displayed correctly)
- **Confidence:** 80%
- **Before Action:** Record the current status of the submission before grading
- **After Action:** Confirm the status has changed to reflect the grading
- **Execution Note:** Use this test to observe the submission status before and after grading. The test already accesses the relevant module and displays grading-related data.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 9.9AS(O-006** -- Verify final grade is displayed correctly
   > Run 9.9AS(O-006 and RECORD the current values before the action

**2. [ACTION] 9.9AS(O-005** -- Verify submission status update after grading
   > Run 9.9AS(O-005 — this is the state-changing action being verified

**3. [POST-VERIFY] 9.9AS(O-006** -- Verify final grade is displayed correctly
   > Run 9.9AS(O-006 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 9.9AS(O-006 → ACTION: Execute 9.9AS(O-005 → POST: Verify with 9.9AS(O-006 (compare against baseline)

---

### 9.9AS(O-012: Verify feedback comments are saved

**Coverage:** NONE None
**Modifies State:** grading_actions

**1. Verify feedback comments are saved and displayed correctly**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or confirm the display of feedback comments specifically. They focus on feedback files, grades, and final grades, which are different data points.
- **Manual Step:** Develop a new test case that enters feedback comments for a submission and verifies that these comments are displayed correctly in the grading_actions state.

**Coverage Gaps:**
- None of the test cases access or confirm the display of feedback comments specifically. They focus on feedback files, grades, and final grades, which are different data points.

#### Execution Plan

**1. [ACTION] 9.9AS(O-012** -- Verify feedback comments are saved
   > Run 9.9AS(O-012 — this is the state-changing action being verified

**Notes:** Execute 9.9AS(O-012 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify feedback comments are saved and displayed correctly
  - Suggested: Develop a new test case that enters feedback comments for a submission and verifies that these comments are displayed correctly in the grading_actions state.

---

### 9.9AS(O-013: Verify feedback files are uploaded

**Coverage:** NONE None
**Modifies State:** grading_actions

**1. Verify feedback files are uploaded and displayed correctly**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases specifically address the verification of feedback files being uploaded and displayed correctly. They focus on feedback comments and grades, not files.
- **Manual Step:** Manually upload feedback files and check the display of these files in the grading_actions section of the Assignment Submissions module.

**Coverage Gaps:**
- None of the test cases specifically address the verification of feedback files being uploaded and displayed correctly. They focus on feedback comments and grades, not files.

#### Execution Plan

**1. [ACTION] 9.9AS(O-013** -- Verify feedback files are uploaded
   > Run 9.9AS(O-013 — this is the state-changing action being verified

**Notes:** Execute 9.9AS(O-013 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify feedback files are uploaded and displayed correctly
  - Suggested: Manually upload feedback files and check the display of these files in the grading_actions section of the Assignment Submissions module.

---

### 10.1A(V-001: Submit assignment with online text

**Coverage:** FULL Full
**Modifies State:** submission_status

**1. Verify the submission status updates to 'Submitted for grading'**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 10.1A(V-003 (Verify submission status updates after submission)
- **Confidence:** 90%
- **Execution Note:** This test can be used to verify the submission status updates to 'Submitted for grading' after the assignment submission.

#### Execution Plan

**1. [ACTION] 10.1A(V-001** -- Submit assignment with online text
   > Run 10.1A(V-001 — this is the state-changing action being verified

**2. [POST-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > This test can be used to verify the submission status updates to 'Submitted for grading' after the assignment submission.

**Notes:** Execute 10.1A(V-001 → then verify with 10.1A(V-003

---

### 10.1A(V-002: Submit assignment with file upload

**Coverage:** FULL Full
**Modifies State:** submission_status

**1. Verify the submission status updates to 'Submitted for grading'**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 10.1A(V-003 (Verify submission status updates after submission)
- **Confidence:** 90%
- **Execution Note:** This test can be used to verify that the submission status updates to 'Submitted for grading' after the assignment is submitted.

#### Execution Plan

**1. [ACTION] 10.1A(V-002** -- Submit assignment with file upload
   > Run 10.1A(V-002 — this is the state-changing action being verified

**2. [POST-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > This test can be used to verify that the submission status updates to 'Submitted for grading' after the assignment is submitted.

**Notes:** Execute 10.1A(V-002 → then verify with 10.1A(V-003

---

### 10.1A(V-003: Verify submission status updates after submission

**Coverage:** FULL Full
**Modifies State:** submission_status

**1. Verify the submission status is 'Submitted for grading'**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 10.1A(V-001 (Submit assignment with online text)
- **Confidence:** 100%
- **Execution Note:** This test case can be used to verify the submission status is 'Submitted for grading' after the assignment is submitted.

#### Execution Plan

**1. [ACTION] 10.1A(V-003** -- Verify submission status updates after submission
   > Run 10.1A(V-003 — this is the state-changing action being verified

**2. [POST-VERIFY] 10.1A(V-001** -- Submit assignment with online text
   > This test case can be used to verify the submission status is 'Submitted for grading' after the assignment is submitted.

**Notes:** Execute 10.1A(V-003 → then verify with 10.1A(V-001

---

### 10.1A(V-005: Edit submission after initial submission

**Coverage:** FULL Full
**Modifies State:** submission_status

**1. Verify the submission status remains 'Submitted for grading' with updated content**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 10.1A(V-003 (Verify submission status updates after submission)
- **Confidence:** 90%
- **Before Action:** Record the submission content before editing
- **After Action:** Confirm the content is updated and status remains 'Submitted for grading'
- **Execution Note:** Use this test to view the submission status before and after editing the assignment to ensure it remains 'Submitted for grading'.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > Run 10.1A(V-003 and RECORD the current values before the action

**2. [ACTION] 10.1A(V-005** -- Edit submission after initial submission
   > Run 10.1A(V-005 — this is the state-changing action being verified

**3. [POST-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > Run 10.1A(V-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 10.1A(V-003 → ACTION: Execute 10.1A(V-005 → POST: Verify with 10.1A(V-003 (compare against baseline)

---

### 10.1A(V-006: Remove submission after initial submission

**Coverage:** FULL Full
**Modifies State:** submission_status

**1. Verify the submission status updates to 'Not submitted'**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 10.1A(V-003 (Verify submission status updates after submission)
- **Confidence:** 90%
- **Before Action:** Record the submission status before removal
- **After Action:** Confirm the status updates to 'Not submitted'
- **Execution Note:** This test can be used to observe the submission status before and after the removal action.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > Run 10.1A(V-003 and RECORD the current values before the action

**2. [ACTION] 10.1A(V-006** -- Remove submission after initial submission
   > Run 10.1A(V-006 — this is the state-changing action being verified

**3. [POST-VERIFY] 10.1A(V-003** -- Verify submission status updates after submission
   > Run 10.1A(V-003 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 10.1A(V-003 → ACTION: Execute 10.1A(V-006 → POST: Verify with 10.1A(V-003 (compare against baseline)

---

### 11.1AG(O-002: Create new grading form from scratch

**Coverage:** NONE None
**Modifies State:** grading_method_creation

**1. Verify a new grading form is created successfully**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases confirm the creation of a new grading form from scratch. They either focus on creating from a template or verifying the availability of options.
- **Manual Step:** After creating a new grading form from scratch, manually verify that the form appears in the list of available grading forms.

**Coverage Gaps:**
- None of the test cases confirm the creation of a new grading form from scratch. They either focus on creating from a template or verifying the availability of options.

#### Execution Plan

**1. [ACTION] 11.1AG(O-002** -- Create new grading form from scratch
   > Run 11.1AG(O-002 — this is the state-changing action being verified

**Notes:** Execute 11.1AG(O-002 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify a new grading form is created successfully
  - Suggested: After creating a new grading form from scratch, manually verify that the form appears in the list of available grading forms.

---

### 11.1AG(O-003: Create new grading form from a template

**Coverage:** NONE None
**Modifies State:** grading_method_creation

**1. Verify a new grading form is created from the selected template successfully**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** The available test cases do not confirm the expected outcome of a new grading form being created from a template. Test ID 11.1AG(O-002 is for creating a form from scratch, and Test ID 11.1AG(O-005 only verifies the availability of the option to create from a template, not the creation itself.
- **Manual Step:** Manually verify that a new grading form is created from the selected template by checking the list of grading forms after the creation action.

**Coverage Gaps:**
- The available test cases do not confirm the expected outcome of a new grading form being created from a template. Test ID 11.1AG(O-002 is for creating a form from scratch, and Test ID 11.1AG(O-005 only verifies the availability of the option to create from a template, not the creation itself.

#### Execution Plan

**1. [ACTION] 11.1AG(O-003** -- Create new grading form from a template
   > Run 11.1AG(O-003 — this is the state-changing action being verified

**Notes:** Execute 11.1AG(O-003 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify a new grading form is created from the selected template successfully
  - Suggested: Manually verify that a new grading form is created from the selected template by checking the list of grading forms after the creation action.

---

### 12.1G/GR(-001: Save changes with valid data in all columns

**Coverage:** FULL Full
**Modifies State:** grading_actions

**1. Verify the changes in grades are reflected in the Gradebook**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 12.1G/GR(-002 (Verify changes are reflected in the Overall average row)
- **Confidence:** 85%
- **Before Action:** Record the current grades in the BUS301 columns before the action
- **After Action:** Compare the grades in the BUS301 columns and confirm they reflect the new entries
- **Execution Note:** Use this test to observe the Overall average row before and after the action to verify changes in grades.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 12.1G/GR(-002** -- Verify changes are reflected in the Overall average row
   > Run 12.1G/GR(-002 and RECORD the current values before the action

**2. [ACTION] 12.1G/GR(-001** -- Save changes with valid data in all columns
   > Run 12.1G/GR(-001 — this is the state-changing action being verified

**3. [POST-VERIFY] 12.1G/GR(-002** -- Verify changes are reflected in the Overall average row
   > Run 12.1G/GR(-002 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 12.1G/GR(-002 → ACTION: Execute 12.1G/GR(-001 → POST: Verify with 12.1G/GR(-002 (compare against baseline)

---

### 12.1G/GR(-002: Verify changes are reflected in the Overall average row

**Coverage:** NONE None
**Modifies State:** grading_actions

**1. Verify the Overall average row is updated to reflect the changes made**

- **Status:** MISSING not_found
- **Strategy:** Before/After
- **Matched Test:** -
- **Confidence:** -
- **Before Action:** Record the current Overall average before the changes
- **After Action:** Compare and confirm the Overall average reflects the updated grades
- **Reason:** None of the test cases access or display the Overall average row in the Gradebook / Grader Report.
- **Manual Step:** Manually check the Overall average row before and after changes to verify the update.

**Coverage Gaps:**
- None of the test cases access or display the Overall average row in the Gradebook / Grader Report.

#### Execution Plan

**1. [ACTION] 12.1G/GR(-002** -- Verify changes are reflected in the Overall average row
   > Run 12.1G/GR(-002 — this is the state-changing action being verified

**Notes:** Execute 12.1G/GR(-002 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the Overall average row is updated to reflect the changes made
  - Suggested: Manually check the Overall average row before and after changes to verify the update.

---

### 15.15.PRO-001: Update profile with all valid inputs

**Coverage:** FULL Full
**Modifies State:** profile_modification

**1. Verify the profile is updated with the new information**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 15.15.PRO-002 (Verify profile fields are displayed correctly)
- **Confidence:** 90%
- **Before Action:** Record the current profile details before the update
- **After Action:** Compare the profile details and confirm they reflect the new inputs
- **Execution Note:** Use this test to display the profile fields (first name, last name, email) before and after the update to verify the changes.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 15.15.PRO-002** -- Verify profile fields are displayed correctly
   > Run 15.15.PRO-002 and RECORD the current values before the action

**2. [ACTION] 15.15.PRO-001** -- Update profile with all valid inputs
   > Run 15.15.PRO-001 — this is the state-changing action being verified

**3. [POST-VERIFY] 15.15.PRO-002** -- Verify profile fields are displayed correctly
   > Run 15.15.PRO-002 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 15.15.PRO-002 → ACTION: Execute 15.15.PRO-001 → POST: Verify with 15.15.PRO-002 (compare against baseline)

---

## Navigation Graph

![Navigation Graph](output/moodle/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| 1. Login | /login | No | 7 |
| 2. Dashboard | /dashboard | Yes | 20 |
| 3. My Courses | /my-courses | Yes | 7 |
| 4. Course Page | /course | Yes | 15 |
| 5. Adding Activities (Teacher Only) | /course/add-activities | Yes | 16 |
| 6. Course Settings (Teacher Only) | /course/settings | Yes | 8 |
| 7. Participants | /course/participants | Yes | 26 |
| 8. Assignment (Teacher View) | /assignment/teacher | Yes | 11 |
| 9. Assignment Submissions (Teacher Only) | /assignment/submissions | Yes | 15 |
| 10. Assignment (Student View) | /assignment/student | Yes | 9 |
| 11. Advanced Grading (Teacher Only) | /assignment/advanced-grading | Yes | 7 |
| 12. Gradebook / Grader Report (Teacher Only) | /gradebook | Yes | 10 |
| 13. Grades / User Report (Student View) | /grades/user-report | Yes | 5 |
| 14. Activities (Student View) | /activities | Yes | 8 |
| 15. Profile | /profile | Yes | 9 |
