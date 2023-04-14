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
    
    def convert_date_to_day(self) -> pd.DataFrame:
        self.data["date"] = pd.to_datetime(self.data["date"])
        self.data["day"] = self.data["date"].dt.day_name()
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
    
    def convert_delay_minutes_to_bool(self, delay) -> int:
        if 0 <= int(delay) and int(delay) < 5:
            return 0
        else:
            return 1
        
    def convert_delay(self) -> pd.DataFrame:
        self.data['delay'] = self.data["delay_minutes"].apply(self.convert_delay_minutes_to_bool)
        return self.data
    
    def drop_unnecessary_columns(self) -> pd.DataFrame:
        self.data.drop(columns=['train_id', 'actual_time', 'delay_minutes'], inplace=True)
        return self.data
    
    def save_first_60k(self, path: str):
        df_first_60 = self.data.head(60000)
        df_first_60.to_csv(path, index=False)
    
    def prep_df(self, path: str='data/NJ.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)