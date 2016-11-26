### A MySQL-based Flask Application
- Clone the app
- Build the image with `docker-compose build`
- Run the container with `docker-compose up`
- Initialize tables with `docker exec -it counterapp_web_1 python dbinit.py`
- Hit `/` and see the counter incrementing every time you refresh the page
- To use the app container `docker exec -it counterapp_web_1 /bin/bash`
- To use the mysql server do `docker exec -it counterapp_db_1 mysql -uroot -prootpass`
- If you do any changes and need to reset the containers, you can do `docker-compose rm -v`
- Run tests by doing `docker exec -it counterapp_web_1 python tests.py`
