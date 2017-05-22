# appypod-pdf-rendering-service

Flask-based microservice docker image to render a PDF document from an
ODT template and JSON values using
the [appy.pod](http://appyframework.org/pod.html) Python library.

## To Run

    $ cd appypod-pdf-rendering-service
    $ docker build -t appypod-pdf-rendering-service .

## To Test

    $ cd test

Either

    $ curl -F "tmpl=@test.odt" -F "values=@values.json" localhost -O -J

or

    $ python test.py

They both should result in a `test.pdf` rendered file.

## Caveats

* appy.pod is Python 2 only
* Runs the Flask server directly (using uWSGI e.g. would be more robust)
