
import os
import shutil
import re
import requests
from bs4 import BeautifulSoup


# Option A: Move all .jpg files from one folder to another
def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dest_path)
            moved_count += 1
            print(f"Moved: {filename}")

    print(f"\nDone. {moved_count} .jpg files moved to {destination_folder}")


# Option B: Extract emails from a .txt file
def extract_emails(input_file, output_file):
    with open(input_file, "r") as f:
        content = f.read()

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))

    with open(output_file, "w") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email(s). Saved to {output_file}")


# Option C: Scrape the title of a fixed webpage
def scrape_title(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    with open(output_file, "w") as f:
        f.write(f"URL: {url}\n")
        f.write(f"Title: {title}\n")

    print(f"Title scraped: {title}")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    print("Choose automation task:")
    print("1. Move .jpg files")
    print("2. Extract emails from .txt file")
    print("3. Scrape webpage title")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        src = input("Enter source folder path: ")
        dst = input("Enter destination folder path: ")
        move_jpg_files(src, dst)
    elif choice == "2":
        infile = input("Enter input .txt file path: ")
        outfile = input("Enter output file name: ")
        extract_emails(infile, outfile)
    elif choice == "3":
        url = input("Enter webpage URL: ")
        outfile = input("Enter output file name: ")
        scrape_title(url, outfile)
    else:
        print("Invalid choice.")
