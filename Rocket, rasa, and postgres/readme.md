## Docker Compose for Rasa chatbot integrated with Postgres BD and Rocketchat.

### To Test all using this docker-compose 

- Run ```docker-compose up```

- open `localhost:3000`

- create admin user and then create bot user with these following roles. 
    1. bot
    2. livechat-agent
   
- enable Omnichannel.
  -`Administration` > `workspace` > `setting` > `Omnichannel` > `Omnichannel enabled`

- Assign new conversations to bot agent.
-`Administration` > `workspace` > `setting` > `Omnichannel`  > `Routing` > `Assign new conversations to bot agent`

#### Setup Rocket chat Omnichannel

- make sure the bot assign as `Agents` 
  - `Administration` > `Omnichannel` > `Agents` 
- Add new `Department`
  - add department with the name **`general`**, `enable` it and add the bot user as Agent >> Make sure to press `Add`
  - then add email for it and hit `save`


#### Rasa App setup
- Download directly from Rocket.Chat marketplace
- Fill neccessary fields in `Setting`
  - Bot Username (required)
    - the bot user name we created.
  - Rasa Server Url (required)
    - The URL for rasa server, here we will put another url for a python flask server. >> will be demonstrated later.
    - ex: http://**ip**:4000 >> put you device ip, dont put localhost
  - Default Handover Department Name (required)
    - add `general` that we created before.

#### Note
- you need to login as the bot user and enable the omnichannle `Turn on answer chat`
- you need to run the redirectServer to get responce back