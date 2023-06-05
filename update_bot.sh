#!/bin/bash

# Step 1: Stop the Python process running the bot
pkill -SIGINT -f "python3 app.py"

# Check if the process was successfully stopped
if [ $? -ne 0 ]; then
    echo "Failed to stop the Python process. Exiting..."
    exit 1
fi

# Step 2: Copy the database to a backup location
cp ./bot/data/bot.db ../bot.db.backup

# Check if the database backup was successfully created
if [ $? -ne 0 ]; then
    echo "Failed to create a backup of the database. Exiting..."
    exit 1
fi

# Step 3: Perform a git pull
git pull
# Check if the git pull was successful
if [ $? -ne 0 ]; then
    echo "Failed to perform a git pull. Exiting..."
    exit 1
fi

# Step 4: Copy the database back to its original location
cp ../bot.db.backup ./bot/data/bot.db

# Check if the database was successfully restored
if [ $? -ne 0 ]; then
    echo "Failed to restore the database. Exiting..."
    exit 1
fi

# Step 5: Run the initPhrases.py script
cd bot
python3 initPhrases.py
cd ..

# Check if the initPhrases.py script executed successfully
if [ $? -ne 0 ]; then
    echo "Failed to run the initPhrases.py script. Exiting..."
    exit 1
fi

# Step 6: Run the Python app.py script in the existing tmux session named "realtor"
tmux send-keys -t motor 'python3 app.py' C-m

# Check if the command to run app.py in tmux was successful
if [ $? -ne 0 ]; then
    echo "Failed to run the app.py script in the motor tmux session. Exiting..."
    exit 1
fi