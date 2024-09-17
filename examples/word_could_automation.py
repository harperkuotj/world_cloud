#!/usr/bin/env python
"""
Automatically generate word clouds for all .txt files in a specified folder.
"""

import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud_for_folder(input_folder):
    # Check if the folder exists
    if not path.exists(input_folder):
        print(f"Folder '{input_folder}' does not exist.")
        return

    # List all files in the folder
    files = os.listdir(input_folder)
    
    # Filter only .txt files
    txt_files = [f for f in files if f.endswith('.txt')]
    
    if not txt_files:
        print(f"No .txt files found in the folder '{input_folder}'.")
        return

    # Generate word cloud for each .txt file
    for txt_file in txt_files:
        file_path = path.join(input_folder, txt_file)

        # Read the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Remove unwanted strings
        text = text.lower().replace('speaker 0', '').replace('speaker 1', '').replace('okay', '').replace('yes', '').replace('yeah', '').replace('oh', '').replace('will', '').replace('one', '').replace('think', '').replace('know', '')

        # Generate word cloud
        wordcloud = WordCloud().generate(text)

        # Save word cloud as image file
        output_image_path = path.join(input_folder, f"{path.splitext(txt_file)[0]}_wordcloud.png")
        wordcloud.to_file(output_image_path)

        # Optionally display the word cloud (can be commented out if not needed)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

        print(f"Word cloud saved for '{txt_file}' as '{output_image_path}'.")


if __name__ == "__main__":    
    # Generate word clouds for all .txt files in the input folder
    input_folder = "./input"
    generate_wordcloud_for_folder(input_folder)



# #!/usr/bin/env python
# """
# Minimal Example
# ===============

# Generating a square wordcloud from the US constitution using default arguments.
# """

# import os
# from os import path
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
# d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# # Read the whole text.
# filename = "himeet_4337059_2023-06-01-20-00-15"
# text = open(path.join(d, f"{filename}.txt")).read()

# # Generate a word cloud image
# wordcloud = WordCloud().generate(text)

# # Save the generated image to a file
# wordcloud.to_file(path.join(d, "wordcloud_output.png"))  # Save as PNG

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

# # Lower max_font_size and save again
# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")

# # Save the updated word cloud with different font size
# wordcloud.to_file(path.join(d, f"{filename}.png"))  # Save as PNG

# plt.show()