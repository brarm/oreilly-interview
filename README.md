# oreilly-interview

A containerized API to read Postgres Data

## API Schema
GET all_books
GET subset_id <id_FROM> <id_to>
GET subset_author <author>
GET single_id <work_id>
GET single_isbn <isbn>
  
## Test
```
  docker run --platform linux/amd64 --name ormdb -d 
    -e POSTGRES_PASSWORD=hunter2 -e POSTGRES_USER=oreilly 
    -d registry.hub.docker.com/caedus41/oreilly-cloud-engineer-postgres
  
 pip3 install -r requirements.txt
 export FLASK_APP=api
 python3 -m flask run
 
 curl localhost:5000/subset_id/1/2
```
  
## Deploy
`kubectl -- apply -f ./api-and-db-pod.yaml`
