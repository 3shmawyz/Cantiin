# Runnng Cantiin using Docker


## Up And Running:

### 1) Validations:
Inside the CLI (Git bash for example) run these commands

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






### 2) Create a volume called "cantiin_volume":


Inside the CLI (Git bash for example run these commands)

<b>

```bash
docker volume create cantiin_volume
```
</b>

Then validate that the **cantiin_volume** volume has been created, using
this command
<b>

```bash
docker volume ls
```
</b>

A volume called "**cantiin_volume**" should appear now.






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
	It should include **Dockerfile**




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

2. **Open One Browser Tab**

3. In the tab, in the address bar, type this

<b>

```address
http://127.0.0.1:5000/
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
	There is 1 container





## Return to the original docker setup:

Now after you have executed these commands, you want to return to the
original setup.



### 1) Delete the container

Run this command to show the conatiners

<b>

```bash
docker ps -a
```

</b>
Now you will see a list of the running containers.<br>
Copy the id of the container, and use it in the following command:
<b>

```bash
docker rm -f <conatiner id>
```

</b>
Now validate that the conatainer has been deleted, using this command:
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
Copy the id of one of the image, and use it in the following command:

<b>

```bash
docker rmi -f <image id>
```

</b>
Now validate that the image has been deleted, using this command:
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
<b>Note: there is a volume called "cantiin_volume".</b><br>
Now delete this volume using this command:
<b>

```bash
docker volume rm cantiin_volume
```

</b>
Now validate that the volume have been deleted, using this command:
<b>

```bash
docker volume ls
```

</b>

Now the volume is not among the volumes.



