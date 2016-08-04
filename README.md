# HideMyPython!
	 _    _ _     _      __  __       _____       _   _                 _ 
	| |  | (_)   | |    |  \/  |     |  __ \     | | | |               | |
	| |__| |_  __| | ___| \  / |_   _| |__) |   _| |_| |__   ___  _ __ | |
	|  __  | |/ _` |/ _ \ |\/| | | | |  ___/ | | | __| '_ \ / _ \| '_ \| |
	| |  | | | (_| |  __/ |  | | |_| | |   | |_| | |_| | | | (_) | | | |_|
	|_|  |_|_|\__,_|\___|_|  |_|\__, |_|    \__, |\__|_| |_|\___/|_| |_(_)
								 __/ |       __/ |                        
								|___/       |___/                         
A parser for the free proxy list on HideMyAss! **Now, it can be imported as Python package.**

## Declaration

This origin sources belong to [the-useless-one][hide_my_python].
My works is making `hide_my_python` into a Python package, and some modifications to simplify.

*Note: All `pr`-prefixed commits come from pull requests in original project [hide_my_python][hide_my_python-pr].*

[hide_my_python]: https://github.com/the-useless-one/hide_my_python
[hide_my_python-pr]: https://github.com/the-useless-one/hide_my_python/pulls

## Requirements

Python 2.7+, Python 3.3+

## Installation

```bash
$ pip install git+https://github.com/leVirve/hide_my_python#egg=hidemypython
```

or

clone the project, and then

```bash
$ python setup.py install
```

## Usages

### Programable

```python
	from hidemypython.proxy_parser import generate_proxy
	from hidemypython.utils import Dict

    params = Dict(
        number_of_proxies=20,
        countries_list=['Taiwan', 'Japan'],
        ports=[80, 8080],
        protocols=['http', 'https', 'socks'],
        keep_alive=True,  	# choices: Treu / False
        anonymity=3,  		# levels from (0, 1, 2, 3)
        speed=2,  			# levels from (0, 1, 2)
        connection_time=2,  # levels from (0, 1, 2)
        verbose=False
    )

    proxies = generate_proxy(params)  # a <generator> of available proies!!
```

### Command line

For a command line feature, you should add lines shownbelow into your `setup.py`

```python
    entry_points = {
        'console_scripts': ['hidemypython=hidemypython.cli:main'],
    },
```

Just go to your favoriate terminal and with the following command:

```bash
    $ hidemypython -o <output_file>
