# Text Clean-Up Script

## Overview
I developed this script to simplify the process of cleaning up and reformatting bibliography files during my PhD. It removes unwanted fields like abstracts and ensures consistent indentation, making it easy to integrate bibliographies into LaTeX or other document preparation workflows. The tool saves time and effort and can be adapted for various text clean-up tasks, ensuring organized and uniform output.

## Features
- **Abstract Removal**: Automatically removes `abstract = { ... }` fields and their trailing commas.
- **Consistent Formatting**: Re-indents bibliography entries for improved readability and uniformity.

---

## Usage
### Command-Line Arguments
The script requires the following command-line arguments:
1. **input_file**: Path to the input text file.
2. **output_file**: Path to save the cleaned text file.

### Example
To clean up a bibliography file located at `/path/to/input_file.txt` and save the results to `/path/to/output_file.txt`, run:
```bash
python txt_converter.py /path/to/input_file.txt /path/to/output_file.txt
```
---

## Additional Ideas
- **Expand Functionality**: Extend the script to handle other unwanted fields such as `doi`, `issn`, or custom tags.
- **Robust Error Handling**: Improve handling for scenarios like missing files, read/write permission issues, or invalid file formats.
- **Enhanced User Options**: Add command-line flags for toggling specific clean-up tasks or handling custom patterns.
- **Improved Usability**: Introduce interactive prompts or configuration files for advanced customization.

---


## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution
Suggestions, feedback, and contributions are welcome! Feel free to star, fork the repository, create issues, or submit pull requests to enhance this tool.

