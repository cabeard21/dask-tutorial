#!/bin/bash
docker run -it -p 8888:8888 -p 8787:8787 -e JUPYTER_ENABLE_LAB=yes -v "$(dirname "$PWD")":/home/jovyan/dask-tutorial dask-tutorial