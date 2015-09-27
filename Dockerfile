FROM ubuntu:14.04
MAINTAINER  pat claffey patclaffey@gmail.com

# this image runs jupyter notebook with Python 3.4
# jupyter uses notebook document version 4.0 (latest)

# also installs
#     pip3 (python3 installer) 
#     matplotlib (for visualization and graphics),
#     pandas (for data analysis)

# do NOT inlcude ipython3 in the image as it may conflict with jupyter
# Python 3.4 is pre-installed on ubuntu image

RUN apt-get update && \
	apt-get install -y python3-pip && \
	apt-get install -y python3-matplotlib && \
	apt-get install -y python3-pandas 

# using pip3 to install jupyter
RUN pip3 install jupyter

# default port of Jupyter
EXPOSE 8888

# run Jupyter Notebook
# --config gives location of Jupyter configuration file 
# --notebook-dir gives root location where notebooks are saved and read from
ENTRYPOINT jupyter notebook \ 
	--config=/opt/jupyter/config/jupyter_notebook_config.py \
	--notebook-dir=/opt/jupyter/notebooks/
