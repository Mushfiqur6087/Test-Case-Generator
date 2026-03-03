# Moodle

**Base URL:** 
**Generated:** 2026-03-04T04:16:51.604224

## Summary

| Metric | Count |
|--------|-------|
| **Total Tests** | 180 |

### By Type

| Type | Count |
|------|-------|
| Positive | 136 |
| Negative | 32 |
| Edge Case | 12 |

### By Priority

| Priority | Count |
|----------|-------|
| High | 69 |
| Medium | 92 |
| Low | 19 |

### Post-Verification Coverage

| Metric | Count |
|--------|-------|
| Tests Needing Verification | 22 |
| Full Coverage | 2 |
| Partial Coverage | 4 |
| No Coverage | 16 |

### Execution Plans

| Metric | Value |
|--------|-------|
| Total Plans | 15 |
| Automated Steps | 6 |
| Manual Steps | 11 |
| Automation Rate | 35.3% |

---

## Test Cases

### 1. Login

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1.LOG-001 | Successful login with valid username and password | User has valid credentials | 1. Enter a valid username<br>2. Enter a valid password<br>3. Click the Log in button | Redirects to the Dashboard | High |
| 1.LOG-007 | Access as a guest | None | 1. Click the Access as a guest button | Redirects to the guest access page | Low |
| 1.LOG-008 | Cookies notice button functionality | None | 1. Click the Cookies notice button | Cookies notice is dismissed | Low |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1.LOG-002 | Username field empty | None | 1. Leave the Username field empty<br>2. Enter a valid password<br>3. Click the Log in button | Error message appears indicating the username is required | Medium |
| 1.LOG-003 | Password field empty | None | 1. Enter a valid username<br>2. Leave the Password field empty<br>3. Click the Log in button | Error message appears indicating the password is required | Medium |
| 1.LOG-004 | Invalid username and valid password | None | 1. Enter an invalid username<br>2. Enter a valid password<br>3. Click the Log in button | Error message appears indicating invalid credentials | Medium |
| 1.LOG-005 | Valid username and invalid password | None | 1. Enter a valid username<br>2. Enter an invalid password<br>3. Click the Log in button | Error message appears indicating invalid credentials | Medium |
| 1.LOG-006 | Username field remains populated after error | None | 1. Enter a valid username<br>2. Enter an invalid password<br>3. Click the Log in button | Username field remains populated for correction | Medium |

---

### 2. Dashboard

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 2.DAS-001 | Verify current date is highlighted in calendar block | None | 1. Open the Calendar block<br>2. Observe the calendar display | Current date is highlighted | High |
| 2.DAS-002 | Verify event names are displayed on dates with events | None | 1. Open the Calendar block<br>2. Identify a date with an existing event<br>3. Observe the event name display on the date | Event names are displayed on dates with events | High |
| 2.DAS-003 | Create a new calendar entry for a future date | None | 1. Open the Calendar block<br>2. Click on the 'New event' button<br>3. Enter valid event details for a future date<br>4. Save the event | New event is saved and displayed on the selected future date | High |
| 2.DAS-004 | Create a new calendar entry for the current date | None | 1. Open the Calendar block<br>2. Click on the 'New event' button<br>3. Enter valid event details for the current date<br>4. Save the event | New event is saved and displayed on the current date | High |
| 2.DAS-005 | Toggle edit mode to add a block | Dashboard is open | 1. Click on the Edit mode toggle<br>2. Verify Edit mode is activated | Edit mode is activated successfully | High |
| 2.DAS-006 | Open Add a block modal | Edit mode is activated | 1. Click on the + Add a block button | Add a block modal is displayed | High |
| 2.DAS-007 | Verify block is added to the dashboard | Add a block modal is open and block type is selected | 1. Click on the Add button in the Add a block modal | New block is added to the dashboard | High |
| 2.DAS-008 | Cancel adding a block using X button | Add a block modal is open | 1. Click on the X button in the Add a block modal | Add a block modal is closed | Medium |
| 2.DAS-009 | Cancel adding a block using Cancel button | Add a block modal is open | 1. Click on the Cancel button in the Add a block modal | Add a block modal is closed | Medium |
| 2.DAS-010 | Cancel adding a block using Cancel link | Add a block page is open | 1. Click on the Cancel link on the Add a block page | User is returned to the previous state without adding a block | Medium |
| 2.DAS-011 | Move a block using Move icon | Dashboard has multiple blocks | 1. Click and hold the Move icon on a block<br>2. Drag the block to a new position<br>3. Release the Move icon | Block is moved to the new position on the dashboard | Medium |
| 2.DAS-012 | Access block options using Three-dot menu | Dashboard has at least one block | 1. Click on the Three-dot menu of a block | Options menu for the block is displayed | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 2.DAS-013 | Create a new calendar entry with a past date | None | 1. Open the Calendar block<br>2. Click on the 'New event' button<br>3. Enter valid event details for a past date<br>4. Attempt to save the event | System prevents saving an event with a past date | Medium |
| 2.DAS-014 | Create a new calendar entry with an empty event name | None | 1. Open the Calendar block<br>2. Click on the 'New event' button<br>3. Leave the event name field empty<br>4. Enter valid details for other fields<br>5. Attempt to save the event | System prevents saving an event with an empty event name | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 2.DAS-015 | Create a new calendar entry with maximum length event name | None | 1. Open the Calendar block<br>2. Click on the 'New event' button<br>3. Enter an event name with maximum allowed characters<br>4. Enter valid details for other fields<br>5. Save the event | New event is saved and displayed correctly with the maximum length event name | Low |

---

### 3. My Courses

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 3MC-001 | Verify My Courses heading is displayed | None | 1. Check if the 'My courses' heading is visible on the page | 'My courses' heading is displayed | High |
| 3MC-002 | Verify Course overview subheading is displayed | None | 1. Check if the 'Course overview' subheading is visible on the page | 'Course overview' subheading is displayed | High |
| 3MC-003 | Verify course cards are displayed | User is enrolled in courses | 1. Check if course cards are displayed on the page | Course cards are displayed | High |
| 3MC-004 | Verify course name link is clickable | Course card is displayed | 1. Click on the course name link on a course card | Course name link is clickable and navigates to the course details | High |
| 3MC-005 | Verify search field functionality | None | 1. Enter a course name in the search field<br>2. Press Enter or click the search icon | Courses matching the search criteria are displayed | High |
| 3MC-006 | Verify category name is displayed on course card | Course card is displayed | 1. Check if the category name is visible on a course card | Category name is displayed on the course card | Medium |
| 3MC-007 | Verify All dropdown functionality | None | 1. Click on the 'All' dropdown<br>2. Select an option from the dropdown | Courses are filtered based on the selected option | Medium |
| 3MC-008 | Verify Sort by course name dropdown functionality | None | 1. Click on the 'Sort by course name' dropdown<br>2. Select an option to sort courses | Courses are sorted based on the selected option | Medium |
| 3MC-009 | Verify Card dropdown functionality | Course card is displayed | 1. Click on the card dropdown on a course card<br>2. Select an option from the dropdown | Selected action is performed on the course card | Medium |
| 3MC-010 | Verify Three-dot menu functionality | Course card is displayed | 1. Click on the three-dot menu on a course card<br>2. Select an option from the menu | Selected action is performed on the course card | Medium |
| 3MC-011 | Verify Star this course option | Course card is displayed | 1. Click on the three-dot menu on a course card<br>2. Select 'Star this course' option | Course is starred and marked as favorite | Medium |
| 3MC-012 | Verify Remove from view option | Course card is displayed | 1. Click on the three-dot menu on a course card<br>2. Select 'Remove from view' option | Course is removed from the view | Medium |

