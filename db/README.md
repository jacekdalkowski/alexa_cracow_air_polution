RUN LOCALLY

Run Mongo
sudo mongod --dbpath /Users/jacekdalkowski/Dev/gardenmate_projects/gardenmate_local_db

Connect via Mongo console
mongo
show dbs
use airpolution
// show collections
// db.getCollectionNames()
db.airpolution.find()
db.airpolution.remove( { } )

