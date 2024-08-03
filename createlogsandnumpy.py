import numpy as np
import logging as lg

#logging: https://docs.python.org/3/howto/logging.html
"""This is a means of tracking events when a software or program is executed.
There are logging functions associated with the severity or level of importance of the event being monitored. These functions include:
DEBUG: Provides detailed information for diagnostics
INFO: Confirms that an event was executed as expected.
Warning: A flag that something went wrong unexpectedly, or some problem that might occure soon e.g disk space running out.
ERROR: Program broke at somepoint because of a problem that prevented an event from occuring
CRITICAL: A serious issue that stops the program from running.

Most often logging events are tracked in a file. e.g see function that creates different log files.
"""

def creatlogfile(*arg):
##creating a basic log file. To see this result, uncomment and comment the next logger. Result is overriden.
    if arg[0] == 1:
        lg.basicConfig(filename= 'numpyevent.log',filemode='w', encoding='utf-8',level= lg.DEBUG)
        lg.debug("Python strings are immutable objects..")
        lg.info('numpy arrays are used only when data is of same datatype')
        lg.warning("If you are not sure then raise an error")
        lg.error('It is a zero division error!') 

##Create another basic log file with formating. It is not possible to create two log files in the same filename. Result of every run is appended to file.
    elif arg[0] == 2:
        lg.basicConfig(filename='mylogging.log', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s.', datefmt='%d.%m.%Y %I:%M:%S', level=lg.INFO)
        lg.debug("Python strings are immutable objects..")
        lg.info('numpy arrays are used only when data is of same datatype')
        lg.warning("If you are not sure then raise an error")
        lg.error('It is a zero division error!')
##create a logger by confuguration then add a handler and format to it. This is another way to initial a handler object before using its message methods.
    else:
        level = lg.DEBUG
        mylog = lg.getLogger("learningnumpy")
        mylog.setLevel(level)

        "create a console handler and set level. With console handler or streamhandler the logs are printed in the console. To create a file, use filehandler with the expected arguments"
        conhandler = lg.FileHandler(filename="mylogs.log", encoding='utf-8')
        conhandler.setLevel(level)

        "specify the formating for the log entries"
        formater = lg.Formatter(fmt='%(levelname)s: %(asctime)s %(message)s.', datefmt='%d.%m.%Y %I:%M:%S')

        "now add the format to the handler"
        conhandler.setFormatter(formater)

        "now add handler to the logger"
        mylog.addHandler(conhandler)

        "now create logs using the message methods as on examples above"
        mylog.debug("Python strings are immutable objects..")
        mylog.info('numpy arrays are used only when data is of same datatype')
        mylog.warning("If you are not sure then raise an error")
        mylog.error('It is a zero division error!')
    return 

for i in range(1,4):
    creatlogfile(i)


# Numpy arrays
'''This array is designed for scientific computing with alot of libraries and tools around it for optimal computing.
In fact most machine learning calculations expect numpy arrays as input otherwise they convert inputs to numpy arrays,
perform the designated computation and return the results as a numpy arrays. Numpy arrays can be 1...n-dimensions.

when a numpy array is created, its size is set. This means the size of a numpy array cannot be altered or reshaped without creating 
another numpy array. Numpy arrays are always of same datatypes.This must be highly considered before working with numpy arrays. 
These arrays are luckily not bound only to 2-dimensions.
'''
conloglevel = lg.INFO
conlog = lg.getLogger("consol log")
conlog.setLevel(conloglevel)

conuser = lg.StreamHandler()
conuser.setLevel(conloglevel)

formater = lg.Formatter(fmt='%(levelname)s - %(asctime)s - %(message)s', datefmt="%d.%m.%Y %I:%M:%S")

conuser.setFormatter(formater)
conlog.addHandler(conuser)

## 1-dimension array
dt = [1,2,3,4,5,6]
firstdt = np.array(dt)
conlog.info(f'this is my first 1-d array!\n {firstdt}')

## creating a numpy array of zeros
npzeros = np.zeros(5)
conlog.info(f"This is a 1-d array of zeros!\n {npzeros}")

## creating a numpy array of ones
npones = np.ones(7)
conlog.info(f"This is a 1-d array of ones!\n {npones}")

## creating a numpy array using range method
nprange = np.arange(100)
conlog.info(f"This is a 1-d array of ones!\n {nprange}")

## creating a numpy array using range method by specifying start, end and step. The datatype of the array is specified but can be altered with reshape.
nprang = np.arange(1,9,2, dtype= np.int8)
conlog.info(f"This is a 1-d array of ones!\n {nprang}, {nprang.shape}, {nprang.dtype}, {nprang.ndim}")


## creating higher dimensional arrays from a list of list
dt1 = [[1,2,3],[4,5,6],[7,8,9]]
np2_array = np.array(dt1)
conlog.info(f"This is a 2-d array!\n {np2_array}\nwith a shape of:\n{np2_array.shape}\nand a dimension of:\n{np2_array.ndim}\nof type:\n{np2_array.dtype}")
conlog.info(f"The size of the 2-d array is:{np2_array.size}. That is the number of elements in the array.")

# create or reshape a numpy array. Remember that once the shape of an array is set it cannot be change so it is only possible to create a new array from an existing array.
nprange_1 = nprange.reshape(5,2,5,2)
conlog.info(f"the new shape of our array is:{nprange_1.shape} with a dimension of {nprange_1.ndim} and it looks like:\n{nprange_1}")

## performing operations with numpy arrays
np1 = np.arange(9).reshape(3,3)
np2 = np.arange(0,18,2).reshape(3,3)

conlog.info(f'np1 array is:\n{np1}\nnp2 array is:\n{np2}')

'adding numpy arrays'
np3 = np1 + np2
conlog.info(f'\n{np3}')

'multiply numpy arrays'
np4 = np1 * np2
conlog.info(f'\n{np4}')

'dividing numpy by a constant'
np5 = np1 / 2
conlog.info(f'np5 array is:\n{np5}\nand its transpose is\n{np5.transpose()}')
conlog.info(f'The diagonal of np5 is:\n{np5.diagonal()}\nwhile the diagonal of its transpose is:\n{np5.transpose().diagonal()}')

