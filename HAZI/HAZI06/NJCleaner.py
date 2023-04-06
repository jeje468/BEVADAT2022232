import pandas as pd
from datetime import datetime

class NJCleaner():
    def __init__(self, csv_path: str):
        df = pd.read_csv(csv_path)
        self.data = df
    
    def order_by_scheduled_time(self) -> pd.DataFrame:
        self.data = self.data.sort_values(by="scheduled_time")
        return self.data
    
    def drop_columns_and_nan(self) -> pd.DataFrame:
        self.data = self.data.drop(columns=['from', 'to'])
        droped = self.data.dropna()
        self.data = droped
        return self.data
    
    def convert_day_to_date(self) -> pd.DataFrame:
        self.data["day"] = self.data["date"].apply(pd.to_datetime).dt.strftime('%A')
        self.data.drop(columns=["date"], inplace=True)

        return self.data
    
    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        
        self.data['part_of_day'] = self.data["scheduled_time"].apply(self.convert_datetime_to_time_of_day)
        self.data.drop(columns=["scheduled_time"], inplace=True)
        return self.data
    
    def convert_datetime_to_time_of_day(self, datetime_string):
        time_range_dict = {'early_morning': range(4, 8), 'morning': range(8, 12), 'afternoon': range(12, 16),
                        'evening': range(16, 20), 'night': range(20, 24), 'late_night': range(0, 4)}

        datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')

        hour = datetime_obj.hour

        time_of_day = next(key for key, value in time_range_dict.items() if hour in value)

        return time_of_day

    