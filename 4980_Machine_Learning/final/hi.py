
import json, re
import pandas as pd
import numpy as np





review = []
review_stars = []

columns = ['name','address','city','state','zip','latitude','longitude','is_open','stars','work_weekend','total_hours']


class CleanData:
    def __init__(self, file_name):
        self.file = file_name,
        self.review = []
        #self.columns = ['name','address','city','state','zip','latitude','longitude','is_open','stars','work_weekend','total_hours']
        self.attr_list = []
        self.attr_value_list = []

    def read_file(self):
        with open(self.file[0], encoding = 'utf-8') as f:
        #with open('hi.json', encoding = 'utf-8') as f:
            for line in f:
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
                    attr = json_line['attributes']
                    attr_prelist = list(attr)
                    for item in attr_prelist:
                        if item not in self.attr_list:
                            self.attr_list.append(item)


                except:
                    pass


                sublist = [name, address, city, state, postcode, latitude, longitude, is_open, stars, work_weekend, total_hours]
                #sublist = [name, address, city, state, postcode, latitude, longitude, is_open, stars, work_weekend, total_hours, ByAppointmentOnly, BusinessAcceptsCreditCards, BusinessAcceptsBitcoin, OutdoorSeating, RestaurantsTakeOut, RestaurantsDelivery, RestaurantsGoodForGroups, RestaurantsPriceRange2, WiFi, BikeParking, Alcohol, GoodForKids, Ambience, BusinessParking, Caters, RestaurantsReservations, RestaurantsAttire,NoiseLevel, GoodForMeal, HasTV, DogsAllowed, WheelchairAccessible, Corkage, BYOBCorkage, AcceptsInsurance, GoodForDancing, Smoking, HappyHour,CoatCheck, Music, RestaurantsTableService, BestNights, DriveThru, HairSpecializesIn, AgesAllowed, Open24Hours, DietaryRestrictions, RestaurantsCounterService, BYOB]
                self.review.append(sublist)


        print(len(self.attr_list))

        dataset = np.array(self.review)
        self.df = pd.DataFrame(dataset)
        col = ['name','address','city','state','zip','latitude','longitude','is_open','stars','work_weekend','total_hours', 'ByAppointmentOnly', 'BusinessAcceptsCreditCards', 'BusinessAcceptsBitcoin', 'OutdoorSeating', 'RestaurantsTakeOut', 'RestaurantsDelivery', 'RestaurantsGoodForGroups', 'RestaurantsPriceRange2', 'WiFi', 'BikeParking', 'Alcohol', 'GoodForKids', 'Ambience', 'BusinessParking', 'Caters', 'RestaurantsReservations', 'RestaurantsAttire','NoiseLevel', 'GoodForMeal', 'HasTV', 'DogsAllowed', 'WheelchairAccessible', 'Corkage', 'BYOBCorkage', 'AcceptsInsurance', 'GoodForDancing', 'Smoking', 'HappyHour','CoatCheck', 'Music', 'RestaurantsTableService', 'BestNights', 'DriveThru', 'HairSpecializesIn', 'AgesAllowed', 'Open24Hours', 'DietaryRestrictions', 'RestaurantsCounterService', 'BYOB']
        self.df.columns = col
        print(self.df)
            

            







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

                    #print(openhours)
                #print(total_hours)
                #print(total_mins)
                # trans mins to hours
                min_to_hours = total_mins/60
                total_hours += min_to_hours
                
            except:
                total_hours = 0
        except:
            wh = 0
            work_weekend = 0

        return work_weekend, total_hours






if __name__ == '__main__':
    file_name = 'business_sample.json'
    #CleanData(file_name).read_file()



    c = []
    a = [1,2,3,4,5]
    for i in range(3):
        c.append(a)

    print(c)


    #cate_list = []
    #with open('sample.json','r') as f:
    #    content = json.load(f)
    #    try:
    #        cate = content['categories']
    #        cate = cate.split(',')
    #        for i in cate:
    #            if cate not in cate_list:
    #                cate_list.append(i)
    #    except:
    #        pass

    #print(cate_list)




