
# Testing

## Contents

- [Testing](#testing)
  - [Contents](#contents)
  - [Code Style and Quality](#code-style-and-quality)
    - [Python Enhancement Proposal (PEP8)](#python-enhancement-proposal-pep8)
    - [HTML Validation tests](#html-validation-tests)
    - [CSS validation was done using W3C CSS Validator](#css-validation-was-done-using-w3c-css-validator)
  - [Lighthouse tests results:](#lighthouse-tests-results)
  - [Responsiveness test:](#responsiveness-test)
  - [Testing User Stories](#testing-user-stories)
    - [New Visitors Goals](#new-visitors-goals)
    - [Existing Visitors Goals](#existing-visitors-goals)
  - [Full Testing](#full-testing)
  - [Back to README](#back-to-readme)

___

## Code Style and Quality

### Python Enhancement Proposal (PEP8)

PEP8 outlines the conventions for writing clean, readable, and maintainable Python code. Adhering to these guidelines helps ensure that the codebase remains consistent and understandable for all contributors.
All Python code in this project has been checked and verified for adherence to the PEP8 style guide using the extension [Flake8](https://flake8.pycqa.org/en/latest/) on [VSCode](https://code.visualstudio.com/) and double checked using the [CI PEP8 linter](https://pep8ci.herokuapp.com/).


### HTML Validation tests

HTML Validation tests were performed using the [W3C Markup validation service](https://validator.w3.org/#validate_by_uri):

- [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2F)
- [Posts All Categories](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2F)
- [Post Specific Category - Pregnancy and Birth](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fpregnancy-and-birth%2F)
- [Post Specific Category - Parenting Advice](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fparenting-advice%2F)
- [Post Specific Category - Nutrition](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fnutrition%2F)
- [Post Specific Category - Education and Development](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Feducation-and-development%2F)
- [Post Specific Category - Cultural Traditions](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fcultural-traditions%2F)
- [Post Specific Category - Bullying](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fbullying%2F)
- [Post Specific Category - Childcare](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fchildcare%2F)
- [Post Specific Category - Legal and Administrative Processes](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Flegal-and-administrative-processes%2F)
- [Post Specific Category - Healthcare](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fcategory%2Fhealthcare%2F)
- [Post Detail - Specific Post](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fposts%2Fdo-pregnant-women-and-new-mothers-need-a-hebamme-exploring-the-role-of-midwives-in-germany%2F)
- [About page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fabout%2F)
- [Events page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fevents%2F)
- [Useful links](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Fuseful_links%2F)
- [Login page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Faccounts%2Flogin%2F)
- [Signup page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Faccounts%2Fsignup%2F)
- [Logout page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2Faccounts%2Flogout%2F)

**Notes**
 - All 7 pages of Posts (All Categories) were tested. I only included the results of page 1 here for illustration purpose.

 - All 37 posts were individually tested, I have only included the result for the test on the "Do Pregnant Women and New Mothers Need a Hebamme? Exploring the Role of Midwives in Germany" here for illustration purpose.

 - All pages with authenticated user and page 404 were tested by pasting the source code from the rendered page and also passed with no error nor warnings.

___

### CSS validation was done using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- [CSS validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fparenting-in-munich-site-527d6bb8b97c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enn)

___

## Lighthouse tests results:

Performance, accessibility, SEO, and best practices were evaluated using Google's Lighthouse tool. The results for each page are included below. Results with a white background represent mobile audits, while those with a black background represent desktop audits.

- black background: desktop
- white background: mobile


- Homepage:

![Homepage desktop](documentation/lighthouse-tests/lh-homepage-desktop.png)
![Homepage mobile](documentation/lighthouse-tests/lh-homepage-mobile.png)

- Posts - All categories page:

![Posts page desktop](documentation/lighthouse-tests/lh-posts-desktop.png)
![Posts page mobile](documentation/lighthouse-tests/lh-posts-mobile.png)

- Post - Category specific page:

![Posts categories page desktop](documentation/lighthouse-tests/lh-category-desktop.png)
![Posts categories page mobile](documentation/lighthouse-tests/lh-category-mobile.png)

- Post detail page:

![Posts detail desktop](documentation/lighthouse-tests/lh-post_detail-desktop.png)
![Posts detail mobile](documentation/lighthouse-tests/lh-post_detail-mobile.png)

- About page:

![About page desktop](documentation/lighthouse-tests/lh-about-desktop.png)
![About page mobile](documentation/lighthouse-tests/lh-about-mobile.png)

- Events page:

![Events desktop](documentation/lighthouse-tests/lh-events-desktop.png)
![Events mobile](documentation/lighthouse-tests/lh-events-mobile.png)

- Events restricted area page:

![Events restricted area desktop](documentation/lighthouse-tests/lh-events-restricted-desktop.png)
![Events restricted area mobile](documentation/lighthouse-tests/lh-events-restricted-mobile.png)

- Useful links page:

![Useful links desktop](documentation/lighthouse-tests/lh-useful-links-desktop.png)
![Useful links mobile](documentation/lighthouse-tests/lh-useful-links-mobile.png)

- Signup page:

![Signup page desktop](documentation/lighthouse-tests/lh-signup-desktop.png)
![Signup page mobile](documentation/lighthouse-tests/lh-signup-mobile.png)

- Login page:

![Login page desktop](documentation/lighthouse-tests/lh-login-desktop.png)
![Login page  mobile](documentation/lighthouse-tests/lh-login-mobile.png)

- User Profile page:

![User Profile page desktop](documentation/lighthouse-tests/lh-useful-links-desktop.png)
![User Profile page mobile](documentation/lighthouse-tests/lh-user-profile-mobile.png)

- Profile Update page:

![Profile update page desktop](documentation/lighthouse-tests/lh-profile-update-desktop.png)
![Profile update page mobile](documentation/lighthouse-tests/lh-profile-update-mobile.png)

- Logout page:

![Logout page desktop](documentation/lighthouse-tests/lh-logout-desktop.png)
![Logout page mobile](documentation/lighthouse-tests/lh-logout-mobile.png)

--- 

## Responsiveness test:

The resposiveness amongts different devices was checked using [Am I Responsive](https://ui.dev/amiresponsive).
To perform the testing, it was necessary to adjust the `X_FRAME_OPTIONS` to `ALLOWALL` temporarily on settings.py and change back to `SAMEORIGIN` as soon as the test was finished for security reasons.

- Homepage:

![Homepage](documentation/amiresponsive/responsive-home.png)


- Posts page:

![Posts page](documentation/amiresponsive/responsive-posts-all.png)


- Post category page:

![Posts detail](documentation/amiresponsive/responsive-posts-category.png)


- Post detail page:

![Posts detail](documentation/amiresponsive/responsive-post-detail.png)


- About page:

![About page](documentation/amiresponsive/responsive-about.png)


- Events restricted area page:

![Events restricted area](documentation/amiresponsive/responsive-events-restricted.png)


- Useful links page:

![Useful links](documentation/amiresponsive/responsive-links.png)


- Signup page:

![Signup page](documentation/amiresponsive/responsive-signup.png)


- Login page:

![Login page](documentation/amiresponsive/responsive-login.png)


- Site rules page:

![Site rules page](documentation/amiresponsive/responsive-site-rules.png)


* The Events, User Profile, Profile Update and Logout pages could not be tested on the website because the login doesn't work during the testing, but they were manually tested in different devices and are responsive as well.

___

## Testing User Stories

### New Visitors Goals

As a new visitor, I expect to:

**Easily navigate the website**
  - The navigation menu includes links to all sections of the website, including a dropdown for categories under "Posts" and a search engine, present in the navbar on the posts section.

**Quickly understand the website's purpose and target audience**
  - There is an About page with clear information about the website's purpose and target audience.

**Sign up and access exclusive content effortlessly**
  - Visitors can sign up using the navbar link, and upon creating their accounts, they have immediate access to content exclusive to registered members.

**Easily find and read the website policies**
  - The link for the website policies can be easily found in the footer of all webpages as well as on the signup page.

**Contact the website moderators without difficulty**
  - There is a "Contact Us" section on the About page and a link in the footer of all webpages that directs the user straight to the "Contact Us" section. In this section, the visitor can send a message by entering their name and email.


### Existing Visitors Goals

As a user, I expect to:
**Manage my profile information, including my bio and profile picture, to keep my account current**
  - Users can easily manage their information, including email, bio, profile picture, and location, by clicking the Edit button on their profile page.

**Connect with other parents through comments on posts to share experiences and seek advice**
  - Users can leave comments on posts and click on the usernames of other commenters to view their information, including their email (if they have chosen to display it publicly).

**Edit and delete my comments as needed**
  - Users have access to all comments they have left on the website from their profile page. They can click on a comment to be redirected to the respective post and comment, where they can edit or delete their comments as desired.

**Access exclusive content offered by the website, such as information on local events**
  - Registered users can view all events published on the events page.

**Permanently terminate my account if I choose to**
  - Users can permanently delete their accounts at any time by clicking the Delete button on their profile page.

___

## Full Testing


___

## Back to README

Go [Back to README](README.md)

___