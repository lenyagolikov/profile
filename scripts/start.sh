#!/bin/bash

# wait db
sleep 5

# make migrations 
app-db upgrade head

# run app
app
