# Tweeter (A Twitter Clone)

## Author

David Alvarado

## Description

This is a social website called Tweeter that will allow users to
be able to make posts called Twits that other users can view.
Users of the site will be able to make Twits that contain both text and
pictures via a URL field to a picture. Users can also like and unlike Twits that
other users make. As with all the assignments thus far, all views should be Class-Based Views.
In short, there should be a lot of similarity with what we did with in-class-4.

Installing `requirements.txt` is a required package.

The program allows the following functionality:

1. A Custom User model that adds a date of birth field.
2. Full user authentication so that only authenticated users can use the site.
3. Sign up and authentication forms / views so that users can authenticate with the system.
4. Ability for users to be able to change and reset their password.
5. A private profile page where a user can update details about themselves. (username, fname, lname, email, date of birth)
6. A Dashboard for each user that will show all the Twits in the system listed with the most recent ones first.
7. Pages / forms to be able to CUD a Twit. Update and Delete should be limited to the person that made the twit.
8. New Twits should allow both text and URL for a picture. Image URL can then be used with a img tag to render the image.
9. A Public Profile page for each user that shows all the Twits for that user.
10. Ability for users to like or unlike a particular Twit that someone has made using AJAX.
11. Ability for users to add a comment on Twits. This will only be create functionality. 
12. Tests to verify all functionality.


### Database Requirements
Here are the requirements for the database in an ERD. There are other authentication related tables that I did not include but are provided via Django's auth system. The Users table is the only one that really needed to be shown since there are so many relations between Users and our other tables. There are no relations between the other authentication tables and our tables, which is why I omitted them.

NOTE: For the URL field on the Twit model, I am not using an ImageField. Those are extremely hard to properly set up. Instead, I am are simply loading images via a URLField. Meaning that the user will provide a URL to an image that already exists on the internet.

![Database Entity Relationship Diagram](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_erd.png "Database Entity Relationship Diagram")

### Screenshots

Here are some images of the non-admin pages that I made. This is more or less to give you an idea as to what the general concept is in case the written description is not clear. 

#### Sign Up
![Sign Up](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_sign_up.png "Sign Up")

#### Login
![Login](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_login.png "Login")

#### Forgot Password
![Forgot Password](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_forgot_password.png "Forgot Password")

#### Dashboard
![Dashboard](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_feed.png "Dashboard")

#### Private Profile
![Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_personal_profile.png "Profile")

#### Public Profile
![Public Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_public_profile.png "Public Profile")

#### Twit Create
![Twit Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_add.png "Twit Creation")

#### Twit Edit
![Twit Edit](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_edit.png "Twit Update")

#### Twit Delete
![Twit Delete](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_delete.png "Twit Delete")

#### Comment Add
![Comment Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_comment_add.png "Comment Creation")


### Notes
All Views are Class-Based Views.

Any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all available Bootstrap examples here:

https://getbootstrap.com/docs/5.3/examples/

In addition, you can find the documentation for Bootstrap here:

https://getbootstrap.com/docs/5.3/getting-started/introduction/

# Quick Features Recap
 Features                                    
---------------------------------------------
 Models match ERD                            
 Custom User Model                          
 Full User Sign Up / Authentication        
 Password change / reset functionality       
 Personal Profile page. Update personal info 
 Public Profile page. Twits from one user.   
 Dashboard feed of Twits from all users      
 CUD Twit                                    
 Allowing Text and Picture URL in Twit       
 Liking / Unliking a Twit                    
 New Comment Form / Functionality            
 Navigation between pages                    
 Crispy Forms                                
 Styling / Bootstrap                         
 Automated Tests                             
 Heroku Deployment Files and Settings                                             


## Known Problems, Issues, And/Or Errors in the Program

Im aware of the following problems:

    Profile (Save Changes Button) ---- Now working as intended, but stills fetches the data?

    Password Reset (I wasn't able to use the email backend correctly, but still had the all password reset pages)

    (Liking a twit without login in shows a error)

    2 of my test don't pass really don't know why.