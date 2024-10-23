This repo was created for a friend of mine in data analysis, in order for him to get him started with version control and python virtual environment management.

(Use vs code)

NEW PROJECT:

Open terminal, navigate to the folder you'd like your project to live in.
Create an app.py file in the directory.
To set up virtual environment directory: 
run the command python -m venv {enter enviornment name} to set up your virtual environment.
Then, ctrl+shift+p and search for Python: Select interpreter.
Select the virutal environment you created. Doing so will allow your IDE to automatically actiavate and use your venv
To install any packages, use the command pip i {package name} in the terminal

To view any installed packages, run the command pip list

To create a requirements.txt file, run the command pip freeze > requirements.txt in the terminal.
The requirements.txt file takes all of your installed packages and places them in a single txt file.
This will help to show others the necessary packages for your project, and make it easy for them to be installed.

To run a python file, navigate to the app.py file, click the play button drop down in the top right and click run with python.


If you want to upload your new project to a gitub repository...

To initiailize the repository run the "git init" command
Source control on the left will now show the files that need to be commited.
Commit them all, add a message, and click commit + push.
You can either create the repo on github, and paste the link, or you can create it in vscode by following along


EXISTING PROJECT:

Once the project is pulled from github or another repository, create a virtual environment (above).
You dont need to cd to into the environment to run the command.
Run the command pip install -r requirements.txt. This installs the necessary packages (remember when we generated one of these files above)
Create a branch in github, and change to your created branch (bottom left, probably says main or master to begin). 
This way if you make any changes, they do not immediately change the main files until necessary.
Once you make changes to files, youll see them appear on the source control on the left.
Once you are ready to push the changes, make sure they are selected, add a message, and commit + push.


WHEN PUSHING CODE:

Do NOT git push your created virtul environment folder
Do not push any .env files





