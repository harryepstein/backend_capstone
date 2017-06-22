# Django Sleep Tracker
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A django webapp where users chronicle their sleep habits and data, gaining valuable insights into their data

## Table of Content

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## About
Hi I'm Harry

### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django and REST framework:
```
pip install django
```

```


## Installation
```
git clone https://github.com/harryepstein/backend_capstone.git
cd thesleeptrackerapp
```
Setting up the database:

```
./refresh_database.sh
```
Run project in browser:

```
python manage.py runserver
```

Wanna be a SuperUser of the future. Try this:

```
python manage.py createsuperuser:
url: '/login'
```




## Usage
User can input data in the morning and evening for storage in the database and display on the homepage.


## Contribute
1. Fork it!
2. Create your feature branch:
```git checkout -b <new-feature-branch-name-here>```
3. Commit your changes:
```git commit -m 'Add some feature'```
4. Push to the branch:
```git push origin <new-feature-branch-name-here-too>```
5. Submit a pull request :D

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits

Contributor:
  * [Harry Epstein](https://github.com/harryepstein)


## License
[MIT © Harry Epstein](./LICENSE)
