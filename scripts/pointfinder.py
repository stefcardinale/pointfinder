#!/usr/bin/env python3

import argparse
import sys
import datetime
import subprocess as sp

import glob

def parse_args(org_names):
	parser = argparse.ArgumentParser(
	description="Finds information on the point mutation positions.")
	#parser.add_argument("--id", help="Id to use for same-folder running", required=True)
	#parser.add_argument("--db", help="Path to db", required=True)
	parser.add_argument("--i", "--inputfasta", help="Input fasta file")
	parser.add_argument("--o", help="Desired output directory")
	parser.add_argument("--s", help="Sets a specific organism", choices=org_names, required=True)
	return parser.parse_args()

def run_pointfinder(fasta, outdir, organism):
	#sp.run(["cd", seqid])
	sp.run(["/bifrost_resources/pointfinder/PointFinder.py",
	 "-i", fasta, "-o", outdir, "-s", organism, "-p", "/bifrost/pointfinder/pointfinder_db", "-m", "blastn", "-m_p", "/opt/conda/pkgs/blast-2.9.0-h20b68b9_1/bin/blastn"])


# def find_contigs(seqid, fasta):
# 	if fasta is None:
# 		fasta = glob.glob(seqid + "*/contigs.fasta")[0]

# 	return fasta

# def pointfinder_res_search(organism, seqid, db, outdir, fasta):
# 	fasta = find_contigs(seqid, fasta)
# 	run_pointfinder(fasta, seqid, db, outdir, organism)

if __name__ == "__main__":
    org_names = ['salmonella','campylobacter','escherichia_coli']

    args = parse_args(org_names)
    run_pointfinder(args.i, args.o, args.s)