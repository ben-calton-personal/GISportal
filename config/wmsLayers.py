layers = [
   {
      "name": "cmorph_rainfall_daily",
      "options": {
         "providerShortTag": "CNR"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/cnr/cmorph-daily-rainfall-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/cnr/cmorph-daily-rainfall-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "rfe": {
            "Confidence": "Unknown",
            "interval": "Daily",
            "niceName": "Rainfall (CMORPH), daily",
            "data_provider": "CNR",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },   
   {
      "name": "tamsat_rfe_dekadal",
      "options": {
         "providerShortTag": "CNR"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/cnr/tamsat-rfe-dekadal-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/cnr/tamsat-rfe-dekadal-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "rfe": {
            "Confidence": "Unknown",
            "interval": "Dekadal",
            "niceName": "Rainfall Estimate - Africa",
            "data_provider": "CNR",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Africa"
         }
      }
   },
   {
      "name": "mod16_monthly_aet",
      "options": {
         "providerShortTag": "Deltares"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/deltares/aet-pet/MOD16_AET_corr_monthly_2000_2013.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/deltares/aet-pet/MOD16_AET_corr_monthly_2000_2013.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "AET": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Actual ET - New Zealand (monthly)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Australasia"
         },
         "Uncertainty": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Actual ET uncertainty - New Zealand (monthly)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Australasia"
         }
      }
   },
   {
      "name": "mod16_monthly_pet",
      "options": {
         "providerShortTag": "Deltares"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/deltares/aet-pet/MOD16_PET_corr_monthly_2000_2013.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/deltares/aet-pet/MOD16_PET_corr_monthly_2000_2013.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "PET": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Potential ET - New Zealand (monthly)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Australasia"
         },
         "Uncertainty": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Potential ET uncertainty - New Zealand (monthly)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Australasia"
         }
      }
   },
   {
      "name": "reference-et-hargreaves",
      "options": {
         "providerShortTag": "Deltares"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/deltares/reference-et/hargreaves-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/deltares/reference-et/hargreaves-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "HR": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Reference Potential ET - Hargreaves (daily)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "reference-et-penmanmonteith",
      "options": {
         "providerShortTag": "Deltares"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/deltares/reference-et/penmanmonteith-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/deltares/reference-et/penmanmonteith-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "PM": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Reference Potential ET - Penman Monteith (daily)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "reference-et-priestleytaylor",
      "options": {
         "providerShortTag": "Deltares"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/deltares/reference-et/priestleytaylor-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/deltares/reference-et/priestleytaylor-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "PT": {
            "Confidence": "Unknown",
            "interval": "Monthly",
            "niceName": "Reference Potential ET - Priestley Taylor (daily)",
            "data_provider": "Deltares",
            "indicator_type": [
               "Evapotranspiration"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_lwdown",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/lwdown_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/lwdown_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "LWdown": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Surface incident longwave radiation",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Radiation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_psurf",
      "options": {
         "providerShortTag": "ECMWF",
         "license": "The Apache Software License",
         "licenseUrl": "https://www.apache.org/licenses/LICENSE-2.0.html",
         "allowDownload": "false"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/psurf_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/psurf_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "PSurf": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Surface atmospheric pressure",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_qair",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/qair_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/qair_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qair": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Near surface specific humidity",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_rainf",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/rainf_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/rainf_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_swdown",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/swdown_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/swdown_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "SWdown": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Surface incident shortwave radiation",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Radiation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_snowf",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/snowf_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/snowf_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Snowf": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Snowfall rate",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_tair",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/tair_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/tair_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Tair": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Air Temperature",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_wind",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/wind_3hourly.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/wind_3hourly.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Wind": {
            "Confidence": "Unknown",
            "interval": "3-hourly",
            "niceName": "Wind Speed",
            "data_provider": "ECMWF Forcing Data",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "esa_cci_soil_moisture",
      "options": {
         "providerShortTag": "TUWien"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/tuw/esa-cci-soilmoisture-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/tuw/esa-cci-soilmoisture-daily-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "sm": {
            "Confidence": "Unknown",
            "interval": "daily",
            "niceName": "Soil moisture",
            "data_provider": "Technische Universitat Wien",
            "indicator_type": [
               "Sub-Surface Water"
            ],
            "region": "Global"
         },
         "sm_uncertainty": {
            "Confidence": "Unknown",
            "interval": "daily",
            "niceName": "Soil moisture uncertainty",
            "data_provider": "Technische Universitat Wien",
            "indicator_type": [
               "Sub-Surface Water"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "csiro_wrr1_monthly",
      "options": {
         "providerShortTag": "CSIRO"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/csiro/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/csiro/wrr1-monthly-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bar Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },
   {
      "name": "csiro_wrr1_daily",
      "options": {
         "providerShortTag": "CSIRO"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/csiro/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/csiro/wrr1-daily-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "W3RA - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },

   {
      "name": "univk_wrr1_monthly",
      "options": {
         "providerShortTag": "UniKassel"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/univk/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/univk/wrr1-monthly-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bar Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },
   {
      "name": "univk_wrr1_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/univk/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/univk/wrr1-daily-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "WaterGAP3 - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },
   {
      "name": "ecmwf_wrr1_monthly",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/wrr1-monthly-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bar Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },
   {
      "name": "ecmwf_wrr1_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/wrr1-daily-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "HTESSEL - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },

   {
      "name": "uu_wrr1_monthly",
      "options": {
         "providerShortTag": "UU"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/uu/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/uu/wrr1-monthly-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bar Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Monthly (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   },
   {
      "name": "uu_wrr1_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/uu/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/uu/wrr1-daily-agg.nc?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "Qh": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowDepth": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Depth of Snow Layer",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Rainf": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWnet": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SWE": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TotMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsm": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RivOut": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "TVeg": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Albedo": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qsb": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SurfMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Evap": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qs": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Surface Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "AvgSurfT": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ESoil": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "ECanop": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "SnowFrac": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Snow Cover Fraction",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Precip": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Precipitation",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "RootMoist": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "CanopInt": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Canopy Water Storage",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "LAI": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Qle": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         },
         "Runoff": {
            "Confidence": "Unknown",
            "interval": "monthly",
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            
            "model": "PCR-GLOBWB - Daily (WRR1)",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1"
            ]
         }
      }
   }

]
