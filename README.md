# Multi User Blog
This project creates a blog site where users can register themselves and are able to create new posts, read other people's posts, comment and like them.

### Contents
Included in this release are the following folders and files:
* main.py: File that maps handlers with URLs.
* static folder: Contains a CSS file with the styles applied to the HTML files.
* templates folder: Contains the HTML files.
* views folder: Contains the base and specific handlers.
* models folder: Contains three model classes for entities used in the blog: users, posts and comments.
* utils folder: Contains a module with utility functions.

### Requirements
* Web Browser (tested on Safari and Chrome)
* Python >= 2.7
* Google Cloud SDK >= 137.0.1
* jinja >= 2.6

### Usage
* To run the program locally, open a terminal and run these commands:

```bash
cd <path_to_project_folder>
gcloud init
dev_appserver.py .
```
The output should tell you where the Starting module "default" is running at. Write the address in your browser follwed by "/blog" to look at the web output of the application.

example: http://localhost:8080/blog

* To open it externally visit the following URL:
https://dianas-blog.appspot.com/blog

### Author
Diana Gonzalez