---

### 4. Course Page

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 4CP-001 | Verify course full name is displayed as a heading | None | 1. Check if the course full name is displayed as a heading at the top of the page | Course full name is displayed as a heading | High |
| 4CP-002 | Verify horizontal navigation bar is present | None | 1. Check if the horizontal navigation bar is present below the course full name | Horizontal navigation bar is present | High |
| 4CP-003 | Verify Course tab is clickable | None | 1. Click on the Course tab in the navigation bar | Course tab is clickable and displays course content | High |
| 4CP-004 | Verify Edit mode can be toggled | None | 1. Click on the Edit mode button to toggle it | Edit mode can be toggled on and off | High |
| 4CP-005 | Verify BUS301 Course Overview is accessible | None | 1. Click on BUS301 Course Overview | BUS301 Course Overview is accessible and displays content | High |
| 4CP-006 | Verify BUS301 Business Discussion is accessible | None | 1. Click on BUS301 Business Discussion | BUS301 Business Discussion is accessible and displays content | High |
| 4CP-007 | Verify BUS301 - Case Study Analysis is accessible | None | 1. Click on BUS301 - Case Study Analysis | BUS301 - Case Study Analysis is accessible and displays content | High |
| 4CP-008 | Verify BUS301 - Business Plan Draft is accessible | None | 1. Click on BUS301 - Business Plan Draft | BUS301 - Business Plan Draft is accessible and displays content | High |
| 4CP-009 | Verify BUS301 - Final Presentation is accessible | None | 1. Click on BUS301 - Final Presentation | BUS301 - Final Presentation is accessible and displays content | High |
| 4CP-010 | Verify Settings tab is clickable | None | 1. Click on the Settings tab in the navigation bar | Settings tab is clickable and displays settings options | Medium |
| 4CP-011 | Verify Participants tab is clickable | None | 1. Click on the Participants tab in the navigation bar | Participants tab is clickable and displays participants list | Medium |
| 4CP-012 | Verify Grades tab is clickable | None | 1. Click on the Grades tab in the navigation bar | Grades tab is clickable and displays grades overview | Medium |
| 4CP-013 | Verify Activities tab is clickable | None | 1. Click on the Activities tab in the navigation bar | Activities tab is clickable and displays activities list | Medium |
| 4CP-014 | Verify More dropdown is clickable | None | 1. Click on the More dropdown in the navigation bar | More dropdown is clickable and displays additional options | Medium |
| 4CP-015 | Verify Competencies tab is clickable | None | 1. Click on the Competencies tab in the navigation bar | Competencies tab is clickable and displays competencies overview | Medium |
| 4CP-016 | Verify collapsible chevron arrow functionality | None | 1. Click on the collapsible chevron arrow next to a section name | Section content is expanded or collapsed | Medium |
| 4CP-017 | Verify Collapse all link collapses all sections | None | 1. Click on the Collapse all link | All sections are collapsed | Medium |
| 4CP-018 | Verify announcements are displayed | None | 1. Check if announcements are displayed on the course page | Announcements are displayed | Medium |
| 4CP-019 | Verify Course Index is accessible | None | 1. Click on the Course Index | Course Index is accessible and displays content | Medium |
| 4CP-020 | Verify Close button (X) closes the overlay | An overlay is open | 1. Click on the Close button (X) | Overlay is closed | Medium |
| 4CP-021 | Verify activity icon is displayed next to activity name | None | 1. Check if an activity icon is displayed next to each activity name | Activity icon is displayed next to each activity name | Low |

---

