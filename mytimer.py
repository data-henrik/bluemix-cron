 # Sample file similar to those provided by the package "schedule"
 # Define the tasks to be executed based on the specified schedule.
 # For details see my related blog post
 import schedule  
 import time  
 
 # Some jobs to execute later on:
 def job():  
 #put the task to execute here  
 
 def anotherJob():  
 #another task can be defined here  
 
 # schedule the first job to run every 10 minutes, the second for daily execution at 10.30am
 schedule.every(10).minutes.do(job)  
 schedule.every().day.at("10:30").do(anotherJob)  
 
 while True:  
   schedule.run_pending()  
   time.sleep(1) 
