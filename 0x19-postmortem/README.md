The following is an incident report for madukaonline.co.ke that occurred on January 21, 2024.We understand this incident has affected our value customers and we humbly request for apology on the negative impact of this issue.
Issue Summary
From 7pm to 7:56pm GMT, request to madukaonline.co.ke ecommerce site resulted to overlapping images and text. The issue affected 100% of traffic to our website. Users could not understand the page, logging or neither make purchases. The root cause of the incident was an invalid update of the CSS styles sheets that causes abnormal appearance of the commerce site.
Timeline (all times GMT)
·       6:57 PM: Configuration push begins
·       7:00 PM: Errors begins
·       7:03 pm: Datadog alerted teams
·       7:40 PM: Successful configuration change rollback
·       7:50 PM: Server restarts begin
·       7:56 PM: 100% of traffic back online
Root Cause
At 6:40 PM GMT, editing of our CSS files begin to improve our users experience. The change was immediately released before proper testing. As a result, the changes made caused the images and text to overlap making it difficult for users to navigate in our pages. The main cause of the issues was wrong address of the files in out HTML files and improper arrange of the classes. The issues affected 100% of activities in our site before restoration was achieved.
Resolution and recovery
At 7:03 GMT, the monitoring systems alerted our engineers, the alert was low high bounce rate to our pages. At 7:06 we also got complains from our social media platform from user. The incident response team narrowed down to the root cause of the matter and identified that the issue was caused by the recent updates that was made to our styles sheets.
At 7:36 PM GMT, the root cause had already been identified and restored. Before the solved configuration push the changes was tested locally and the success changed was push. The servers were restarted to load the newly changes.
At 7:52 PM GMT everything was back normal and by 7:56 PM 100% traffic was restored.
Corrective and Preventative Measures
We have set aside some couple of time to look into details on the root cause of the problem and we have come up with some measures to put into place to avoid failing into the same problem.
Disable the current configuration release mechanism until safer measures are implemented. (Completed.)
  Improves the process of going through the new changes before they are deployed.
Automating some of our changes to avoid human errors
Improve our alert systems for quicker alerts and quick fixes
We have added human resources to our testing team and monitoring department
Madukaonline is committed to improve our delivery and satisfied our users accordingly. We will continue doing our best to give it best to our users and improve our output as best as we can.
