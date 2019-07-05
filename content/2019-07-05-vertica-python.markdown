Title: Developing Python on Vertica
Author: Andy Reagan
Date: 2019-07-05

Vertica is a very powerful analytics database,
and we can easily extend functionality now by building in Python functions.
This is great and all,
so here I'll focus on setting up a development environment for building a simple UDx.

For the local setup, we'll be using https://github.com/jbfavre/docker-vertica/.
I'm going to focus on the CentOS version, since it is most similar to Amazon's RHEL images.
To get started (on OSX, you need the Docker client first):

```
docker pull jbfavre/vertica:9.2.0-7_centos-7
```

Also take a second to get [Python 3.5.1 here](https://www.python.org/downloads/release/python-351/).
Those are the two steps that require the most bandwidth!

Now, run that thing:

```
docker run -p 5433:5433 jbfavre/vertica:9.2.0-7_centos-7
```

Grab the name of the running container from `docker ps` command, and set it to `$DOCKER_NAME`, and copy in our Python source:

```
DOCKER_NAME=suspicious_chatelet
docker cp Downloads/Python-3.5.1.tgz $DOCKER_NAME:/home/dbadmin/
```

Phew! We're done with the parts that are specific to a local setup.
If you're working on a server somewhere, copy up the `Python-3.5.1.tgz`
and put it at `/home/dbadmin/Python-3.5.1.tgz`.
For good measure (i.e., if you copied with the root user) make sure it's owned by `dbadmin`:

```
chown dbadmin /home/dbadmin/Python-3.5.1.tgz
```

As root, do
```
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
```

Grab a coffee.

Still as root,

```
cd /home/dbadmin/Python-3.5.1
./configure
make
make install
```

Probably another coffee for that one!

If you run the above as `dbadmin`, which you should, skip the `make install` line.
Or only do that last line as `root`.

Maybe still as root, though again this should be fine (and preferable) as dbadmin user in the `/home/dbadmin` directory. If you used root for anything above other than `make install`, you might need to keep `root` user active. Here goes:

```
Python-3.5.1/python -m venv pyenv
pyenv/bin/pip install -U pip
pyenv/bin/pip install requirements.txt
```

If you're within a firewall, you might need `--index-url=[your company's artifactory]` for the pip install lines.
What is the `requirements.txt` line? All of the packages that your function needs,
just like the requirements file from any python package.

Finally you should be able to execute the SQL needed to build your function!
Put your code in `myfunction.py` and then you can run `vsql` as dbadmin, and do:

```
\set libfile '\''`pwd`'/myfunction.py\''
DROP LIBRARY mylib CASCADE;

CREATE LIBRARY mylib AS :libfile DEPENDS '/home/dbadmin/pyenv/lib/python3.5/site-packages/' LANGUAGE 'Python';
CREATE FUNCTION myfunction AS NAME 'myfunction_factory' LIBRARY mylib;
```

Cheers!
