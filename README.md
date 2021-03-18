# mfi_project

### Deployment
`docker-compose up`

If you have this error:
> web_1 | django.db.utils.OperationalError: could not connect to server: Connection refused

> web_1 | Is the server running on host "db" (172.18.0.2) and accepting

> web_1 | TCP/IP connections on port 5432?

Launching `docker-compose up` again should get rid of it

### Api Rest Documentation
You can find a documentation for the API with some examples values here https://documenter.getpostman.com/view/2690818/Tz5tZbsj
