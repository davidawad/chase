## chase

Chase is the sad, underpaid legal intern that looks up your citations within state laws.

Send him your requests and he'll do all the work for you.


## Getting Started

Chase needs docker, and also uses json files from [statedb](github.com/davidawad/statedb)

```
$ make
# builds the container for you
$ make run
# runs the container for you
$ curl -X GET  -H "Content-Type: application/json" -d '{"keyword":"arson"}' '0.0.0.0:8000/search'
# make requests against chase for keywords
```

## Implementation Details

Chase is implemented in python flask.

He quickly parses through json files and finds relevant information for you.
