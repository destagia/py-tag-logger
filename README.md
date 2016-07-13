# Python Tag Logger

## Filtering your stdout with tag!

Using `tlogger.log` function but not `print` function, it must give us happy hacking life, I'm not sure tho :D

## Instration

```
pip install git+https://github.com/miyatin/py-tag-logger.git
```

## Usage

```python
import tlogger as tl

tl.log("hello", "Youtube")
tl.log("world", "is mine")
```

Then run your application or scripts with Args!

```
$ python yourapp.py -vt hello
```

This results in
```
#hello Youtube
```

In the other case,
```
$ python yourapp.py --verbose
```

```
#hello Youtube
#wolrd is mine
```

