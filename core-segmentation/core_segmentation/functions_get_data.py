# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:42:46 2021

@author: chris.cirelli
"""


def get_catcols():
    return ['Construction', 'OccupancyCode', 'Financed', 'GL1OccupancyCode', 'County', 'BGIIConstructionSymbol',
            'PropertyTerritoryBGII', 'GLClassCode1Description', 'EarthquakeTerritory', 'PropertyClassDescription']

def get_intcols():
    return ['LN_cp_othr_socl', 'LN_cp_othr_fd',
       'LN_cp_liab_socl', 'LN_cp_wwat_socl', 'PropertyClassCode',
       'Demo_ESHMEDINC', 'LN_cp_wind_weath', 'LN_cp_wate_socl',
       'LN_cp_thft_fd', 'ProtectionClass', 'LN_cp_wate_llh', 'GL1Exposure',
       'VandalismExclusion', 'LN_cp_fire_topo', 'LiabilityTerritory',
       'LN_cp_thft_llh', 'LN_cp_fire_fd', 'LN_cp_hail_socl',
       'LN_cp_fire_weath', 'WindandHailExclusion', 'GLClassCode1',
       'LN_cp_hail_topo', 'LN_cp_wind_llh', 'LN_cp_liab_llh',
       'SprinklerCredit', 'LN_cp_othr_topo', 'LN_iso_territory',
       'LN_cp_wwat_topo', 'Demo_ESHAVGINC', 'LN_cp_wwat_weath',
       'LN_cp_fire_socl', 'LN_cp_fire_llh', 'LN_cp_hail_llh', 'LN_cp_othr_llh',
       'LN_cp_wind_socl', 'LN_cp_thft_socl', 'LN_cp_wind_topo',
       'LN_cp_liab_fd', 'BuildingLimit', 'LN_cp_hail_weath',
       'ConstructionCode', 'PropertyTerritoryBGI', 'LN_cp_wwat_llh',
       'Demo_ESPERCPINC', 'LN_cp_thft_topo']

def get_floatcols():
    return ['Demo_pct_60_64', 'LN_rl_wwat_llh', 'Demo_pct40_45K', 'Demo_pct_80_84',
       'LN_rl_hail_weath', 'PropertyTerrorismTier', 'Demo_ESPOPCHPCT',
       'LN_liability_factor', 'Demo_pct25_30K', 'Demo_pct10_14K',
       'LN_rl_liab_fd', 'Stories', 'LN_fire_factor', 'Demo_pct_85P',
       'Demo_pct_50_54', 'LN_rl_othr_socl', 'Demo_ESPOPDENS', 'LN_wind_factor',
       'LN_rl_othr_llh', 'Demo_pct_75_79', 'Demo_pct_10_14', 'Demo_pct_35_39',
       'LN_sfr_count', 'LN_rl_wwat_socl', 'Demo_pct_15_19', 'Demo_pct_55_59',
       'Demo_pctMALES', 'LN_rl_wind_weath', 'LN_rl_wind_topo',
       'Demo_pct35_40K', 'LN_rl_fire_weath', 'Demo_pct10K', 'LN_rl_wate_llh',
       'SquareFootage', 'Demo_ESAVGHHSZE', 'LN_rl_hail_topo',
       'LN_theft_factor', 'Demo_pct_65_69', 'LN_rl_wwat_topo', 'Demo_pct_0_4',
       'Demo_pct_25_29', 'Demo_pct75_100K', 'LN_rl_othr_fd', 'Demo_pct_20_24',
       'LN_rl_othr_topo', 'LN_rl_thft_fd', 'Demo_pct150_200K',
       'LN_water_weather_factor', 'Demo_pct125_150K', 'LN_other_factor',
       'LN_rl_liab_socl', 'FireIndex', 'LN_rl_fire_llh', 'TIV', 'YearBuilt',
       'Demo_pct15_20K', 'LN_rl_liab_llh', 'LN_rl_thft_llh', 'Demo_pct200KP',
       'Demo_pctHUVACANT', 'Demo_pctHURENTER', 'LN_rl_thft_socl',
       'Demo_pct20_25K', 'LN_rl_thft_topo', 'LN_rl_hail_socl', 'Demo_pct_5_9',
       'Demo_pct100_125K', 'Demo_pct_40_44', 'LN_rl_wwat_weath',
       'Demo_pct50_60K', 'Demo_pct30_35K', 'LN_rl_wind_socl', 'Demo_pct60_75K',
       'Demo_pct45_50K', 'LN_rl_hail_llh', 'LN_rl_fire_socl', 'LN_rl_wind_llh',
       'LN_water_factor', 'Demo_pct_45_49', 'Demo_pct_70_74',
       'Demo_pctONEPERSHH', 'LN_rl_wate_socl', 'LN_hail_factor',
       'Demo_ESMEDAGE', 'Demo_pctHUOWNER', 'Demo_avgAGGINC', 'LN_rl_fire_fd',
       'LN_rl_fire_topo']

def get_top10_vars():
    return ['TIV', 'YearBuilt', 'Demo_pctHUVACANT', 'Demo_pctHUOWNER', 'Demo_pct_45_49',
           'Demo_pct20_25K', 'Demo_pct30_35K', 'Demo_pct35_40K', 'Demo_pct45_50K']
