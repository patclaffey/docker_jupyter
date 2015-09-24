# Jupyter Notebook in a Docker Container
This project installs and runs Jupyter Notebook with Python 3.4 in a Docker container.  Also installed are the Python matplotlib and pandas packages for data visualization and analysis. 
A sample data set and Notebook is to provided to verify the install - and to demo the use of Jupyter for data analysis.

Jupyter in a container must run in public mode over an SSL connection - even on a private network.
This complicates the Jupyter setup because the Docker impage must contain a public key file.
Also a logon password needs to be defined in the Jupyter configuration file.


## Pre-requisites.

1.0  Docker must be installed on your system


## Software Installation Steps

1.0	Download the project from GitHub and install in your project directory
2.0	Add public key file called mycert.pem to the project directory
3.0     Create the project docker image
4.0	Create and run the Docker Container
5.0	Logon to Jupyter and view the sample notebook


### Clone repository
Download the software from GitHub into a project directory.  The project directory will look like this:

Project Directory
--- Dockerfile  the Docker file that defines the Jupyter image.
                For this project the image is named jupyter_notebook_image
--- mycert.pem  you need to add this file manually - not part of download 
		See next section for info on generating
		your own public key with this file name
--- jupyter_notebook_config.py  Jupyter configuration file
                  This file contains custom setups as Jupyter must use SSL 
--- build_jupyter_image.sh     shell script to build docker image
--- run_jupyter_container.sh   shell script to create and run docker container
--- data   the data file directory
    ---  csv   csv is a directory under the data sub-directory
         ---   activity_speed.csv  this csv contains the sample data
--- notebooks  sub-directory under Project Directory to hold notebook documents
    --- activity speed analysis.ipynb   this is a sample jupyter notebook


### Add public key file to Project Directory
If you have a public key file named mycert.pem then just copy it to project directory.  If not you need to generate your own public key file with this name.

### Build the Docker image for Jupyter
from the project directory execute the following script:
./build_jupyter_image.sh
Use "docker image" command to verify image named jupyter_image has been created successfully 


### Run the Docker Container
from the project directory execute the following script:
./run_jupyter_container.sh
Use "docker ps" command to verify contaner named jupyter_container is running.
 
### Logon to Jupyter Notebook
Go to the url https://127.0.0.1:8888 to logon to Jupyter (note this is https and not http).
The password is "password" (all lowercase letters, do not type quotes). 
Contents of Config File
You should see the sample notebook called "activity speed analysis".  You can open this notebook and make any changes you wish.


 
                
