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
* The function processes 3 type of logs: click, view and navigate and stores in a sqlite3 database(In the real world, S3 or any other NoSQL DB would be ideal for storing data with different structure). 
* The function accepts all request and returns a submitted message to the client but will skip any logs with an invalid error type(accepted: click, view, navigate).
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
To make it more scalable in the cloud, rather than saving all the individual database to reduce storage cost, we could store the logs from each session as a single log file and store the a Primary Key consists of UserId + SessionId, We can use AWS Kinesis to capture the data and store it in S3 and for stream a large amount of data, we can potentially use AWS Athena to query the S3 bucket since it can process the logs files as text. 

