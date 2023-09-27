bContinue = True

# Requires Functions.py
from Functions import *
from datetime import datetime
from datetime import timedelta
import json

#API Key
ApiKey = ""

if len(ApiKey) < 1:
    print("\033[91mAPI Key is not entered / Not valid! Please check the API key variable!\033[0m")
    bContinue = False

if bContinue == True:
    #Start by selecting a Workspace
    data = json.loads(ListWorkspaces(ApiKey))
    key = 0
    while key < len(data['workspaces']):
        print(key, ": ", data['workspaces'][key]['name'], "(" + data['workspaces'][key]['id'] + ")")
        key = key + 1
    WorkspaceID = int(input("Input workspace number: (default: 0)") or "0")
    WorkspaceIDAPI = data['workspaces'][WorkspaceID]['id'] # This ID is needed to create a list of projects in the next step.
    print("\033[92mWorkspace "+ str(data['workspaces'][WorkspaceID]['name']) +" Selected.\033[0m")

    #Select a Project
    data = json.loads(ListProjects(ApiKey, WorkspaceIDAPI))
    key = 0
    while key < len(data['projects']):
        print(key, ": ", data['projects'][key]['name'], "(" + data['projects'][key]['id'] + ")")
        key = key + 1
    ProjectID = int(input("Input Project number: (default: 0)") or "0")
    ProjectIDAPI = data['projects'][WorkspaceID]['id'] # This ID is needed in the next step.
    print("\033[92mProject "+ str(data['projects'][ProjectID]['name']) +" Selected.\033[0m")


    #Select an Assignee
    data = json.loads(ListUsers(ApiKey, WorkspaceIDAPI))
    key = 0
    while key < len(data['users']):
        print(key, ": ", data['users'][key]['name'], "(" + data['users'][key]['id'] + ")")
        key = key + 1
    UserID = int(input("Input Project number: (default: 0)") or "0")
    UserIDAPI = data['users'][WorkspaceID]['id'] # This ID is needed in the next step.
    print("\033[92mUser "+ str(data['users'][ProjectID]['name']) +" Selected.\033[0m")

    #Create the task
    StartDate = datetime.now() + timedelta(days=1)
    TaskName = input("Task name:")
    if CreateTask(ApiKey, WorkspaceIDAPI, ProjectIDAPI, UserIDAPI, TaskName, StartDate):
        print("\033[92mTask added!: " + TaskName + "\033[0m")