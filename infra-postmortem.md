# Infra Postmortem

If you participated in the event, it was apparent that we had infrastructure issues at the very start. This resulted in a 6h 6m downtime. 

This document serves to give commentary on what went wrong, what we did to resolve it, and what we plan on doing for the future. 

Please note, an hour and a half into the event, with having having restored the infrastructure, we decided to release the challenges via Google Drive so that people could get started. As a result, we also pushed the end time of CTF back by an hour and a half.

# What Happened

With 10 minutes prior to the start of the event, we immediately noticed degraded performance of our CTFd instance. Upon analyzing the logs, we had a significantly higher amount of traffic. 

We attempted to force the number of replicas of the CTFd instance to mitigate this issue. This fixed the stability of the frontend of the site, while passing the instability to the backend.

In addition to this, in our manifests, we had an issue that we had not priorly realized. We had mistakenly had certain persistent storage volumes set to ReadWriteOnce, rather than ReadWriteMany.  

In the process of these events, we ran out of storage for some of our persistent volumes, including logs. We increased this storage. 

We then were still having issues with too many concurrent requests being made to the database as users were attempting to log in. 

After struggling with the Kubernetes even more, we made a change that wiped out our database.

At this point, we decided to take the approach differently, and attempt to roll out an instance of CTFd running through Google Cloud App Engine. 

At this point, each terraform update we made in deploying to app engine would take 15-20 minutes, then give us a small trivial error that we made because we were in a rush. This repeated multiple times. 

At the five hour mark, we decided we needed to look into alternatives while other members continued to work on deploying to App Engine. At this time, we paid for CTFd.io and replicated our challenges and setup to that instance, and setup a new subdomain for it (ctfd.broncoctf.xyz)

# What went wrong

- Our estimation for event partipants was off by a factor of 10.
- Our infrastructure was not designed nor capable of handling a significant excess of people. 
  - We had tested the infrastructure at 1.5 * the max user count from last year (500), so simulating 750 users. According to logs and the amount of users we had registered, we had around 5000 users attempting to concurrently use our service.
- Our mitigation attempts caused more issues, increasing the difficulty of restore. 
- Our rush to fix lead to mistakes, especially with long build times, resulting to longer downtime.
- We did not backup our DB. 

# Where did we get Lucky?

- Infrastructure for Challenges was not decimated by load
- Prior BroncoSec members with better infrastructure knowledge were available and willing to help. 
- We had funding
- CTFd.io was able to instantly deploy an instance.

# Takeaways for the future

- Test at a much larger factor than expected. 
- Backup the CTFd instance and database before the event and consistently throughout.
- Post the Discord link on CTFtime earlier. We added it after the infrastructure issues began, but people did not realize this had updated. This will allow us to communicate updates to issues. 
- While difficult, try to take a step back when mitigating. We made mistakes that made our life harder because we were in a rush. 

# Closing Note

Ultimately, we could have done better a lot better. But with all that said, we still had a great event with record-setting participation and lots of great feedback to help us grow as hackers and organizers. Thank you to our board, for the combined effort in mitigating this. Thank you to past BronocSec members, for reaching out and volunteering a substatial period of time to help. And thank you to those who stuck with us despite the challenges with infrastructure to participate in the event. 