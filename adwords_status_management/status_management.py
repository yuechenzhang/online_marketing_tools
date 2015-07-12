import urllib
import pandas as pd

################################################################################################################################
###################  This code scrapes a list of landing pages, looking for ones with no products to show  #####################
###################  in order to later pause the keywords or ads (depending on client's setup) linking to ######################
###################  these pages.                                                                         ######################
################################################################################################################################


# Reading a CSV report file with the Destination URLs listed (Keyword or Ad level)
# Column names have to be adjusted according to your needs


def status_mgmt(df):
	'''
	input:

	df : pd.DataFrame.
		The Adwords Keyword report including the Destination URL column. 
		Read into a pandas dataframe by pd.read_csv()

	returns:

	df : pd.DataFrame
		The Adwords Keyword report with the "Status_updated" column set to active/paused depending on 
		the number of products found on the landing page.

	'''
	
	all_LPs = df["Destination URL"].unique().tolist()

	all_pages = dict()

	#The text pattern which appears on page if no products are available

	pattern = "No products found."

	#Scraping each landing page, looking for the text pattern, deleting all but empty URL keys.
	#Background info: urllib returns -1 if text not found, or an index of this text if found.

	for LP in all_LPs:
	    all_pages[LP] = urllib.urlopen(LP).read().find(pattern)
	    if all_pages[LP] == -1:
	        del all_pages[LP]

	#Creating a list of all empty URLs.

	empty_urls = all_pages.keys().tolist()

	#Marking the empty URLs in the CSV file

	df['empty'] = df["Destination URL"].isin(empty_urls)
	mask = df['empty'] == True

	#Creating a copy of the status column for quality check purposes
	df['Status_updated'] = 0
	df.ix[mask, "Status_updated"] = "Paused"
	df.ix[~mask, "Status_updated"] = "Active"

	return df

#Now the file is ready for upload using Adwords or Bing Editor, pausing the keywords or ads with no inventory on their landing pages.


