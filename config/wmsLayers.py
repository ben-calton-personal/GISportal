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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
            "data_provider": "ECMWF Model Data",
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
   }

]
