# Jupyter Notebook with Pandas in a Docker Container
Install and run Jupyter Notebook, Python 3.4 with Pandas in a Docker container. Python pandas package is installed for data analysis and matplotlib for data visualization. 
A sample data set and notebook is provided to verify the install - and to demo the use of Jupyter for data analysis.

Jupyter in a container must run in public mode over an SSL connection - even on a private network.
This complicates the Jupyter setup requiring a public key file,
and also a Jupyter configuration file to define a logon password.


## Pre-requisites.

Docker must be installed on your system

To avoid having to use `sudo` with the `docker` command, add your user to the docker group as follows:
```
sudo usermod -aG docker user_name
```

If running on a public network ensure firewall is open so that port 8888 can accept inbound requests

## Software Installation Steps

- clone this GitHub repository
- generate public key file named mycert.pem 
- load docker image `patclaffey/jupyter_pandas:v2` from Docker Hub
- create the Docker Container
- logon to Jupyter and view the sample notebook


### Clone this GitHub repository
```
git clone git@github.com:patclaffey/docker_jupyter.git
```
Afer cloning this repository (and adding mycert.pem as per next section) the docker_jupyter project directory should look like this:

```
docker_jupyter        - this is the project directory
--- Dockerfile  the Docker file to define the project Docker image.
--- build_jupyter_image.sh     shell script to build docker image
--- run_jupyter_container.sh   shell script to create docker container
--- config    - sub-directory to hold configuration files
    --- mycert.pem  you need to add this file manually - not part of download 
		See next section for info on generating
		your own public key with this file name
    --- jupyter_notebook_config.py  Jupyter configuration file
                  This file contains custom setups as Jupyter must use SSL 
--- data   the data file directory
    ---  csv   csv is a directory under the data sub-directory
         ---   activity_speed.csv  this csv contains the sample data
--- notebooks  sub-directory under Project Directory to hold notebook documents
    --- speed.ipynb   this is a sample jupyter notebook
```

### Generate public key file and add to /config sub-directory

A self-signed certificate can be generated with openssl. For example, the following command will create a certificate valid for 365 days with both the key and certificate data written to the same file:
```
$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
```
When running above command accept all defaults. 
Add the my_cert.pem file to the /config directory.

### Load the Docker image for Docker Hub 
```
docker load patclaffey/jupyter_pandas:v2
```

### Create Docker container
from the project directory execute the following script:
```
./run_jupyter_container.sh
```
Use `docker ps` command to verify contaner named jupyter_container is running.
 
### Logon to Jupyter Notebook
Go to https://your_public_IP_Address:8888 to logon to Jupyter (note this is https and not http).  On a PC the address is usually https://127.0.0.1:8888, however on a public network it will be the public IP or DNS address.

Your browser will warn you of a dangerous certificate because it is self-signed. Ignore this warning and go to Jupyter logon screen. 
The login password is "password" (all lowercase letters, do not type quotes). 
You should see the sample notebook called "speed".  You can open this notebook and make any changes you wish.

