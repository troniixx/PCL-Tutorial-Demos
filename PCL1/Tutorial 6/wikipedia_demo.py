# Step 1: Install the Wikipedia module (Run this line in your terminal if it's not installed already)
# pip install wikipedia (windwows) // pip3 install wikipedia (mac)

# Step 2: Import the Wikipedia module
import wikipedia

# Step 3: Set the language to English
wikipedia.set_lang("en")  # Change "en" to any language code (e.g., "es" for Spanish)

# Step 4: Search for pages related to a topic (e.g., "Python programming")
results = wikipedia.search("Pytho")
print("Search results:", results)

# Step 5: Get a summary of the topic
summary = wikipedia.summary("Python programming", sentences=2)
print("\nSummary of Python programming:\n", summary)

# Step 6: Access detailed page content
page = wikipedia.page("Python (programming language)")

# Step 7: Access various details about the page
print("\nTitle of the page:", page.title)
print("URL of the page:", page.url)
print("\nContent (first 500 characters):\n", page.content[:500])  # Printing the first 500 characters for brevity
print("\nSummary:\n", page.summary)
print("\nList of images:", page.images[:5])  # Displaying only the first 5 image URLs
print("\nReferences:", page.references[:5])  # Displaying only the first 5 references
print("\nLinks on the page:", page.links[:5])  # Displaying only the first 5 links
print("\nSections in the page:", page.sections)