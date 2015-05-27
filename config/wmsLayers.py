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
            "data_type" : "Earth Observation",
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
            "data_type" : "Earth Observation",
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
            "data_type" : "Earth Observation",
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
            "data_type" : "Earth Observation",
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
            "data_type" : "Earth Observation",
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
            "data_type" : "Earth Observation",
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
            "data_type" : "Ecosystem Model",
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
            "data_type" : "Ecosystem Model",
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
            "data_type" : "Ecosystem Model",
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_lwdown_3h",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_lwdown_3h_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/lwdown_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/lwdown_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Surface incident longwave radiation",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Radiation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_psurf_daily",
      "options": {
         "providerShortTag": "ECMWF",
         "license": "The Apache Software License",
         "licenseUrl": "https://www.apache.org/licenses/LICENSE-2.0.html",
         "allowDownload": "false"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/psurf_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/psurf_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Surface atmospheric pressure",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_qair_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/qair_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/qair_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Near surface specific humidity",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_rainf_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/rainf_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/rainf_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Rainfall Rate",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_swdown_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/swdown_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/swdown_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Surface incident shortwave radiation",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Radiation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_snowf_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/snowf_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/snowf_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Snowfall rate",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Precipitation"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_tair_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/tair_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/tair_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Air Temperature",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "indicator_type": [
               "Meteorology"
            ],
            "region": "Global"
         }
      }
   },
   {
      "name": "ecmwf_forcing_wind_daily",
      "options": {
         "providerShortTag": "ECMWF"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ecmwf/met_forcing_v0/wind_daily.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ecmwf/met_forcing_v0/wind_daily.nc?",
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
            "interval": "Daily",
            "niceName": "Wind Speed",
            "data_provider": "ECMWF",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
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
            "interval": "Daily",
            "niceName": "Soil moisture",
            "data_provider": "Technische Universitat Wien",
            "indicator_type": [
               "Sub-Surface Water"
            ],
            "data_type": "Earth Observation",
            "region": "Global"
         },
         "sm_uncertainty": {
            "interval": "Daily",
            "niceName": "Soil moisture uncertainty",
            "data_provider": "Technische Universitat Wien",
            "indicator_type": [
               "Sub-Surface Water"
            ],
            "data_type": "Earth Observation",
            "region": "Global"
         }
      }
   },
   {
      "name": "ceh_wrr1_monthly",
      "options": {
         "providerShortTag": "CEH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ceh/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ceh/wrr1-monthly-agg.nc?",
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
         "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Monthly",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "ceh_wrr1_daily",
      "options": {
         "providerShortTag": "CEH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/ceh/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/ceh/wrr1-daily-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Centre for Ecology and Hydrology, UK",
            "interval": "Daily",            
            "model": "JULES",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "CSIRO",
            "interval": "Monthly",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "CSIRO",
            "interval": "Daily",            
            "model": "W3RA",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ECMWF",
            "interval": "Monthly",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ECMWF",
            "interval": "Daily",            
            "model": "HTESSEL",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "eth_wrr1_monthly",
      "options": {
         "providerShortTag": "ETH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/eth/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/eth/wrr1-monthly-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "eth_wrr1_daily",
      "options": {
         "providerShortTag": "ETH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/eth/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/eth/wrr1-daily-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "eth_wrr1_exp1_monthly",
      "options": {
         "providerShortTag": "ETH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/eth/wrr1-exp1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/eth/wrr1-exp1-monthly-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ETH",
            "interval": "Monthly",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "eth_wrr1_exp1_daily",
      "options": {
         "providerShortTag": "ETH"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/eth/wrr1-exp1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/eth/wrr1-exp1-daily-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "ETH",
            "interval": "Daily",            
            "model": "SWBM - Exp1",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "metfr_wrr1_monthly",
      "options": {
         "providerShortTag": "METFR"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/metfr/wrr1-monthly-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/metfr/wrr1-monthly-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Meteo France",
            "interval": "Monthly",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "metfr_wrr1_daily",
      "options": {
         "providerShortTag": "METFR"
      },
      "services": {
         "wms": {
            "url": "https://wci.earth2observe.eu/thredds/wms/metfr/wrr1-daily-agg.nc?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://wci.earth2observe.eu/thredds/wcs/metfr/wrr1-daily-agg.nc?",
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Meteo France",
            "interval": "Daily",            
            "model": "Surfex-Trip",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Universitat Kassel",
            "interval": "Monthly",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         }
      }
   },
   {
      "name": "univk_wrr1_daily",
      "options": {
         "providerShortTag": "UniKassel"
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
               "Precip": {
            "niceName": "Total Precipitation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Precipitation"
            ]
         },
         "Evap": {
            "niceName": "Total Evapotranspiration",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "Runoff": {
            "niceName": "Total Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Rainf": {
            "niceName": "Rainfall",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Meteorology",
            ]
         },
         "Qs": {
            "niceName": "Total Surface Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Qsb": {
            "niceName": "Sub-Surface Runoff",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Sub-Surface Water"
            ]
         },
         "Qrec": {
            "niceName": "Recharge",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
            ]
         },
         "Qsm": {
            "niceName": "Snowmelt",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "PotEvap": {
            "niceName": "Potential Evapotranspiration",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration",
            ]
         },
         "ECanop": {
            "niceName": "Interception Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "TVeg": {
            "niceName": "Vegetation Transpiration",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "ESoil": {
            "niceName": "Bare Soil Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "EWater": {
            "niceName": "Open Water Evaporation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Evapotranspiration"
            ]
         },
         "RivOut": {
            "niceName": "River Discharge",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "Dis": {
            "niceName": "Point River Discharge",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Water Balance Components",
               "Surface Water"
            ]
         },
         "SWnet": {
            "niceName": "Net Shortwave Radiation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "LWnet": {
            "niceName": "Net Longwave Radiation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
               "Radiation"
            ]
         },
         "Qle": {
            "niceName": "Latent Heat Flux",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "Qh": {
            "niceName": "Sensible Heat Flux",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "Energy Balance Components",
            ]
         },
         "AvgSurfT": {
            "niceName": "Average Surface Temperature",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Meteorology"
            ]
         },
         "Albedo": {
            "niceName": "Surface Albedo",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "LAI": {
            "niceName": "Leaf Area Index",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWE": {
            "niceName": "Snow Water Equivalent",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "CanopInt": {
            "niceName": "Total Canopy water Storage",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SWEVeg": {
            "niceName": "SWE Intercepted by Vegetation",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
            ]
         },
         "SurfStor": {
            "niceName": "Surface Water Storage",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "WaterTableD": {
            "niceName": "Water Table Depth",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "SnowFrac": {
            "niceName": "Snow Covered Fraction",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SnowDepth": {
            "niceName": "Snow Depth",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "SurfMoist": {
            "niceName": "Surface Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Surface Water"
            ]
         },
         "RootMoist": {
            "niceName": "Root Zone Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "TotMoist": {
            "niceName": "Total Soil Moisture",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
            ]
         },
         "GroundMoist": {
            "niceName": "Ground Water",
            "data_provider": "Universitat Kassel",
            "interval": "Daily",            
            "model": "WaterGAP3",
            "data_type": "Ecosystem Model",
            "forcing_version": "Version 0",
            "region": "Global",
            "indicator_type": [
               "Water Resource Re-analysis v1",
               "State Variables",
               "Sub-Surface Water"
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
      __HERE__
      }
   },
   {
      "name": "uu_wrr1_daily",
      "options": {
         "providerShortTag": "UU"
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
      __HERE__
      }
   }

]
