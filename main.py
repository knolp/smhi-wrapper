import requests

class SMHI():
	def __init__(self, station):
		self.station = station
		self.metobs = "https://opendata-download-metobs.smhi.se"


	def temperature_right_now(self):
		smhi_info = requests.get(self.metobs + "/api/version/1.0/parameter/1/station/{}/period/latest-hour/data.json".format(self.station))
		return float(smhi_info.json()["value"][0]["value"])


	










if __name__ == '__main__':
	marsta = SMHI("97400")

	print(marsta.temperature_right_now())