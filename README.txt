NEW PROJECT:

Open terminal
To set up virtual environment directory: run the command python -m venv {enter enviornment name}
To activate the virtual environment, cd into the environment directory that was created. Then run
the command ".\Scripts\activate"
To deactivate, simply type deactivate

(Only necessary when installing new packages, but even then once your vs code connects
to your interpreter(below) you wont need to activate/deactivate anymore)


To set up interpreter: ctrl+shift+p and search for Python: Select interpreter
select the virutal environment you created. Now when you run python files they should run 
with the proper packages.

To view packages run pip list

To create a requirements.txt file, run pip freeze > requirements.txt in the terminal.
The requirements.txt file shows others the necessary packages for the project, and makes
it easy for them to install them all.

To run a python file, click the play button drop down in the top right and click run with python

If you want to upload your new project to a gitub repository...

Make sure you have a .gitignore file created so that you ignore the folders/files mentioned above
To initiailize the repository run the "git init" command
Source control on the left will now show the files that need to be commited.
Commit them all, add a message, and click commit + push.
You can either create the repo on github, and paste the link, or you can create it in vscode by following along




EXISTING PROJECT:

Once the project is pulled from github or another repository, create a virtual environment (above).
Run the command pip install -r requirements.txt. This installs the necessary packages (remember when we generated one of these files above)
Create a branch in github, and change to your created branch (bottom left, probably says main or master to begin). 
This way if you make any changes, they do not immediately change the main files until necessary.
Once you make changes to files, youll see them appear on the source control on the left.
Once you are ready to push the changes, make sure they are selected, add a message, and commit + push.


WHEN PUSHING CODE:

Do NOT git push your created virtul environment folder
Do not push any .env files





