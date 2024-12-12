# Text Clean-up Script

A simple Python script to remove abstract sections from references in a bibliography file and reformat indentation for improved readability and transfer into LaTex. Created for personal use when creating PhD thesis bibliography, however it can be adapted for any text file that requires similar edits. 

Current Features:

* Automatically removes abstract = { ... } and trailing comma. 
* Re-indents entries for consistent formatting.

Run following code in command-line and change the directory paths;

```
python txt_converter.py /path/to/input_file.txt /path/to/output_file.txt
```

Additional Ideas:

* Extend the script to handle other unwanted fields.
* Enhance error handling for missing files or permissions.
* Customize command-line options for further things. 
* Improving user-friendlyness
