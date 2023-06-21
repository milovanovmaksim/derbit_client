#!/bin/bash

export PYTHONPATH=.
source .venv/bin/activate


if [ $1 == api ]
then
	python ./api/main.py
elif [ $1 == client ]
then
	python ./derbit_client/main.py
fi