# TermsForTerms
This repository includes the code for the TermsForTerms infrastructure for mapping legal documents onto graphical analogs. These analogs can be visualized, merged, or compared, providing a framework to make data governance more salient and accessible.

Instructions for installation:
Please first install graph_tool on your machine. The instructions for this can be found here: https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions.
Then, install the termsforterms package using the below command.
```
python3 -m pip install --index-url --no-deps https://test.pypi.org/simple/ termsforterms
```
Now, you can import termsforterms into a python package 
```
import termsforterms
```
or
```
from termsforterms import *
```
Note that the second option is preferred, since it will provide all the infrastructure needed for manipulating the graphs. This option should be used if running the test in LogicalFormatExamples/abridgedTest/AbridgedTest.py. To use this test, please also change the paths in the file to match your desired output locations.