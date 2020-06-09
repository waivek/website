from columnar import columnar
import argparse
import subprocess
import os.path
import re
parser = argparse.ArgumentParser(description='Batch subsets a font to an accepted unicode range')
parser.add_argument("directory")
parser.add_argument("unicode_range")
args = parser.parse_args()

headers = [ "Input", "Output", "Input Size", "Output Size"]
data = []

# correct - fonts\Vollkorn\Vollkorn.400italic.ttf

filenames = os.listdir(args.directory)
layout_features="lnum,tnum"
directory_save = os.getcwd()
os.chdir(args.directory)
selected_filenames = [ filename for filename in filenames if re.match(r"(\w+)\.(\d)00(italic)?\.ttf", filename) ]

total_selected_filenames = len(selected_filenames)
padding_length = len(str(total_selected_filenames))
for i, filename in enumerate(selected_filenames, start=1):
    status_message = "[%s/%s] %s" % (str(i).rjust(padding_length), total_selected_filenames, filename)
    print(status_message)
    m = re.match(r"(\w+)\.(\d)00(italic)?\.ttf", filename)
    font_name_with_underscores, font_weight, font_style = m.groups()
    font_style = font_style if font_style else "normal"
    input_filename_root, extension = os.path.splitext(filename)
    output_filename = input_filename_root + "-subset"
    ttf_subset_command = 'pyftsubset {input_filename} --unicodes={unicode_range} --output-file={output_filename}.ttf --layout-features={layout_features}'.format(
            input_filename=filename, unicode_range=args.unicode_range, output_filename=output_filename, layout_features=layout_features)
    woff_subset_command = 'pyftsubset {input_filename} --unicodes={unicode_range} --output-file={output_filename}.woff --layout-features={layout_features} --flavor=woff'.format(
            input_filename=filename, unicode_range=args.unicode_range, output_filename=output_filename, layout_features=layout_features)
    woff2_subset_command = 'pyftsubset {input_filename} --unicodes={unicode_range} --output-file={output_filename}.woff2 --layout-features={layout_features} --flavor=woff2'.format(
            input_filename=filename, unicode_range=args.unicode_range, output_filename=output_filename, layout_features=layout_features)
    subprocess.run(ttf_subset_command)
    input_byte_size = os.path.getsize(filename)
    input_kilobyte_size_string = str(round(input_byte_size / 1024, 2)) + " KB"
    # Subsetting fonts/Vollkorn/Vollkorn.400.ttf to Vollkorn.400-subset.ttf (was 313.88 KB, now 5.72 KB)
    # Subsetting fonts/Vollkorn/Vollkorn.400.ttf to Vollkorn.400-subset.zopfli.woff (was 313.88 KB, now 3.44 KB)
    # Subsetting fonts/Vollkorn/Vollkorn.400.ttf to Vollkorn.400-subset.woff2 (was 313.88 KB, now 2.8 KB)
    output_ttf_byte_size = os.path.getsize("%s.ttf" % output_filename)
    output_ttf_kilboyte_size_string = str(round(output_ttf_byte_size / 1024, 2)) + " KB"
    data.append([ filename, "%s.ttf" % output_filename, input_kilobyte_size_string, output_ttf_kilboyte_size_string ])

    subprocess.run(woff_subset_command)
    output_woff_byte_size = os.path.getsize("%s.woff" % output_filename)
    output_woff_kilboyte_size_string = str(round(output_woff_byte_size / 1024, 2)) + " KB"
    data.append([ filename, "%s.woff" % output_filename, input_kilobyte_size_string, output_woff_kilboyte_size_string ])

    subprocess.run(woff2_subset_command)
    output_woff2_byte_size = os.path.getsize("%s.woff2" % output_filename)
    output_woff2_kilboyte_size_string = str(round(output_woff2_byte_size / 1024, 2)) + " KB"
    data.append([ filename, "%s.woff2" % output_filename, input_kilobyte_size_string, output_woff2_kilboyte_size_string ])

os.chdir(directory_save)


print()
table = columnar(data, headers, no_borders=True, justify=["l", "l", "r", "r"] )
print(table)
