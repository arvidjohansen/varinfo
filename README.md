# varinfo
**varinfo** is a set of helper functions for displaying human friendly information about an object's attributes.

```python
>>> from varinfo import varinfo
>>> file = open('example.txt')
>>> varinfo(file)
["buffer -> <class '_io.BufferedReader'>",
 'close()',
 'closed: bool -> False',
 'detach()',
 'encoding: str -> cp1252',
 'errors: str -> strict',
 'fileno()',
 'flush()',
 'isatty()',
 'line_buffering: bool -> False',
 'mode: str -> r',
 'name: str -> example.txt',
 "newlines -> <class 'NoneType'>",
 'read()',
 'readable()',
 'readline()',
 'readlines()',
 'reconfigure()',
 'seek()',
 'seekable()',
 'tell()',
 'truncate()',
 'writable()',
 'write()',
 'write_through: bool -> False',
 'writelines()']
>>>
 ```


