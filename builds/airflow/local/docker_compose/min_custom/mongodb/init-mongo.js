db = db.getSiblingDB("platform");
db.createUser(
    {
        user  : "pmadmin",
        pwd   : "pmpass",
        roles : [
            {
                role : "readWrite",
                db   : "platform"
            }
        ]
    }
);
db.createCollection('clients');

db.clients.insertMany([
    {
        client: "lala",
        desc: "some description",
        projects: ['ctc']
    },
    {
        client: "dingy",
        desc: "din-gy r us",
        projects: ['abbca']
    }
]);
