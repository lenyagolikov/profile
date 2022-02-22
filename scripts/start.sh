#!/bin/bash

# wait db
sleep 5

# make migrations 
app-db

# run app
app
