# jenkins-freestyle-project

Testing for Jenkins

Added line to test webhook

This repo is set up with Jenkins for automated testing on a temporary AWS EC2 instance. The Jenkins server is set up on the EC2 instance and is configured to run a freestyle project that will run a shell script to test the code in this repo. The shell script is run on the EC2 instance and will clone this repo, run the tests, and then delete the repo.

change made here
