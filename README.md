# Django Essential Training
This is the repository for the LinkedIn Learning course Django Essential Training. The full course is available from [LinkedIn Learning][lil-course-url].

![Django Essential Training][lil-thumbnail-url] 

Django is a robust and powerful framework with a lot of moving parts. Although starting a new project can be quite easy, there is a lot to uncover. This course teaches fundamentals, such as what a framework is, what an HTTP request is, and how Django replies to HTTP requests. Software developer and podcaster Leticia Portella walks you through each step of building a working system that can create, edit, and list books per user with an authentication system. Topics include getting started, creating users and data, ORMs, creating a dynamic template, Django class-based files and static views, and so much more!

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Installing
1. To use these exercise files, you must have the following installed:
	- [list of requirements for course]
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.
3. [Course-specific instructions]


### Instructor

Leticia Portella 
                            


                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/leticia-portella).

[lil-course-url]: https://www.linkedin.com/learning/django-essential-training
[lil-thumbnail-url]: https://cdn.lynda.com/course/2894047/2894047-1632244073199-16x9.jpg
