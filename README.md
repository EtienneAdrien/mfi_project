# mfi_project

### Project context
The context of this test is to provide a simple web service for storing and retrieving moutain peaks.

Using the **python** web framework Django OR **PHP** web framework on your chosing and a database. (postgresql database is better (postGIS can be used for geo features)),
 implement the following features:

- models/db tables for storing a peak location and attribute: lat, lon, altitude, name
- REST api endpoints to :
    * create/read/update/delete a peak
    * retrieve a list of peaks in a given geographical bounding box
- add an api/docs url to allow viewing the documentation of the api and send requests on endpoints
- add an html/javascript page to view the peaks on a map (use opensource packages) 
- deploy all this stack using docker and docker-compose
- [Optional] add ip filtering with a country whitelist settings. Connections from a country not in the list should return a http 403. An admin page protected
with user/password authentication should allow viewing rejected connections.


The source code should be delivered using bitbucket or github with detailed explanations on how to deploy and launch the project.

##### I ran out of time for the html/javascript part, so it isn't present in the project

### Deployment
`docker-compose up`

If you have this error:
> web_1 | django.db.utils.OperationalError: could not connect to server: Connection refused

> web_1 | Is the server running on host "db" (172.18.0.2) and accepting

> web_1 | TCP/IP connections on port 5432?

Launching `docker-compose up` again should get rid of it

The API is served on the port 8088

### Api Rest Documentation
You can find a documentation for the API with some examples values here https://documenter.getpostman.com/view/2690818/Tz5tZbsj
