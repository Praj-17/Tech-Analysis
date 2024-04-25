class ProcessDataframe:
    def __init__(self) -> None:
        pass
    def preprocess(self, df):
        df.columns=['time', 'open', 'high', 'low', 'close', 'volume']
        #Check if NA values are in data
        df=df[df['volume']!=0]
        df.reset_index(drop=True, inplace=True)
        df.isna().sum()
        return df