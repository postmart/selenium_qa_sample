This is a sample for a docker container that includes all the dependencies for
running test framework (selenium, page-objects and phantomjs).

- https://www.docker.com

To build image locally, run:
```
docker build -t postmart/test_machine .
```

To run container:
```
docker run -t -i postmart/test_machine
```

To run test in container:
```
root@752c8be4c15f:/# cd qa_sample/auto_test/tests/ && python SearchMainPage.py
```

p.s. You may want to run docker container with -v option to share volumes for easy access of test report.
