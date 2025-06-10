Serverless URL Shortener 
A lightweight serverless application that converts long URLs into short, memorable links using AWS Lambda, API Gateway, and DynamoDB—all within AWS Free Tier limits.

Features
Fully Serverless: No infrastructure management, just pure automation DynamoDB Storage: Shortened links stored for instant retrieval Scalable API: Built with API Gateway for seamless integration Free Tier Optimized: Runs entirely within AWS Free Tier constraints

 How It Works
1️⃣ Users send a URL to the API. 2️⃣ AWS Lambda generates a unique short code. 3️⃣ The mapping is stored in DynamoDB. 4️⃣ Users retrieve the original URL using the short code.
