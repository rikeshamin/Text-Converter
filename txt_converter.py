import argparse
import re

class TextFormatter:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.indent_level = '    ' # set to 4 indentations

    # this removes the abstract and everything inside the {}, trailing commans and the empty line space after
    def remove_abstract(self, content):
        pattern = r'^\s*abstract\s*=\s*\{.*?\},?\s*[\r\n]*'
        return re.sub(pattern, '', content, flags=re.DOTALL | re.MULTILINE)
    
    # edits the content for the correct indentation
    def correct_indentation(self, content):
        lines = content.splitlines()
        processed_lines = []
        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:
                processed_lines.append('\n')
            elif stripped_line.startswith('@article'):
                processed_lines.append(stripped_line + '\n')
            else:
                processed_lines.append(self.indent_level + stripped_line + '\n')
        return ''.join(processed_lines)
    
    def format_file(self):
        with open(self.input_path, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()
        content = self.remove_abstract(content)
        content = self.correct_indentation(content)
        with open(self.output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Abstract sections removed and file formatted.")

# Providing directory paths for input and output in command line. 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove abstract sections and reformat a references file.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("output_file", help="Path to the output file.")
    args = parser.parse_args()

    formatter = TextFormatter(input_path=args.input_file, output_path=args.output_file)
    formatter.format_file()







