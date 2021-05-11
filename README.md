# ds3002project2


I first started by setting up a RDS in AWS, called project2. I then created a lambda function that imported requests in order to get the data from the api. Attatched to this lambda function was an EventBridge (CloudWatch Events) trigger that ran the function every 60 seconds. Each minute the function pulled from the api, transformed it into SQL, and added the data into my databases. The function stopped after exactly one hour (60 entries).

 
Analysis:

Over the course of the hour, I noticed a few trends in the data.


Explination of Patterns:

I believe that these trends in the data were 
