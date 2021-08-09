#!/usr/bin/env python3
import os
import shutil

#Setting up file destination
source = "/home/user/data/dev/organizer/testSource"
txt_path = "/home/user/data/dev/organizer/txt"
pdf_path = "/home/user/data/dev/organizer/pdf"
xlsx_path = "/home/user/data/dev/organizer/xlsx"
docx_path = "/home/user/data/dev/organizer/docx"
pptx_path = "/home/user/data/dev/organizer/pptx"
#unidentified_path = ""
#vid_path = ""
#vid_format = {}

# list all files in main dir
files = os.listdir(source)

for file in files:
  # move Text files
  if file.endswith(".txt"):
    shutil.move(f"{source}/{file}", txt_path)
  # move pdf files
  elif file.endswith(".pdf"):
    shutil.move(f"{source}/{file}", pdf_path)
  # move Excel files (.xlsx or .csv files)
  elif file.endswith(".xlsx") or file.endswith(".csv"):
    shutil.move(f"{source}/{file}", xlsx_path)
  # move MS Word files
  elif file.endswith(".docx"):
    shutil.move(f"{source}/{file}", docx_path)
  # move MS PowerPoint files
  elif file.endswith(".pptx"):
    shutil.move(f"{source}/{file}", pptx_path)
  # move vidoes
  elif file.endswith(vid_format):
    shutil.move(f"{source}/{file}", vid_path)

  #else:
   # shutil.move(f"{source}/{file}", unidentified_path)
