# SteamMiser

Steam Miser is a simple web application that allows you to flag a game on steam and recieve a notification via email when it reaches a desired price point.

This is built is a "fun" project with the goal to utilize a bunch of modern web technoligies and cloud APIs. These are technoligies that I don't necessarily use every single day and I wanted to have a project that let me get familiar with them.

I had a few self-imposed rules for this project as an added challenge:
- Devlop this application on Windows (I am usually a linux guy but I wanted to see how far WSL had come) via WSL2/VSCode
- Use as many cool technoligies as I can pack into this, I think I did an OK job:

    - AWS
        - EC2 VM will host the back-end
        - AWS Dynamo DB for the NoSQL DB
    - Google Cloud Platform
        - Google Cloud functions for sending alerts
    - Twilio
        - Sendgrid is used for email notifications
    - React
        - React.JS will be used for the front-end
