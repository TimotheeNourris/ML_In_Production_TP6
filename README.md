# ML_In_Production_TP6

code comes from dev part.

First, we needed to create and train a model based on the fashion-mnist dataset, right after, we had to load it into a flask application and create a root "/classify" to load the image as an array and test it with the model. Once everything is done, we launch the application.

<img width="670" alt="launch_app" src="https://user-images.githubusercontent.com/66907341/215291946-1a25da0e-8ad0-4d69-9010-6d04fdd9ecbd.png">

Moreover, we test directly the app by sending a request with Postman or google Chrome, i personnaly made both.
<img width="672" alt="postman_test" src="https://user-images.githubusercontent.com/66907341/215291948-9227ae2c-10bb-4361-bf64-0676357f9a9c.png">
<img width="834" alt="chrome_test" src="https://user-images.githubusercontent.com/66907341/215291943-69057559-c7a5-46c4-b170-1aff40873976.png">



Then, we need to make a unittest to see if the application works if we send a specific row.
<img width="663" alt="unittest" src="https://user-images.githubusercontent.com/66907341/215291922-b286793b-0e11-411c-acdc-2b33dfb463f4.png">

Finally, we add our project to github by adding a Jenkinsfile containing all the steps (creating staging branch and push, build, test, and deploy part), a Dockerfile to push our project to docker and dockerHub. We do configure the webhook on github and we launch the Jenkinsfile from Jenkins to run the pipeline with all the steps.
<img width="699" alt="jenkins_test" src="https://user-images.githubusercontent.com/66907341/215291945-25f8db8b-02ea-494e-9d25-2cdf56e411c4.png">

