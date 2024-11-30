## Manual Test Cases

**Functional Testing**
1. Verify login with valid credentials.
2. Verify login with invalid credentials.
3. Verify creation of a new repository through the UI.
4. Verify navigation between repository tabs (Code, Issues, Pull Requests, Actions).
5. Verify creation of an issue in a repository.
6. Verify creation of a pull request between two branches.
7. Verify merging of a pull request with no conflicts.
8. Verify repository deletion via the GitHub interface.
9. Verify editing repository details (e.g., description, visibility).

**API Testing**
1. Verify repository creation using API.
2. Verify issue creation using API.
3. Verify pull request creation using API.
4. Verify updating issue details using API.
5. Verify fetching repository details using API.
6. Verify error handling for invalid API tokens.
7. Verify response for non-existent repositories using API.
8. Verify the list of repositories for a given user using API.
 
**Non-Functional Testing**
1. Verify github login/repo access/switching tabs behavior under different network conditions (slow, intermittent).
2. Verify github login/repo access/switching tabs across browsers (Chrome, Firefox).
3. Verifygithub login/repo access/switching tabs across devices (desktop, mobile).
4. Verify responsiveness of GitHub interface on different screen resolutions.
5. Verify the time taken to load the dashboard after login.
6. Verify accessibility features (e.g., keyboard navigation, screen readers).
 
**Stress and Performance Testing**
1. Verify application behavior with a high number of concurrent logins.
2. Verify repository creation with a high frequency of requests.
3. Verify application performance when loading a repository with a large number of issues.
4. Verify pull request creation under heavy server load.
5. Verify API response time for large payloads.
6. Verify API rate limit handling when exceeding request thresholds.
7. Verify the UI behavior when thousands of repositories are created and listed.
8. Verify API response under a high number of concurrent requests.
9. Verify handling of repositories with exceptionally long names or descriptions. 
