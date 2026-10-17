"""
Catalog of NSE and BSE listed stocks in India.
Provides search, autocomplete, and curated indices (Nifty 50, Nifty Next 50, Sensex, Midcaps).
"""
from typing import List, Dict, Optional
import re
import urllib.request
import urllib.parse
import json
import logging
from cachetools import TTLCache

logger = logging.getLogger(__name__)

# Search cache to make repeated searches instant
search_cache = TTLCache(maxsize=1000, ttl=3600)

# Mapping for prominent corporate rebranding and ticker symbol changes in Indian markets
TICKER_ALIASES = {
    "ZOMATO": "ETERNAL",
    "ZOMATO.NS": "ETERNAL.NS",
    "ZOMATO.BO": "ETERNAL.BO",
    "MUTHOOTHFINANCE": "MUTHOOTFIN.NS",
    "MUTHOOTFINANCE": "MUTHOOTFIN.NS",
    "MUTHOOTH": "MUTHOOTFIN.NS",
    "MUTHOOT": "MUTHOOTFIN.NS",
    "543320": "ETERNAL.BO",
    "543320.BO": "ETERNAL.BO",
    "MOTHERSUMI": "MOTHERSON",
    "MOTHERSUMI.NS": "MOTHERSON.NS",
    "ADANITRANS": "ADANIENSOL",
    "ADANITRANS.NS": "ADANIENSOL.NS",
    "CADILAHC": "ZYDUSLIFE",
    "CADILAHC.NS": "ZYDUSLIFE.NS",
    "LTI": "LTIM",
    "LTI.NS": "LTIM.NS",
}

