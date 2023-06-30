# tvo

#Testcases
  1) Verify "featured documentary" section is present or not.
  2) Verify "featured documentary" title.
  3) Verify "featured documentary" description
  4) Verify "featured documentary" Watch Now button URL link.
  5) Verify "Recently Added" list.
  6) Verify "See More" links.

#Automation
  1) POM is used - scalable for any pages with the root URL docs and series.
  2) POM Pages read locators from locator.json ( central file for all locators ).
  3) POM Page design changes if you are working on a page with fields / forms etc. In this case, all clicks are done here and sending results back but no assertion done here so it can be used as common method for different tests. 
  4) Assuming every page has separate test data ( json file ), testdata file name matches the page file name
  5) different test data can be passed for the same testfile since "recently added", "featured documentary" etc will be keep changing  so you can pass the appropriate testdata json file ( can be passed jenkins file parameter or just update in repo.)
  
  6) HTML report (pytest-html) is generated using the command  python -m pytest -v -s  --capture=tee-sys  --html=reports/report.html
  7) New log file is created for every run. This can be saved /copied in Jenkins CI/CD before running the framework. SO no need of saving old reports in repo or framework itself.
  8) Parallel execution (pytest-xdist) can be done using the command - python -m pytest -v -s  -n 6  --capture=tee-sys  --html=reports/report.html
  9) conftest is setup at the class level which also gives you driver, util, and page objects and these are initialized only once and passed around test cases.
  10) testcase has all assertions
  


     
