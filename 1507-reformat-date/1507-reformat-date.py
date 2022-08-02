class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        
        dict_month = {"jan":'01', "feb":'02', "mar":'03',
                      "apr":'04', "may":'05', "jun":'06',
                      "jul":'07', "aug":'08', "sep":'09',
                      "oct":'10', "nov":'11', "dec":'12'}
        date_list = date.split()
        
        #process day
        day = date_list[0][:-2]
        if int(day) < 10:
            day = '0'+ day
        #process month:
        moth = dict_month[date_list[1].lower()]
        year = date_list[2]
        
        return "-".join((year,moth,day))
        
        
        