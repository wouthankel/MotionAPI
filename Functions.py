## UseMotion.com REST api.

#Imports
import http.client
from http import HTTPStatus
from datetime import datetime

ServerUrl = "api.usemotion.com"
Connection = http.client.HTTPSConnection(ServerUrl)

def ListWorkspaces(ApiKey):
    Headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'X-API-Key': ApiKey
    }

    Connection.request("GET", "/v1/workspaces", headers=Headers)
    Result = Connection.getresponse()
    Data = Result.read()
    return Data.decode("utf-8")

def ListProjects(ApiKey, WorkspaceID):
    Headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'X-API-Key': ApiKey
    }

    Connection.request("GET", "/v1/projects?workspaceId=" + WorkspaceID, headers=Headers)
    Result = Connection.getresponse()
    Data = Result.read()
    return Data.decode("utf-8")


def ListUsers(ApiKey, WorkspaceID):
    Headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'X-API-Key': ApiKey
    }

    Connection.request("GET", "/v1/users?workspaceId=" + WorkspaceID, headers=Headers)
    Result = Connection.getresponse()
    Data = Result.read()
    return Data.decode("utf-8")

def CreateTask(ApiKey, WorkspaceID, ProjectID, UserID, TaskName, StartDate, Duration=30):
    Headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'X-API-Key': ApiKey
    }

    Payload = "{\n  \"dueDate\": \""+str(StartDate)+"\",\n  \"duration\": \"NONE\",\n  \"status\": \"Auto-Scheduled\",\n  \"autoScheduled\": {\n    \"startDate\": \""+str(StartDate)+"\",\n    \"deadlineType\": \"SOFT\",\n    \"schedule\": \"Work Hours\"\n  },\n  \"name\": \"" + TaskName + "\",\n  \"projectId\": \""+ProjectID+"\",\n  \"workspaceId\": \"" + WorkspaceID + "\",\n  \"description\": \"This task was created by Wout Hankel's python API\",\n  \"priority\": \"MEDIUM\",\n  \"assigneeId\": \""+ UserID +"\"\n}"

    Connection.request("POST", "/v1/tasks", Payload, headers=Headers)
    Result = Connection.getresponse()
    if Result.status == 201:
        return True
    else:
        return False
