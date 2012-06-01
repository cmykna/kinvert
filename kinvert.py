#!/usr/bin/python
import argparse, glob

parser = argparse.ArgumentParser(description="Python wrapper for Amazon's Kindlegen command-line tool")

parser.add_argument("-d", "--output_dir", 
					default="mobi_files",
					help="specify output directory")
parser.add_argument("-w", "--western",
					action="store_true",
					help="force build of Windows-1252 book")
parser.add_argument("-g", "--gif",
					action="store_true",
					help="images are converted to GIF format (no JPEG in the book)")
parser.add_argument("file", help="file or fileglob to convert")


verbosity = parser.add_mutually_exclusive_group()
verbosity.add_argument("-v", "--verbosity",
					   type=int,
					   choices=[1, 2],
					   help="increase output verbosity")
verbosity.add_argument("-q", "--quiet",
					   action="store_true",
					   help="suppress all output")

compression = parser.add_mutually_exclusive_group()
compression.add_argument("-c0", 
						 action="store_true", 
						 help="no compression")
compression.add_argument("-c1", 
						 action="store_true", 
						 help="standard DOC compression")
compression.add_argument("-c2", 
						 action="store_true", 
						 help="Kindle huffdic compression")

args = parser.parse_args()

def build_kindlegen_cmd(args):

	print args

if __name__ == '__main__':
	build_kindlegen_cmd(args)
