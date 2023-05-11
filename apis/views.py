from django.shortcuts import render
from rest_framework import generics ,status
import pandas as pd
from apis.utills import Divvy_bike_apis
from rest_framework.response import Response

# Create your views here.
class Total_docks_avail(generics.GenericAPIView):
    def get(self, request):
        try:
            station_details_json = Divvy_bike_apis()
            jsons = station_details_json.station_status_api()
            station_details_df = pd.DataFrame(jsons)
            
            station_details_df.to_csv('file2.csv', header=True, index=False)
            if jsons:
                context={'status':True,'message':"Success","total_docks_avail":station_details_df['num_docks_available'].sum()}
            else:
                context = {'status': False,'message': "No records."}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            # logger.error(f'FailedCSVExcelReportUser:error => {str(e)}')
            context = {'status': False, 'error': {'message': 'Something Went Wrong'}}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class Total_bikes_avail(generics.GenericAPIView):
    def get(self, request):
        try:
            
            station_details_json = Divvy_bike_apis()
            jsons = station_details_json.station_status_api()
            station_details_df = pd.DataFrame(jsons)
            print(station_details_df.columns)
            station_details_df.to_csv('file2.csv', header=True, index=False)
            if jsons:
                context={'status':True,'message':"Success","num_ebikes_available":station_details_df['num_bikes_available'].sum()}
            else:
                context = {'status': False,'message': "No records."}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            # logger.error(f'FailedCSVExcelReportUser:error => {str(e)}')
            context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class Total_active_stations(generics.GenericAPIView):
    def get(self, request):
        try:    
            station_details_json = Divvy_bike_apis()
            jsons = station_details_json.station_status_api()
            station_details_df = pd.DataFrame(jsons)
            total_active_stations = station_details_df[station_details_df['station_status'] == "active"]
            print(total_active_stations,"-------------")
            active_stations_count = total_active_stations['station_status'].tolist()
            print(station_details_df.columns)
            station_details_df.to_csv('file2.csv', header=True, index=False)
            if jsons:
                context={'status':True,'message':"Success","total_active_stations":len(active_stations_count)}
            else:
                context = {'status': False,'message': "No records."}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            # logger.error(f'FailedCSVExcelReportUser:error => {str(e)}')
            context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class Total_reserved_bike(generics.GenericAPIView):
    def get(self, request):
        try:
            free_bike_status_json = Divvy_bike_apis()
            jsons = free_bike_status_json.free_bike_status_api()
            free_bike_status_df = pd.DataFrame(jsons)
            
            reserved_bike = free_bike_status_df[free_bike_status_df['is_reserved'] != 0]
            reserved_bike_count = reserved_bike['is_reserved'].tolist()
            free_bike_status_df.to_csv('free_bike_status_df.csv', header=True, index=False)
            if jsons:
                context={'status':True,'message':"Success","total_bike_reserved":len(reserved_bike_count)}
            else:
                context = {'status': False,'message': "No records."}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            # logger.error(f'FailedCSVExcelReportUser:error => {str(e)}')
            context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Total_availables(generics.GenericAPIView):
    def get(self, request):
        try:
            free_bike_status_json = Divvy_bike_apis()
            station_status_jsons = free_bike_status_json.station_status_api()
            station_status_df = pd.DataFrame(station_status_jsons)
            
            free_bile_jsons = free_bike_status_json.free_bike_status_api()
            free_bike_status_df = pd.DataFrame(free_bile_jsons)
            reserved_bike = free_bike_status_df[free_bike_status_df['is_reserved'] != 0]
            reserved_bike_count = reserved_bike['is_reserved'].tolist()
            
            total_active_stations = station_status_df[station_status_df['station_status'] == "active"]
            active_stations_count = total_active_stations['station_status'].tolist()
            
            
            data_dict = {}

            active_stations_count = total_active_stations['station_status'].tolist()
            data_dict['reserved_bike_count'] = station_status_df['num_docks_available'].sum()
            data_dict['num_bikes_available'] = station_status_df['num_bikes_available'].sum()
            data_dict['total_active_stations'] = len(active_stations_count)
            data_dict['reserved_bike_count'] = len(reserved_bike_count)
            
            
            station_status_df.to_csv('station_status_df.csv', header=True, index=False)
            free_bike_status_df.to_csv('free_bike_status_df.csv', header=True, index=False)
            if free_bile_jsons:
                context={'status':True,'message':"Success","total_availables":data_dict}
            else:
                context = {'status': False,'message': "No records."}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            # logger.error(f'FailedCSVExcelReportUser:error => {str(e)}')
            context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)