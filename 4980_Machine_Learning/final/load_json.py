import json, re
import pandas as pd
import numpy as np






class CleanData:

    def __init__(self, file_name):
        self.file = file_name,
        self.columns = ['name','address','city','state','zip','latitude','longitude','is_open','stars','work_weekend','total_hours']
        self.obs_list = []
        self.attr_list = []
        self.cate_list = []
        self.raw_cate = []
        self.all_obs_cate_dummy = []


    def read_file(self):
        a = 0
        with open(self.file[0], encoding = 'utf-8') as f:
            for line in f:
                a += 1
                print(a)
                json_line = json.loads(line)
                name = json_line['name']
                address = json_line['address']
                city = json_line['city']
                state = json_line['state']
                postcode = json_line['postal_code']
                latitude = json_line['latitude']
                longitude = json_line['longitude']
                is_open = json_line['is_open']
                stars = json_line['stars']
                work_weekend, total_hours = self.compute_hours(json_line)

                
                ### attributes
                try:
                    attr_value_list = self.obtain_attr(json_line)
                except:
                    attr_value_list = ['NIU' for i in range(39)]




                ### categories
                # count how many categories in the data, save to <self.cate_list>
                try:
                    cate = json_line['categories']
                    cate = cate.split(',')
                    for item in cate:
                        if item not in self.cate_list:
                            self.cate_list.append(item)
                    self.raw_cate.append(cate)
                except:
                    cate = []
                    self.raw_cate.append(cate)


                ## write data into a dataframe
                ## Pandas is bull shit when writing large number of obs...even slower than snail...lol
                sublist = [stars, name, address, city, state, postcode, latitude, longitude, is_open, work_weekend, total_hours] + attr_value_list
                self.obs_list.append(sublist)
            
        ## make dummy, 1 = in this category, 0 = not
        zero_list = [0 for i in range(len(self.cate_list))]
        for obs in self.raw_cate:
            # each obs is a list containing categories for this observation
            cate_dummy = zero_list
            ## if obs doesn't have category, len(obs) == 0
            if len(obs) != 0:
                for cate in obs:
                    # obtain index of this category
                    indexing = self.cate_list.index(cate)
                    cate_dummy[indexing] = 1

            self.all_obs_cate_dummy.append(cate_dummy)

            


        obs_list = np.array(self.obs_list)
        all_obs_cate_dummy = np.array(self.all_obs_cate_dummy)
        print(obs_list.shape)
        print(all_obs_cate_dummy.shape)



        



        #col = ['stars','name','address','city','state','zip','latitude','longitude','is_open','work_weekend','total_hours', 'ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'BusinessAcceptsBitcoin', 'OutdoorSeating', 'RestaurantsTakeOut', 'RestaurantsDelivery', 'RestaurantsGoodForGroups', 'RestaurantsPriceRange2', 'WiFi', 'BikeParking', 'Alcohol', 'GoodForKids', 'Ambience', 'BusinessParking', 'Caters', 'RestaurantsReservations', 'RestaurantsAttire','NoiseLevel', 'GoodForMeal', 'HasTV', 'DogsAllowed', 'WheelchairAccessible', 'Corkage', 'BYOBCorkage', 'AcceptsInsurance', 'GoodForDancing', 'Smoking', 'HappyHour','CoatCheck', 'Music', 'RestaurantsTableService', 'BestNights', 'DriveThru', 'HairSpecializesIn', 'AgesAllowed', 'Open24Hours', 'DietaryRestrictions', 'RestaurantsCounterService', 'BYOB']


        #obs_list = np.array(self.obs_list)
        #print(obs_list.shape)
        #df = pd.DataFrame(obs_list)
        #df.columns = col
        #print(obs_list.shape)
        #print(df)
        ##df.to_csv('rough_data.csv')





    def compute_hours(self, json_line):
        try:
            workhours = json_line['hours']
            # get which day open
            # wh = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            total_hours = 0
            total_mins = 0
            wh = list(workhours)

            #### variable(work_weekend) add to df: if open in weekend
            if 'Saturday' or 'Sunday' in wh:
                work_weekend = 1
            else:
                work_weekend = 0

            try:

                for day in wh:
                    openhours = workhours[day]
                    ## 9:0-20:0
                    ## hours_str = ['9', '20']
                    hours_str = re.compile(r'(\d*):').findall(openhours)
                    
                    #10:0-0:0
                    # this mean to 12pm, it actually work 24-10 = 14 hrs rather -10 hrs
                    # if work 24hrs: 0-0 we don't want the workhours = 0
                    if int(hours_str[1]) <= int(hours_str[0]):
                        total_hours += int(hours_str[1]) + 24 - int(hours_str[0])
                    else:
                        total_hours += int(hours_str[1]) - int(hours_str[0])
                    ## 8:30-23:30
                    ## mins = ['30', '30']
                    mins_str = re.compile(r':(\d*)').findall(openhours)
                    total_mins += int(mins_str[1]) - int(mins_str[0])

                # trans mins to hours
                min_to_hours = total_mins/60
                total_hours += min_to_hours
                
            except:
                total_hours = 0
        except:
            wh = 0
            work_weekend = 0

        return work_weekend, total_hours



    def obtain_attr(self, json_line):

        ### attributes
        attr = json_line['attributes']
        attr_prelist = list(attr)
        for item in attr_prelist:
            if item not in self.attr_list:
                self.attr_list.append(item)
        try:
            ByAppointmentOnly = attr['ByAppointmentOnly']
        except:
            ByAppointmentOnly = 'NIU'
        try:
            BusinessAcceptsCreditCards = attr['BusinessAcceptsCreditCards']
        except:
            BusinessAcceptsCreditCards = 'NIU'
        try:
            BusinessAcceptsBitcoin = attr['BusinessAcceptsBitcoin']
        except:
            BusinessAcceptsBitcoin = 'NIU'
        try:
            OutdoorSeating = attr['OutdoorSeating']
        except:
            OutdoorSeating = 'NIU'
        try:
            RestaurantsTakeOut = attr['RestaurantsTakeOut']
        except:
            RestaurantsTakeOut = 'NIU'
        try:
            RestaurantsDelivery = attr['RestaurantsDelivery']
        except:
            RestaurantsDelivery = 'NIU'
        try:
            RestaurantsGoodForGroups = attr['RestaurantsGoodForGroups']
        except:
            RestaurantsGoodForGroups = 'NIU'
        try:
            RestaurantsPriceRange2 = attr['RestaurantsPriceRange2']
        except:
            RestaurantsPriceRange2 = 'NIU'
        try:
            WiFi = attr['WiFi']
        except:
            WiFi = 'NIU'
        try:
            BikeParking = attr['BikeParking']
        except:
            BikeParking = 'NIU'
        try:
            Alcohol = attr['Alcohol']
        except:
            Alcohol = 'NIU'
        try:
            GoodForKids = attr['GoodForKids']
        except:
            GoodForKids = 'NIU'
        try:
            Ambience = attr['Ambience']
        except:
            Ambience = 'NIU'
        try:
            BusinessParking = attr['BusinessParking']
        except:
            BusinessParking = 'NIU'
        try:
            Caters = attr['Caters']
        except:
            Caters = 'NIU'
        try:
            RestaurantsReservations = attr['RestaurantsReservations']
        except:
            RestaurantsReservations = 'NIU'
        try:
            RestaurantsAttire = attr['RestaurantsAttire']
        except:
            RestaurantsAttire = 'NIU'
        try:
            NoiseLevel = attr['NoiseLevel']
        except:
            NoiseLevel = 'NIU'
        try:
            GoodForMeal = attr['GoodForMeal']
        except:
            GoodForMeal = 'NIU'
        try:
            HasTV = attr['HasTV']
        except:
            HasTV = 'NIU'
        try:
            DogsAllowed = attr['DogsAllowed']
        except:
            DogsAllowed = 'NIU'
        try:
            WheelchairAccessible = attr['WheelchairAccessible']
        except:
            WheelchairAccessible = 'NIU'
        try:
            Corkage = attr['Corkage']
        except:
            Corkage = 'NIU'
        try:
            BYOBCorkage = attr['BYOBCorkage']
        except:
            BYOBCorkage = 'NIU'
        try:
            AcceptsInsurance = attr['AcceptsInsurance']
        except:
            AcceptsInsurance = 'NIU'
        try:
            GoodForDancing = attr['GoodForDancing']
        except:
            GoodForDancing = 'NIU'
        try:
            Smoking = attr['Smoking']
        except:
            Smoking = 'NIU'
        try:
            HappyHour = attr['HappyHour']
        except:
            HappyHour = 'NIU'
        try:
            CoatCheck = attr['CoatCheck']
        except:
            CoatCheck = 'NIU'
        try:
            Music = attr['Music']
        except:
            Music = 'NIU'
        try:
            RestaurantsTableService = attr['RestaurantsTableService']
        except:
            RestaurantsTableService = 'NIU'
        try:
            BestNights = attr['BestNights']
        except:
            BestNights = 'NIU'
        try:
            DriveThru = attr['DriveThru']
        except:
            DriveThru = 'NIU'
        try:
            HairSpecializesIn = attr['HairSpecializesIn']
        except:
            HairSpecializesIn = 'NIU'
        try:
            AgesAllowed = attr['AgesAllowed']
        except:
            AgesAllowed = 'NIU'
        try:
            Open24Hours = attr['Open24Hours']
        except:
            Open24Hours = 'NIU'
        try:
            DietaryRestrictions = attr['DietaryRestrictions']
        except:
            DietaryRestrictions = 'NIU'
        try:
            RestaurantsCounterService = attr['RestaurantsCounterService']
        except:
            RestaurantsCounterService = 'NIU'
        try:
            BYOB = attr['BYOB']
        except:
            BYOB = 'NIU'



        return [ByAppointmentOnly, BusinessAcceptsCreditCards, BusinessAcceptsBitcoin, OutdoorSeating, RestaurantsTakeOut, RestaurantsDelivery, RestaurantsGoodForGroups, RestaurantsPriceRange2, WiFi, BikeParking, Alcohol, GoodForKids, Ambience, BusinessParking, Caters, RestaurantsReservations, RestaurantsAttire,NoiseLevel, GoodForMeal, HasTV, DogsAllowed, WheelchairAccessible, Corkage, BYOBCorkage, AcceptsInsurance, GoodForDancing, Smoking, HappyHour,CoatCheck, Music, RestaurantsTableService, BestNights, DriveThru, HairSpecializesIn, AgesAllowed, Open24Hours, DietaryRestrictions, RestaurantsCounterService, BYOB]





def check_frequency(csv_file):
    df = pd.read_csv(csv_file)
    niu_df = pd.DataFrame()

    for i in range(12,51):
        attr_name = df.columns[i]
        attr = df.iloc[:,i].values
        niu_count = 0
        for attr_value in attr:
            if attr_value == 'NIU':
                niu_count += 1
        total_obs = len(attr)
        percent_niu = niu_count/total_obs
        niu_df = niu_df.append({
            'name':attr_name,
            'niu_count':niu_count,
            'percent_niu':percent_niu
            }, ignore_index = True)
    print(niu_df)
    niu_df.to_csv('attr_NIU_percentage.csv')






    print(df.shape)


if __name__ == '__main__':
    file_name = 'business_sample.json'
    CleanData(file_name).read_file()
    ## check in what percent this attribute encounter a missing data problem.
    #check_frequency('rough_data.csv')