```

where `output_file` is the database file where the proxies will be stored.


To see a list of the options, just issue:

	$ hidemypython -h
	usage: hide_my_python [-h] -o DATABASE_FILE [-n NUMBER_OF_PROXIES]
						  [-ct COUNTRIES_FILE] [-p PORTS [PORTS ...]]
						  [-pr {http,https,socks} [{http,https,socks} ...]] [-a]
						  [-ka] [-s] [-c] [-v]

	A parser to retrieve proxies from HideMyAss!

	optional arguments:
	  -h, --help            show this help message and exit
	  -o DATABASE_FILE      database file where the proxies will be saved
	  -n NUMBER_OF_PROXIES  maximum number of proxies to retrieve (default: all)
	  -ct COUNTRIES_FILE    file containing the countries where the proxies can be
							based (default: countries_all)
	  -p PORTS [PORTS ...]  list of ports (max: 20 ports) the proxies listen on
							(default: every port)
	  -pr {http,https,socks} [{http,https,socks} ...]
							protocols used by the proxies (default: HTTP, HTTPS
							and SOCKS4/5)
	  -a                    flag used to determine the proxies minimum anonymity
							level, e.g. -a sets the minimum anonymity level to
							Low, -aa to Medium, -aaa to High, etc. (default
							minimum level: None)
	  -ka                   flag used to determine if proxies with the Keep Alive
							option should be returned, as they are likely honey
							pots (default: no)
	  -s                    flag used to determine the proxies minimum speed
							level, e.g. -s sets the minimum speed level to Medium,
							-ss to Fast (default minimum level: Slow)
	  -c                    flag used to determine the proxies minimum connection
							time level, e.g. -c sets the minimum connection time
							level to Medium, -cc to Fast (default minimum level:
							Slow)
	  -v                    explain what is being done

	Go to https://hidemyass.com/proxy-list/ to see the different available
	options.

### Database file

The proxies will be saved in this file. If the file doesn't exist, it will be
created. If it exists, the proxies will be appended to it (the file won't be
overwritten). The database contains only one table, named `proxies`, with the
following structure:

* `id`: a unique identifier (type: `INTEGER PRIMARY KEY AUTOINCREMENT`)
* `ip`: the proxy's IP address (type: `TEXT`)
* `port`: the port the proxy listens on (type: `INTEGER`)
* `type`: the type of the proxy (HTTP, HTTPS or SOCKS4/5) (type: `TEXT`)
* `country`: the country the proxy is based in (type: `TEXT`)
* `anonymity`: the anonymity level guarantied by the proxy (type: `TEXT`)
* `speed`: the speed level of the proxy (type: `TEXT`)
* `connection_time`: the connection time of the proxy (type: `TEXT`)

### Number of proxies

If this argument is defined, the script will only return the first `n`
proxies he finds. Otherwise, every found proxy will be returned. For example:

	$ hidemypython -n 25 -o output.db

will only return the first 25 proxies.

### Countries file

The script will only return proxies based in the countries specified in this
file. To see a complete list of the available countries, see the file
`countries_all`.

### Ports

The script will only return proxies listening on the specified ports. You can
specify up to 20 different ports. For example:

	$ hidemypython -p 80 8080 443 -o output.db

will only return proxies listening either on port 80, 8080, or 443.

### Protocols

The script will only return proxies using the specified protocols. The possible
protocols are HTTP, HTTPS, and SOCKS4/5. For example:

	$ hidemypython -pr http socks -o output.db

will only return proxies using HTTP or SOCKS4/5.

### Anonymity

The script will only return proxies guarantying an anonymity level greater
than the one specified by the user. HideMyAss! proxies have these anonymity
levels:

* None
* Low
* Medium
* High
* High + Keep Alive

**WARNING:** Here's what HideMyAss! has to say on proxies with Keep Alive:

> If a high-anonymous proxy supports keep-alive you can consider it to be
> extremely-anonymous. However, such a host is highly possible to be a
> honey-pot.

**Use these proxies at your own risk!**

By default, the script doesn't take into account the proxies' anonymity
(they can have an anonymity level of None, High, Medium, ...). But this
command:

	$ hidemypython -a -o output.db

will only return proxies with an anonymity level of at least Low.

This command:

	$ hidemypython -aa -o output.db

will only return proxies with an anonymity level of at least Medium.

### Keep Alive

As said on the HideMyAss! proxy list, proxies with the Keep Alive option are
most likely honey pots. In order to avoid them, the script, by default, doesn't
retrieve proxies with an anonymity level of High +KA. If you want proxies with
the Keep Alive option, use this flag:

	$ hidemypython -ka -o output.db

### Speed

The script will only return proxies guarantying a speed level greater
than the one specified by the user. HideMyAss! proxies have these speed 
levels:

* Slow
* Medium
* Fast

By default, the script doesn't take into account the proxies' speed (they can
have a speed of Slow, Medium, Fast). But this command:

	$ hidemypython -s -o output.db

will only return proxies with a speed level of at least Medium.

This command:

	$ hidemypython -ss -o output.db

will only return proxies with a speed level of at least Fast.

### Connection time

The script will only return proxies guarantying a connection time level greater
than the one specified by the user. HideMyAss! proxies have these connection
time levels:

* Slow
* Medium
* Fast

By default, the script doesn't take into account the proxies' connection time
(they can have a connection time of Slow, Medium, Fast). But this command:

	$ hidemypython -c -o output.db

will only return proxies with a connection time level of at least Medium.

This command:

	$ hidemypython -cc -o output.db

will only return proxies with a connection time level of at least Fast.

### Verbose mode

If the `-v` flag is used, the script will described what is being done.
First, it will display the arguments, then it will print the progress of the
parsing.

	$ hidemypython -o output.db -p 80 8080 -n 100 -v
	[info] number of proxies: 100
	[info] countries: ['China', 'Indonesia', 'United States', 'Brazil', 'Venezuela'] and 86 more
	[info] ports: 80, 8080
	[info] protocols: ['http', 'https', 'socks']
	[info] anonymity: ['None', 'Low', 'Medium', 'High']
	[info] speed: ['Medium', 'High']
	[info] retrieved 100/100 proxies

## COPYRIGHT

HideMyPython! - A parser for the free proxy list on HideMyAss!

Yannick Méheut [useless (at) utouch (dot) fr] - Copyright © 2013

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at your 
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
Public License for more details.

You should have received a copy of the GNU General Public License along 
with this program. If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).
