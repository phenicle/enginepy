# enginepy
A simple and powerful python API for running external commands.

Arguments toggle the behavior of STDOUT and STDERR. 
* DISPLAY   - prints stdout to stdout, stderr to stderr
* CAPTURE   - returns stdout as result['stdout'], stderr as result['stderr']
* IGNORE    - ignores the value
* APPEND    - append to a file you specify
* OVERWRITE - write to a file you specify


Specify stdout_filepath or stderr_filepath using keyword arguments.

The result returned is a dictionary.

The return code is found in result['code'].

```
    result = Engine('ls -l', Engine.CAPTURE, Engine.CAPTURE).run()
    pprint(result)
```
