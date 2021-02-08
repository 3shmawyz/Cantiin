//var {assert} = require("chai")
//var validate = require("validate")
//var Schema = validate.Schema
import Schema from 'validate'
/*
import Schema from 'validate'
*/
const user = new Schema({
	username: 
	{
		type: String,
		required: true,
		length: { min: 3, max: 32 }
	},
	pets: 
	[
		{
			name: 
			{
	  			type: String,
	  			required: true
			},
			animal: 
			{
	  			type: String,
	  			enum: ['cat', 'dog', 'cow']
			}
  		}
  	],
	address: 
	{
		street: 
		{
			type: String,
			required: true
		},
		city: 
		{
			type: String,
			required: true
		},
		zip: 
		{
	  		type: String,
	  		match: /^[0-9]+$/,
		required: true
		}
  	}
})


/*
describe("validate", ()=>
{
	afterEach(function(done) {
       console.log("____________________")
    });

	describe("test0",()=>{
		assert.equal(1, 1);
		console.log("test0:Testing Validate")
	})
})
*/