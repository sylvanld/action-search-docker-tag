import re
import sys
import os
import requests

def search_image_tags(image_name: str, searched_pattern: re.Pattern) -> str:
    response = requests.get("https://hub.docker.com/v2/repositories/%s/tags" % image_name)
    all_tags = response.json()["results"]
    try:
        return next(tag for tag in all_tags if searched_pattern.match(tag["name"]))
    except StopIteration:
        raise Exception("Can't find tag matching pattern %s for image %s" % (searched_pattern, image_name))

def main():
    image_name = sys.argv[1]
    searched_pattern = re.compile(sys.argv[2])
    matching_tag = search_image_tags(image_name, searched_pattern)
    matching_tag_name = matching_tag["name"]
    print("matching_tag name", matching_tag_name)
    print("GITHUB_OUTPUT", os.getenv("GITHUB_OUTPUT"))
    with open(os.environ["GITHUB_OUTPUT"], "a") as output_file:
        output_file.write("tag=%s\n" % matching_tag_name)

if __name__ == "__main__":
    main()
