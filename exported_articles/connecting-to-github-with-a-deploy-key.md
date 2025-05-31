# Connecting to Github with a Deploy Key

Creating a Deploy Key
=====================


In Zenlytic, you'll first go into Settings, then Workspace Settings



![](images/Screenshot+2023-02-03+at+2.39.21+PM.png)Next, find your git repo details (these will be in Github). 



Make sure to use the "SSH" format of the git URL. The format looks like `git@github.com:<YOUR_ORGANIZATION>/<YOUR_REPO>.git`, and you can find it here in your Github repo under the "Code" button with the SSH tab as shown below.



![](images/Screenshot+2023-02-03+at+2.42.06+PM.png)Now that you have that URL and the branch you want to use as your production branch, return to Zenlytic. In this example, we pasted our Github repo url (SSH format) and our production branch, which was: `master`.



![](images/Screenshot+2023-02-03+at+2.45.00+PM.png)Next we need to generate the SSH key we'll use to connect. Hit the "Generate Deploy Key" button, then the "Confirm" button, and copy the public SSH key generated.



![](images/Screenshot+2023-02-03+at+2.46.57+PM.png)Then hit Copy Deploy Key.



![](images/Screenshot+2023-02-03+at+2.48.04+PM.png)Now that you have the deploy key copied return to Github and go to "Settings."



![](images/Screenshot+2023-02-03+at+2.49.12+PM.png)Then go to Deploy Keys in the left-hand menu.



![](images/Screenshot+2023-02-03+at+2.49.25+PM.png)Then, click "Add new" and give your deploy key a name. Finally, paste that SSH key and click "Add Key." 



![](images/Screenshot+2023-02-03+at+2.49.50+PM.png)Then click "Save" in the Zenlytic UI. If this saves without an error, you can close the window. You're fully connected to Github!



![](images/Screenshot+2023-02-03+at+2.53.04+PM.png)


