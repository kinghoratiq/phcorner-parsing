import webparser
import output

url = input('Input URL from PHCorner: ')

data_parsed = webparser.parseIt(url)
output.writeJSON(data_parsed)