import argparse
print("--- Cloud Build Python script has started ---")
parser = argparse.ArgumentParser()
parser.add_argument('--file-path', required=True, help='The GCS path of the input file.')
args = parser.parse_args()
print(f"SUCCESS: Received file to process: {args.file_path}")
print("--- Cloud Build Python script has finished ---")
