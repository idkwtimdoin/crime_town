# some_project 🔬📊🔥
small python tutorial

<p align="center">
  <img
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Seal_of_the_Central_Intelligence_Agency_%28B%26W%29.svg/500px-Seal_of_the_Central_Intelligence_Agency_%28B%26W%29.svg.png"
      style="width: 10vw; min-width: 20px;"
  />
</p>

## objective
* create a backend app for the FBI in the USA (API and database) where the user would be able to:
> API:

    1. filter crimes by year, month, crime type, case status

        1.1. crime type: murder, attempted murder, arson, etc
        1.2. case status: unsolved, cold case, pending, Casey-Anthony-solved, you get it ...

    2. optional filters for fun 🔥: crime name, criminal name, race 

        2.1. crime name: greenlease kidnapping, 9/11, JFK assassination (Casey-Anthony-solved status probably), etc
        2.2. criminal name: just go on chatGPT and generate thug names
        2.3. race: _... i am not getting cancelled for a stupid project_

> Database:

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
        name: str   # full name, skip the first name last name bs
        age: int
        race: Enum  # lol

    class Case:
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
> Necessary Utils

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

> Suggested `make` utils

1. `make install` for installing python packages `requirements.txt`
2. `make clean` delete db container volume / clean project
3. `make test` for running pytests
4. `make lint` for formatting linting your code