### 5. Adding Activities (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5AA(O-001 | Enable edit mode successfully | None | 1. Click on the edit mode toggle | Edit mode is enabled | High |
| 5AA(O-002 | Open Activity Chooser modal | Edit mode is enabled | 1. Click on the + button | Activity Chooser modal is displayed | High |
| 5AA(O-003 | Select an activity from Activity Chooser | Activity Chooser modal is open | 1. Select an activity or resource option from the grid | Selected activity or resource is highlighted | High |
| 5AA(O-004 | Confirm selection of an activity | An activity or resource is selected | 1. Click on the Add button | Activity or resource is added to the course | High |
| 5AA(O-005 | Create new assignment with all valid inputs | None | 1. Enter a valid assignment name<br>2. Enter a description in the rich text editor<br>3. Check the 'Display description on course page' checkbox<br>4. Enter activity instructions in the rich text editor<br>5. Upload a valid file in the additional files upload area<br>6. Set a valid 'Allow submissions from' date/time<br>7. Set a valid 'Due date' date/time<br>8. Set a valid 'Cut-off date' date/time<br>9. Set a valid 'Remind me to grade by' date/time<br>10. Check the 'Always show description' checkbox<br>11. Check the 'Online text' checkbox<br>12. Check the 'File submissions' checkbox<br>13. Select a valid option from 'Maximum number of uploaded files' dropdown<br>14. Select a valid option from 'Maximum submission size' dropdown<br>15. Enter valid accepted file types<br>16. Check the 'Send content change notification' checkbox<br>17. Click the 'Save and return to course' button | Assignment is created and the user is returned to the course page | High |
| 5AA(O-006 | Create new assignment with 'Save and display' | None | 1. Enter a valid assignment name<br>2. Click the 'Save and display' button | Assignment is created and the activity page is displayed | High |
| 5AA(O-008 | Search for an activity in Activity Chooser | Activity Chooser modal is open | 1. Enter a search term in the search field | Relevant activities or resources are filtered and displayed | Medium |
| 5AA(O-009 | Filter activities by category | Activity Chooser modal is open | 1. Select a category filter such as Assessment | Activities or resources related to the selected category are displayed | Medium |
| 5AA(O-010 | View information about an activity | Activity Chooser modal is open | 1. Click on the Info button for an activity | Information about the selected activity is displayed | Medium |
| 5AA(O-011 | Star an activity for quick access | Activity Chooser modal is open | 1. Click on the Star button for an activity | Activity is starred and marked for quick access | Medium |
| 5AA(O-012 | Cancel creating a new assignment | None | 1. Enter a valid assignment name<br>2. Click the 'Cancel' button | Changes are discarded and no assignment is created | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5AA(O-007 | Assignment name field empty | None | 1. Leave the assignment name field empty<br>2. Click the 'Save and return to course' button | Error message indicating that the assignment name is required | High |
| 5AA(O-013 | Add button disabled when no activity selected | Activity Chooser modal is open with no activity selected | 1. Attempt to click the Add button | Add button remains disabled | Medium |
| 5AA(O-014 | Upload file exceeding maximum size | None | 1. Upload a file larger than 100 MB in the additional files upload area<br>2. Click the 'Save and return to course' button | Error message indicating the file exceeds the maximum size limit | Medium |
| 5AA(O-015 | Maximum submission size exceeds site limit | None | 1. Select an option from 'Maximum submission size' dropdown that exceeds 100 MB<br>2. Click the 'Save and return to course' button | Error message indicating the submission size exceeds the site limit | Medium |
| 5AA(O-016 | Search with no matching results | Activity Chooser modal is open | 1. Enter a search term that does not match any activity | No activities or resources are displayed | Low |
| 5AA(O-017 | Filter by category with no activities | Activity Chooser modal is open | 1. Select a category filter with no available activities | No activities or resources are displayed | Low |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 5AA(O-018 | Set same date for 'Allow submissions from' and 'Due date' | None | 1. Set the same date/time for 'Allow submissions from' and 'Due date'<br>2. Click the 'Save and return to course' button | Assignment is created successfully with the same start and due date | Low |
| 5AA(O-019 | Set future date for 'Due date' | None | 1. Set a future date/time for 'Due date'<br>2. Click the 'Save and return to course' button | Assignment is created successfully with a future due date | Low |

---

### 6. Course Settings (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6CS(O-001 | Save course settings with all valid inputs | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category<br>4. Select a course visibility option<br>5. Select a course start date<br>6. Enable course end date and select a date<br>7. Enter a valid course ID number<br>8. Enter a course summary<br>9. Upload a valid file<br>10. Select a format from the dropdown<br>11. Select an option for hidden sections<br>12. Select a course layout<br>13. Select a force language option<br>14. Enter a number of announcements<br>15. Select an option to show gradebook to students<br>16. Select an option to show activity reports<br>17. Select an option to show activity dates<br>18. Select a maximum upload size<br>19. Enable completion tracking<br>20. Select an option to show activity completion conditions<br>21. Select a group mode<br>22. Select a force group mode<br>23. Select a default grouping<br>24. Enter tags<br>25. Click the Save and display button | Course settings are saved successfully and displayed | High |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6CS(O-002 | Course full name field empty | User is on the Course Settings page | 1. Leave the course full name field empty<br>2. Enter a valid course short name<br>3. Select a valid course category<br>4. Click the Save and display button | An error message is displayed indicating that the course full name is required | Medium |
| 6CS(O-003 | Course short name field empty | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Leave the course short name field empty<br>3. Select a valid course category<br>4. Click the Save and display button | An error message is displayed indicating that the course short name is required | Medium |
| 6CS(O-004 | Course category field empty | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Leave the course category field empty<br>4. Click the Save and display button | An error message is displayed indicating that the course category is required | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 6CS(O-005 | Course start date and end date are the same | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category<br>4. Select the same date for course start date and course end date<br>5. Click the Save and display button | Course settings are saved successfully with the same start and end date | Low |
| 6CS(O-006 | Maximum upload size at boundary value | User is on the Course Settings page | 1. Enter a valid course full name<br>2. Enter a valid course short name<br>3. Select a valid course category<br>4. Select the maximum allowed upload size from the dropdown<br>5. Click the Save and display button | Course settings are saved successfully with the maximum upload size | Low |

---

### 7. Participants

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 7.PAR-001 | Apply filter with a single condition | None | 1. Select a criterion from the Any dropdown<br>2. Select a corresponding value from the Select dropdown<br>3. Click the Apply filters button | Count displays the number of participants matching the filter criteria | High |
| 7.PAR-002 | Apply filter with multiple conditions | None | 1. Select a criterion from the Any dropdown<br>2. Select a corresponding value from the Select dropdown<br>3. Click the + Add condition link<br>4. Select another criterion from the Any dropdown<br>5. Select a corresponding value from the Select dropdown<br>6. Click the Apply filters button | Count displays the number of participants matching all filter criteria | High |
| 7.PAR-003 | Enroll user with valid username and role | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Click on the Enrol users button | User is successfully enrolled with the selected role | High |
| 7.PAR-004 | Enroll user with valid email and role | User is on the enrol users page | 1. Select a valid email from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Click on the Enrol users button | User is successfully enrolled with the selected role | High |
| 7.PAR-005 | Clear filters after applying | Filters have been applied | 1. Click the Clear filters button | All filters are removed and the full list of participants is displayed | Medium |
| 7.PAR-006 | Remove a single condition using X button | Multiple filter conditions are applied | 1. Click the X button next to a condition | The selected condition is removed and the participant count updates accordingly | Medium |
| 7.PAR-007 | Use alphabetical filter buttons | None | 1. Click on an alphabetical filter button | List of participants is filtered to show only those whose names start with the selected letter | Medium |
| 7.PAR-008 | Enroll user with enrollment duration set | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Set a valid enrollment duration<br>4. Click on the Enrol users button | User is successfully enrolled with the selected role and duration | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 7.PAR-009 | Apply filter with no conditions | None | 1. Ensure no conditions are selected<br>2. Click the Apply filters button | No filters are applied and the full list of participants is displayed | Medium |
| 7.PAR-010 | Add condition without selecting criteria | None | 1. Click the + Add condition link<br>2. Leave the Any dropdown unselected<br>3. Click the Apply filters button | No filters are applied and an error message prompts the user to select criteria | Medium |
| 7.PAR-011 | Add condition without selecting value | None | 1. Select a criterion from the Any dropdown<br>2. Leave the Select dropdown unselected<br>3. Click the Apply filters button | No filters are applied and an error message prompts the user to select a value | Medium |
| 7.PAR-012 | Enroll user with no username selected | User is on the enrol users page | 1. Leave the Enrolled users dropdown empty<br>2. Select a valid role from the role dropdown<br>3. Click on the Enrol users button | Error message displayed indicating username is required | Medium |
| 7.PAR-013 | Enroll user with no role selected | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Leave the role dropdown empty<br>3. Click on the Enrol users button | Error message displayed indicating role is required | Medium |
| 7.PAR-014 | Enroll user with invalid enrollment duration | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Enter an invalid enrollment duration<br>4. Click on the Enrol users button | Error message displayed indicating invalid enrollment duration | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 7.PAR-015 | Apply filter with maximum number of conditions | None | 1. Add the maximum number of conditions allowed using the + Add condition link<br>2. Select criteria and corresponding values for each condition<br>3. Click the Apply filters button | Count displays the number of participants matching all filter criteria | Low |
| 7.PAR-016 | Enroll user with maximum enrollment duration | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Enter the maximum allowed enrollment duration<br>4. Click on the Enrol users button | User is successfully enrolled with the selected role and maximum duration | Low |
| 7.PAR-017 | Enroll user with minimum enrollment duration | User is on the enrol users page | 1. Select a valid username from the Enrolled users dropdown<br>2. Select a valid role from the role dropdown<br>3. Enter the minimum allowed enrollment duration<br>4. Click on the Enrol users button | User is successfully enrolled with the selected role and minimum duration | Low |

---

### 8. Assignment (Teacher View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 8A(V-001 | Verify assignment icon is displayed | None | 1. Check if the assignment icon is visible on the page | Assignment icon is displayed | High |
| 8A(V-002 | Verify heading 'ASSIGNMENT' is displayed | None | 1. Check if the heading 'ASSIGNMENT' is visible on the page | Heading 'ASSIGNMENT' is displayed | High |
| 8A(V-003 | Verify assignment name is displayed | None | 1. Check if the assignment name is visible on the page | Assignment name is displayed | High |
| 8A(V-004 | Verify Assignment tab is displayed | None | 1. Check if the Assignment tab is visible on the page | Assignment tab is displayed | High |
| 8A(V-005 | Verify Settings tab is displayed | None | 1. Check if the Settings tab is visible on the page | Settings tab is displayed | High |
| 8A(V-006 | Verify Submissions tab is displayed | None | 1. Check if the Submissions tab is visible on the page | Submissions tab is displayed | High |
| 8A(V-007 | Verify Advanced grading tab is displayed | None | 1. Check if the Advanced grading tab is visible on the page | Advanced grading tab is displayed | High |
| 8A(V-008 | Verify More dropdown is displayed | None | 1. Check if the More dropdown is visible on the page | More dropdown is displayed | High |
| 8A(V-009 | Verify Opened date is displayed | None | 1. Check if the Opened date is visible on the page | Opened date is displayed | High |
| 8A(V-010 | Verify Due date is displayed | None | 1. Check if the Due date is visible on the page | Due date is displayed | High |
| 8A(V-011 | Verify assignment description text is displayed | None | 1. Check if the assignment description text is visible on the page | Assignment description text is displayed | High |
| 8A(V-012 | Verify Grade button is displayed | None | 1. Check if the Grade button is visible on the page | Grade button is displayed | High |
| 8A(V-013 | Verify Grading summary section is displayed | None | 1. Check if the Grading summary section is visible on the page | Grading summary section is displayed | High |
| 8A(V-014 | Verify 'Hidden from students' indicator is displayed | None | 1. Check if the 'Hidden from students' indicator is visible on the page | 'Hidden from students' indicator is displayed | High |
| 8A(V-015 | Verify Participants count is displayed | None | 1. Check if the Participants count is visible on the page | Participants count is displayed | High |
| 8A(V-016 | Verify Submitted count is displayed | None | 1. Check if the Submitted count is visible on the page | Submitted count is displayed | High |
| 8A(V-017 | Verify Needs grading count is displayed | None | 1. Check if the Needs grading count is visible on the page | Needs grading count is displayed | High |
| 8A(V-018 | Verify Time remaining until due date is displayed | None | 1. Check if the Time remaining until due date is visible on the page | Time remaining until due date is displayed | High |

---

### 9. Assignment Submissions (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 9AS(O-001 | Verify all elements are displayed correctly on the Submissions tab | None | 1. Check the presence of the Search users field<br>2. Check the presence of the Filter by name dropdown<br>3. Check the presence of the Status filter<br>4. Check the presence of the Advanced dropdown<br>5. Check the presence of the Grade button<br>6. Check the presence of the Quick grading checkbox<br>7. Check the presence of the Actions dropdown<br>8. Check the presence of the Select checkbox<br>9. Check the presence of First name / Last name link<br>10. Check the presence of Email address<br>11. Check the presence of Status<br>12. Check the presence of Grade<br>13. Check the presence of Last modified (submission)<br>14. Check the presence of Online text<br>15. Check the presence of File submissions<br>16. Check the presence of Submission comments<br>17. Check the presence of Last modified (grade)<br>18. Check the presence of Feedback comments<br>19. Check the presence of Feedback files<br>20. Check the presence of Final grade<br>21. Check the presence of Three-dot menus | All elements are displayed correctly on the Submissions tab | High |
| 9AS(O-002 | Search for a user using the Search users field | None | 1. Enter a valid username into the Search users field<br>2. Press the Enter key | The table displays submissions for the searched user | High |
| 9AS(O-003 | Grade a submission using the Grade button | None | 1. Click on the Grade button for a submission<br>2. Enter a valid grade<br>3. Save the grade | The submission is graded successfully and the grade is displayed | High |
| 9AS(O-004 | Filter submissions by name using the Filter by name dropdown | None | 1. Select a name from the Filter by name dropdown | The table displays submissions filtered by the selected name | Medium |
| 9AS(O-005 | Filter submissions by status using the Status filter | None | 1. Select a status from the Status filter | The table displays submissions filtered by the selected status | Medium |
| 9AS(O-006 | Use the Advanced dropdown to apply additional filters | None | 1. Click on the Advanced dropdown<br>2. Select additional filters | The table displays submissions filtered by the selected advanced filters | Medium |
| 9AS(O-007 | Enable quick grading using the Quick grading checkbox | None | 1. Check the Quick grading checkbox | Quick grading is enabled, allowing grades to be entered directly into the table | Medium |
| 9AS(O-008 | Perform an action using the Actions dropdown | None | 1. Select an action from the Actions dropdown | The selected action is performed on the chosen submissions | Medium |
| 9AS(O-009 | Select a submission using the Select checkbox | None | 1. Click on the Select checkbox for a submission | The submission is selected | Medium |
| 9AS(O-010 | Access student details via First name / Last name link | None | 1. Click on the First name / Last name link for a student | The student details page is displayed | Medium |
| 9AS(O-011 | View submission details using the Three-dot menu | None | 1. Click on the Three-dot menu for a submission<br>2. Select 'View details' | The submission details are displayed | Medium |

---

### 10. Assignment (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1A(V-001 | Submit assignment with online text | Assignment is available for submission | 1. Click on 'Add submission' button<br>2. Enter valid text in the 'Online text' field<br>3. Click on 'Submit' button | Submission status updates to 'Submitted for grading' | High |
| 1A(V-002 | Submit assignment by uploading files | Assignment is available for submission | 1. Click on 'Add submission' button<br>2. Upload valid file(s) in the 'Upload files' section<br>3. Click on 'Submit' button | Submission status updates to 'Submitted for grading' | High |
| 1A(V-003 | Verify grade and feedback appear after grading | Assignment has been graded | 1. View the assignment details page | Grade and feedback are displayed | High |
| 1A(V-004 | Edit submission before due date | Assignment is submitted and due date has not passed | 1. Click on 'Edit submission' button<br>2. Modify the content in the 'Online text' field or replace uploaded files<br>3. Click on 'Save changes' button | Submission is updated with the new content | Medium |
| 1A(V-005 | Remove submission before due date | Assignment is submitted and due date has not passed | 1. Click on 'Edit submission' button<br>2. Remove all content from 'Online text' and 'Upload files'<br>3. Click on 'Save changes' button | Submission status updates to 'Draft (not submitted)' | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1A(V-006 | Attempt to submit assignment with empty online text | Assignment is available for submission | 1. Click on 'Add submission' button<br>2. Leave 'Online text' field empty<br>3. Click on 'Submit' button | Error message displayed indicating online text is required | Medium |
| 1A(V-007 | Attempt to submit assignment without uploading files | Assignment is available for submission | 1. Click on 'Add submission' button<br>2. Do not upload any files in the 'Upload files' section<br>3. Click on 'Submit' button | Error message displayed indicating file upload is required | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1A(V-008 | Submit assignment with maximum length online text | Assignment is available for submission | 1. Click on 'Add submission' button<br>2. Enter maximum allowed characters in the 'Online text' field<br>3. Click on 'Submit' button | Submission status updates to 'Submitted for grading' | Low |
| 1A(V-009 | Submit assignment with future due date | Assignment is available for submission and due date is set in the future | 1. Click on 'Add submission' button<br>2. Enter valid text in the 'Online text' field<br>3. Click on 'Submit' button | Submission status updates to 'Submitted for grading' | Low |

---

### 11. Advanced Grading (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1AG(O-001 | Verify dropdown default selection is 'Rubric' | None | 1. Locate the 'Change active grading method to' dropdown<br>2. Check the default selected option | The default selected option is 'Rubric' | High |
| 1AG(O-002 | Verify 'Define new grading form from scratch' option is displayed | None | 1. Locate the 'Define new grading form from scratch' card | The 'Define new grading form from scratch' option is displayed | High |
| 1AG(O-003 | Verify 'Create new grading form from a template' option is displayed | None | 1. Locate the 'Create new grading form from a template' card | The 'Create new grading form from a template' option is displayed | High |
| 1AG(O-004 | Verify notification message when advanced grading form is not ready | None | 1. Ensure the advanced grading form is not in a valid status<br>2. Check for the notification message | Notification message 'Please note: the advanced grading form is not ready at the moment. Simple grading method will be used until the form has a valid status.' is displayed | Medium |

---

### 12. Gradebook / Grader Report (Teacher Only)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1G/GR(-001 | Save changes with valid data in all fields | Grader report is in edit mode | 1. Enter valid data in all assignment columns<br>2. Click the Save changes button | Changes are saved successfully and reflected in the Grader report | High |
| 1G/GR(-002 | Verify Grader report dropdown is displayed | None | 1. Check the presence of the Grader report dropdown | Grader report dropdown is displayed | Medium |
| 1G/GR(-003 | Verify Search users field is displayed | None | 1. Check the presence of the Search users field | Search users field is displayed | Medium |
| 1G/GR(-004 | Verify Filter by name dropdown is displayed | None | 1. Check the presence of the Filter by name dropdown | Filter by name dropdown is displayed | Medium |
| 1G/GR(-005 | Verify Three-dot menu in course name header is displayed | None | 1. Check the presence of the Three-dot menu in course name header | Three-dot menu in course name header is displayed | Medium |
| 1G/GR(-006 | Verify First name / Last name links are displayed | None | 1. Check the presence of First name / Last name links | First name / Last name links are displayed | Medium |
| 1G/GR(-007 | Verify Email address column is displayed | None | 1. Check the presence of the Email address column | Email address column is displayed | Medium |
| 1G/GR(-008 | Verify Assignment columns are displayed | None | 1. Check the presence of Assignment columns | Assignment columns are displayed | Medium |
| 1G/GR(-009 | Verify r column is displayed | None | 1. Check the presence of the r column | r column is displayed | Medium |
| 1G/GR(-010 | Verify Course total column is displayed | None | 1. Check the presence of the Course total column | Course total column is displayed | Medium |
| 1G/GR(-011 | Verify Three-dot menu in column headers is displayed | None | 1. Check the presence of the Three-dot menu in column headers | Three-dot menu in column headers is displayed | Medium |
| 1G/GR(-012 | Verify Three-dot menu in grade cells is displayed | None | 1. Check the presence of the Three-dot menu in grade cells | Three-dot menu in grade cells is displayed | Medium |
| 1G/GR(-013 | Verify Overall average row is displayed | None | 1. Check the presence of the Overall average row | Overall average row is displayed | Medium |
| 1G/GR(-014 | Verify Save changes button is displayed | None | 1. Check the presence of the Save changes button | Save changes button is displayed | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1G/GR(-015 | Attempt to save changes with an empty assignment column | Grader report is in edit mode | 1. Leave one assignment column empty<br>2. Click the Save changes button | An error message is displayed indicating the assignment column cannot be empty | Medium |
| 1G/GR(-016 | Attempt to save changes with invalid data in assignment column | Grader report is in edit mode | 1. Enter invalid data in an assignment column<br>2. Click the Save changes button | An error message is displayed indicating the data is invalid | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1G/GR(-017 | Save changes with maximum length data in assignment column | Grader report is in edit mode | 1. Enter maximum length valid data in an assignment column<br>2. Click the Save changes button | Changes are saved successfully and reflected in the Grader report | Low |

---

### 13. Grades / User Report (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1G/UR(-001 | Verify student can view their own grades | Student is logged in and on the Grades page | 1. Locate the 'User report' dropdown<br>2. Verify the dropdown indicates the current report view<br>3. Check that the grades displayed belong to the logged-in student | Student's own grades are displayed correctly | High |
| 1G/UR(-002 | Verify display of ungraded items | Student is logged in and on the Grades page | 1. Locate a grade item that has not been submitted or graded<br>2. Verify that '(Empty)' is displayed in the Calculated weight column | Ungraded items show '(Empty)' in Calculated weight | Medium |
| 1G/UR(-003 | Verify grade item details display | Student is logged in and on the Grades page | 1. Locate a grade item<br>2. Verify the presence of Grade, Range, Percentage, Feedback, Contribution to course total, Type label, and Activity name link | All grade item details are displayed correctly | Medium |
| 1G/UR(-004 | Verify AGGREGATION Course total row display | Student is logged in and on the Grades page | 1. Scroll to the bottom of the grades list<br>2. Verify the presence of the AGGREGATION Course total row | AGGREGATION Course total row is displayed correctly | Medium |
| 1G/UR(-005 | Verify three-dot menu functionality | Student is logged in and on the Grades page | 1. Locate the three-dot menu next to a grade item<br>2. Click on the three-dot menu<br>3. Verify that additional options are displayed | Three-dot menu displays additional options | Low |

---

### 14. Activities (Student View)

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 1A(V-001 | Verify Activities page heading displays correctly | None | 1. Verify the page heading displays 'Activities' at the top of the page | The page heading 'Activities' is displayed correctly | High |
| 1A(V-002 | Verify Assignments section is displayed | None | 1. Check if the Assignments section is present on the Activities page | Assignments section is displayed on the Activities page | High |
| 1A(V-003 | Verify Forums section is displayed | None | 1. Check if the Forums section is present on the Activities page | Forums section is displayed on the Activities page | High |
| 1A(V-004 | Verify Resources section is displayed | None | 1. Check if the Resources section is present on the Activities page | Resources section is displayed on the Activities page | High |
| 1A(V-005 | Verify activity name is displayed in Assignments section | Assignments section is displayed | 1. Check if each activity in the Assignments section has a name displayed | Each activity in the Assignments section has a name displayed | Medium |
| 1A(V-006 | Verify due date is displayed in Assignments section | Assignments section is displayed | 1. Check if each activity in the Assignments section has a due date displayed | Each activity in the Assignments section has a due date displayed | Medium |
| 1A(V-007 | Verify submission status is displayed in Assignments section | Assignments section is displayed | 1. Check if each activity in the Assignments section has a submission status displayed | Each activity in the Assignments section has a submission status displayed | Medium |
| 1A(V-008 | Verify arrow icon is present for each activity | Activities are displayed in any section | 1. Check if an arrow icon is present next to each activity | An arrow icon is present next to each activity | Low |

---

### 15. Profile

#### Functional Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.PRO-001 | Update profile with valid first name, last name, and email | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Enter a valid first name<br>3. Enter a valid last name<br>4. Enter a valid email address<br>5. Click the Update profile button | Profile is updated successfully with the new details | High |
| 15.PRO-002 | Verify profile fields are displayed correctly | User is logged in and on the profile page | 1. Verify the presence of the first name field<br>2. Verify the presence of the last name field<br>3. Verify the presence of the email address field<br>4. Verify the presence of the timezone dropdown<br>5. Verify the presence of the description rich text editor | All profile fields are displayed correctly | High |
| 15.PRO-003 | Update profile with valid picture upload | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Upload a valid picture file within the size limit<br>3. Click the Update profile button | Profile picture is updated successfully | Medium |

#### Negative Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.PRO-004 | First name field empty | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Leave the first name field empty<br>3. Enter a valid last name<br>4. Enter a valid email address<br>5. Click the Update profile button | An error message is displayed indicating the first name is required | Medium |
| 15.PRO-005 | Last name field empty | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Enter a valid first name<br>3. Leave the last name field empty<br>4. Enter a valid email address<br>5. Click the Update profile button | An error message is displayed indicating the last name is required | Medium |
| 15.PRO-006 | Email address field empty | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Enter a valid first name<br>3. Enter a valid last name<br>4. Leave the email address field empty<br>5. Click the Update profile button | An error message is displayed indicating the email address is required | Medium |
| 15.PRO-007 | Upload file exceeding maximum size | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Attempt to upload a file larger than 100 MB<br>3. Click the Update profile button | An error message is displayed indicating the file size exceeds the limit | Medium |
| 15.PRO-008 | Upload more than one file | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Attempt to upload more than one file<br>3. Click the Update profile button | An error message is displayed indicating only one file can be uploaded | Medium |
| 15.PRO-009 | Upload unsupported file type | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Attempt to upload a file with an unsupported file type<br>3. Click the Update profile button | An error message is displayed indicating the file type is not supported | Medium |

#### Edge Case Tests

| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |
|-------|-----------|---------------|-------|-----------------|----------|
| 15.PRO-010 | Update profile with maximum length first name | User is logged in and on the profile page | 1. Click on the Edit profile link<br>2. Enter a first name with maximum allowed characters<br>3. Enter a valid last name<br>4. Enter a valid email address<br>5. Click the Update profile button | Profile is updated successfully with the maximum length first name | Low |

---

## Post-Verification Details

This section shows verification requirements for tests that modify application state.
Tests using the **before/after** strategy require running a verification test BEFORE
and AFTER the action to compare values.

### 2.DAS-003: Create a new calendar entry for a future date

**Coverage:** PARTIAL Partial
**Modifies State:** activity_schedule

**1. Verify the new calendar event appears on the selected future date**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 2.DAS-002 (Verify event names are displayed on dates with events)
- **Confidence:** 60%
- **Execution Note:** This test can be adapted to verify if the new event is displayed on a specific date by modifying it to check the selected future date instead of any date with an existing event.
- **Reason:** The test operates on the correct module and accesses the calendar to display event names. However, it does not specifically confirm the presence of a new event on a selected future date.
- **Manual Step:** Manually navigate to the selected future date in the calendar and verify the new event is displayed.

**Coverage Gaps:**
- The test operates on the correct module and accesses the calendar to display event names. However, it does not specifically confirm the presence of a new event on a selected future date.

#### Execution Plan

**1. [ACTION] 2.DAS-003** -- Create a new calendar entry for a future date
   > Run 2.DAS-003 — this is the state-changing action being verified

**2. [POST-VERIFY] 2.DAS-002** -- Verify event names are displayed on dates with events
   > This test can be adapted to verify if the new event is displayed on a specific date by modifying it to check the selected future date instead of any date with an existing event.
   > Limitation: The test operates on the correct module and accesses the calendar to display event names. However, it does not specifically confirm the presence of a new event on a selected future date.

**Notes:** Execute 2.DAS-003 → then verify with 2.DAS-002

---

### 2.DAS-004: Create a new calendar entry for the current date

**Coverage:** FULL Full
**Modifies State:** activity_schedule

**1. Verify the new calendar event appears on the current date**

- **Status:** FOUND found
- **Strategy:** After Only
- **Matched Test:** 2.DAS-002 (Verify event names are displayed on dates with events)
- **Confidence:** 80%
- **Execution Note:** Use this test to open the Calendar block and verify that the new event is displayed on the current date.

#### Execution Plan

**1. [ACTION] 2.DAS-004** -- Create a new calendar entry for the current date
   > Run 2.DAS-004 — this is the state-changing action being verified

**2. [POST-VERIFY] 2.DAS-002** -- Verify event names are displayed on dates with events
   > Use this test to open the Calendar block and verify that the new event is displayed on the current date.

**Notes:** Execute 2.DAS-004 → then verify with 2.DAS-002

---

### 2.DAS-007: Verify block is added to the dashboard

**Coverage:** NONE None
**Modifies State:** user_dashboard

**1. Verify the new block is added to the dashboard**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or display the presence of a new block on the dashboard.
- **Manual Step:** Manually check the dashboard for the presence of the new block after the action.

**Coverage Gaps:**
- None of the test cases access or display the presence of a new block on the dashboard.

#### Execution Plan

**1. [ACTION] 2.DAS-007** -- Verify block is added to the dashboard
   > Run 2.DAS-007 — this is the state-changing action being verified

**Notes:** Execute 2.DAS-007 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the new block is added to the dashboard
  - Suggested: Manually check the dashboard for the presence of the new block after the action.

---

### 5AA(O-004: Confirm selection of an activity

**Coverage:** NONE None
**Modifies State:** course_content_management

**Coverage Gaps:**
- No verification scenarios identified

---

### 5AA(O-005: Create new assignment with all valid inputs

**Coverage:** NONE None
**Modifies State:** course_content_management

**Coverage Gaps:**
- No verification scenarios identified

---

### 5AA(O-006: Create new assignment with 'Save and display'

**Coverage:** NONE None
**Modifies State:** course_content_management

**Coverage Gaps:**
- No verification scenarios identified

---

### 6CS(O-001: Save course settings with all valid inputs

**Coverage:** PARTIAL Partial
**Modifies State:** course_configuration

**1. Verify the course settings are saved and displayed correctly**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 6CS(O-005 (Course start date and end date are the same)
- **Confidence:** 50%
- **Execution Note:** This test case verifies that course settings are saved successfully, but it does not explicitly confirm that all settings are displayed correctly.
- **Reason:** The test case operates on the correct module and confirms that settings are saved, but it focuses on a specific condition (same start and end date) rather than verifying all settings are displayed correctly.
- **Manual Step:** Manually check that all course settings are displayed correctly on the course settings page after saving.

**Coverage Gaps:**
- The test case operates on the correct module and confirms that settings are saved, but it focuses on a specific condition (same start and end date) rather than verifying all settings are displayed correctly.

#### Execution Plan

**1. [ACTION] 6CS(O-001** -- Save course settings with all valid inputs
   > Run 6CS(O-001 — this is the state-changing action being verified

**2. [POST-VERIFY] 6CS(O-005** -- Course start date and end date are the same
   > This test case verifies that course settings are saved successfully, but it does not explicitly confirm that all settings are displayed correctly.
   > Limitation: The test case operates on the correct module and confirms that settings are saved, but it focuses on a specific condition (same start and end date) rather than verifying all settings are displayed correctly.

**Notes:** Execute 6CS(O-001 → then verify with 6CS(O-005

---

### 7.PAR-003: Enroll user with valid username and role

**Coverage:** NONE None
**Modifies State:** enrollment_management

**1. Verify the user is enrolled with the selected role**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on the enrollment process itself, but none verify the outcome by checking the participants list for the new user with the correct role.
- **Manual Step:** Manually check the participants list to confirm the new user is listed with the selected role.

**Coverage Gaps:**
- All candidate test cases focus on the enrollment process itself, but none verify the outcome by checking the participants list for the new user with the correct role.

#### Execution Plan

**1. [ACTION] 7.PAR-003** -- Enroll user with valid username and role
   > Run 7.PAR-003 — this is the state-changing action being verified

**Notes:** Execute 7.PAR-003 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the user is enrolled with the selected role
  - Suggested: Manually check the participants list to confirm the new user is listed with the selected role.

---

### 7.PAR-004: Enroll user with valid email and role

**Coverage:** NONE None
**Modifies State:** enrollment_management

**1. Verify the user is enrolled with the selected role**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on the enrollment process itself and do not include steps to verify the participants list for the new user with the correct role after enrollment.
- **Manual Step:** After enrolling a user, manually check the participants list to confirm the user is listed with the correct role.

**Coverage Gaps:**
- All candidate test cases focus on the enrollment process itself and do not include steps to verify the participants list for the new user with the correct role after enrollment.

#### Execution Plan

**1. [ACTION] 7.PAR-004** -- Enroll user with valid email and role
   > Run 7.PAR-004 — this is the state-changing action being verified

**Notes:** Execute 7.PAR-004 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the user is enrolled with the selected role
  - Suggested: After enrolling a user, manually check the participants list to confirm the user is listed with the correct role.

---

### 7.PAR-008: Enroll user with enrollment duration set

**Coverage:** NONE None
**Modifies State:** enrollment_management

**1. Verify the user is enrolled with the selected role and duration**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on the enrollment process itself and do not include steps to verify the presence of the user in the participants list with the correct role and duration after enrollment.
- **Manual Step:** After enrolling a user, manually check the participants list to confirm the user is listed with the correct role and duration.

**Coverage Gaps:**
- All candidate test cases focus on the enrollment process itself and do not include steps to verify the presence of the user in the participants list with the correct role and duration after enrollment.

#### Execution Plan

**1. [ACTION] 7.PAR-008** -- Enroll user with enrollment duration set
   > Run 7.PAR-008 — this is the state-changing action being verified

**Notes:** Execute 7.PAR-008 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the user is enrolled with the selected role and duration
  - Suggested: After enrolling a user, manually check the participants list to confirm the user is listed with the correct role and duration.

---

### 9AS(O-003: Grade a submission using the Grade button

**Coverage:** NONE None
**Modifies State:** grading

**1. Verify the grade is displayed correctly for the submission**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or display the grade for a submission, which is necessary to confirm the expected outcome in an after_only strategy.
- **Manual Step:** Manually check the submission table to ensure the grade is displayed correctly for the submission.

**2. Verify the grade appears in the Grader report**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or confirm the presence of a specific grade in the Grader report.
- **Manual Step:** Manually check the Grader report to confirm the updated grade is displayed.

**Coverage Gaps:**
- None of the test cases access or display the grade for a submission, which is necessary to confirm the expected outcome in an after_only strategy.
- None of the test cases access or confirm the presence of a specific grade in the Grader report.

#### Execution Plan

**1. [ACTION] 9AS(O-003** -- Grade a submission using the Grade button
   > Run 9AS(O-003 — this is the state-changing action being verified

**Notes:** Execute 9AS(O-003 → Manual verification needed for 2 item(s)

**Manual Verification Required:**
- Verify the grade is displayed correctly for the submission
  - Suggested: Manually check the submission table to ensure the grade is displayed correctly for the submission.
- Verify the grade appears in the Grader report
  - Suggested: Manually check the Grader report to confirm the updated grade is displayed.

---

### 1A(V-001: Submit assignment with online text

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify the page heading 'Activities' is displayed correctly**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate tests focus on verifying specific sections within the Activities page, such as Assignments, Forums, and Resources, but none of them check the page heading.
- **Manual Step:** Manually navigate to the Activities page and verify that the page heading is 'Activities'.

**Coverage Gaps:**
- All candidate tests focus on verifying specific sections within the Activities page, such as Assignments, Forums, and Resources, but none of them check the page heading.

#### Execution Plan

**1. [ACTION] 1A(V-001** -- Verify Activities page heading displays correctly
   > Run 1A(V-001 — this is the state-changing action being verified

**Notes:** Execute 1A(V-001 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the page heading 'Activities' is displayed correctly
  - Suggested: Manually navigate to the Activities page and verify that the page heading is 'Activities'.

---

### 1A(V-002: Submit assignment by uploading files

**Coverage:** PARTIAL Partial
**Modifies State:** work_submission

**1. Verify the Assignments section is displayed on the Activities page**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 1A(V-005 (Verify activity name is displayed in Assignments section)
- **Confidence:** 60%
- **Execution Note:** This test case checks the Assignments section but focuses on activity names. It confirms the presence of the section indirectly by verifying content within it.
- **Reason:** The test case operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the section itself.
- **Manual Step:** Manually verify the presence of the Assignments section on the Activities page.

**Coverage Gaps:**
- The test case operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the section itself.

#### Execution Plan

**1. [ACTION] 1A(V-002** -- Verify Assignments section is displayed
   > Run 1A(V-002 — this is the state-changing action being verified

**2. [POST-VERIFY] 1A(V-005** -- Verify activity name is displayed in Assignments section
   > This test can be adapted to verify the presence of the Assignments section by confirming that it exists before checking for activity names.
   > Limitation: The test operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the Assignments section itself.

**Notes:** Execute 1A(V-002 → then verify with 1A(V-005

---

### 1A(V-004: Edit submission before due date

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify the Resources section is displayed on the Activities page**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate tests focus on different sections (Assignments, Forums) or general page elements (page heading) and do not confirm the presence of the Resources section.
- **Manual Step:** Manually navigate to the Activities page in the Student View and check for the presence of the Resources section.

**Coverage Gaps:**
- All candidate tests focus on different sections (Assignments, Forums) or general page elements (page heading) and do not confirm the presence of the Resources section.

#### Execution Plan

**1. [ACTION] 1A(V-004** -- Verify Resources section is displayed
   > Run 1A(V-004 — this is the state-changing action being verified

**Notes:** Execute 1A(V-004 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the Resources section is displayed on the Activities page
  - Suggested: Manually check the Activities page to confirm the Resources section is displayed.

---

### 1A(V-005: Remove submission before due date

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify each activity in the Assignments section has a name displayed**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases check for the presence of activity names in the Assignments section. They focus on due dates, submission status, or the presence of the section itself.
- **Manual Step:** Manually verify that each activity in the Assignments section has a name displayed by checking the Activities page in the Student View.

**Coverage Gaps:**
- None of the test cases check for the presence of activity names in the Assignments section. They focus on due dates, submission status, or the presence of the section itself.

#### Execution Plan

**1. [ACTION] 1A(V-005** -- Verify activity name is displayed in Assignments section
   > Run 1A(V-005 — this is the state-changing action being verified

**Notes:** Execute 1A(V-005 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify each activity in the Assignments section has a name displayed
  - Suggested: Manually navigate to the Assignments section in the Activities module and verify that each activity has a name displayed.

---

### 1G/GR(-001: Save changes with valid data in all fields

**Coverage:** NONE None
**Modifies State:** grade_management

**1. Verify changes are reflected in the Grader report**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases confirm changes in the Grader report. They only check for the presence of UI elements.
- **Manual Step:** Manually check the Grader report to ensure that the expected changes are visible and correctly reflected.

**Coverage Gaps:**
- None of the test cases confirm changes in the Grader report. They only check for the presence of UI elements.

#### Execution Plan

**1. [ACTION] 1G/GR(-001** -- Save changes with valid data in all fields
   > Run 1G/GR(-001 — this is the state-changing action being verified

**Notes:** Execute 1G/GR(-001 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify changes are reflected in the Grader report
  - Suggested: Manually check the Grader report to ensure that the expected changes are visible and correctly reflected.

---

### 1A(V-001: Verify Activities page heading displays correctly

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify the page heading 'Activities' is displayed correctly**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on verifying the presence of specific sections (Assignments, Forums, Resources) within the Activities module, but none check the page heading itself.
- **Manual Step:** Manually navigate to the Activities page and verify that the page heading is 'Activities'.

**Coverage Gaps:**
- All candidate test cases focus on verifying the presence of specific sections (Assignments, Forums, Resources) within the Activities module, but none check the page heading itself.

#### Execution Plan

**1. [ACTION] 1A(V-001** -- Verify Activities page heading displays correctly
   > Run 1A(V-001 — this is the state-changing action being verified

**Notes:** Execute 1A(V-001 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the page heading 'Activities' is displayed correctly
  - Suggested: Manually navigate to the Activities page and verify that the page heading is 'Activities'.

---

### 1A(V-002: Verify Assignments section is displayed

**Coverage:** PARTIAL Partial
**Modifies State:** work_submission

**1. Verify the Assignments section is displayed on the Activities page**

- **Status:** PARTIAL partial
- **Strategy:** After Only
- **Matched Test:** 1A(V-005 (Verify activity name is displayed in Assignments section)
- **Confidence:** 60%
- **Execution Note:** This test can be adapted to verify the presence of the Assignments section by confirming that it exists before checking for activity names.
- **Reason:** The test operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the Assignments section itself.
- **Manual Step:** Manually verify the presence of the Assignments section on the Activities page.

**Coverage Gaps:**
- The test operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the Assignments section itself.

#### Execution Plan

**1. [ACTION] 1A(V-002** -- Verify Assignments section is displayed
   > Run 1A(V-002 — this is the state-changing action being verified

**2. [POST-VERIFY] 1A(V-005** -- Verify activity name is displayed in Assignments section
   > This test can be adapted to verify the presence of the Assignments section by confirming that it exists before checking for activity names.
   > Limitation: The test operates on the correct module and accesses the Assignments section, but it does not explicitly confirm the presence of the Assignments section itself.

**Notes:** Execute 1A(V-002 → then verify with 1A(V-005

---

### 1A(V-004: Verify Resources section is displayed

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify the Resources section is displayed on the Activities page**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** All candidate test cases focus on different sections or elements of the Activities page and do not address the Resources section.
- **Manual Step:** Manually check the Activities page to confirm the Resources section is displayed.

**Coverage Gaps:**
- All candidate test cases focus on different sections or elements of the Activities page and do not address the Resources section.

#### Execution Plan

**1. [ACTION] 1A(V-004** -- Verify Resources section is displayed
   > Run 1A(V-004 — this is the state-changing action being verified

**Notes:** Execute 1A(V-004 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the Resources section is displayed on the Activities page
  - Suggested: Manually check the Activities page to confirm the Resources section is displayed.

---

### 1A(V-005: Verify activity name is displayed in Assignments section

**Coverage:** NONE None
**Modifies State:** work_submission

**1. Verify each activity in the Assignments section has a name displayed**

- **Status:** MISSING not_found
- **Strategy:** After Only
- **Matched Test:** -
- **Confidence:** -
- **Reason:** None of the test cases access or display the activity names in the Assignments section. They focus on due dates, submission status, and the presence of the Assignments section itself.
- **Manual Step:** Manually navigate to the Assignments section in the Activities module and verify that each activity has a name displayed.

**Coverage Gaps:**
- None of the test cases access or display the activity names in the Assignments section. They focus on due dates, submission status, and the presence of the Assignments section itself.

#### Execution Plan

**1. [ACTION] 1A(V-005** -- Verify activity name is displayed in Assignments section
   > Run 1A(V-005 — this is the state-changing action being verified

**Notes:** Execute 1A(V-005 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify each activity in the Assignments section has a name displayed
  - Suggested: Manually navigate to the Assignments section in the Activities module and verify that each activity has a name displayed.

---

### 15.PRO-001: Update profile with valid first name, last name, and email

**Coverage:** FULL Full
**Modifies State:** profile_update

**1. Verify the profile details are updated with the new first name, last name, and email**

- **Status:** FOUND found
- **Strategy:** Before/After
- **Matched Test:** 15.PRO-002 (Verify profile fields are displayed correctly)
- **Confidence:** 90%
- **Before Action:** Record the current first name, last name, and email before the update
- **After Action:** Compare the profile details and confirm they match the new inputs
- **Execution Note:** Use this test to display the profile fields before and after the update. It verifies the presence of the first name, last name, and email fields, which allows for observation of the data.

#### Execution Plan

> **Strategy:** Run verification tests BEFORE and AFTER the action to compare values.

**1. [PRE-VERIFY] 15.PRO-002** -- Verify profile fields are displayed correctly
   > Run 15.PRO-002 and RECORD the current values before the action

**2. [ACTION] 15.PRO-001** -- Update profile with valid first name, last name, and email
   > Run 15.PRO-001 — this is the state-changing action being verified

**3. [POST-VERIFY] 15.PRO-002** -- Verify profile fields are displayed correctly
   > Run 15.PRO-002 AGAIN and COMPARE with baseline values recorded in pre-verify

**Notes:** PRE: Record baseline with 15.PRO-002 → ACTION: Execute 15.PRO-001 → POST: Verify with 15.PRO-002 (compare against baseline)

---

### 15.PRO-003: Update profile with valid picture upload

**Coverage:** NONE None
**Modifies State:** profile_update

**1. Verify the profile picture is updated successfully**

- **Status:** MISSING not_found
- **Strategy:** Before/After
- **Matched Test:** -
- **Confidence:** -
- **Before Action:** Record the current profile picture before the update
- **After Action:** Compare the profile picture and confirm it matches the uploaded file
- **Reason:** None of the test cases access or display the profile picture, which is necessary for the before_after strategy to observe the data.
- **Manual Step:** Manually navigate to the profile page and verify the profile picture is displayed correctly before and after the update.

**Coverage Gaps:**
- None of the test cases access or display the profile picture, which is necessary for the before_after strategy to observe the data.

#### Execution Plan

**1. [ACTION] 15.PRO-003** -- Update profile with valid picture upload
   > Run 15.PRO-003 — this is the state-changing action being verified

**Notes:** Execute 15.PRO-003 → Manual verification needed for 1 item(s)

**Manual Verification Required:**
- Verify the profile picture is updated successfully
  - Suggested: Manually navigate to the profile page and verify the profile picture is displayed correctly before and after the update.

---

## Navigation Graph

![Navigation Graph](output/moodle/navigation_graph.png)

### Pages

| Module | URL | Auth Required | Test Cases |
|--------|-----|---------------|------------|
| 1. Login | /login | No | 8 |
| 2. Dashboard | /dashboard | Yes | 15 |
| 3. My Courses | /my-courses | Yes | 12 |
| 4. Course Page | /course | Yes | 21 |
| 5. Adding Activities (Teacher Only) | /course/activities | Yes | 19 |
| 6. Course Settings (Teacher Only) | /course/settings | Yes | 6 |
| 7. Participants | /course/participants | Yes | 17 |
| 8. Assignment (Teacher View) | /course/assignment | Yes | 18 |
| 9. Assignment Submissions (Teacher Only) | /course/assignment/submissions | Yes | 11 |
| 10. Assignment (Student View) | /course/assignment | Yes | 9 |
| 11. Advanced Grading (Teacher Only) | /course/assignment/advanced-grading | Yes | 4 |
| 12. Gradebook / Grader Report (Teacher Only) | /course/gradebook | Yes | 17 |
| 13. Grades / User Report (Student View) | /grades | Yes | 5 |
| 14. Activities (Student View) | /course/activities | Yes | 8 |
| 15. Profile | /profile | Yes | 10 |
