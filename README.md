# help the FBI 🔬📊🔥
small python tutorial
<p align="center">
  <img
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Seal_of_the_Federal_Bureau_of_Investigation.svg/300px-Seal_of_the_Federal_Bureau_of_Investigation.svg.png"
      style="width: 10vw; min-width: 20px;"
  />
</p>

## getting started
```shell
$ pip3 install virtualenv                            # for creating virtual env
$ python3 -m virtualenv .venv                        # init venv
$ source .venv/bin/activate                          # activate
$ (.venv) pip3 install --upgrade pip
$ (.venv) pip3 install -r requirements.txt           # install requirements for venv
```

## objective
* create a backend app for the FBI in the USA (API and database) where the user would be able to:
### API:
1. filter crimes by year, month, crime type, case status

    1.1. crime type: murder, attempted murder, arson, etc

    1.2. case status: unsolved, cold case, pending, Casey-Anthony-solved, you get it ...

2. optional filters for fun 🔥: crime name, criminal name, race

    2.1. crime name: greenlease kidnapping, 9/11, JFK assassination (Casey-Anthony-solved status probably), etc

    2.2. criminal name: just go on chatGPT and generate thug names

    2.3. race: ... fuck if you know

### database:
1. should store all the above mentioned stuff
2. archi suggestions:
```python
    class Crime:
        _id: str
        datetime_start: str
        datetime_end: str
        location: str
        type: str
        name: Optional[str]

    class Criminal:
        _id: str
        name: str   # full name, skip the first name last name bs
        age: int
        race: Enum  # lol

    class Case:
        _id: str
        crime_id: str                   # references Crime._id
        crime_name: Optional[str]       # references Crime.name
        criminals: Optional[List[str]]  # references Criminal.name
        status: str
        date_open: str
        date_closed: Optional[str]
        suspects: Optional[List[str]]
        lead_detective: List[str]
        funds_allocated: Optional[float]    # in case of Casey Anothony: probably 15 bucks

    class Detective: ...    # ?

    # but of course you do what you want
```
### necessary deliverables
1. A module for RNGing a bunch of crimes, criminals and linking some in solved cases: 1-to-1, multi-to-1, 0-1 etc.\
    suggested tools: 
    * chatGPT for RNGing random crime & criminal names
    * `numpy`, `pandas` for simulating population curves, stddevs
2. Unit tests in `test/`
    * using `pytest` with `conftest` probably
3. API documentation
    * probably `fastAPI swagger` is easiest
4. containerized database and API app in `docker-compose.yml`
5. A `make` command for generating some crime stats using `mkdocs`
6. good degree of modularity

### extras
1. play with different kinds of API methods for each enpdoint
2. realistic stats lmao

### suggested `make` utils
1. `make install` for installing python packages `requirements.txt`
2. `make clean` delete db container volume / clean project
3. `make test` for running pytests
4. `make lint` for formatting linting your code

### make sure:
1. REST API standards
2. good queries, try sqlalchemy
3. follow MVC arch or something standard
4. containerize both the API and the db
