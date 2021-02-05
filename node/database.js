var  Sequelize = require('sequelize');
// Option 1: Passing a connection URI
const connection = new Sequelize(
'postgresql://postgres:Rq5mVTej7Zb4xY@localhost:5432/cantiin_node'); 



/*
sequelize.org -> documentation -> getting started
*/





connection.sync().then(function () {
     console.log("Promise Resolved");
}).catch(function (error) {
     console.log("Promise Rejected");
     console.log(error)
});



