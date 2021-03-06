# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run instructions](README.md#run-instructions)
4. [Test instructions](README.md#test-instructions)
5. [Questions?](README.md#questions?)

# Problem

The purpose of the script `h1b_stats.py` is to process H1B visa application data contained in a semicolon-separated file and provide the top occupations and states for certified applications.

There are several problems to overcome to achieve this. First, the data need to be read. Then, we have to filter the data to find the values associated with occupation and state, and count corresponding certified applications. After this, the count data need to be sorted in a decreasing fashion for the number of application, but in increasing alphabetical order in case there are ties between occupations. Finally, the data have to be written to a text file. All of this should be achieved without the help of non-standard modules such as `pandas`.

# Approach

## Read the data

To read the data, I implemented the function `read_csv` which takes the input file name as argument. Since the user is expected to put the data in the `./input/` folder, I use the `join` function of the `os.path` module so the user can simply type the file name.

First, I declare an empty list, which I will fill with lines I read from the `csv` file. Initially, I considered the use of a named tuple but nested lists provide the same functionality with simpler use (for example, named tuples are less flexible for column names). I open the file using `with ... as ...:` to automatically manage file opening and closing, and use the *utf-8* encoding to prevent errors during file reading. Finally, a reader object from the `csv` module is declared with the appropriate delimiter (semicolon) and rows are iteratively read and added to the previously declared list. The function returns the list containing the data in nested lists. Each nested list contains one row of the original `csv` file.

## Get top occupations or states for certified applications

To filter the data, count the occupations or states, and save the results as a text file, I implemented two similar functions called `get_top_occupations` and `get_top_states`. These functions take the following arguments: *data* is the list generated by the `read_csv` function, *top* is the number of top occupations or states which should be returned, and *output_name* is the name of the file where the user expects to find the results. 

First, I extract the column names which are stored in the first nested list of the *data* list. I put the first nested list, which contains row names, in a list called *col_names*. To get the column indexes where I can find the application status and the occupation name, I scan through *col_names* to find the ones containing the strings 'STATUS' or 'SOC_NAME'. I can now collect the occupation names and put them in a list. I iteratively go through data rows in the *data* list and append the occupation name of this row if the status corresponds to 'CERTIFIED'. The process is similar for top states, except I am looking for columns names containing 'WORKSITE_STATE' (for 2015 and 2016 data) or 'WORKLOC1_STATE' (in the case of 2014 data). Data from 2014 also have a column called 'WORKLOC2_STATE' but what it represents is not clear and a lot of rows are missing, so for now I assumed this was not the relevant column.

To count the number of each occupation, I use the `Counter` tool from the `collections` module. There is a useful function called `most_common` which enables getting the *n* most common occurences. To sort the data according to our problem definition I use a lambda function. I first sort the top occurences by number, then by name in reverse order. This is done because we want to sort the top occupations in states by decreasing number but have ties sorted by alphabetical order of their names.

Then, the total number of certified applications is calculated using the `sum` function on the method `values` of the `Counter`. We will calculate the percentage of certified application for the top occupations or state when the data are saved in the text file.

Finally, the data are saved in a text file using the `writer` object from the `csv` module. Using `open ... as ...:` to automatically open and close the file, we first write column names then iteratively go through the list of top occupations or states and write them as rows of the text file. Similar to path management for the `read_csv` function, we use `os.path.join` to save the text file in the `output` directory.

Both `get_top_` functions return a list of tuples of the top occupations or states, although there are not used. This is why we set dummy variables as underscore when the code executes as a script.

## Running h1b_stats.py as a script

When the code is executed as a script, I collect the name of the input and the two output files with `sys.argv` and call the functions defined in the script.

# Run instructions

To run the script, place the input `csv` file in the `input` folder then navigate to the top of the `h1b_stats` directory and run `run.sh` in your shell. It is also possible to directly run the script `h1b_stats.py` in the `src/` folder by navigating to the top of the `h1b_stats` directory and entering the following instructions in the shell: `python3 ./src/h1b_stats.py <input-file-name> <output-file-name-1> <output-file-name-2>`. The output files will be saved in the output folder.

# Test instructions

The folder `insight_testsuite` contains utilities to test the script `h1b_stats.py`. The shell script `run_tests.sh` will test repository structure and output for the test. A unit test is available for the function `read_csv` of the `h1b_stats.py` script in the folder `insight_testsuite/tests/test_read_csv`. To run it, navigate to this folder and run `test_read_csv.py` with Python in the console.

# Questions?

If you cannot find an answer to you question in this README email me at jonathan.schnabel31@gmail.com
