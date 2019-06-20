# -*- coding: UTF-8 -*-
###
# Some sensitive informations should be written here 
#   and kept out of the version controller.
# For example. database passwords and API keys, 
#   or defining variables specific to a given machine.
# This file will be loaded by `instance_relative_config=True` in app.py or app/__init__.py
# The folder that hold this configuration file ought to called 'instance'.
###
DEBUG= True
SQLALCHEMY_ECHO = True

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
SQLALCHEMY_DATABASE_URI= ""