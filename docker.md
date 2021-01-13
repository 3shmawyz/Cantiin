# Docker Flask Example

## About

This is an MIT licensed Flask Application running on docker






## Up And Running:

### 1) Validations:
Inside the CLI (Git bash for example run these commands)

<b>

```bash
docker --help
```
```bash
docker volume --help
```
```bash
docker-compose --help
```
</b>
If you get any error while running any of these commands, then you
need to fix the problem.  
There are some missing software on your device, 
and you need to install them correctly.






### 2) Create a volume called "the_data_base":


Inside the CLI (Git bash for example run these commands)

<b>

```bash
docker volume create the_data_base
```
</b>

Then validate that the **the_data_base** volume has been created, using
this command
<b>

```bash
docker volume ls
```
</b>

A volume called "**the_data_base**" should appear now.






### 3) cd into project directory:

1. Download the the project form github.
2. Open your CLI (Command Line Interface)
3. cd (Change Directory) into the project directory  
	So that you can execute commands here  
	for more info about how to change directory, 
	watch this video on Youtube:<br><a 
	href="https://www.youtube.com/watch?v=oQc-2gsjgDg">
	Youtube: Git Bash, Bash Basics</a>
4. validate that you are in the correct directory using the command  
	<b>
	
	```bash
	ls
	```
	
	</b>

	and now should see a list of file and direcories in this folder  
	It should include **app.py**




### 4) Run it:
Inside the CLI (Command line interface), run this command:
<b>

```bash
docker-compose up --force-recreate --build -d
```

</b>
It will take a while, let it take it's time.




### 5) Validate that every thing is running correctly:


1. **Open** your favourite **browser**  
(Like Google chrome, or Firefox)

2. **Open three** different **tabs**

3. In the tabs, in the address bar, type these

<b>

```address
http://127.0.0.1:5000/
```
```address
http://127.0.0.1:5001/
```
```address
http://127.0.0.1:5002/
```

</b>


4. Make sure that you do not see any error



5. Run this command:

	<b>
	
	```bash
	docker ps
	```
	
	</b>
	Now you will see a list of the running containers.<br>
	There are 3 containers






### 6) Connected to same volume:

Now, Keep refreshing each tab, to make sure that are connected 
to the same db.  
This db is inside the volume that we have created earlier.















## Return to the original docker setup:

Now after you have executed these commands, you want to return to the
original setup.



### 1) Delete the containers

Run this command to show the conatiners

<b>

```bash
docker ps -a
```

</b>
Now you will see a list of the running containers.<br>
Copy the id of each one of them, and use it in the following command:
<b>

```bash
docker rm -f <conatiner1 id> <conatiner2 id> <conatiner2 id>
```

</b>
Now validate that the conatainers have been deleted, using this command:
<b>

```bash
docker ps -a
```

</b>






### 2) Delete the images

Run this command to show the images

<b>

```bash
docker images
```

</b>
Now you will see a list of the images.<br>
<b>Note: the image id is repeated.</b><br>
Copy the id of one of them, and use it in the following command:

<b>

```bash
docker rmi -f <image1 id>
```

</b>
Now validate that the images have been deleted, using this command:
<b>

```bash
docker images
```

</b>



### 3) Delete the volume

Run this command to show the volumes

<b>

```bash
docker volume ls
```

</b>
Now you will see a list of the volumes.<br>
<b>Note: there is a volume called "the_data_base".</b><br>
Now delete this volume using this command:
<b>

```bash
docker volume rm the_data_base
```

</b>
Now validate that the volume have been deleted, using this command:
<b>

```bash
docker volume ls
```

</b>

Now the volume is not among the volumes.



