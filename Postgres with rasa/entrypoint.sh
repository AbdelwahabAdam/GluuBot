#!/bin/bash

set -e

# Train the Rasa model
rasa train

# Start the Rasa server
rasa run --enable-api --model /app/models