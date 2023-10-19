# discord-twitter-x-link-bot

`docker run -e TOKEN='' -e PREFIX='' ghcr.io/owine/discord-twitter-x-link-bot:main`

`TOKEN` (required) your Discord bot token (from developer center)
`PREFIX` (option, default `!`) a bot trigger prefix (currently nonfunctional)

1. Create a new application on the Discord [Developer Portal](https://discord.com/developers/applications).
2. Enable Bot functionality, give your prefered name and avatar.
3. Copy the Token for use above.
4. Run the container as specified above.
5. Authorize the bot and add it to your server by visiting: `https://discord.com/oauth2/authorize?client_id=<YOUR BOT APPLICATION ID>&permissions=274878000128&scope=bot%20applications.commands`
