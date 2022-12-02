from bs4 import BeautifulSoup
import requests

url = "https://www.hamilton.edu/academics/areas-of-study"

# url = "https://www.ssa.gov/OACT/babynames/decades/century.html"

source_code = requests.get(url).text

parsed_code = BeautifulSoup(source_code,"html.parser")

header = parsed_code.find("head")

# print(header)

# print(type(header))

title = header.find("title")

title_as_string = title.text

spans = parsed_code.find_all("span")

# print(spans)

# for index in range(len(spans)):
#     if '198 College Hill Road' in spans[index].text:
#         print("found it in", index)
#         print(spans[index])

# for index, span in enumerate(spans):
#     print("found it in", index)
#     print(span)

address = parsed_code.find("div", class_ = "meta_info_detail meta_info_detail_address")
# print(address)
# print(address.text)

# print(spans[182])

africana = parsed_code.find(string = "Africana Studies")
# print(africana.parent)

areas = parsed_code.find_all("span", class_ = "study_link_title")

area_of_study = {}

for area in areas:
    print(area.text)
    if area.text[-1] == '*' and area.text[-2] != '*':
        area_of_study[area.text] = 'Minor'
    if area.text[-1] == '*' and area.text[-2] == '*':
        area_of_study[area.text] = 'Language'
    if area.text[-1] != '*':
        area_of_study[area.text] = 'Major'


# new key know whether major or minor
print(area_of_study)
    
# dictionary = {"Name" , "Number" : 0}


        