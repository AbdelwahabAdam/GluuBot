## Docker Compose for Rasa chatbot integrated with Postgres BD.

### To Test using this docker-compose 

- first build Dockerfile using the following command:
  ```docker build -t my_rasa_image .```
- then just run the compose:
  ```docker-compose up```
- To test run the rasa shell as -it 
  ```docker run -it rasa_image_id bash ```
- you will find the following files in this image:
    ```Dockerfile    
    coverter.py         
    data_not_used  
    database_wrapper.py  
    docker-compose.yml  
    entrypoint.sh  
    readme.md
    FromDataBase  
    config.yml   
    custom_importer.py  
    database       
    db_command.py        
    domain.yml          
    models
    ```


- using `db_command.py` we can get the db entries:
   ```db_command.py get ```

- then we can use the same file to do any add, edit, update, getvalue, and delete :
- running ```db_command.py```
  - Please Provide some parametar
  - parametar:
    - get: to get all data in the DB, ex: python3 db_command.py get
    - add: to add a new values, ex: python3 db_command.py add id intent_name ['intent','example'] responce
    - update: to update certain value, ex: python3 db_command.py update response Bye! id 1
    - getValue: to get certain value, ex: python3 db_command.py get_Value response id 1
    - delete: to delete a row (on id), ex: python3 db_command.py delete 1 


- after updating the db, you can simply restart my_rasa_image:
  - ```docker-compose restart my_rasa_image ``` 
-  then run it again in interactive mode using:
     - ``` docker run -it rasa_image_id bash```
- Finally 
    - ``` rasa shell ```