import sys
import os
import re

def cleanup_mobirise(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return

    try:
        # Read the file content
        with open(file_name, 'r') as file:
            content = file.read()

        # 1. Remove Mobirise branding and links
        content = re.sub(r'<!-- Site made with Mobirise Website Builder.*?-->', '', content)
        content = re.sub(r'<section class="display-7".*?AI Website Generator</a></section>', '', content)
        
        # 2. Add Google Analytics tag
        google_tag = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-2G4GYDL8RZ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-2G4GYDL8RZ');
    </script>"""
        
        # Insert Google tag after <head>
        content = content.replace("<head>", "<head>\n" + google_tag, 1)

        # 3. Remove the second footer (the one with "If you like the website...")
        # Find the first footer's end and scripts start
        footer_end = content.find('</section>', content.find('class="footer7 cid-uCqNzh6cji"'))
        scripts_start = content.find('<script src="assets/bootstrap/js/bootstrap.bundle.min.js">')
        
        if footer_end != -1 and scripts_start != -1:
            # Get content before footer end and after scripts start
            content = content[:footer_end + 10] + content[scripts_start:]

        # Write the modified content back to the file
        with open(file_name, 'w') as file:
            file.write(content)
        
        print(f"Successfully cleaned up '{file_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Filename missing, Picking default file TYL index.html")
        file_name = "/Users/kitkat/Workspace/GitHub/theyogiclens.org/index.html"
    else:
        file_name = sys.argv[1]
    cleanup_mobirise(file_name) 