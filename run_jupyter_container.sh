docker run -d --name jupyter_container -p 8888:8888 -v ${PWD}/notebooks/:/opt/notebook/notebooks/ -v ${PWD}/data/:/opt/notebook/data/ jupyter_image 
