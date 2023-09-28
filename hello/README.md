# Tested Functions in PyTest

This is a "good practice environment" for running python with continuous
testing and protection of the main branch on github.

## Run (continuous testing mode)

To get a shell with the local directory mounted as `/app`  Changing local files on the host (or container) re-runs `pytest` using `ptw`
```sh
./run 
```

## Run (one-off command)
To run a command in the docker environment
```sh
./run ls -la
```

## Test on push to main

The .pre-push-main file contains a script that must exit (status 0) successfully for a push to the main branch is allowed.



