import frontmatter
import os
from datetime import datetime

# Get today's date in ISO format (you can change the format as needed)
today_date = datetime.today().strftime('%Y-%m-%d')

# Get the list of new and modified files from GitHub Actions environment variables
new_files = os.getenv("NEW_FILES", "").splitlines()
modified_files = os.getenv("MODIFIED_FILES", "").splitlines()

# Function to update frontmatter
def update_frontmatter(file_path, frontmatter_key, date_value):
    try:
        post = frontmatter.load(file_path)

        if frontmatter_key not in post.metadata:
            post.metadata[frontmatter_key] = date_value  # Add the key if it's not there
            print(f"Added '{frontmatter_key}' to {file_path}")
        else:
            post.metadata[frontmatter_key] = date_value  # Update the key
            print(f"Updated '{frontmatter_key}' for {file_path}")

        # Save the modified file with updated frontmatter
        frontmatter.dump(post, file_path)
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

# Process new files (Add 'publish' frontmatter)
for new_file in new_files:
    if new_file.endswith('.md'):
        update_frontmatter(new_file, 'publish', today_date)

# Process modified files (Update 'lastUpdate' frontmatter)
for modified_file in modified_files:
    if modified_file.endswith('.md'):
        update_frontmatter(modified_file, 'lastUpdate', today_date)