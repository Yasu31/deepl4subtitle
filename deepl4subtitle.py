#!/usr/bin/env python3
import deepl
import argparse

parser = argparse.ArgumentParser(description='Translate subtitles from one language to another.')
parser.add_argument('-i', '--input', help='Input .sbv file', required=True)
parser.add_argument('-o', '--output', help='Output .sbv file', required=True)
parser.add_argument('-l', '--key', help='Deepl PI key', required=True)

args = parser.parse_args()
input_file = args.input
output_file = args.output
key = args.key
print(f"Input\t{input_file}\tOutput:\t{output_file}")

formatted_input = ""
with open(input_file, 'r') as reader:
    formatted_input = reader.read()
