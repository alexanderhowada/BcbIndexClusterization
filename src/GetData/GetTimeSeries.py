import sgs
import pandas as pd
from tqdm import tqdm


class GetTimeSeries:
	"""
	wrapper for sgs library (https://pypi.org/project/sgs/)
	Gets data as sgs.dataframe, however shows progress and returns metadata

	Example:
		GTS = GetTimeSeries()
		df, meta = GTS([1, 188], start_date='20/12/2017', end_date='31/03/2018')
	"""
	def __init__(self):
		pass

	def __call__(self, ids, start_date, end_date):
		"""
		param ids: series ids
		param start_date: start date for series
		param end_date: end date for series

		return dataframe (with time series), dataframe (with metadata)
		"""

		df = self._get_raw_dataframe(ids, start_date, end_date)
		meta = self._get_metadata(df)
		df = self._assign_columns(df, meta)

		return df, meta

	@staticmethod
	def _get_raw_dataframe(series_ids, start_date, end_date):
		full = []
		for idx in tqdm(series_ids):
			ts = sgs.time_serie(idx, start=start_date, end=end_date)
			full.append(ts)
		full = pd.concat(full, axis=1)

		return full

	@staticmethod
	def _get_metadata(df):
		return pd.DataFrame(sgs.metadata(df))

	@staticmethod
	def _assign_columns(df, meta):
		meta = meta.set_index('code')
		columns = [meta.loc[i, 'name'] for i in df.columns]
		df.columns = columns
		return df

if __name__ == '__main__':
	from IPython.display import display
	GTS = GetTimeSeries()
	df, meta = GTS([1, 188], start_date='20/12/2017', end_date='31/03/2018')

	print('--------------------------------')
	# display(help(GetTimeSeries))
	print('--------------------------------')
	display(df.iloc[:10])
	print('--------------------------------')
	display(meta)
