//var {assert} = require("chai")
//var validate = require("validate")
//var Schema = validate.Schema
//import Schema from 'validate'
/*
import Schema from 'validate'
*/

/*
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
*/

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



var Validator = require('validatorjs');

/*

let data = {
  name: 'John',
  email: 'johndoe@gmail.com',
  age: 28
};

let rules = {
  name: 'required',
  email: 'required|email',
  age: 'min:18'
};

let validation = new Validator(data, rules);

validation.passes(); // true
validation.fails(); // false

vali = validation.errors.first('email'); // 'The email format is invalid.'
errs = validation.errors.get('email'); 
// returns an array of all email error messages

console.log("Hello")

*/




let input = { name: '', email: '' };
let rules = { name : 'required', email : 'required' };

let validation = new Validator(input, rules);

validation.passes();
vali = validation.errors.first('name'); // returns  'The name field is required.'
errs = validation.errors.first('email'); // returns 'Without an email we can\'t reach you!'

console.log(typeof(validation.errors))
console.log((validation.errors))
console.log((validation))




console.log(validation)
console.log(errs)
console.log("______________________")

input = {name:1,email:"abc"}
let validation1 = new Validator(input, rules);
console.log(validation1)