# Comprehensive list of prominent NSE/BSE companies with tickers, names, and sectors
STOCKS_DATABASE: List[Dict[str, str]] = [
    # Top Nifty 50 & Heavyweights
    {"symbol": "RELIANCE.NS", "name": "Reliance Industries Ltd", "sector": "Energy & Conglomerate", "exchange": "NSE", "bse_code": "RELIANCE.BO", "bse_scrip": "500325", "index": "Nifty 50"},
    {"symbol": "TCS.NS", "name": "Tata Consultancy Services Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "TCS.BO", "bse_scrip": "532540", "index": "Nifty 50"},
    {"symbol": "HDFCBANK.NS", "name": "HDFC Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "HDFCBANK.BO", "bse_scrip": "500180", "index": "Nifty 50"},
    {"symbol": "ICICIBANK.NS", "name": "ICICI Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "ICICIBANK.BO", "bse_scrip": "532174", "index": "Nifty 50"},
    {"symbol": "INFY.NS", "name": "Infosys Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "INFY.BO", "bse_scrip": "500209", "index": "Nifty 50"},
    {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel Ltd", "sector": "Telecommunication", "exchange": "NSE", "bse_code": "BHARTIARTL.BO", "bse_scrip": "532454", "index": "Nifty 50"},
    {"symbol": "SBIN.NS", "name": "State Bank of India", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "SBIN.BO", "bse_scrip": "500112", "index": "Nifty 50"},
    {"symbol": "ITC.NS", "name": "ITC Ltd", "sector": "FMCG / Cigarettes / Hotels", "exchange": "NSE", "bse_code": "ITC.BO", "bse_scrip": "500875", "index": "Nifty 50"},
    {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever Ltd", "sector": "FMCG", "exchange": "NSE", "bse_code": "HINDUNILVR.BO", "bse_scrip": "500696", "index": "Nifty 50"},
    {"symbol": "LICI.NS", "name": "Life Insurance Corporation of India", "sector": "Insurance", "exchange": "NSE", "bse_code": "LICI.BO", "bse_scrip": "543526", "index": "Nifty 50"},
    {"symbol": "LT.NS", "name": "Larsen & Toubro Ltd", "sector": "Construction & Engineering", "exchange": "NSE", "bse_code": "LT.BO", "bse_scrip": "500510", "index": "Nifty 50"},
    {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance Ltd", "sector": "Financial Services / NBFC", "exchange": "NSE", "bse_code": "BAJFINANCE.BO", "bse_scrip": "500034", "index": "Nifty 50"},
    {"symbol": "HCLTECH.NS", "name": "HCL Technologies Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "HCLTECH.BO", "bse_scrip": "532281", "index": "Nifty 50"},
    {"symbol": "MARUTI.NS", "name": "Maruti Suzuki India Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "MARUTI.BO", "bse_scrip": "532500", "index": "Nifty 50"},
    {"symbol": "SUNPHARMA.NS", "name": "Sun Pharmaceutical Industries Ltd", "sector": "Healthcare / Pharma", "exchange": "NSE", "bse_code": "SUNPHARMA.BO", "bse_scrip": "524715", "index": "Nifty 50"},
    {"symbol": "TATAMOTORS.NS", "name": "Tata Motors Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "TATAMOTORS.BO", "bse_scrip": "500570", "index": "Nifty 50"},
    {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "KOTAKBANK.BO", "bse_scrip": "500247", "index": "Nifty 50"},
    {"symbol": "AXISBANK.NS", "name": "Axis Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "AXISBANK.BO", "bse_scrip": "532215", "index": "Nifty 50"},
    {"symbol": "NTPC.NS", "name": "NTPC Ltd", "sector": "Power Generation", "exchange": "NSE", "bse_code": "NTPC.BO", "bse_scrip": "532555", "index": "Nifty 50"},
    {"symbol": "ONGC.NS", "name": "Oil & Natural Gas Corporation Ltd", "sector": "Oil & Gas Exploration", "exchange": "NSE", "bse_code": "ONGC.BO", "bse_scrip": "500312", "index": "Nifty 50"},
    {"symbol": "TITAN.NS", "name": "Titan Company Ltd", "sector": "Consumer Discretionary", "exchange": "NSE", "bse_code": "TITAN.BO", "bse_scrip": "500114", "index": "Nifty 50"},
    {"symbol": "ADANIENT.NS", "name": "Adani Enterprises Ltd", "sector": "Metals & Trading", "exchange": "NSE", "bse_code": "ADANIENT.BO", "bse_scrip": "512599", "index": "Nifty 50"},
    {"symbol": "ADANIPORTS.NS", "name": "Adani Ports and SEZ Ltd", "sector": "Infrastructure / Ports", "exchange": "NSE", "bse_code": "ADANIPORTS.BO", "bse_scrip": "532921", "index": "Nifty 50"},
    {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation of India Ltd", "sector": "Power Transmission", "exchange": "NSE", "bse_code": "POWERGRID.BO", "bse_scrip": "532898", "index": "Nifty 50"},
    {"symbol": "TATASTEEL.NS", "name": "Tata Steel Ltd", "sector": "Metals & Mining", "exchange": "NSE", "bse_code": "TATASTEEL.BO", "bse_scrip": "500470", "index": "Nifty 50"},
    {"symbol": "COALINDIA.NS", "name": "Coal India Ltd", "sector": "Mining", "exchange": "NSE", "bse_code": "COALINDIA.BO", "bse_scrip": "533278", "index": "Nifty 50"},
    {"symbol": "BAJAJFINSV.NS", "name": "Bajaj Finserv Ltd", "sector": "Financial Services", "exchange": "NSE", "bse_code": "BAJAJFINSV.BO", "bse_scrip": "532978", "index": "Nifty 50"},
    {"symbol": "ASIANPAINT.NS", "name": "Asian Paints Ltd", "sector": "Paints / Chemicals", "exchange": "NSE", "bse_code": "ASIANPAINT.BO", "bse_scrip": "500820", "index": "Nifty 50"},
    {"symbol": "M&M.NS", "name": "Mahindra & Mahindra Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "M&M.BO", "bse_scrip": "500520", "index": "Nifty 50"},
    {"symbol": "WIPRO.NS", "name": "Wipro Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "WIPRO.BO", "bse_scrip": "507685", "index": "Nifty 50"},
    {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement Ltd", "sector": "Materials / Cement", "exchange": "NSE", "bse_code": "ULTRACEMCO.BO", "bse_scrip": "532538", "index": "Nifty 50"},
    {"symbol": "JSWSTEEL.NS", "name": "JSW Steel Ltd", "sector": "Metals & Mining", "exchange": "NSE", "bse_code": "JSWSTEEL.BO", "bse_scrip": "500228", "index": "Nifty 50"},
    {"symbol": "NESTLEIND.NS", "name": "Nestle India Ltd", "sector": "FMCG / Food", "exchange": "NSE", "bse_code": "NESTLEIND.BO", "bse_scrip": "500790", "index": "Nifty 50"},
    {"symbol": "GRASIM.NS", "name": "Grasim Industries Ltd", "sector": "Diversified Materials", "exchange": "NSE", "bse_code": "GRASIM.BO", "bse_scrip": "500300", "index": "Nifty 50"},
    {"symbol": "HINDALCO.NS", "name": "Hindalco Industries Ltd", "sector": "Metals & Aluminium", "exchange": "NSE", "bse_code": "HINDALCO.BO", "bse_scrip": "500440", "index": "Nifty 50"},
    {"symbol": "TECHM.NS", "name": "Tech Mahindra Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "TECHM.BO", "bse_scrip": "532755", "index": "Nifty 50"},
    {"symbol": "BPCL.NS", "name": "Bharat Petroleum Corporation Ltd", "sector": "Oil & Refining", "exchange": "NSE", "bse_code": "BPCL.BO", "bse_scrip": "500547", "index": "Nifty 50"},
    {"symbol": "EICHERMOT.NS", "name": "Eicher Motors Ltd", "sector": "Automobile / Royal Enfield", "exchange": "NSE", "bse_code": "EICHERMOT.BO", "bse_scrip": "505200", "index": "Nifty 50"},
    {"symbol": "CIPLA.NS", "name": "Cipla Ltd", "sector": "Healthcare / Pharma", "exchange": "NSE", "bse_code": "CIPLA.BO", "bse_scrip": "500087", "index": "Nifty 50"},
    {"symbol": "DRREDDY.NS", "name": "Dr. Reddy's Laboratories Ltd", "sector": "Healthcare / Pharma", "exchange": "NSE", "bse_code": "DRREDDY.BO", "bse_scrip": "500124", "index": "Nifty 50"},
    {"symbol": "BRITANNIA.NS", "name": "Britannia Industries Ltd", "sector": "FMCG / Food", "exchange": "NSE", "bse_code": "BRITANNIA.BO", "bse_scrip": "500825", "index": "Nifty 50"},
    {"symbol": "BAJAJ-AUTO.NS", "name": "Bajaj Auto Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "BAJAJ-AUTO.BO", "bse_scrip": "532977", "index": "Nifty 50"},
    {"symbol": "HEROMOTOCO.NS", "name": "Hero MotoCorp Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "HEROMOTOCO.BO", "bse_scrip": "500182", "index": "Nifty 50"},
    {"symbol": "TATACONSUM.NS", "name": "Tata Consumer Products Ltd", "sector": "FMCG", "exchange": "NSE", "bse_code": "TATACONSUM.BO", "bse_scrip": "500800", "index": "Nifty 50"},
    {"symbol": "DIVISLAB.NS", "name": "Divi's Laboratories Ltd", "sector": "Healthcare / API Pharma", "exchange": "NSE", "bse_code": "DIVISLAB.BO", "bse_scrip": "532488", "index": "Nifty 50"},
    {"symbol": "APOLLOHOSP.NS", "name": "Apollo Hospitals Enterprise Ltd", "sector": "Healthcare / Hospitals", "exchange": "NSE", "bse_code": "APOLLOHOSP.BO", "bse_scrip": "508869", "index": "Nifty 50"},
    {"symbol": "INDUSINDBK.NS", "name": "IndusInd Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "INDUSINDBK.BO", "bse_scrip": "532187", "index": "Nifty 50"},
    {"symbol": "SHRIRAMFIN.NS", "name": "Shriram Finance Ltd", "sector": "Financial Services / NBFC", "exchange": "NSE", "bse_code": "SHRIRAMFIN.BO", "bse_scrip": "511218", "index": "Nifty 50"},
    {"symbol": "BEL.NS", "name": "Bharat Electronics Ltd", "sector": "Defense & Electronics", "exchange": "NSE", "bse_code": "BEL.BO", "bse_scrip": "500049", "index": "Nifty 50"},
    {"symbol": "TRENT.NS", "name": "Trent Ltd (Westside & Zudio)", "sector": "Retail & Fashion", "exchange": "NSE", "bse_code": "TRENT.BO", "bse_scrip": "500251", "index": "Nifty 50"},

    {"symbol": "ETERNAL.NS", "name": "Eternal Ltd (formerly Zomato Ltd / Blinkit)", "sector": "Internet / Food & Quick Commerce", "exchange": "NSE", "bse_code": "ETERNAL.BO", "bse_scrip": "543320", "index": "Nifty Next 50"},
    {"symbol": "HAL.NS", "name": "Hindustan Aeronautics Ltd", "sector": "Aerospace & Defense", "exchange": "NSE", "bse_code": "541154.BO", "index": "Nifty Next 50"},
    {"symbol": "VBL.NS", "name": "Varun Beverages Ltd", "sector": "Beverages / FMCG", "exchange": "NSE", "bse_code": "540180.BO", "index": "Nifty Next 50"},
    {"symbol": "CHOLAFIN.NS", "name": "Cholamandalam Investment and Finance", "sector": "Financial Services", "exchange": "NSE", "bse_code": "511243.BO", "index": "Nifty Next 50"},
    {"symbol": "JIOFIN.NS", "name": "Jio Financial Services Ltd", "sector": "Financial Services", "exchange": "NSE", "bse_code": "543940.BO", "index": "Nifty Next 50"},
    {"symbol": "DMART.NS", "name": "Avenue Supermarts Ltd (DMart)", "sector": "Retail", "exchange": "NSE", "bse_code": "540376.BO", "index": "Nifty Next 50"},
    {"symbol": "POLYCAB.NS", "name": "Polycab India Ltd", "sector": "Electricals & Cables", "exchange": "NSE", "bse_code": "542652.BO", "index": "Nifty Next 50"},
    {"symbol": "IRFC.NS", "name": "Indian Railway Finance Corporation", "sector": "Railways / NBFC", "exchange": "NSE", "bse_code": "543257.BO", "index": "Nifty Next 50"},
    {"symbol": "PFC.NS", "name": "Power Finance Corporation Ltd", "sector": "Financials / Power NBFC", "exchange": "NSE", "bse_code": "532810.BO", "index": "Nifty Next 50"},
    {"symbol": "RECLTD.NS", "name": "REC Ltd", "sector": "Financials / Power NBFC", "exchange": "NSE", "bse_code": "532955.BO", "index": "Nifty Next 50"},
    {"symbol": "TATAPOWER.NS", "name": "Tata Power Company Ltd", "sector": "Power Generation / Green Energy", "exchange": "NSE", "bse_code": "500400.BO", "index": "Nifty Next 50"},
    {"symbol": "GAIL.NS", "name": "GAIL (India) Ltd", "sector": "Gas Transmission", "exchange": "NSE", "bse_code": "532155.BO", "index": "Nifty Next 50"},
    {"symbol": "VEDL.NS", "name": "Vedanta Ltd", "sector": "Metals & Mining", "exchange": "NSE", "bse_code": "500295.BO", "index": "Nifty Next 50"},
    {"symbol": "SIEMENS.NS", "name": "Siemens Ltd", "sector": "Capital Goods & Tech", "exchange": "NSE", "bse_code": "500550.BO", "index": "Nifty Next 50"},
    {"symbol": "ABB.NS", "name": "ABB India Ltd", "sector": "Heavy Electrical Equipment", "exchange": "NSE", "bse_code": "500002.BO", "index": "Nifty Next 50"},
    {"symbol": "DLF.NS", "name": "DLF Ltd", "sector": "Real Estate", "exchange": "NSE", "bse_code": "532868.BO", "index": "Nifty Next 50"},
    {"symbol": "GODREJCP.NS", "name": "Godrej Consumer Products Ltd", "sector": "FMCG", "exchange": "NSE", "bse_code": "532424.BO", "index": "Nifty Next 50"},
    {"symbol": "PIDILITIND.NS", "name": "Pidilite Industries Ltd (Fevicol)", "sector": "Chemicals & Adhesives", "exchange": "NSE", "bse_code": "500331.BO", "index": "Nifty Next 50"},
    {"symbol": "HAVELLS.NS", "name": "Havells India Ltd", "sector": "Consumer Electricals", "exchange": "NSE", "bse_code": "517354.BO", "index": "Nifty Next 50"},
    {"symbol": "BANKBARODA.NS", "name": "Bank of Baroda", "sector": "Banking / PSU", "exchange": "NSE", "bse_code": "532134.BO", "index": "Nifty Next 50"},
    {"symbol": "PNB.NS", "name": "Punjab National Bank", "sector": "Banking / PSU", "exchange": "NSE", "bse_code": "532461.BO", "index": "Nifty Next 50"},
    {"symbol": "CANBK.NS", "name": "Canara Bank", "sector": "Banking / PSU", "exchange": "NSE", "bse_code": "532483.BO", "index": "Nifty Next 50"},
    {"symbol": "IOC.NS", "name": "Indian Oil Corporation Ltd", "sector": "Oil & Refining", "exchange": "NSE", "bse_code": "530965.BO", "index": "Nifty Next 50"},
    {"symbol": "INDIGO.NS", "name": "InterGlobe Aviation Ltd (IndiGo)", "sector": "Aviation", "exchange": "NSE", "bse_code": "539448.BO", "index": "Nifty Next 50"},
    {"symbol": "TVSMOTOR.NS", "name": "TVS Motor Company Ltd", "sector": "Automobile / Two-Wheelers", "exchange": "NSE", "bse_code": "532343.BO", "index": "Nifty Next 50"},
    {"symbol": "LTIM.NS", "name": "LTIMindtree Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "540005.BO", "index": "Nifty Next 50"},
    {"symbol": "PERSISTENT.NS", "name": "Persistent Systems Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "533179.BO", "index": "Nifty Midcap"},
    {"symbol": "COFORGE.NS", "name": "Coforge Ltd", "sector": "Information Technology", "exchange": "NSE", "bse_code": "532541.BO", "index": "Nifty Midcap"},
    {"symbol": "KPITTECH.NS", "name": "KPIT Technologies Ltd", "sector": "Automotive Software / Tech", "exchange": "NSE", "bse_code": "542651.BO", "index": "Nifty Midcap"},
    {"symbol": "TATAELXSI.NS", "name": "Tata Elxsi Ltd", "sector": "Design & Technology", "exchange": "NSE", "bse_code": "500408.BO", "index": "Nifty Midcap"},
    {"symbol": "BOSCHLTD.NS", "name": "Bosch Ltd", "sector": "Auto Ancillary", "exchange": "NSE", "bse_code": "500530.BO", "index": "Nifty Next 50"},
    {"symbol": "MOTHERSON.NS", "name": "Samvardhana Motherson International", "sector": "Auto Components", "exchange": "NSE", "bse_code": "517334.BO", "index": "Nifty Next 50"},
    {"symbol": "PAYTM.NS", "name": "One 97 Communications Ltd (Paytm)", "sector": "Fintech", "exchange": "NSE", "bse_code": "543396.BO", "index": "Nifty Midcap"},
    {"symbol": "NYKAA.NS", "name": "FSN E-Commerce Ventures (Nykaa)", "sector": "Beauty & E-Commerce", "exchange": "NSE", "bse_code": "543384.BO", "index": "Nifty Midcap"},
    {"symbol": "POLICYBZR.NS", "name": "PB Fintech Ltd (PolicyBazaar)", "sector": "Insurtech", "exchange": "NSE", "bse_code": "543390.BO", "index": "Nifty Midcap"},
    {"symbol": "RVNL.NS", "name": "Rail Vikas Nigam Ltd", "sector": "Railways Infrastructure", "exchange": "NSE", "bse_code": "542649.BO", "index": "Nifty Midcap"},
    {"symbol": "MAZDOCK.NS", "name": "Mazagon Dock Shipbuilders Ltd", "sector": "Defense / Shipbuilding", "exchange": "NSE", "bse_code": "543237.BO", "index": "Nifty Midcap"},
    {"symbol": "COCHINSHIP.NS", "name": "Cochin Shipyard Ltd", "sector": "Defense / Shipbuilding", "exchange": "NSE", "bse_code": "540679.BO", "index": "Nifty Midcap"},
    {"symbol": "BDL.NS", "name": "Bharat Dynamics Ltd", "sector": "Defense Missiles", "exchange": "NSE", "bse_code": "541143.BO", "index": "Nifty Midcap"},
    {"symbol": "BHEL.NS", "name": "Bharat Heavy Electricals Ltd", "sector": "Power Equipment / Capital Goods", "exchange": "NSE", "bse_code": "500103.BO", "index": "Nifty Next 50"},
    {"symbol": "SUZLON.NS", "name": "Suzlon Energy Ltd", "sector": "Renewable Wind Energy", "exchange": "NSE", "bse_code": "532667.BO", "index": "Nifty Midcap"},
    {"symbol": "IDFCFIRSTB.NS", "name": "IDFC First Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "539437.BO", "index": "Nifty Midcap"},
    {"symbol": "FEDERALBNK.NS", "name": "Federal Bank Ltd", "sector": "Banking", "exchange": "NSE", "bse_code": "500469.BO", "index": "Nifty Midcap"},
    {"symbol": "AUBANK.NS", "name": "AU Small Finance Bank Ltd", "sector": "Banking / SFB", "exchange": "NSE", "bse_code": "540611.BO", "index": "Nifty Midcap"},
    {"symbol": "PRESTIGE.NS", "name": "Prestige Estates Projects Ltd", "sector": "Real Estate", "exchange": "NSE", "bse_code": "533274.BO", "index": "Nifty Midcap"},
    {"symbol": "OBEROIRLTY.NS", "name": "Oberoi Realty Ltd", "sector": "Real Estate", "exchange": "NSE", "bse_code": "533273.BO", "index": "Nifty Midcap"},
    {"symbol": "GODREJPROP.NS", "name": "Godrej Properties Ltd", "sector": "Real Estate", "exchange": "NSE", "bse_code": "533150.BO", "index": "Nifty Midcap"},
    {"symbol": "LODHA.NS", "name": "Macrotech Developers Ltd (Lodha)", "sector": "Real Estate", "exchange": "NSE", "bse_code": "543287.BO", "index": "Nifty Midcap"},
    {"symbol": "TATACOMM.NS", "name": "Tata Communications Ltd", "sector": "Telecom & Cloud", "exchange": "NSE", "bse_code": "500483.BO", "index": "Nifty Midcap"},
    {"symbol": "VOLTAS.NS", "name": "Voltas Ltd (Tata AC)", "sector": "Consumer Durables / AC", "exchange": "NSE", "bse_code": "500575.BO", "index": "Nifty Midcap"},
    {"symbol": "DEEPAKNTR.NS", "name": "Deepak Nitrite Ltd", "sector": "Specialty Chemicals", "exchange": "NSE", "bse_code": "506401.BO", "index": "Nifty Midcap"},
    {"symbol": "SRF.NS", "name": "SRF Ltd", "sector": "Chemicals & Packaging", "exchange": "NSE", "bse_code": "503806.BO", "index": "Nifty Midcap"},
    {"symbol": "ASTRAL.NS", "name": "Astral Ltd", "sector": "Building Materials / Pipes", "exchange": "NSE", "bse_code": "532830.BO", "index": "Nifty Midcap"},
    {"symbol": "SUPREMEIND.NS", "name": "Supreme Industries Ltd", "sector": "Plastics & Pipes", "exchange": "NSE", "bse_code": "509930.BO", "index": "Nifty Midcap"},
    {"symbol": "KAYNES.NS", "name": "Kaynes Technology India Ltd", "sector": "Electronics Manufacturing", "exchange": "NSE", "bse_code": "543664.BO", "index": "Nifty Smallcap"},
    {"symbol": "DIXON.NS", "name": "Dixon Technologies (India) Ltd", "sector": "Electronics Manufacturing", "exchange": "NSE", "bse_code": "540699.BO", "index": "Nifty Midcap"},
    {"symbol": "CDSL.NS", "name": "Central Depository Services (India)", "sector": "Financial Market Infrastructure", "exchange": "NSE", "bse_code": "542323.BO", "index": "Nifty Midcap"},
    {"symbol": "BSE.NS", "name": "BSE Ltd (Stock Exchange)", "sector": "Financial Market Infrastructure", "exchange": "NSE", "bse_code": "540565.BO", "index": "Nifty Midcap"},
    {"symbol": "MCX.NS", "name": "Multi Commodity Exchange of India", "sector": "Financial Exchange", "exchange": "NSE", "bse_code": "534091.BO", "index": "Nifty Midcap"},
    {"symbol": "ANGELONE.NS", "name": "Angel One Ltd", "sector": "Fintech / Stock Broking", "exchange": "NSE", "bse_code": "543235.BO", "index": "Nifty Midcap"},
    {"symbol": "IREDA.NS", "name": "Indian Renewable Energy Development Agency", "sector": "Green Energy Financing", "exchange": "NSE", "bse_code": "544026.BO", "index": "Nifty Midcap"},
    {"symbol": "HUDCO.NS", "name": "Housing & Urban Development Corp", "sector": "Housing Finance / PSU", "exchange": "NSE", "bse_code": "540530.BO", "index": "Nifty Midcap"},
    {"symbol": "NBCC.NS", "name": "NBCC (India) Ltd", "sector": "Construction / PSU", "exchange": "NSE", "bse_code": "534309.BO", "index": "Nifty Midcap"},
    {"symbol": "NHPC.NS", "name": "NHPC Ltd", "sector": "Hydro Power", "exchange": "NSE", "bse_code": "533098.BO", "index": "Nifty Midcap"},
    {"symbol": "SJVN.NS", "name": "SJVN Ltd", "sector": "Hydro & Solar Power", "exchange": "NSE", "bse_code": "533206.BO", "index": "Nifty Midcap"},
    {"symbol": "OIL.NS", "name": "Oil India Ltd", "sector": "Oil Exploration", "exchange": "NSE", "bse_code": "533106.BO", "index": "Nifty Midcap"},
    {"symbol": "PETRONET.NS", "name": "Petronet LNG Ltd", "sector": "Gas Infrastructure", "exchange": "NSE", "bse_code": "532522.BO", "index": "Nifty Midcap"},
    {"symbol": "APLAPOLLO.NS", "name": "APL Apollo Tubes Ltd", "sector": "Steel Pipes", "exchange": "NSE", "bse_code": "533758.BO", "index": "Nifty Midcap"},
    {"symbol": "JSWINFRA.NS", "name": "JSW Infrastructure Ltd", "sector": "Ports & Infra", "exchange": "NSE", "bse_code": "543994.BO", "index": "Nifty Midcap"},
    {"symbol": "SWIGGY.NS", "name": "Swiggy Ltd", "sector": "Internet / Food & Grocery Delivery", "exchange": "NSE", "bse_code": "544285.BO", "index": "New Age"},
    {"symbol": "HYUNDAI.NS", "name": "Hyundai Motor India Ltd", "sector": "Automobile", "exchange": "NSE", "bse_code": "544274.BO", "index": "Large Cap"},
    {"symbol": "MUTHOOTFIN.NS", "name": "Muthoot Finance Ltd", "sector": "Financial Services / Gold Loans", "exchange": "NSE", "bse_code": "MUTHOOTFIN.BO", "bse_scrip": "533398", "index": "Nifty Next 50"},
    {"symbol": "MANAPPURAM.NS", "name": "Manappuram Finance Ltd", "sector": "Financial Services / Gold Loans", "exchange": "NSE", "bse_code": "MANAPPURAM.BO", "bse_scrip": "531213", "index": "Nifty Midcap"},
    {"symbol": "YESBANK.NS", "name": "Yes Bank Ltd", "sector": "Financial Services / Banking", "exchange": "NSE", "bse_code": "YESBANK.BO", "bse_scrip": "532648", "index": "Nifty Midcap"},
    {"symbol": "IDEA.NS", "name": "Vodafone Idea Ltd", "sector": "Telecommunication", "exchange": "NSE", "bse_code": "IDEA.BO", "bse_scrip": "532822", "index": "Nifty Midcap"},
    {"symbol": "OLAELEC.NS", "name": "Ola Electric Mobility Ltd", "sector": "Automobile / EV", "exchange": "NSE", "bse_code": "OLAELEC.BO", "bse_scrip": "544226", "index": "Midcap"},
    {"symbol": "IRCTC.NS", "name": "Indian Railway Catering and Tourism Corp", "sector": "Railways / Tourism", "exchange": "NSE", "bse_code": "IRCTC.BO", "bse_scrip": "542830", "index": "Nifty Next 50"},
]

def normalize_ticker(query: str, default_exchange: str = "NS") -> str:
    """
    Normalizes any user query into a valid Yahoo Finance ticker for NSE or BSE,
    automatically resolving corporate name/ticker changes (e.g. ZOMATO -> ETERNAL).
    """
    clean = query.strip().upper()
    if clean in TICKER_ALIASES:
        return TICKER_ALIASES[clean]

    # Check without exchange extension
    base = clean.replace(".NS", "").replace(".BO", "")
    if base in TICKER_ALIASES:
        mapped = TICKER_ALIASES[base]
        suffix = ".BO" if clean.endswith(".BO") else f".{default_exchange}"
        return mapped if (mapped.endswith(".NS") or mapped.endswith(".BO")) else f"{mapped}{suffix}"

    if clean.endswith(".NS") or clean.endswith(".BO"):
        return clean
    
    # If purely numeric, it's typically a BSE security code (e.g., 500325)
    if clean.isdigit():
        return f"{clean}.BO"
        
    return f"{clean}.{default_exchange}"

def search_stocks(query: str, limit: int = 15) -> List[Dict[str, str]]:
    """
    Search stocks across NSE and BSE (just like Zerodha & Groww).
    Matches local curated catalog, resolves brand aliases, and queries live
    Indian equities via Yahoo Finance Search API for all 4,000+ listed companies.
    """
    if not query or not query.strip():
        return STOCKS_DATABASE[:limit]

    q_clean = query.strip()
    cache_key = q_clean.lower()
    if cache_key in search_cache:
        return search_cache[cache_key]

    q = q_clean.lower()
    matches: List[Dict[str, str]] = []
    seen = set()

    # 1. Check exact aliases (e.g. ZOMATO -> ETERNAL, MUTHOOTHFINANCE -> MUTHOOTFIN)
    alias_key = re.sub(r'[^a-zA-Z0-9]', '', q_clean.upper().replace(".NS", "").replace(".BO", ""))
    if alias_key in TICKER_ALIASES:
        resolved_sym = TICKER_ALIASES[alias_key]
        if not resolved_sym.endswith(".NS") and not resolved_sym.endswith(".BO"):
            resolved_sym = f"{resolved_sym}.NS"
        alias_item = next((s for s in STOCKS_DATABASE if s["symbol"] == resolved_sym), None)
        if not alias_item:
            alias_item = {
                "symbol": resolved_sym,
                "name": resolved_sym.replace(".NS", "").replace(".BO", ""),
                "sector": "Indian Equities",
                "exchange": "BSE" if resolved_sym.endswith(".BO") else "NSE",
                "bse_code": resolved_sym.replace(".NS", ".BO"),
                "index": "Listed Equity"
            }
        matches.append(alias_item)
        seen.add(alias_item["symbol"])

    # 2. Match against local curated STOCKS_DATABASE (Instant 0ms)
    for item in STOCKS_DATABASE:
        sym = item["symbol"].lower().replace(".ns", "").replace(".bo", "")
        bse = item.get("bse_code", "").lower().replace(".bo", "")
        name = item["name"].lower()
        sector = item.get("sector", "").lower()

        if sym == q or bse == q:
            if item["symbol"] not in seen:
                matches.insert(0, item)
                seen.add(item["symbol"])
        elif sym.startswith(q) or any(w.startswith(q) for w in name.split()):
            if item["symbol"] not in seen:
                matches.append(item)
                seen.add(item["symbol"])
        elif q in name or q in sector:
            if item["symbol"] not in seen:
                matches.append(item)
                seen.add(item["symbol"])

    # 3. Query Yahoo Finance Search API for real Indian equities across NSE & BSE
    if len(matches) < limit:
        # Build search variations (e.g. "muthoothfinance" -> "muthooth finance")
        query_candidates = [q_clean]
        m = re.match(r'^([a-zA-Z]+)(finance|bank|motors|steel|power|tech|ind|ltd)$', q_clean, re.I)
        if m:
            query_candidates.append(f"{m.group(1)} {m.group(2)}")
            query_candidates.append(m.group(1))

        for candidate_q in query_candidates:
            if len(matches) >= limit:
                break
            try:
                url = f"https://query2.finance.yahoo.com/v1/finance/search?q={urllib.parse.quote(candidate_q)}&quotesCount=15&newsCount=0"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req, timeout=3.5) as resp:
                    data = json.loads(resp.read().decode())
                    for quote in data.get("quotes", []):
                        raw_sym = quote.get("symbol", "")
                        exch = quote.get("exchange", "")
                        # Filter strictly for Indian stock market exchanges
                        if raw_sym.endswith(".NS") or raw_sym.endswith(".BO") or exch in ("NSI", "BSE", "NSE"):
                            is_bse = raw_sym.endswith(".BO") or exch == "BSE"
                            clean_sym = raw_sym if (raw_sym.endswith(".NS") or raw_sym.endswith(".BO")) else (f"{raw_sym}.BO" if is_bse else f"{raw_sym}.NS")
                            if clean_sym not in seen:
                                seen.add(clean_sym)
                                name = quote.get("shortname") or quote.get("longname") or clean_sym
                                sector = quote.get("sector") or quote.get("industry") or "Indian Equity"
                                matches.append({
                                    "symbol": clean_sym,
                                    "name": name,
                                    "sector": sector,
                                    "exchange": "BSE" if is_bse else "NSE",
                                    "bse_code": clean_sym.replace(".NS", ".BO") if not is_bse else clean_sym,
                                    "index": "NSE/BSE Listed"
                                })
            except Exception as e:
                logger.debug(f"Live Yahoo search error for '{candidate_q}': {e}")

    results = matches[:limit]
    search_cache[cache_key] = results
    return results

def get_screener_stocks(category: str = "nifty50") -> List[Dict[str, str]]:
    """
    Returns a list of stocks belonging to a requested index or category.
    """
    cat = category.lower()
    if cat == "nifty50":
        return [s for s in STOCKS_DATABASE if s.get("index") == "Nifty 50"]
    elif cat in ("niftynext50", "next50"):
        return [s for s in STOCKS_DATABASE if s.get("index") == "Nifty Next 50"]
    elif cat in ("midcap", "niftymidcap"):
        return [s for s in STOCKS_DATABASE if s.get("index") == "Nifty Midcap"]
    elif cat == "tech":
        return [s for s in STOCKS_DATABASE if "Information Technology" in s.get("sector", "") or "Tech" in s.get("sector", "")]
    elif cat == "banking":
        return [s for s in STOCKS_DATABASE if "Banking" in s.get("sector", "") or "Financial" in s.get("sector", "")]
    elif cat == "auto":
        return [s for s in STOCKS_DATABASE if "Automobile" in s.get("sector", "")]
    # Default to all curated stocks
    return STOCKS_DATABASE
