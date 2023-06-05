@echo off
scp -i "./realtor.pem" "./categorical.json" ubuntu@ec2-3-66-165-37.eu-central-1.compute.amazonaws.com:/home/ubuntu/motormentor/trained_model/categorical.json
scp -i "./realtor.pem" "./xgb_model.pkl" ubuntu@ec2-3-66-165-37.eu-central-1.compute.amazonaws.com:/home/ubuntu/motormentor/trained_model/xgb_model.pkl
scp -i "./realtor.pem" "./encoder.pkl" ubuntu@ec2-3-66-165-37.eu-central-1.compute.amazonaws.com:/home/ubuntu/motormentor/trained_model/encoder.pkl
echo File uploaded successfully.