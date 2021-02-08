var {assert} = require("chai")
var {Schema} = require("validate")


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
	  			type: String
	  			required: true
			},
			animal: 
			{
	  			type: String
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
		}
		zip: 
		{
	  		type: String,
	  		match: /^[0-9]+$/,
		required: true
		}
  	}
})



describe("test", ()=>
{
	describe("test1",()=>{
		assert.equal(1, 1);
		console.log("tst1")
	})
	describe("test3",()=>{
		assert.equal(3, 3);
		console.log("tst3")
	})
	describe("test2",()=>{
		assert.equal(2, 2);
		console.log("tst2")
	})
})
