### This project is a REST API for N

### The instructions are linux based

#### Prerequisites: installed python, pip

#### Clone the repository with:

```
~git clone https://github.com/healta/nbs_API.git
```

```
~cd nbs_API
```

##### To run in a virtual environment you'll need

```
~pip install virtualenv
```

```
~virtualenv –-version(to validate install)
```

```
~virtualenv virtual_env_name
```

##### To activate it

```
~source home/user/Downloads/nbs_API/virtual_env_name/bin/activate
```

```
~pip install -r requirements.txt
```

##### To run the API

```
~uvicorn main:app --reload
```

##### Datapoints

| Datapoint                | HTTP Method | Description                              |
| ------------------------ | ----------- | ---------------------------------------- |
| /articles/               | GET         | get all articles                         |
| /articles/?label={label} | GET         | get list of articles with the same label |
| /articles/?date={date}   | GET         | get list of articles from the date       |
| /article/{article_id}    | GET         | get a single article                     |
| /article/{article_id}    | DELETE      | delete a single article                  |
| /article/{article_id}    | PUT         | update the text of a single article      |
