import requests, csv


# This class will be handling the api and the data 
class DataHandler:
	def data(self, portfolio=False, company=None):
		if portfolio is False:
			company = company
			self.yahoo = 'http://ichart.finance.yahoo.com/table.csv?s=%s&c=1962' % company
			with requests.Session() as sess:
				download = sess.get(self.yahoo)
				decoded_content = download.content.decode('utf-8')
				decoded_data = csv.reader(decoded_content.splitlines(), delimiter=',')
				return list(decoded_data) #
		elif portfolio is True: 
			# Todo
			pass
		else:
			raise Exception("Problem with portfolio in data")
	
	def urls(self):
		# TODO
		pass

