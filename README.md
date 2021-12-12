# Welcome to our New Year's greeting card G2-20

This program generates personalized and creative poem/prosa/haiku greeting cards automatically when given user's information on the webpage. The recipients can be friends, family, lovers, or colleagues depending on users' needs.

As the Chinese New Year comes soon, the user can also generate personalized and creative Chinese New Year's greeting cards upon his/her needs.

This program also includes a feedback platform that provides the user with a chance to add their datasets if they are not satisfied with the outputs. The neural network will then retrain after adding 50 sentences.


**Developers:**  

	Fischer,Janika
	Senbayrak, Serdar Doruk
	Wan, Qingfangzi   
	Sanhinova, Malika 
	Michalopoulos, Georgios  

**Version:** 07.02.2021

## Setup

1. Go to the python-model folder and install a virtual environment (if you use MacOS or Linux, please remove the encoding "mbcs")

2. Execute the api.py in the environment

3. Open another terminal and navigate to the client-app folder

4. Install 'node-modules' and go to a browser of your choice

5. Open up localhost:8080 and start our app

#### Run the server-side Flask app in one terminal window:
```
$ cd python-model
```

```
$ python3.7(3.8) -m venv env
```

```
$ source env/bin/activate
```

```
(env)$ pip install -r requirements.txt
```

```
(env)$ python api.py
```

Navigate to http://localhost:5000

### Run the client-side Vue app in a different terminal window:

```
$ cd client-app
```

```
$ npm install
```

```
$ npm run serve
```
Navigate to http://localhost:8080
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
