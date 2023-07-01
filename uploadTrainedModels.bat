@echo off
scp -i "./realtor.pem" -r "./trained_models" ubuntu@ec2-3-126-146-58.eu-central-1.compute.amazonaws.com:/home/ubuntu/motormentor/trained_models

echo File uploaded successfully.