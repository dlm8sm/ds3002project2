# ds3002project2


I first started by setting up a RDS in AWS, called project2. I then created a lambda function that imported requests in order to get the data from the api. Attatched to this lambda function was an EventBridge (CloudWatch Events) trigger that ran the function every 60 seconds. Each minute the function pulled from the api, transformed it into SQL, and added the data into my databases. The function stopped after exactly one hour (60 entries).

 
Analysis:



Explination of Patterns:



################### Picture Uploads ###################

![project2-rds](https://user-images.githubusercontent.com/78705257/117752188-5adc9f00-b1e4-11eb-86e1-6fd16f496e39.PNG)

![lambda_60sec](https://user-images.githubusercontent.com/78705257/117752197-5f08bc80-b1e4-11eb-94bf-1025da975f4c.PNG)

![php blank data table](https://user-images.githubusercontent.com/78705257/117752204-60d28000-b1e4-11eb-95f7-284592173b04.PNG)
