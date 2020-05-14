#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Settings for scheduler/scriptbot.
"""
import os

#logging settings
import logging
LOG_LEVEL = logging.INFO
LOG_PATH = '/var/log/scriptbot/scheduler.log'
STATUS_PATH = '/var/log/scriptbot/scheduler.status.json'


#sudo command
#make sure scriptbot runner has sudoer privilege
SUDO = '/usr/bin/sudo'

#scriptbot root
SCRIPTBOT_ROOT = '/opt/ictf/scriptbot'

#script cache path
#make sure it is readable by sandbox user
#TMP_SCRIPT_PATH = '/dev/shm/ctf/scripts'
#TMP_BOT_PATH = '/dev/shm/ctf/'
TMP_SCRIPT_PATH = '/var/ctf/scripts'
TMP_BOT_PATH = '/var/ctf/'

#MODIFY THIS SALT VALUE to hide other scripts from sandbox user
TMP_SCRIPT_PATH_SALT = 'path_salt'

#tmp path where scripts can write
TMP_SCRIPT_OUTPUT = '/tmp/script_output/'

#Sandbox python while running submitted scripts
#For now use the default python
SANDBOX_PYTHON_PATH = '/opt/ictf/venv/scriptbot/bin/python'

SANDBOX_RUNNER_PATH = '/opt/ictf/scriptbot/main_sandbox_run.py'

#team info
TEAM_LIST_PATH = 'team_list.json'
TEAM_LOCAL_USER_FORMAT = 'ctf-sandbox-team-%d'



#how much output to send to DB
MAX_SCRIPT_OUTPUT_BYTES = 1000

#scheduler settings
SIGMA_FACTOR = 10.0/100 #(10 percent of the script call interval)
SCRIPT_TIMEOUT_SOFT = 60 # 1 minute, roughly 1/3 of the length of a tick
SCRIPT_TIMEOUT_HARD = SCRIPT_TIMEOUT_SOFT + 10 # give the script 10 seconds to die and traceback
SETUP_SLEEP = 5 #seconds
STATE_CHECK_INTERVAL = 2
STATE_EXPIRE_MIN = SCRIPT_TIMEOUT_SOFT #seconds
SET_GET_FLAG_TIME_DIFFERENCE_MIN = 3.0


# Registry settings
# REGISTRY_USERNAME = "{{DOCKER_REGISTRY_USERNAME}}"
# REGISTRY_PASSWORD = "{{DOCKER_REGISTRY_PASSWORD}}"
# REGISTRY_ENDPOINT = "{{DOCKER_REGISTRY_ENDPOINT}}"

REGISTRY_USERNAME = ""
REGISTRY_PASSWORD = ""
REGISTRY_ENDPOINT = ""
IS_LOCAL_REGISTRY = bool(os.environ['IS_LOCAL_REGISTRY'])


#DB settings
# DB_HOST = '{{ICTF_API_ADDRESS}}'
# DB_SECRET = '{{ICTF_API_SECRET}}'

DB_HOST = "database.ictf"
DB_SECRET = os.environ['API_SECRET']
# Retry at most 2 times if we get a HTTP 502 back
DATABASE_REQUEST_RETRIES = 2
# Sleep 1 second before each retry
DATABASE_REQUEST_RETRY_INTERVAL = 1

# ID of the current bot
BOT_ID = int(os.environ["BOT_ID"])
# Number of all bots we have
ALL_BOTS = int(os.environ["ALL_BOTS"])
