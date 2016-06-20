## convert-json-to-d3-csv

This is a little script that can convert any JSON file to CSV that can be used in D3.

I usually get confused when I downloaded a JSON file, finding the correct key or value I want to call in the JSON document. This little tool helps me to visualize the JSON content into a tree struccture.

## Usage

Simply type this command in Terminal:

```bash
$ python convertToCSV.py [inputFileName].json
```

The output will shows up in the "output" directory.

Tested with Python 3.4.3.

## What else?

You can view the visualized tree by open "/output/tidyjsontree.html", powered by [D3.js](http://d3js.org) and the ["Tidy Tree" block](http://bl.ocks.org/mbostock/9d0899acb5d3b8d839d9d613a9e1fe04) made by [Mike Bostock](http://bl.ocks.org/mbostock).
