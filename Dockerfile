FROM ubuntu:14.04
MAINTAINER  pat claffey patclaffey@gmail.com

# this image runs jupyter notebook with Python 3.4
# jupyter uses latest notebook document version 4.0

#do NOT inlcude ipython3 in the image as ipython3 can conflict

#also installs
#     pip3 (python3 installer) 
#     matplotlib (for visualization and graphics),
#     pandas (for data analysis)
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y python3-matplotlib && apt-get install -y python3-pandas 

#using pip3 to install jupyter
RUN pip3 install jupyter

#jupyter needs to run in public mode over ssl.  Required are:
#      a jupyter config file 
#      and also a public key file
ADD ${PWD}/mycert.pem  ${PWD}/jupyter_notebook_config.py  /opt/notebook/ 

EXPOSE 8888

ENTRYPOINT jupyter notebook --config=/opt/notebook/jupyter_notebook_config.py --notebook-dir=/opt/notebook/notebooks/
