## API Reference

#### Get all items

```http
  GET /api/retrievelogs
```

| Parameter | Type     | 
| :-------- | :------- | 
| `userId`  | `string` | 
| `logType` | `string` | 
| `fromTime`| `string` | 
| `toTime`  | `string` | 

* Since we are processing up to 100 users every 5 mins, I have decided to create a thread for each request for faster processing time. 
* The function processes 3 type of logs: click, view and navigate and stores in a sqlite3 database. In the real world, we could:
    *  NoSQL, data strucure is not uniformed.  
    *  Use S3 to store the log files and AWS Athena to process and analyze the data.
* The function accepts all request and returns a submitted message to the client but will skip any logs with an invalid log type(accepted: click, view, navigate).
---

``` http
 POST /api/submitlogs
```
```
[
"userId": "CBC123XYZ",
  "sessionId": "XYZ456ABC",
  "actions": [
    {
      "time": "2018-10-20T21:37:28-06:00",
      "type": "CLICK",
      "properties": {
        "locationX": 52,
        "locationY": 11
      }
    }
 ]
```

* This API allows multiple form of retrieval based on the parameters passed, any combination of user, time range(both from and to time must be provided) and log type. Errors will be returned
  * if no parameters are provided
  * if logType is not one of: click, view, navigate
* A 200 success code along with the logs will be returned(if any) if proper parameters are provided.
---

# The application can be run locally by (Windows):
1. create a virtual environment and by running python3 -m venv <env_name>
2. activate the env and install packages in requirements.txt - pip3 install -r requirements.txt
3. Optional: create a fresh database but running the follow commands in python in the project's root level:
    1. from app import app
    2. from extensions import db  
    3. from models.click_action import ClickAction 
    4. from models.view_action import ViewAction
    5. from models.navigate_action import NavigateAction
    6. db.create_all(app=create_app())
4. lastly, run 'flask run' to run the application

# Unit Test:
     You can run unittest in another command prompt while the application is running:
        - open another command prompt
        - activate the development environment
        - 'python3 test.py'

# Follow up question:
I would deploy the main applicaiton to an ECS, it pushes logs to a SQS which will then trigger a lambda function to store it in DynamoDB. 
  * We use a lambda function because it is integrated with CloudWatch logs to monitor any errors. 
  * We use a SQS to prevent and data loss due to transient network issue, it has Dead Letter Queue, it also can add any failed process to a DLQ for retry.
  * We use ECS to allow auto scaling
  * We use DynamoDB to store not uniform data
  * All of the above resources can be managed by CloudFormation to easily deploy to various environment(dev, beta, uat, prod, etc), by doing it this way, we can ensure consistency between environments

To stream large amount of data to client, we can use AWS Kinesis to batch process the DynamoDB Stream and feed it into a Amazon Open Search so that any data can be easily queried by the client. 

 We can use AWS App Config to store any environment variable to avoid any running application if we need to modify any variable
  
 We can use CodePipeline for continous development

