var  {Sequelize, DataTypes} = require('sequelize');
// Option 1: Passing a connection URI
const connection = new Sequelize(
'postgresql://postgres:Rq5mVTej7Zb4xY@localhost:5432/cantiin_node',
{  logging:false
}); 



/*
sequelize.org -> documentation -> getting started
*/


const User = connection.define('User', 
{
  // Model attributes are defined here
  // id is already defined
  username: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
    //defaultValue:""
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false
    // allowNull defaults to true
  }
}, {
  timestamps:false
});


/*

var User = connection.define("user",
	{
		"id": Sequelize.INTEGER({'primaryKey': true}),
		"username": Sequelize.STRING,
		"password": Sequelize.STRING
	}
)

*/



connection.sync().then(function () {
     console.log("Promise Resolved");
}).catch(function (error) {
     console.log("Promise Rejected");
     console.log(error)
});



