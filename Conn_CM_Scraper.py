from cryptocmd import CmcScraper

# Documentation https://github.com/guptarohit/cryptoCMD
# initialise scraper without time interval
scraper = CmcScraper("BTC")

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
xrp_json_data = scraper.get_data("json")

# export the data as csv file, you can also pass optional `name` parameter
scraper.export("csv", name="xrp_all_time")

# Pandas dataFrame for the same data
df = scraper.get_dataframe()


result = xrp_json_data[0]

print(data[0][1])
