docker run -d --name jupyter_container \
	 -p 8888:8888 \
	 -v ${PWD}/config/:/opt/jupyter/config/ \
	 -v ${PWD}/data/:/opt/jupyter/data/  \
	 -v ${PWD}/notebooks/:/opt/jupyter/notebooks/ \
	 patclaffey/jupyter_pandas:v2
