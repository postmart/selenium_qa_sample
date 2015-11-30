####This is a quick sample for QA test case.

Test case template is available here:
```
test_cases
   └── SearchTestTemplate.xls
```

Auto test sample for this test case is available at:
```
tests
  └──── SearchMainPage.py
```

Web browser to test with can be specified in `base/TestSettings.py` file.

Reports are generated in `reports` folder:
```
reports
  └── SearchPage.html
```

#### Requirements
- selenium
- phantomjs (optional, if headless browser support is needed)
- page_objects

Run `pip install -r requirements.txt` to install dependencies (selenium and page_objects).

To download phantomjs, visit: http://phantomjs.org/download.html