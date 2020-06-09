from columnar import columnar
import argparse
import glob
import subprocess
import os.path
parser = argparse.ArgumentParser(description='Batch converts one font format to another')
parser.add_argument('input_pattern')
parser.add_argument('output_extension')
args = parser.parse_args()
input_filepaths = glob.glob(args.input_pattern)

headers = [ "EXT", "INPUT", "EXT", "OUTPUT" ]
data = []
for input_filepath in input_filepaths:
    basename, extension = os.path.splitext(input_filepath)
    output_filepath = basename + "." + args.output_extension
    conversion_command = r'"C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" -lang=ff -c "Open($1); Generate($2)" "%s" "%s"' % (input_filepath, output_filepath)
    subprocess.run(conversion_command)
    data.append([ extension[1:].upper(), input_filepath, args.output_extension.upper(), output_filepath ])

print()
table = columnar(data, headers, no_borders=True)
print(table)
