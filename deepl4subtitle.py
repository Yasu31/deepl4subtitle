#!/usr/bin/env python3
import deepl
import argparse
import re

parser = argparse.ArgumentParser(description='Translate subtitles from one language to another.')
parser.add_argument('-i', '--input', help='Input .sbv file', required=True)
parser.add_argument('-o', '--output', help='Output .sbv file', required=True)
parser.add_argument('-k', '--key', help='Deepl PI key', required=True)

args = parser.parse_args()
input_file = args.input
output_file = args.output
key = args.key
print(f"Input\t{input_file}\tOutput:\t{output_file}")

formatted_input = ""
with open(input_file, 'r') as reader:
    formatted_input = reader.read()

# replace timestamps inside .sbv file to XML tags so that it will be ignored by deepl
formatted_input = re.sub(r'^([0-9]:[0-9]+:[0-9]+.[0-9]+,[0-9]:[0-9]+:[0-9]+.[0-9]+)\n', r'<timestamp ts="\1"/>', formatted_input, flags = re.MULTILINE)
# remove newlines
formatted_input = re.sub(r'\n', '', formatted_input)

with open("intermediate1.txt", 'w') as writer:
    writer.write(formatted_input)

print(f"check intermediate.txt and see that all timestamps are converted to XML. If OK, press ENTER and translation will continue\n(will use your credit!)")
input()

translator = deepl.Translator(key)
print("Translating...")
# with the tag_handling = "xml" option, XML tags will be ignored by deepl
formatted_output = translator.translate_text(formatted_input, target_lang="EN-US", tag_handling="xml").text
print("Done!")

with open("intermediate2.txt", 'w') as writer:
    writer.write(formatted_output)

# put back the timestamps
formatted_output = re.sub(r'<timestamp ts="(.+?)"/>', r'\n\n\1\n', formatted_output, flags = re.MULTILINE)

# write to file
with open(output_file, 'w') as writer:
    writer.write(formatted_output)
print(f"written result to \t{output_file}")