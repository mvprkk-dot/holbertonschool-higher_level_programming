The ``say_my_name`` module
============================

Using ``say_my_name``
---------------------

First import ``say_my_name`` from the ``3-say_my_name`` file:

    >>> say_my_name = __import__('3-say_my_name').say_my_name

    >>> say_my_name("Jane")
    My name is Jane 

    >>> say_my_name("John", "Smith")
    My name is John Smith

    >>> say_my_name("brown", 8)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string

    >>> say_my_name(8, 8)
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

    >>> say_my_name(float('inf'), "White")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

    Handle NaN:

    >>> say_my_name(float('NaN'), "White")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string

    >>> say_my_name()
    Traceback (most recent call last):
    	      ...
    TypeError: say_my_name() missing 1 required positional\
        argument: 'first_name'
    
