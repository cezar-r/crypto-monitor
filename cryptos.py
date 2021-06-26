class Cardano:

	def __init__(self):
		self.cur_price = 0
		self.under_1_60 = False
		self.under_1_50 = False
		self.under_1_40 = False
		self.under_1_30 = False
		self.under_1_20 = False
		self.under_1_10 = False
		self.under_1_00 = False

	def init_lvls(self):
		if self.cur_price > 1.6:
			self.under_1_60 = False
			self.under_1_50 = False
			self.under_1_40 = False
			self.under_1_30 = False
			self.under_1_20 = False
			self.under_1_10 = False
			self.under_1_00 = False
		elif self.cur_price > 1.5:
			self.under_1_60 = True
			self.under_1_50 = False
			self.under_1_40 = False
			self.under_1_30 = False
			self.under_1_20 = False
			self.under_1_10 = False
			self.under_1_00 = False
		elif self.cur_price > 1.4:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = False
			self.under_1_30 = False
			self.under_1_20 = False
			self.under_1_10 = False
			self.under_1_00 = False	
		elif self.cur_price > 1.3:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = True
			self.under_1_30 = False
			self.under_1_20 = False
			self.under_1_10 = False
			self.under_1_00 = False
		elif self.cur_price > 1.2:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = True
			self.under_1_30 = True
			self.under_1_20 = False
			self.under_1_10 = False
			self.under_1_00 = False
		elif self.cur_price > 1.1:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = True
			self.under_1_30 = True
			self.under_1_20 = True
			self.under_1_10 = False
			self.under_1_00 = False
		elif self.cur_price > 1.0:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = True
			self.under_1_30 = True
			self.under_1_20 = True
			self.under_1_10 = True
			self.under_1_00 = False
		else:
			self.under_1_60 = True
			self.under_1_50 = True
			self.under_1_40 = True
			self.under_1_30 = True
			self.under_1_20 = True
			self.under_1_10 = True
			self.under_1_00 = True			


class Bitcoin:

	def __init__(self):
		self.cur_price = 0
		self.under_35k = False
		self.under_30k = False
		self.under_28k = False
		self.under_26k = False
		self.under_25k = False
		self.under_22k = False
		self.under_20k = False

	def init_lvls(self):
		if self.cur_price > 35000:
			self.under_35k = False
			self.under_30k = False
			self.under_28k = False
			self.under_26k = False
			self.under_25k = False
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 30000:
			self.under_35k = True
			self.under_30k = False
			self.under_28k = False
			self.under_26k = False
			self.under_25k = False
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 28000:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = False
			self.under_26k = False
			self.under_25k = False
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 26000:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = True
			self.under_26k = False
			self.under_25k = False
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 25000:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = True
			self.under_26k = False
			self.under_25k = False
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 22000:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = True
			self.under_26k = False
			self.under_25k = True
			self.under_22k = False
			self.under_20k = False
		elif self.cur_price > 20000:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = True
			self.under_26k = False
			self.under_25k = True
			self.under_22k = True
			self.under_20k = False
		else:
			self.under_35k = True
			self.under_30k = True
			self.under_28k = True
			self.under_26k = False
			self.under_25k = True
			self.under_22k = True
			self.under_20k = True


class Ethereum:

	def __init__(self):
		self.cur_price = 0
		self.under_3k = False
		self.under_2_8k = False
		self.under_2_6k = False
		self.under_2_5k = False
		self.under_2_2k = False
		self.under_2k = False
		self.under_1_8k = False
		self.under_1_5k = False

	def init_lvls(self):
		if self.cur_price > 3000:
			self.under_3k = False
			self.under_2_8k = False
			self.under_2_6k = False
			self.under_2_5k = False
			self.under_2_2k = False
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 2800:
			self.under_3k = True
			self.under_2_8k = False
			self.under_2_6k = False
			self.under_2_5k = False
			self.under_2_2k = False
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 2600:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = False
			self.under_2_5k = False
			self.under_2_2k = False
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 2500:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = False
			self.under_2_2k = False
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 2200:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = True
			self.under_2_2k = False
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 2000:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = True
			self.under_2_2k = True
			self.under_2k = False
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 1800:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = True
			self.under_2_2k = True
			self.under_2k = True
			self.under_1_8k = False
			self.under_1_5k = False
		elif self.cur_price > 1500:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = True
			self.under_2_2k = True
			self.under_2k = True
			self.under_1_8k = True
			self.under_1_5k = False
		else:
			self.under_3k = True
			self.under_2_8k = True
			self.under_2_6k = True
			self.under_2_5k = True
			self.under_2_2k = True
			self.under_2k = True
			self.under_1_8k = True
			self.under_1_5k = True




class Doge:

	def __init__(self):
		self.cur_price = 0
		self.under_35 = False
		self.under_30 = False
		self.under_25 = False
		self.under_20 = False
		self.under_15 = False
		self.under_10 = False

	def init_lvls(self):
		if self.cur_price > 0.35:
			self.under_35 = False
			self.under_30 = False
			self.under_25 = False
			self.under_20 = False
			self.under_15 = False
			self.under_10 = False
		elif self.cur_price > 0.30:
			self.under_35 = True
			self.under_30 = False
			self.under_25 = False
			self.under_20 = False
			self.under_15 = False
			self.under_10 = False
		elif self.cur_price > 0.25:
			self.under_35 = True
			self.under_30 = True
			self.under_25 = False
			self.under_20 = False
			self.under_15 = False
			self.under_10 = False
		elif self.cur_price > 0.20:
			self.under_35 = True
			self.under_30 = True
			self.under_25 = True
			self.under_20 = False
			self.under_15 = False
			self.under_10 = False
		elif self.cur_price > 0.15:
			self.under_35 = True
			self.under_30 = True
			self.under_25 = True
			self.under_20 = True
			self.under_15 = False
			self.under_10 = False
		elif self.cur_price > 0.10:
			self.under_35 = True
			self.under_30 = True
			self.under_25 = True
			self.under_20 = True
			self.under_15 = True
			self.under_10 = False
		else:
			self.under_35 = True
			self.under_30 = True
			self.under_25 = True
			self.under_20 = True
			self.under_15 = True
			self.under_10 = True			


