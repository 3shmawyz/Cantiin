# Cantiin v1.1.3

## What's new:

### 1. SECRET is now a string  
instead of a randomly generated text.  
A randomly generated text was problematic, because every time the server refreshes, the
secret will change, and the user will have to login again.


### 2. No Open in a new tab
Some buttons used to make the user open in a new tab.  
This was a negative user experience.  



### 3. Fronend refractored
Now the frontend is refractored using Jinja.


### 4. JavaScript refractored
Now some JS codes have common js file, so that the same code is not written 
again in every file.

