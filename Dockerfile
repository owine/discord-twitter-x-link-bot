FROM python:3.11-slim-buster

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot script
COPY discord-twitter-x-link-bot.py .

# Set environment variables
ENV TOKEN="" \
    PREFIX="!"

# Run the bot script
CMD ["python", "discord-twitter-x-link-bot.py"]