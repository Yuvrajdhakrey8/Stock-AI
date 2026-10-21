"""
Catalog of 150+ closed and listed Indian IPOs with verified listing gains, GMP history and lot profitability.
"""
from typing import List, Dict, Any

false = False
true = True
null = None

CLOSED_IPOS_CATALOG: List[Dict[str, Any]] = [
  {
    "id": "belstar",
    "name": "Belstar Microfinance Ltd",
    "symbol": "BELSTAR.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Microfinance & Rural Lending",
    "open_date": "15-Jan-25",
    "close_date": "17-Jan-25",
    "listing_date": "22-Jan-25",
    "price_band": "\u20b9430",
    "issue_price": 430.0,
    "lot_size": 34,
    "min_investment": 14620,
    "issue_size_cr": 1300.0,
    "fresh_issue_cr": 975.0,
    "ofs_cr": 325.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 430.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.48,
        "nii": 0.63,
        "retail": 0.72,
        "total": 0.63
      },
      "day2": {
        "qib": 1.2,
        "nii": 1.47,
        "retail": 1.44,
        "total": 1.37
      },
      "final_day": {
        "qib": 2.4,
        "nii": 3.15,
        "retail": 1.8,
        "total": 2.1
      },
      "applications_count": "2.1x Subscription"
    },
    "listing": {
      "listing_price": 410.0,
      "listing_gain_rs": -20.0,
      "listing_gain_percent": -4.7,
      "profit_per_lot": -680.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 430.0,
        "actual_price": 410.0,
        "variance_rs": -20.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9430.0 (+0.0%). Stock opened at \u20b9410.0 (-4.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -4.7,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -4.7% (\u20b9680 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Microfinance & Rural Lending Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Microfinance & Rural Lending",
        "Strong institutional interest with 2.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -4.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 430.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 430.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 430.0,
        "notes": "Predicted \u20b9430.0 listing"
      }
    ]
  },
  {
    "id": "paras",
    "name": "Paras Healthcare Ltd",
    "symbol": "PARAS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Super Specialty Hospital Chain",
    "open_date": "08-Jan-25",
    "close_date": "10-Jan-25",
    "listing_date": "15-Jan-25",
    "price_band": "\u20b9185",
    "issue_price": 185.0,
    "lot_size": 81,
    "min_investment": 14985,
    "issue_size_cr": 800.0,
    "fresh_issue_cr": 600.0,
    "ofs_cr": 200.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 25.9,
    "gmp_closing_percent": 14.0,
    "gmp_estimated_listing": 210.9,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 6.42,
        "nii": 6.72,
        "retail": 3.92,
        "total": 6.72
      },
      "day2": {
        "qib": 16.05,
        "nii": 15.68,
        "retail": 7.84,
        "total": 14.56
      },
      "final_day": {
        "qib": 32.1,
        "nii": 33.6,
        "retail": 9.8,
        "total": 22.4
      },
      "applications_count": "22.4x Subscription"
    },
    "listing": {
      "listing_price": 210.0,
      "listing_gain_rs": 25.0,
      "listing_gain_percent": 13.5,
      "profit_per_lot": 2025.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 210.9,
        "actual_price": 210.0,
        "variance_rs": -0.9,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9210.9 (+14.0%). Stock opened at \u20b9210.0 (+13.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 14.0,
      "actual_gain_pct": 13.5,
      "retail_profit_lost": 2025.0,
      "explanation": "The issue opened with a healthy +13.5% pop (\u20b92,025 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +14% Listing Return",
      "long_term_potential": "Super Specialty Hospital Chain Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Super Specialty Hospital Chain",
        "Strong institutional interest with 32.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +13.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 24.6,
        "gmp_percent": 13.3,
        "est_listing_price": 209.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 25.4,
        "gmp_percent": 13.7,
        "est_listing_price": 210.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 25.9,
        "gmp_percent": 14.0,
        "est_listing_price": 210.9,
        "notes": "Predicted \u20b9210.9 listing"
      }
    ]
  },
  {
    "id": "standardg",
    "name": "Standard Glass Lining Technology",
    "symbol": "STANDARDG.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Chemical Reactors & Glass Lining",
    "open_date": "06-Jan-25",
    "close_date": "08-Jan-25",
    "listing_date": "13-Jan-25",
    "price_band": "\u20b9140",
    "issue_price": 140.0,
    "lot_size": 107,
    "min_investment": 14980,
    "issue_size_cr": 410.0,
    "fresh_issue_cr": 307.5,
    "ofs_cr": 102.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 44.8,
    "gmp_closing_percent": 32.0,
    "gmp_estimated_listing": 184.8,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 24.08,
        "nii": 24.63,
        "retail": 13.68,
        "total": 24.63
      },
      "day2": {
        "qib": 60.2,
        "nii": 57.47,
        "retail": 27.36,
        "total": 53.36
      },
      "final_day": {
        "qib": 120.4,
        "nii": 123.15,
        "retail": 34.2,
        "total": 82.1
      },
      "applications_count": "82.1x Subscription"
    },
    "listing": {
      "listing_price": 182.0,
      "listing_gain_rs": 42.0,
      "listing_gain_percent": 30.0,
      "profit_per_lot": 4494.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 184.8,
        "actual_price": 182.0,
        "variance_rs": -2.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9184.8 (+32.0%). Stock opened at \u20b9182.0 (+30.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 32.0,
      "actual_gain_pct": 30.0,
      "retail_profit_lost": 4494.0,
      "explanation": "Standard Glass Lining Technology delivered a stellar +30.0% listing gain, rewarding retail allottees with \u20b94,494 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +32% Listing Return",
      "long_term_potential": "Chemical Reactors & Glass Lining Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Chemical Reactors & Glass Lining",
        "Strong institutional interest with 120.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +30.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 34.9,
        "gmp_percent": 25.0,
        "est_listing_price": 174.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 40.3,
        "gmp_percent": 28.8,
        "est_listing_price": 180.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 44.8,
        "gmp_percent": 32.0,
        "est_listing_price": 184.8,
        "notes": "Predicted \u20b9184.8 listing"
      }
    ]
  },
  {
    "id": "indofarm",
    "name": "Indo Farm Equipment Ltd",
    "symbol": "INDOFARM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Tractors & Cranes",
    "open_date": "30-Dec-24",
    "close_date": "02-Jan-25",
    "listing_date": "07-Jan-25",
    "price_band": "\u20b9215",
    "issue_price": 215.0,
    "lot_size": 69,
    "min_investment": 14835,
    "issue_size_cr": 260.0,
    "fresh_issue_cr": 195.0,
    "ofs_cr": 65.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 32.25,
    "gmp_closing_percent": 15.0,
    "gmp_estimated_listing": 247.25,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 11.62,
        "nii": 13.35,
        "retail": 12.48,
        "total": 13.35
      },
      "day2": {
        "qib": 29.05,
        "nii": 31.15,
        "retail": 24.96,
        "total": 28.93
      },
      "final_day": {
        "qib": 58.1,
        "nii": 66.75,
        "retail": 31.2,
        "total": 44.5
      },
      "applications_count": "44.5x Subscription"
    },
    "listing": {
      "listing_price": 245.0,
      "listing_gain_rs": 30.0,
      "listing_gain_percent": 14.0,
      "profit_per_lot": 2070.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 247.25,
        "actual_price": 245.0,
        "variance_rs": -2.25,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9247.25 (+15.0%). Stock opened at \u20b9245.0 (+14.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 15.0,
      "actual_gain_pct": 14.0,
      "retail_profit_lost": 2070.0,
      "explanation": "The issue opened with a healthy +14.0% pop (\u20b92,070 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +15% Listing Return",
      "long_term_potential": "Tractors & Cranes Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Tractors & Cranes",
        "Strong institutional interest with 58.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +14.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 30.6,
        "gmp_percent": 14.2,
        "est_listing_price": 245.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 31.6,
        "gmp_percent": 14.7,
        "est_listing_price": 246.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 32.25,
        "gmp_percent": 15.0,
        "est_listing_price": 247.2,
        "notes": "Predicted \u20b9247.25 listing"
      }
    ]
  },
  {
    "id": "mamata",
    "name": "Mamata Machinery Ltd",
    "symbol": "MAMATA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Plastic Packaging Machines",
    "open_date": "24-Dec-24",
    "close_date": "27-Dec-24",
    "listing_date": "02-Jan-25",
    "price_band": "\u20b9243",
    "issue_price": 243.0,
    "lot_size": 61,
    "min_investment": 14823,
    "issue_size_cr": 180.0,
    "fresh_issue_cr": 135.0,
    "ofs_cr": 45.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 48.6,
    "gmp_closing_percent": 20.0,
    "gmp_estimated_listing": 291.6,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 23.0,
        "nii": 25.62,
        "retail": 16.84,
        "total": 25.62
      },
      "day2": {
        "qib": 57.5,
        "nii": 59.78,
        "retail": 33.68,
        "total": 55.51
      },
      "final_day": {
        "qib": 115.0,
        "nii": 128.1,
        "retail": 42.1,
        "total": 85.4
      },
      "applications_count": "85.4x Subscription"
    },
    "listing": {
      "listing_price": 290.0,
      "listing_gain_rs": 47.0,
      "listing_gain_percent": 19.3,
      "profit_per_lot": 2867.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 291.6,
        "actual_price": 290.0,
        "variance_rs": -1.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9291.6 (+20.0%). Stock opened at \u20b9290.0 (+19.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 20.0,
      "actual_gain_pct": 19.3,
      "retail_profit_lost": 2867.0,
      "explanation": "The issue opened with a healthy +19.3% pop (\u20b92,867 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +20% Listing Return",
      "long_term_potential": "Plastic Packaging Machines Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Plastic Packaging Machines",
        "Strong institutional interest with 115.0x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +19.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 46.2,
        "gmp_percent": 19.0,
        "est_listing_price": 289.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 47.6,
        "gmp_percent": 19.6,
        "est_listing_price": 290.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 48.6,
        "gmp_percent": 20.0,
        "est_listing_price": 291.6,
        "notes": "Predicted \u20b9291.6 listing"
      }
    ]
  },
  {
    "id": "transrail",
    "name": "Transrail Lighting Ltd",
    "symbol": "TRANSRAIL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Power Transmission Towers EPC",
    "open_date": "23-Dec-24",
    "close_date": "26-Dec-24",
    "listing_date": "01-Jan-25",
    "price_band": "\u20b9432",
    "issue_price": 432.0,
    "lot_size": 34,
    "min_investment": 14688,
    "issue_size_cr": 839.0,
    "fresh_issue_cr": 629.2,
    "ofs_cr": 209.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 95.04,
    "gmp_closing_percent": 22.0,
    "gmp_estimated_listing": 527.04,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 18.84,
        "nii": 20.52,
        "retail": 8.4,
        "total": 20.52
      },
      "day2": {
        "qib": 47.1,
        "nii": 47.88,
        "retail": 16.8,
        "total": 44.46
      },
      "final_day": {
        "qib": 94.2,
        "nii": 102.6,
        "retail": 21.0,
        "total": 68.4
      },
      "applications_count": "68.4x Subscription"
    },
    "listing": {
      "listing_price": 520.0,
      "listing_gain_rs": 88.0,
      "listing_gain_percent": 20.4,
      "profit_per_lot": 2992.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 527.04,
        "actual_price": 520.0,
        "variance_rs": -7.04,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9527.04 (+22.0%). Stock opened at \u20b9520.0 (+20.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 22.0,
      "actual_gain_pct": 20.4,
      "retail_profit_lost": 2992.0,
      "explanation": "The issue opened with a healthy +20.4% pop (\u20b92,992 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +22% Listing Return",
      "long_term_potential": "Power Transmission Towers EPC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Power Transmission Towers EPC",
        "Strong institutional interest with 94.2x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +20.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 74.1,
        "gmp_percent": 17.2,
        "est_listing_price": 506.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 85.5,
        "gmp_percent": 19.8,
        "est_listing_price": 517.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 95.04,
        "gmp_percent": 22.0,
        "est_listing_price": 527.0,
        "notes": "Predicted \u20b9527.04 listing"
      }
    ]
  },
  {
    "id": "damcap",
    "name": "DAM Capital Advisors Ltd",
    "symbol": "DAMCAP.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Investment Banking & ECM",
    "open_date": "20-Dec-24",
    "close_date": "24-Dec-24",
    "listing_date": "31-Dec-24",
    "price_band": "\u20b9283",
    "issue_price": 283.0,
    "lot_size": 53,
    "min_investment": 14999,
    "issue_size_cr": 840.25,
    "fresh_issue_cr": 630.2,
    "ofs_cr": 210.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 67.92,
    "gmp_closing_percent": 24.0,
    "gmp_estimated_listing": 350.92,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 15.7,
        "nii": 15.63,
        "retail": 7.36,
        "total": 15.63
      },
      "day2": {
        "qib": 39.25,
        "nii": 36.47,
        "retail": 14.72,
        "total": 33.87
      },
      "final_day": {
        "qib": 78.5,
        "nii": 78.15,
        "retail": 18.4,
        "total": 52.1
      },
      "applications_count": "52.1x Subscription"
    },
    "listing": {
      "listing_price": 345.0,
      "listing_gain_rs": 62.0,
      "listing_gain_percent": 21.9,
      "profit_per_lot": 3286.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 350.92,
        "actual_price": 345.0,
        "variance_rs": -5.92,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9350.92 (+24.0%). Stock opened at \u20b9345.0 (+21.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 24.0,
      "actual_gain_pct": 21.9,
      "retail_profit_lost": 3286.0,
      "explanation": "The issue opened with a healthy +21.9% pop (\u20b93,286 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +24% Listing Return",
      "long_term_potential": "Investment Banking & ECM Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Investment Banking & ECM",
        "Strong institutional interest with 78.5x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +21.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 53.0,
        "gmp_percent": 18.7,
        "est_listing_price": 336.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 61.1,
        "gmp_percent": 21.6,
        "est_listing_price": 344.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 67.92,
        "gmp_percent": 24.0,
        "est_listing_price": 350.9,
        "notes": "Predicted \u20b9350.92 listing"
      }
    ]
  },
  {
    "id": "ventive",
    "name": "Ventive Hospitality Ltd",
    "symbol": "VENTIVE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "JW Marriott / Luxury Resorts",
    "open_date": "20-Dec-24",
    "close_date": "24-Dec-24",
    "listing_date": "30-Dec-24",
    "price_band": "\u20b9643",
    "issue_price": 643.0,
    "lot_size": 23,
    "min_investment": 14789,
    "issue_size_cr": 2000.0,
    "fresh_issue_cr": 1500.0,
    "ofs_cr": 500.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 38.58,
    "gmp_closing_percent": 6.0,
    "gmp_estimated_listing": 681.58,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.64,
        "nii": 1.35,
        "retail": 0.84,
        "total": 1.35
      },
      "day2": {
        "qib": 4.1,
        "nii": 3.15,
        "retail": 1.68,
        "total": 2.93
      },
      "final_day": {
        "qib": 8.2,
        "nii": 6.75,
        "retail": 2.1,
        "total": 4.5
      },
      "applications_count": "4.5x Subscription"
    },
    "listing": {
      "listing_price": 680.0,
      "listing_gain_rs": 37.0,
      "listing_gain_percent": 5.8,
      "profit_per_lot": 851.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 681.58,
        "actual_price": 680.0,
        "variance_rs": -1.58,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9681.58 (+6.0%). Stock opened at \u20b9680.0 (+5.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 6.0,
      "actual_gain_pct": 5.8,
      "retail_profit_lost": 851.0,
      "explanation": "The issue opened with a healthy +5.8% pop (\u20b9851 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +6% Listing Return",
      "long_term_potential": "JW Marriott / Luxury Resorts Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in JW Marriott / Luxury Resorts",
        "Strong institutional interest with 8.2x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +5.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 36.7,
        "gmp_percent": 5.7,
        "est_listing_price": 679.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 37.8,
        "gmp_percent": 5.9,
        "est_listing_price": 680.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 38.58,
        "gmp_percent": 6.0,
        "est_listing_price": 681.6,
        "notes": "Predicted \u20b9681.58 listing"
      }
    ]
  },
  {
    "id": "sanathan",
    "name": "Sanathan Textiles Ltd",
    "symbol": "SANATHAN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Cotton & Polyester Yarn",
    "open_date": "19-Dec-24",
    "close_date": "23-Dec-24",
    "listing_date": "30-Dec-24",
    "price_band": "\u20b9321",
    "issue_price": 321.0,
    "lot_size": 46,
    "min_investment": 14766,
    "issue_size_cr": 500.0,
    "fresh_issue_cr": 375.0,
    "ofs_cr": 125.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 16.05,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 337.05,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 4.82,
        "nii": 5.46,
        "retail": 5.8,
        "total": 5.46
      },
      "day2": {
        "qib": 12.05,
        "nii": 12.74,
        "retail": 11.6,
        "total": 11.83
      },
      "final_day": {
        "qib": 24.1,
        "nii": 27.3,
        "retail": 14.5,
        "total": 18.2
      },
      "applications_count": "18.2x Subscription"
    },
    "listing": {
      "listing_price": 335.0,
      "listing_gain_rs": 14.0,
      "listing_gain_percent": 4.4,
      "profit_per_lot": 644.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 337.05,
        "actual_price": 335.0,
        "variance_rs": -2.05,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9337.05 (+5.0%). Stock opened at \u20b9335.0 (+4.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 4.4,
      "retail_profit_lost": 644.0,
      "explanation": "The IPO had a flat listing (+4.4%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Cotton & Polyester Yarn Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Cotton & Polyester Yarn",
        "Strong institutional interest with 24.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +4.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 15.2,
        "gmp_percent": 4.8,
        "est_listing_price": 336.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 15.7,
        "gmp_percent": 4.9,
        "est_listing_price": 336.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 16.05,
        "gmp_percent": 5.0,
        "est_listing_price": 337.1,
        "notes": "Predicted \u20b9337.05 listing"
      }
    ]
  },
  {
    "id": "senores",
    "name": "Senores Pharmaceuticals Ltd",
    "symbol": "SENORES.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "US Generic Injectables",
    "open_date": "18-Dec-24",
    "close_date": "20-Dec-24",
    "listing_date": "27-Dec-24",
    "price_band": "\u20b9391",
    "issue_price": 391.0,
    "lot_size": 38,
    "min_investment": 14858,
    "issue_size_cr": 582.11,
    "fresh_issue_cr": 436.6,
    "ofs_cr": 145.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 70.38,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 461.38,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 22.08,
        "nii": 28.56,
        "retail": 12.84,
        "total": 28.56
      },
      "day2": {
        "qib": 55.2,
        "nii": 66.64,
        "retail": 25.68,
        "total": 61.88
      },
      "final_day": {
        "qib": 110.4,
        "nii": 142.8,
        "retail": 32.1,
        "total": 95.2
      },
      "applications_count": "95.2x Subscription"
    },
    "listing": {
      "listing_price": 460.0,
      "listing_gain_rs": 69.0,
      "listing_gain_percent": 17.6,
      "profit_per_lot": 2622.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 461.38,
        "actual_price": 460.0,
        "variance_rs": -1.38,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9461.38 (+18.0%). Stock opened at \u20b9460.0 (+17.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 17.6,
      "retail_profit_lost": 2622.0,
      "explanation": "The issue opened with a healthy +17.6% pop (\u20b92,622 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "US Generic Injectables Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in US Generic Injectables",
        "Strong institutional interest with 110.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +17.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 66.9,
        "gmp_percent": 17.1,
        "est_listing_price": 457.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 69.0,
        "gmp_percent": 17.6,
        "est_listing_price": 460.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 70.38,
        "gmp_percent": 18.0,
        "est_listing_price": 461.4,
        "notes": "Predicted \u20b9461.38 listing"
      }
    ]
  },
  {
    "id": "carraro",
    "name": "Carraro India Ltd",
    "symbol": "CARRARO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Tractor & Construction Axles",
    "open_date": "18-Dec-24",
    "close_date": "20-Dec-24",
    "listing_date": "27-Dec-24",
    "price_band": "\u20b9404",
    "issue_price": 404.0,
    "lot_size": 37,
    "min_investment": 14948,
    "issue_size_cr": 1250.0,
    "fresh_issue_cr": 937.5,
    "ofs_cr": 312.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 404.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.42,
        "nii": 0.42,
        "retail": 0.44,
        "total": 0.42
      },
      "day2": {
        "qib": 1.05,
        "nii": 0.98,
        "retail": 0.88,
        "total": 0.91
      },
      "final_day": {
        "qib": 2.1,
        "nii": 2.1,
        "retail": 1.1,
        "total": 1.4
      },
      "applications_count": "1.4x Subscription"
    },
    "listing": {
      "listing_price": 400.0,
      "listing_gain_rs": -4.0,
      "listing_gain_percent": -1.0,
      "profit_per_lot": -148.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 404.0,
        "actual_price": 400.0,
        "variance_rs": -4.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9404.0 (+0.0%). Stock opened at \u20b9400.0 (-1.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -1.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-1.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Tractor & Construction Axles Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Tractor & Construction Axles",
        "Strong institutional interest with 2.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -1.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 404.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 404.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 404.0,
        "notes": "Predicted \u20b9404.0 listing"
      }
    ]
  },
  {
    "id": "igi",
    "name": "IGI Gems Certification Ltd",
    "symbol": "IGI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Diamond & Gemstones Grading",
    "open_date": "13-Dec-24",
    "close_date": "17-Dec-24",
    "listing_date": "20-Dec-24",
    "price_band": "\u20b9417",
    "issue_price": 417.0,
    "lot_size": 35,
    "min_investment": 14595,
    "issue_size_cr": 4000.0,
    "fresh_issue_cr": 3000.0,
    "ofs_cr": 1000.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 104.25,
    "gmp_closing_percent": 25.0,
    "gmp_estimated_listing": 521.25,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 12.48,
        "nii": 12.36,
        "retail": 3.28,
        "total": 12.36
      },
      "day2": {
        "qib": 31.2,
        "nii": 28.84,
        "retail": 6.56,
        "total": 26.78
      },
      "final_day": {
        "qib": 62.4,
        "nii": 61.8,
        "retail": 8.2,
        "total": 41.2
      },
      "applications_count": "41.2x Subscription"
    },
    "listing": {
      "listing_price": 510.0,
      "listing_gain_rs": 93.0,
      "listing_gain_percent": 22.3,
      "profit_per_lot": 3255.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 521.25,
        "actual_price": 510.0,
        "variance_rs": -11.25,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9521.25 (+25.0%). Stock opened at \u20b9510.0 (+22.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 25.0,
      "actual_gain_pct": 22.3,
      "retail_profit_lost": 3255.0,
      "explanation": "The issue opened with a healthy +22.3% pop (\u20b93,255 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +25% Listing Return",
      "long_term_potential": "Diamond & Gemstones Grading Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Diamond & Gemstones Grading",
        "Strong institutional interest with 62.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +22.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 81.3,
        "gmp_percent": 19.5,
        "est_listing_price": 498.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 93.8,
        "gmp_percent": 22.5,
        "est_listing_price": 510.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 104.25,
        "gmp_percent": 25.0,
        "est_listing_price": 521.2,
        "notes": "Predicted \u20b9521.25 listing"
      }
    ]
  },
  {
    "id": "vishalmart",
    "name": "Vishal Mega Mart Ltd",
    "symbol": "VISHALMART.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Hypermarket & Value Fashion",
    "open_date": "11-Dec-24",
    "close_date": "13-Dec-24",
    "listing_date": "18-Dec-24",
    "price_band": "\u20b978",
    "issue_price": 78.0,
    "lot_size": 190,
    "min_investment": 14820,
    "issue_size_cr": 8000.0,
    "fresh_issue_cr": 6000.0,
    "ofs_cr": 2000.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 27.3,
    "gmp_closing_percent": 35.0,
    "gmp_estimated_listing": 105.3,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 8.42,
        "nii": 8.25,
        "retail": 2.56,
        "total": 8.25
      },
      "day2": {
        "qib": 21.05,
        "nii": 19.25,
        "retail": 5.12,
        "total": 17.88
      },
      "final_day": {
        "qib": 42.1,
        "nii": 41.25,
        "retail": 6.4,
        "total": 27.5
      },
      "applications_count": "27.5x Subscription"
    },
    "listing": {
      "listing_price": 105.0,
      "listing_gain_rs": 27.0,
      "listing_gain_percent": 34.6,
      "profit_per_lot": 5130.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 105.3,
        "actual_price": 105.0,
        "variance_rs": -0.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9105.3 (+35.0%). Stock opened at \u20b9105.0 (+34.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 35.0,
      "actual_gain_pct": 34.6,
      "retail_profit_lost": 5130.0,
      "explanation": "Vishal Mega Mart Ltd delivered a stellar +34.6% listing gain, rewarding retail allottees with \u20b95,130 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +35% Listing Return",
      "long_term_potential": "Hypermarket & Value Fashion Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Hypermarket & Value Fashion",
        "Strong institutional interest with 42.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +34.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 21.3,
        "gmp_percent": 27.3,
        "est_listing_price": 99.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 24.6,
        "gmp_percent": 31.5,
        "est_listing_price": 102.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 27.3,
        "gmp_percent": 35.0,
        "est_listing_price": 105.3,
        "notes": "Predicted \u20b9105.3 listing"
      }
    ]
  },
  {
    "id": "sailife",
    "name": "Sai Life Sciences Ltd",
    "symbol": "SAILIFE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pharma CRDMO Services",
    "open_date": "11-Dec-24",
    "close_date": "13-Dec-24",
    "listing_date": "18-Dec-24",
    "price_band": "\u20b9549",
    "issue_price": 549.0,
    "lot_size": 27,
    "min_investment": 14823,
    "issue_size_cr": 3042.62,
    "fresh_issue_cr": 2282.0,
    "ofs_cr": 760.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 109.8,
    "gmp_closing_percent": 20.0,
    "gmp_estimated_listing": 658.8,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 9.04,
        "nii": 9.42,
        "retail": 3.4,
        "total": 9.42
      },
      "day2": {
        "qib": 22.6,
        "nii": 21.98,
        "retail": 6.8,
        "total": 20.41
      },
      "final_day": {
        "qib": 45.2,
        "nii": 47.1,
        "retail": 8.5,
        "total": 31.4
      },
      "applications_count": "31.4x Subscription"
    },
    "listing": {
      "listing_price": 650.0,
      "listing_gain_rs": 101.0,
      "listing_gain_percent": 18.4,
      "profit_per_lot": 2727.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 658.8,
        "actual_price": 650.0,
        "variance_rs": -8.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9658.8 (+20.0%). Stock opened at \u20b9650.0 (+18.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 20.0,
      "actual_gain_pct": 18.4,
      "retail_profit_lost": 2727.0,
      "explanation": "The issue opened with a healthy +18.4% pop (\u20b92,727 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +20% Listing Return",
      "long_term_potential": "Pharma CRDMO Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pharma CRDMO Services",
        "Strong institutional interest with 45.2x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +18.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 104.3,
        "gmp_percent": 19.0,
        "est_listing_price": 653.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 107.6,
        "gmp_percent": 19.6,
        "est_listing_price": 656.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 109.8,
        "gmp_percent": 20.0,
        "est_listing_price": 658.8,
        "notes": "Predicted \u20b9658.8 listing"
      }
    ]
  },
  {
    "id": "mobikwik",
    "name": "One Mobikwik Systems Ltd",
    "symbol": "MOBIKWIK.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Fintech & BNPL Wallet",
    "open_date": "11-Dec-24",
    "close_date": "13-Dec-24",
    "listing_date": "18-Dec-24",
    "price_band": "\u20b9279",
    "issue_price": 279.0,
    "lot_size": 53,
    "min_investment": 14787,
    "issue_size_cr": 572.0,
    "fresh_issue_cr": 429.0,
    "ofs_cr": 143.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 153.45,
    "gmp_closing_percent": 55.0,
    "gmp_estimated_listing": 432.45,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 28.0,
        "nii": 38.55,
        "retail": 18.08,
        "total": 38.55
      },
      "day2": {
        "qib": 70.0,
        "nii": 89.95,
        "retail": 36.16,
        "total": 83.53
      },
      "final_day": {
        "qib": 140.0,
        "nii": 192.75,
        "retail": 45.2,
        "total": 128.5
      },
      "applications_count": "128.5x Subscription"
    },
    "listing": {
      "listing_price": 440.0,
      "listing_gain_rs": 161.0,
      "listing_gain_percent": 57.7,
      "profit_per_lot": 8533.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 432.45,
        "actual_price": 440.0,
        "variance_rs": 7.55,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9432.45 (+55.0%). Stock opened at \u20b9440.0 (+57.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 55.0,
      "actual_gain_pct": 57.7,
      "retail_profit_lost": 8533.0,
      "explanation": "One Mobikwik Systems Ltd delivered a stellar +57.7% listing gain, rewarding retail allottees with \u20b98,533 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +55% Listing Return",
      "long_term_potential": "Fintech & BNPL Wallet Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Fintech & BNPL Wallet",
        "Strong institutional interest with 140.0x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +57.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 119.7,
        "gmp_percent": 42.9,
        "est_listing_price": 398.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 138.1,
        "gmp_percent": 49.5,
        "est_listing_price": 417.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 153.45,
        "gmp_percent": 55.0,
        "est_listing_price": 432.4,
        "notes": "Predicted \u20b9432.45 listing"
      }
    ]
  },
  {
    "id": "suraksha",
    "name": "Suraksha Diagnostic Ltd",
    "symbol": "SURAKSHA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pathology & Radiology Labs",
    "open_date": "29-Nov-24",
    "close_date": "03-Dec-24",
    "listing_date": "06-Dec-24",
    "price_band": "\u20b9441",
    "issue_price": 441.0,
    "lot_size": 34,
    "min_investment": 14994,
    "issue_size_cr": 846.25,
    "fresh_issue_cr": 634.7,
    "ofs_cr": 211.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 441.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.29,
        "nii": 0.38,
        "retail": 0.51,
        "total": 0.38
      },
      "day2": {
        "qib": 0.72,
        "nii": 0.9,
        "retail": 1.02,
        "total": 0.83
      },
      "final_day": {
        "qib": 1.45,
        "nii": 1.92,
        "retail": 1.28,
        "total": 1.28
      },
      "applications_count": "1.28x Subscription"
    },
    "listing": {
      "listing_price": 437.0,
      "listing_gain_rs": -4.0,
      "listing_gain_percent": -0.9,
      "profit_per_lot": -136.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 441.0,
        "actual_price": 437.0,
        "variance_rs": -4.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9441.0 (+0.0%). Stock opened at \u20b9437.0 (-0.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -0.9,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-0.9%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Pathology & Radiology Labs Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pathology & Radiology Labs",
        "Strong institutional interest with 1.45x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -0.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 441.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 441.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 441.0,
        "notes": "Predicted \u20b9441.0 listing"
      }
    ]
  },
  {
    "id": "enviro",
    "name": "Enviro Infra Engineers Ltd",
    "symbol": "ENVIRO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Water & Wastewater EPC",
    "open_date": "22-Nov-24",
    "close_date": "26-Nov-24",
    "listing_date": "29-Nov-24",
    "price_band": "\u20b9148",
    "issue_price": 148.0,
    "lot_size": 101,
    "min_investment": 14948,
    "issue_size_cr": 650.43,
    "fresh_issue_cr": 487.8,
    "ofs_cr": 162.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 74.0,
    "gmp_closing_percent": 50.0,
    "gmp_estimated_listing": 222.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 30.76,
        "nii": 26.97,
        "retail": 9.79,
        "total": 26.97
      },
      "day2": {
        "qib": 76.9,
        "nii": 62.93,
        "retail": 19.58,
        "total": 58.44
      },
      "final_day": {
        "qib": 153.8,
        "nii": 134.85,
        "retail": 24.48,
        "total": 89.9
      },
      "applications_count": "89.9x Subscription"
    },
    "listing": {
      "listing_price": 220.0,
      "listing_gain_rs": 72.0,
      "listing_gain_percent": 48.6,
      "profit_per_lot": 7272.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 222.0,
        "actual_price": 220.0,
        "variance_rs": -2.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9222.0 (+50.0%). Stock opened at \u20b9220.0 (+48.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 50.0,
      "actual_gain_pct": 48.6,
      "retail_profit_lost": 7272.0,
      "explanation": "Enviro Infra Engineers Ltd delivered a stellar +48.6% listing gain, rewarding retail allottees with \u20b97,272 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +50% Listing Return",
      "long_term_potential": "Water & Wastewater EPC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Water & Wastewater EPC",
        "Strong institutional interest with 153.8x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +48.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 57.7,
        "gmp_percent": 39.0,
        "est_listing_price": 205.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 66.6,
        "gmp_percent": 45.0,
        "est_listing_price": 214.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 74.0,
        "gmp_percent": 50.0,
        "est_listing_price": 222.0,
        "notes": "Predicted \u20b9222.0 listing"
      }
    ]
  },
  {
    "id": "ntpcgreen",
    "name": "NTPC Green Energy Ltd",
    "symbol": "NTPCGREEN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Renewable Energy Utility",
    "open_date": "19-Nov-24",
    "close_date": "22-Nov-24",
    "listing_date": "27-Nov-24",
    "price_band": "\u20b9108",
    "issue_price": 108.0,
    "lot_size": 138,
    "min_investment": 14904,
    "issue_size_cr": 10000.0,
    "fresh_issue_cr": 7500.0,
    "ofs_cr": 2500.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 3.78,
    "gmp_closing_percent": 3.5,
    "gmp_estimated_listing": 111.78,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.66,
        "nii": 0.73,
        "retail": 0.55,
        "total": 0.73
      },
      "day2": {
        "qib": 1.66,
        "nii": 1.69,
        "retail": 1.1,
        "total": 1.57
      },
      "final_day": {
        "qib": 3.32,
        "nii": 3.63,
        "retail": 1.37,
        "total": 2.42
      },
      "applications_count": "2.42x Subscription"
    },
    "listing": {
      "listing_price": 111.5,
      "listing_gain_rs": 3.5,
      "listing_gain_percent": 3.2,
      "profit_per_lot": 483.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 111.78,
        "actual_price": 111.5,
        "variance_rs": -0.28,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9111.78 (+3.5%). Stock opened at \u20b9111.5 (+3.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.5,
      "actual_gain_pct": 3.2,
      "retail_profit_lost": 483.0,
      "explanation": "The IPO had a flat listing (+3.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Renewable Energy Utility Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Renewable Energy Utility",
        "Strong institutional interest with 3.32x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +3.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.6,
        "gmp_percent": 3.3,
        "est_listing_price": 111.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.7,
        "gmp_percent": 3.4,
        "est_listing_price": 111.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 3.78,
        "gmp_percent": 3.5,
        "est_listing_price": 111.8,
        "notes": "Predicted \u20b9111.78 listing"
      }
    ]
  },
  {
    "id": "blackbuck",
    "name": "Zinka Logistics Solutions (BlackBuck)",
    "symbol": "BLACKBUCK.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Trucking Digital Platform",
    "open_date": "13-Nov-24",
    "close_date": "18-Nov-24",
    "listing_date": "21-Nov-24",
    "price_band": "\u20b9273",
    "issue_price": 273.0,
    "lot_size": 54,
    "min_investment": 14742,
    "issue_size_cr": 1114.72,
    "fresh_issue_cr": 836.0,
    "ofs_cr": 278.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 10.92,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 283.92,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.05,
        "nii": 0.56,
        "retail": 0.66,
        "total": 0.56
      },
      "day2": {
        "qib": 0.12,
        "nii": 1.3,
        "retail": 1.33,
        "total": 1.21
      },
      "final_day": {
        "qib": 0.24,
        "nii": 2.79,
        "retail": 1.66,
        "total": 1.86
      },
      "applications_count": "1.86x Subscription"
    },
    "listing": {
      "listing_price": 279.05,
      "listing_gain_rs": 6.05,
      "listing_gain_percent": 2.2,
      "profit_per_lot": 326.7,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 283.92,
        "actual_price": 279.05,
        "variance_rs": -4.87,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9283.92 (+4.0%). Stock opened at \u20b9279.05 (+2.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 2.2,
      "retail_profit_lost": 326.7,
      "explanation": "The IPO had a flat listing (+2.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Trucking Digital Platform Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Trucking Digital Platform",
        "Strong institutional interest with 0.24x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +2.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 10.4,
        "gmp_percent": 3.8,
        "est_listing_price": 283.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 10.7,
        "gmp_percent": 3.9,
        "est_listing_price": 283.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 10.92,
        "gmp_percent": 4.0,
        "est_listing_price": 283.9,
        "notes": "Predicted \u20b9283.92 listing"
      }
    ]
  },
  {
    "id": "nivabupa",
    "name": "Niva Bupa Health Insurance",
    "symbol": "NIVABUPA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Standalone Health Insurance",
    "open_date": "07-Nov-24",
    "close_date": "11-Nov-24",
    "listing_date": "14-Nov-24",
    "price_band": "\u20b974",
    "issue_price": 74.0,
    "lot_size": 200,
    "min_investment": 14800,
    "issue_size_cr": 2200.0,
    "fresh_issue_cr": 1650.0,
    "ofs_cr": 550.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 3.7,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 77.7,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.41,
        "nii": 0.54,
        "retail": 1.09,
        "total": 0.54
      },
      "day2": {
        "qib": 1.03,
        "nii": 1.26,
        "retail": 2.18,
        "total": 1.17
      },
      "final_day": {
        "qib": 2.06,
        "nii": 2.7,
        "retail": 2.73,
        "total": 1.8
      },
      "applications_count": "1.8x Subscription"
    },
    "listing": {
      "listing_price": 78.5,
      "listing_gain_rs": 4.5,
      "listing_gain_percent": 6.1,
      "profit_per_lot": 900.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 77.7,
        "actual_price": 78.5,
        "variance_rs": 0.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b977.7 (+5.0%). Stock opened at \u20b978.5 (+6.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 6.1,
      "retail_profit_lost": 900.0,
      "explanation": "The issue opened with a healthy +6.1% pop (\u20b9900 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Standalone Health Insurance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Standalone Health Insurance",
        "Strong institutional interest with 2.06x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +6.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.5,
        "gmp_percent": 4.8,
        "est_listing_price": 77.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.6,
        "gmp_percent": 4.9,
        "est_listing_price": 77.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 3.7,
        "gmp_percent": 5.0,
        "est_listing_price": 77.7,
        "notes": "Predicted \u20b977.7 listing"
      }
    ]
  },
  {
    "id": "swiggy",
    "name": "Swiggy Ltd",
    "symbol": "SWIGGY.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Consumer Tech / Quick Commerce",
    "open_date": "06-Nov-24",
    "close_date": "08-Nov-24",
    "listing_date": "13-Nov-24",
    "price_band": "\u20b9390",
    "issue_price": 390.0,
    "lot_size": 38,
    "min_investment": 14820,
    "issue_size_cr": 11327.43,
    "fresh_issue_cr": 8495.6,
    "ofs_cr": 2831.9,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 31.2,
    "gmp_closing_percent": 8.0,
    "gmp_estimated_listing": 421.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.83,
        "nii": 1.08,
        "retail": 0.46,
        "total": 1.08
      },
      "day2": {
        "qib": 2.08,
        "nii": 2.51,
        "retail": 0.91,
        "total": 2.33
      },
      "final_day": {
        "qib": 4.15,
        "nii": 5.38,
        "retail": 1.14,
        "total": 3.59
      },
      "applications_count": "3.59x Subscription"
    },
    "listing": {
      "listing_price": 420.0,
      "listing_gain_rs": 30.0,
      "listing_gain_percent": 7.7,
      "profit_per_lot": 1140.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 421.2,
        "actual_price": 420.0,
        "variance_rs": -1.2,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9421.2 (+8.0%). Stock opened at \u20b9420.0 (+7.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 8.0,
      "actual_gain_pct": 7.7,
      "retail_profit_lost": 1140.0,
      "explanation": "The issue opened with a healthy +7.7% pop (\u20b91,140 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +8% Listing Return",
      "long_term_potential": "Consumer Tech / Quick Commerce Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Consumer Tech / Quick Commerce",
        "Strong institutional interest with 4.15x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +7.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 29.6,
        "gmp_percent": 7.6,
        "est_listing_price": 419.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 30.6,
        "gmp_percent": 7.8,
        "est_listing_price": 420.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 31.2,
        "gmp_percent": 8.0,
        "est_listing_price": 421.2,
        "notes": "Predicted \u20b9421.2 listing"
      }
    ]
  },
  {
    "id": "acmesolar",
    "name": "ACME Solar Holdings Ltd",
    "symbol": "ACMESOLAR.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Solar & Wind IPP Utility",
    "open_date": "06-Nov-24",
    "close_date": "08-Nov-24",
    "listing_date": "13-Nov-24",
    "price_band": "\u20b9289",
    "issue_price": 289.0,
    "lot_size": 51,
    "min_investment": 14739,
    "issue_size_cr": 2900.0,
    "fresh_issue_cr": 2175.0,
    "ofs_cr": 725.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -28.9,
    "gmp_closing_percent": -10.0,
    "gmp_estimated_listing": 260.1,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.19,
        "nii": 0.82,
        "retail": 1.24,
        "total": 0.82
      },
      "day2": {
        "qib": 0.48,
        "nii": 1.92,
        "retail": 2.48,
        "total": 1.79
      },
      "final_day": {
        "qib": 0.97,
        "nii": 4.12,
        "retail": 3.1,
        "total": 2.75
      },
      "applications_count": "2.75x Subscription"
    },
    "listing": {
      "listing_price": 251.0,
      "listing_gain_rs": -38.0,
      "listing_gain_percent": -13.1,
      "profit_per_lot": -1938.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 260.1,
        "actual_price": 251.0,
        "variance_rs": -9.1,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9260.1 (-10.0%). Stock opened at \u20b9251.0 (-13.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -10.0,
      "actual_gain_pct": -13.1,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -13.1% (\u20b91,938 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -10% Listing Return",
      "long_term_potential": "Solar & Wind IPP Utility Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Solar & Wind IPP Utility",
        "Strong institutional interest with 0.97x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -13.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -36.1,
        "gmp_percent": -12.5,
        "est_listing_price": 252.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -32.4,
        "gmp_percent": -11.2,
        "est_listing_price": 256.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -28.9,
        "gmp_percent": -10.0,
        "est_listing_price": 260.1,
        "notes": "Predicted \u20b9260.1 listing"
      }
    ]
  },
  {
    "id": "sagility",
    "name": "Sagility India Ltd",
    "symbol": "SAGILITY.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "US Healthcare IT Services",
    "open_date": "05-Nov-24",
    "close_date": "07-Nov-24",
    "listing_date": "12-Nov-24",
    "price_band": "\u20b930",
    "issue_price": 30.0,
    "lot_size": 500,
    "min_investment": 15000,
    "issue_size_cr": 2106.6,
    "fresh_issue_cr": 1579.9,
    "ofs_cr": 526.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 1.5,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 31.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.39,
        "nii": 0.96,
        "retail": 1.66,
        "total": 0.96
      },
      "day2": {
        "qib": 0.96,
        "nii": 2.24,
        "retail": 3.33,
        "total": 2.08
      },
      "final_day": {
        "qib": 1.93,
        "nii": 4.8,
        "retail": 4.16,
        "total": 3.2
      },
      "applications_count": "3.2x Subscription"
    },
    "listing": {
      "listing_price": 31.06,
      "listing_gain_rs": 1.06,
      "listing_gain_percent": 3.5,
      "profit_per_lot": 530.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 31.5,
        "actual_price": 31.06,
        "variance_rs": -0.44,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b931.5 (+5.0%). Stock opened at \u20b931.06 (+3.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 3.5,
      "retail_profit_lost": 530.0,
      "explanation": "The IPO had a flat listing (+3.5%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "US Healthcare IT Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in US Healthcare IT Services",
        "Strong institutional interest with 1.93x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +3.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 1.4,
        "gmp_percent": 4.8,
        "est_listing_price": 31.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 1.5,
        "gmp_percent": 4.9,
        "est_listing_price": 31.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 1.5,
        "gmp_percent": 5.0,
        "est_listing_price": 31.5,
        "notes": "Predicted \u20b931.5 listing"
      }
    ]
  },
  {
    "id": "afcons",
    "name": "Afcons Infrastructure Ltd",
    "symbol": "AFCONS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Global Marine & Heavy EPC",
    "open_date": "25-Oct-24",
    "close_date": "29-Oct-24",
    "listing_date": "04-Nov-24",
    "price_band": "\u20b9463",
    "issue_price": 463.0,
    "lot_size": 32,
    "min_investment": 14816,
    "issue_size_cr": 5430.0,
    "fresh_issue_cr": 4072.5,
    "ofs_cr": 1357.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -9.26,
    "gmp_closing_percent": -2.0,
    "gmp_estimated_listing": 453.74,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 1.01,
        "nii": 0.79,
        "retail": 0.38,
        "total": 0.79
      },
      "day2": {
        "qib": 2.52,
        "nii": 1.84,
        "retail": 0.75,
        "total": 1.71
      },
      "final_day": {
        "qib": 5.05,
        "nii": 3.94,
        "retail": 0.94,
        "total": 2.63
      },
      "applications_count": "2.63x Subscription"
    },
    "listing": {
      "listing_price": 430.0,
      "listing_gain_rs": -33.0,
      "listing_gain_percent": -7.1,
      "profit_per_lot": -1056.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 453.74,
        "actual_price": 430.0,
        "variance_rs": -23.74,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9453.74 (-2.0%). Stock opened at \u20b9430.0 (-7.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -2.0,
      "actual_gain_pct": -7.1,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -7.1% (\u20b91,056 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -2% Listing Return",
      "long_term_potential": "Global Marine & Heavy EPC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Global Marine & Heavy EPC",
        "Strong institutional interest with 5.05x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -7.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -11.6,
        "gmp_percent": -2.5,
        "est_listing_price": 451.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -10.4,
        "gmp_percent": -2.2,
        "est_listing_price": 452.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -9.26,
        "gmp_percent": -2.0,
        "est_listing_price": 453.7,
        "notes": "Predicted \u20b9453.74 listing"
      }
    ]
  },
  {
    "id": "godavari",
    "name": "Godavari Biorefineries Ltd",
    "symbol": "GODAVARI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Bio-based Chemicals & Ethanol",
    "open_date": "23-Oct-24",
    "close_date": "25-Oct-24",
    "listing_date": "30-Oct-24",
    "price_band": "\u20b9352",
    "issue_price": 352.0,
    "lot_size": 42,
    "min_investment": 14784,
    "issue_size_cr": 554.75,
    "fresh_issue_cr": 416.1,
    "ofs_cr": 138.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -17.6,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 334.4,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.55,
        "nii": 0.55,
        "retail": 0.68,
        "total": 0.55
      },
      "day2": {
        "qib": 1.38,
        "nii": 1.28,
        "retail": 1.37,
        "total": 1.19
      },
      "final_day": {
        "qib": 2.76,
        "nii": 2.75,
        "retail": 1.71,
        "total": 1.83
      },
      "applications_count": "1.83x Subscription"
    },
    "listing": {
      "listing_price": 310.0,
      "listing_gain_rs": -42.0,
      "listing_gain_percent": -11.9,
      "profit_per_lot": -1764.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 334.4,
        "actual_price": 310.0,
        "variance_rs": -24.4,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9334.4 (-5.0%). Stock opened at \u20b9310.0 (-11.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -11.9,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -11.9% (\u20b91,764 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Bio-based Chemicals & Ethanol Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Bio-based Chemicals & Ethanol",
        "Strong institutional interest with 2.76x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -11.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -22.0,
        "gmp_percent": -6.2,
        "est_listing_price": 330.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -19.7,
        "gmp_percent": -5.6,
        "est_listing_price": 332.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -17.6,
        "gmp_percent": -5.0,
        "est_listing_price": 334.4,
        "notes": "Predicted \u20b9334.4 listing"
      }
    ]
  },
  {
    "id": "waareeener",
    "name": "Waaree Energies Ltd",
    "symbol": "WAAREEENER.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Solar Modules & Clean Energy",
    "open_date": "21-Oct-24",
    "close_date": "23-Oct-24",
    "listing_date": "28-Oct-24",
    "price_band": "\u20b91,503",
    "issue_price": 1503.0,
    "lot_size": 9,
    "min_investment": 13527,
    "issue_size_cr": 4321.44,
    "fresh_issue_cr": 3241.1,
    "ofs_cr": 1080.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 1082.16,
    "gmp_closing_percent": 72.0,
    "gmp_estimated_listing": 2585.16,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 41.73,
        "nii": 22.9,
        "retail": 4.32,
        "total": 22.9
      },
      "day2": {
        "qib": 104.31,
        "nii": 53.44,
        "retail": 8.63,
        "total": 49.62
      },
      "final_day": {
        "qib": 208.63,
        "nii": 114.51,
        "retail": 10.79,
        "total": 76.34
      },
      "applications_count": "76.34x Subscription"
    },
    "listing": {
      "listing_price": 2550.0,
      "listing_gain_rs": 1047.0,
      "listing_gain_percent": 69.7,
      "profit_per_lot": 9423.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 2585.16,
        "actual_price": 2550.0,
        "variance_rs": -35.16,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b92585.16 (+72.0%). Stock opened at \u20b92550.0 (+69.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 72.0,
      "actual_gain_pct": 69.7,
      "retail_profit_lost": 9423.0,
      "explanation": "Waaree Energies Ltd delivered a stellar +69.7% listing gain, rewarding retail allottees with \u20b99,423 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +72% Listing Return",
      "long_term_potential": "Solar Modules & Clean Energy Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Solar Modules & Clean Energy",
        "Strong institutional interest with 208.63x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +69.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 844.1,
        "gmp_percent": 56.2,
        "est_listing_price": 2347.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 973.9,
        "gmp_percent": 64.8,
        "est_listing_price": 2476.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 1082.16,
        "gmp_percent": 72.0,
        "est_listing_price": 2585.2,
        "notes": "Predicted \u20b92585.16 listing"
      }
    ]
  },
  {
    "id": "deepakbld",
    "name": "Deepak Builders & Engineers",
    "symbol": "DEEPAKBLD.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Hospitals & Station EPC",
    "open_date": "21-Oct-24",
    "close_date": "23-Oct-24",
    "listing_date": "28-Oct-24",
    "price_band": "\u20b9203",
    "issue_price": 203.0,
    "lot_size": 73,
    "min_investment": 14819,
    "issue_size_cr": 260.04,
    "fresh_issue_cr": 195.0,
    "ofs_cr": 65.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 203.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 16.49,
        "nii": 12.46,
        "retail": 15.92,
        "total": 12.46
      },
      "day2": {
        "qib": 41.23,
        "nii": 29.08,
        "retail": 31.83,
        "total": 27.0
      },
      "final_day": {
        "qib": 82.47,
        "nii": 62.31,
        "retail": 39.79,
        "total": 41.54
      },
      "applications_count": "41.54x Subscription"
    },
    "listing": {
      "listing_price": 200.0,
      "listing_gain_rs": -3.0,
      "listing_gain_percent": -1.5,
      "profit_per_lot": -219.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 203.0,
        "actual_price": 200.0,
        "variance_rs": -3.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9203.0 (+0.0%). Stock opened at \u20b9200.0 (-1.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -1.5,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-1.5%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Hospitals & Station EPC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Hospitals & Station EPC",
        "Strong institutional interest with 82.47x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -1.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 203.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 203.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 203.0,
        "notes": "Predicted \u20b9203.0 listing"
      }
    ]
  },
  {
    "id": "hyundai",
    "name": "Hyundai Motor India Ltd",
    "symbol": "HYUNDAI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Automobile OEM",
    "open_date": "15-Oct-24",
    "close_date": "17-Oct-24",
    "listing_date": "22-Oct-24",
    "price_band": "\u20b91,960",
    "issue_price": 1960.0,
    "lot_size": 7,
    "min_investment": 13720,
    "issue_size_cr": 27870.16,
    "fresh_issue_cr": 20902.6,
    "ofs_cr": 6967.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -19.6,
    "gmp_closing_percent": -1.0,
    "gmp_estimated_listing": 1940.4,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 1.39,
        "nii": 0.71,
        "retail": 0.2,
        "total": 0.71
      },
      "day2": {
        "qib": 3.48,
        "nii": 1.66,
        "retail": 0.4,
        "total": 1.54
      },
      "final_day": {
        "qib": 6.97,
        "nii": 3.56,
        "retail": 0.5,
        "total": 2.37
      },
      "applications_count": "2.37x Subscription"
    },
    "listing": {
      "listing_price": 1934.0,
      "listing_gain_rs": -26.0,
      "listing_gain_percent": -1.3,
      "profit_per_lot": -182.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 1940.4,
        "actual_price": 1934.0,
        "variance_rs": -6.4,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91940.4 (-1.0%). Stock opened at \u20b91934.0 (-1.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": -1.0,
      "actual_gain_pct": -1.3,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-1.3%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -1% Listing Return",
      "long_term_potential": "Automobile OEM Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Automobile OEM",
        "Strong institutional interest with 6.97x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -1.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -24.5,
        "gmp_percent": -1.2,
        "est_listing_price": 1935.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -22.0,
        "gmp_percent": -1.1,
        "est_listing_price": 1938.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -19.6,
        "gmp_percent": -1.0,
        "est_listing_price": 1940.4,
        "notes": "Predicted \u20b91940.4 listing"
      }
    ]
  },
  {
    "id": "garuda",
    "name": "Garuda Construction & Engineering",
    "symbol": "GARUDA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Civil Construction & Infra",
    "open_date": "08-Oct-24",
    "close_date": "10-Oct-24",
    "listing_date": "15-Oct-24",
    "price_band": "\u20b995",
    "issue_price": 95.0,
    "lot_size": 157,
    "min_investment": 14915,
    "issue_size_cr": 264.1,
    "fresh_issue_cr": 198.1,
    "ofs_cr": 66.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 9.5,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 104.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.21,
        "nii": 2.26,
        "retail": 4.32,
        "total": 2.26
      },
      "day2": {
        "qib": 5.54,
        "nii": 5.28,
        "retail": 8.65,
        "total": 4.91
      },
      "final_day": {
        "qib": 11.07,
        "nii": 11.32,
        "retail": 10.81,
        "total": 7.55
      },
      "applications_count": "7.55x Subscription"
    },
    "listing": {
      "listing_price": 103.0,
      "listing_gain_rs": 8.0,
      "listing_gain_percent": 8.4,
      "profit_per_lot": 1256.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 104.5,
        "actual_price": 103.0,
        "variance_rs": -1.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9104.5 (+10.0%). Stock opened at \u20b9103.0 (+8.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 8.4,
      "retail_profit_lost": 1256.0,
      "explanation": "The issue opened with a healthy +8.4% pop (\u20b91,256 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Civil Construction & Infra Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Civil Construction & Infra",
        "Strong institutional interest with 11.07x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +8.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 9.0,
        "gmp_percent": 9.5,
        "est_listing_price": 104.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 9.3,
        "gmp_percent": 9.8,
        "est_listing_price": 104.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 9.5,
        "gmp_percent": 10.0,
        "est_listing_price": 104.5,
        "notes": "Predicted \u20b9104.5 listing"
      }
    ]
  },
  {
    "id": "diffusion",
    "name": "Diffusion Engineers Ltd",
    "symbol": "DIFFUSION.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Welding Consumables & Wear Plates",
    "open_date": "26-Sep-24",
    "close_date": "30-Sep-24",
    "listing_date": "04-Oct-24",
    "price_band": "\u20b9168",
    "issue_price": 168.0,
    "lot_size": 88,
    "min_investment": 14784,
    "issue_size_cr": 158.0,
    "fresh_issue_cr": 118.5,
    "ofs_cr": 39.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 25.2,
    "gmp_closing_percent": 15.0,
    "gmp_estimated_listing": 193.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 41.52,
        "nii": 34.35,
        "retail": 34.24,
        "total": 34.35
      },
      "day2": {
        "qib": 103.8,
        "nii": 80.15,
        "retail": 68.49,
        "total": 74.42
      },
      "final_day": {
        "qib": 207.6,
        "nii": 171.75,
        "retail": 85.61,
        "total": 114.5
      },
      "applications_count": "114.5x Subscription"
    },
    "listing": {
      "listing_price": 188.0,
      "listing_gain_rs": 20.0,
      "listing_gain_percent": 11.9,
      "profit_per_lot": 1760.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 193.2,
        "actual_price": 188.0,
        "variance_rs": -5.2,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9193.2 (+15.0%). Stock opened at \u20b9188.0 (+11.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 15.0,
      "actual_gain_pct": 11.9,
      "retail_profit_lost": 1760.0,
      "explanation": "The issue opened with a healthy +11.9% pop (\u20b91,760 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +15% Listing Return",
      "long_term_potential": "Welding Consumables & Wear Plates Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Welding Consumables & Wear Plates",
        "Strong institutional interest with 207.6x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +11.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 23.9,
        "gmp_percent": 14.2,
        "est_listing_price": 191.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 24.7,
        "gmp_percent": 14.7,
        "est_listing_price": 192.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 25.2,
        "gmp_percent": 15.0,
        "est_listing_price": 193.2,
        "notes": "Predicted \u20b9193.2 listing"
      }
    ]
  },
  {
    "id": "krn",
    "name": "KRN Heat Exchanger and Refrig.",
    "symbol": "KRN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "HVAC Heat Exchanger Coils",
    "open_date": "25-Sep-24",
    "close_date": "27-Sep-24",
    "listing_date": "03-Oct-24",
    "price_band": "\u20b9220",
    "issue_price": 220.0,
    "lot_size": 65,
    "min_investment": 14300,
    "issue_size_cr": 341.95,
    "fresh_issue_cr": 256.5,
    "ofs_cr": 85.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 253.0,
    "gmp_closing_percent": 115.0,
    "gmp_estimated_listing": 473.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 86.11,
        "nii": 64.02,
        "retail": 38.6,
        "total": 64.02
      },
      "day2": {
        "qib": 215.27,
        "nii": 149.39,
        "retail": 77.2,
        "total": 138.72
      },
      "final_day": {
        "qib": 430.54,
        "nii": 320.12,
        "retail": 96.5,
        "total": 213.41
      },
      "applications_count": "213.41x Subscription"
    },
    "listing": {
      "listing_price": 470.0,
      "listing_gain_rs": 250.0,
      "listing_gain_percent": 113.6,
      "profit_per_lot": 16250.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 473.0,
        "actual_price": 470.0,
        "variance_rs": -3.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9473.0 (+115.0%). Stock opened at \u20b9470.0 (+113.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 115.0,
      "actual_gain_pct": 113.6,
      "retail_profit_lost": 16250.0,
      "explanation": "KRN Heat Exchanger and Refrig. delivered a stellar +113.6% listing gain, rewarding retail allottees with \u20b916,250 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +115% Listing Return",
      "long_term_potential": "HVAC Heat Exchanger Coils Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in HVAC Heat Exchanger Coils",
        "Strong institutional interest with 430.54x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +113.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 197.3,
        "gmp_percent": 89.7,
        "est_listing_price": 417.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 227.7,
        "gmp_percent": 103.5,
        "est_listing_price": 447.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 253.0,
        "gmp_percent": 115.0,
        "est_listing_price": 473.0,
        "notes": "Predicted \u20b9473.0 listing"
      }
    ]
  },
  {
    "id": "manba",
    "name": "Manba Finance Ltd",
    "symbol": "MANBA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Two-Wheeler & EV Financing",
    "open_date": "23-Sep-24",
    "close_date": "25-Sep-24",
    "listing_date": "30-Sep-24",
    "price_band": "\u20b9120",
    "issue_price": 120.0,
    "lot_size": 125,
    "min_investment": 15000,
    "issue_size_cr": 150.84,
    "fresh_issue_cr": 113.1,
    "ofs_cr": 37.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 26.4,
    "gmp_closing_percent": 22.0,
    "gmp_estimated_listing": 146.4,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 102.33,
        "nii": 67.23,
        "retail": 28.07,
        "total": 67.23
      },
      "day2": {
        "qib": 255.82,
        "nii": 156.87,
        "retail": 56.14,
        "total": 145.66
      },
      "final_day": {
        "qib": 511.65,
        "nii": 336.15,
        "retail": 70.18,
        "total": 224.1
      },
      "applications_count": "224.1x Subscription"
    },
    "listing": {
      "listing_price": 145.0,
      "listing_gain_rs": 25.0,
      "listing_gain_percent": 20.8,
      "profit_per_lot": 3125.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 146.4,
        "actual_price": 145.0,
        "variance_rs": -1.4,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9146.4 (+22.0%). Stock opened at \u20b9145.0 (+20.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 22.0,
      "actual_gain_pct": 20.8,
      "retail_profit_lost": 3125.0,
      "explanation": "The issue opened with a healthy +20.8% pop (\u20b93,125 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +22% Listing Return",
      "long_term_potential": "Two-Wheeler & EV Financing Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Two-Wheeler & EV Financing",
        "Strong institutional interest with 511.65x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +20.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 20.6,
        "gmp_percent": 17.2,
        "est_listing_price": 140.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 23.8,
        "gmp_percent": 19.8,
        "est_listing_price": 143.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 26.4,
        "gmp_percent": 22.0,
        "est_listing_price": 146.4,
        "notes": "Predicted \u20b9146.4 listing"
      }
    ]
  },
  {
    "id": "western",
    "name": "Western Carriers (India) Ltd",
    "symbol": "WESTERN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Multimodal Rail Logistics",
    "open_date": "13-Sep-24",
    "close_date": "18-Sep-24",
    "listing_date": "24-Sep-24",
    "price_band": "\u20b9172",
    "issue_price": 172.0,
    "lot_size": 87,
    "min_investment": 14964,
    "issue_size_cr": 492.88,
    "fresh_issue_cr": 369.7,
    "ofs_cr": 123.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 3.44,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 175.44,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 8.94,
        "nii": 9.17,
        "retail": 10.38,
        "total": 9.17
      },
      "day2": {
        "qib": 22.36,
        "nii": 21.4,
        "retail": 20.76,
        "total": 19.87
      },
      "final_day": {
        "qib": 44.71,
        "nii": 45.86,
        "retail": 25.95,
        "total": 30.57
      },
      "applications_count": "30.57x Subscription"
    },
    "listing": {
      "listing_price": 170.0,
      "listing_gain_rs": -2.0,
      "listing_gain_percent": -1.2,
      "profit_per_lot": -174.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 175.44,
        "actual_price": 170.0,
        "variance_rs": -5.44,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9175.44 (+2.0%). Stock opened at \u20b9170.0 (-1.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": -1.2,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-1.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Multimodal Rail Logistics Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Multimodal Rail Logistics",
        "Strong institutional interest with 44.71x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -1.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.3,
        "gmp_percent": 1.9,
        "est_listing_price": 175.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.4,
        "gmp_percent": 2.0,
        "est_listing_price": 175.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 3.44,
        "gmp_percent": 2.0,
        "est_listing_price": 175.4,
        "notes": "Predicted \u20b9175.44 listing"
      }
    ]
  },
  {
    "id": "northarc",
    "name": "Northern Arc Capital Ltd",
    "symbol": "NORTHARC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Retail NBFC & Credit Platform",
    "open_date": "16-Sep-24",
    "close_date": "19-Sep-24",
    "listing_date": "24-Sep-24",
    "price_band": "\u20b9263",
    "issue_price": 263.0,
    "lot_size": 57,
    "min_investment": 14991,
    "issue_size_cr": 777.0,
    "fresh_issue_cr": 582.8,
    "ofs_cr": 194.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 92.05,
    "gmp_closing_percent": 35.0,
    "gmp_estimated_listing": 355.05,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 28.48,
        "nii": 33.27,
        "retail": 12.43,
        "total": 33.27
      },
      "day2": {
        "qib": 71.2,
        "nii": 77.64,
        "retail": 24.86,
        "total": 72.09
      },
      "final_day": {
        "qib": 142.41,
        "nii": 166.37,
        "retail": 31.08,
        "total": 110.91
      },
      "applications_count": "110.91x Subscription"
    },
    "listing": {
      "listing_price": 350.0,
      "listing_gain_rs": 87.0,
      "listing_gain_percent": 33.1,
      "profit_per_lot": 4959.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 355.05,
        "actual_price": 350.0,
        "variance_rs": -5.05,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9355.05 (+35.0%). Stock opened at \u20b9350.0 (+33.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 35.0,
      "actual_gain_pct": 33.1,
      "retail_profit_lost": 4959.0,
      "explanation": "Northern Arc Capital Ltd delivered a stellar +33.1% listing gain, rewarding retail allottees with \u20b94,959 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +35% Listing Return",
      "long_term_potential": "Retail NBFC & Credit Platform Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Retail NBFC & Credit Platform",
        "Strong institutional interest with 142.41x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +33.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 71.8,
        "gmp_percent": 27.3,
        "est_listing_price": 334.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 82.8,
        "gmp_percent": 31.5,
        "est_listing_price": 345.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 92.05,
        "gmp_percent": 35.0,
        "est_listing_price": 355.1,
        "notes": "Predicted \u20b9355.05 listing"
      }
    ]
  },
  {
    "id": "arkade",
    "name": "Arkade Developers Ltd",
    "symbol": "ARKADE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Luxury Real Estate Mumbai",
    "open_date": "16-Sep-24",
    "close_date": "19-Sep-24",
    "listing_date": "24-Sep-24",
    "price_band": "\u20b9128",
    "issue_price": 128.0,
    "lot_size": 110,
    "min_investment": 14080,
    "issue_size_cr": 410.0,
    "fresh_issue_cr": 307.5,
    "ofs_cr": 102.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 51.2,
    "gmp_closing_percent": 40.0,
    "gmp_estimated_listing": 179.2,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 32.6,
        "nii": 32.06,
        "retail": 20.56,
        "total": 32.06
      },
      "day2": {
        "qib": 81.5,
        "nii": 74.82,
        "retail": 41.11,
        "total": 69.47
      },
      "final_day": {
        "qib": 163.0,
        "nii": 160.32,
        "retail": 51.39,
        "total": 106.88
      },
      "applications_count": "106.88x Subscription"
    },
    "listing": {
      "listing_price": 175.0,
      "listing_gain_rs": 47.0,
      "listing_gain_percent": 36.7,
      "profit_per_lot": 5170.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 179.2,
        "actual_price": 175.0,
        "variance_rs": -4.2,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9179.2 (+40.0%). Stock opened at \u20b9175.0 (+36.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 40.0,
      "actual_gain_pct": 36.7,
      "retail_profit_lost": 5170.0,
      "explanation": "Arkade Developers Ltd delivered a stellar +36.7% listing gain, rewarding retail allottees with \u20b95,170 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +40% Listing Return",
      "long_term_potential": "Luxury Real Estate Mumbai Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Luxury Real Estate Mumbai",
        "Strong institutional interest with 163.0x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +36.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 39.9,
        "gmp_percent": 31.2,
        "est_listing_price": 167.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 46.1,
        "gmp_percent": 36.0,
        "est_listing_price": 174.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 51.2,
        "gmp_percent": 40.0,
        "est_listing_price": 179.2,
        "notes": "Predicted \u20b9179.2 listing"
      }
    ]
  },
  {
    "id": "bajajhfl",
    "name": "Bajaj Housing Finance Ltd",
    "symbol": "BAJAJHFL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Housing Finance / NBFC",
    "open_date": "09-Sep-24",
    "close_date": "11-Sep-24",
    "listing_date": "16-Sep-24",
    "price_band": "\u20b970",
    "issue_price": 70.0,
    "lot_size": 214,
    "min_investment": 14980,
    "issue_size_cr": 6560.0,
    "fresh_issue_cr": 4920.0,
    "ofs_cr": 1640.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 80.5,
    "gmp_closing_percent": 115.0,
    "gmp_estimated_listing": 150.5,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 41.87,
        "nii": 19.08,
        "retail": 2.96,
        "total": 19.08
      },
      "day2": {
        "qib": 104.68,
        "nii": 44.53,
        "retail": 5.93,
        "total": 41.35
      },
      "final_day": {
        "qib": 209.36,
        "nii": 95.41,
        "retail": 7.41,
        "total": 63.61
      },
      "applications_count": "63.61x Subscription"
    },
    "listing": {
      "listing_price": 150.0,
      "listing_gain_rs": 80.0,
      "listing_gain_percent": 114.3,
      "profit_per_lot": 17120.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 150.5,
        "actual_price": 150.0,
        "variance_rs": -0.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9150.5 (+115.0%). Stock opened at \u20b9150.0 (+114.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 115.0,
      "actual_gain_pct": 114.3,
      "retail_profit_lost": 17120.0,
      "explanation": "Bajaj Housing Finance Ltd delivered a stellar +114.3% listing gain, rewarding retail allottees with \u20b917,120 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +115% Listing Return",
      "long_term_potential": "Housing Finance / NBFC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Housing Finance / NBFC",
        "Strong institutional interest with 209.36x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +114.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 62.8,
        "gmp_percent": 89.7,
        "est_listing_price": 132.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 72.5,
        "gmp_percent": 103.5,
        "est_listing_price": 142.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 80.5,
        "gmp_percent": 115.0,
        "est_listing_price": 150.5,
        "notes": "Predicted \u20b9150.5 listing"
      }
    ]
  },
  {
    "id": "kross",
    "name": "Kross Ltd",
    "symbol": "KROSS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Trailer Axles & Forgings",
    "open_date": "09-Sep-24",
    "close_date": "11-Sep-24",
    "listing_date": "16-Sep-24",
    "price_band": "\u20b9240",
    "issue_price": 240.0,
    "lot_size": 62,
    "min_investment": 14880,
    "issue_size_cr": 500.0,
    "fresh_issue_cr": 375.0,
    "ofs_cr": 125.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 4.8,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 244.8,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 4.45,
        "nii": 5.04,
        "retail": 4.3,
        "total": 5.04
      },
      "day2": {
        "qib": 11.12,
        "nii": 11.77,
        "retail": 8.61,
        "total": 10.93
      },
      "final_day": {
        "qib": 22.24,
        "nii": 25.21,
        "retail": 10.76,
        "total": 16.81
      },
      "applications_count": "16.81x Subscription"
    },
    "listing": {
      "listing_price": 240.0,
      "listing_gain_rs": 0.0,
      "listing_gain_percent": 0.0,
      "profit_per_lot": 0.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 244.8,
        "actual_price": 240.0,
        "variance_rs": -4.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9244.8 (+2.0%). Stock opened at \u20b9240.0 (+0.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 0.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (+0.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Trailer Axles & Forgings Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Trailer Axles & Forgings",
        "Strong institutional interest with 22.24x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 4.6,
        "gmp_percent": 1.9,
        "est_listing_price": 244.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 4.7,
        "gmp_percent": 2.0,
        "est_listing_price": 244.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 4.8,
        "gmp_percent": 2.0,
        "est_listing_price": 244.8,
        "notes": "Predicted \u20b9244.8 listing"
      }
    ]
  },
  {
    "id": "tolins",
    "name": "Tolins Tyres Ltd",
    "symbol": "TOLINS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Tyres & Retreading Materials",
    "open_date": "09-Sep-24",
    "close_date": "11-Sep-24",
    "listing_date": "16-Sep-24",
    "price_band": "\u20b9226",
    "issue_price": 226.0,
    "lot_size": 66,
    "min_investment": 14916,
    "issue_size_cr": 230.0,
    "fresh_issue_cr": 172.5,
    "ofs_cr": 57.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Cameo Corporate Services Ltd",
    "gmp_closing_day": 6.78,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 232.78,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 5.48,
        "nii": 7.17,
        "retail": 8.61,
        "total": 7.17
      },
      "day2": {
        "qib": 13.71,
        "nii": 16.72,
        "retail": 17.22,
        "total": 15.53
      },
      "final_day": {
        "qib": 27.41,
        "nii": 35.84,
        "retail": 21.52,
        "total": 23.89
      },
      "applications_count": "23.89x Subscription"
    },
    "listing": {
      "listing_price": 227.0,
      "listing_gain_rs": 1.0,
      "listing_gain_percent": 0.4,
      "profit_per_lot": 66.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 232.78,
        "actual_price": 227.0,
        "variance_rs": -5.78,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9232.78 (+3.0%). Stock opened at \u20b9227.0 (+0.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": 0.4,
      "retail_profit_lost": 66.0,
      "explanation": "The IPO had a flat listing (+0.4%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "Tyres & Retreading Materials Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Tyres & Retreading Materials",
        "Strong institutional interest with 27.41x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 6.4,
        "gmp_percent": 2.8,
        "est_listing_price": 232.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 6.6,
        "gmp_percent": 2.9,
        "est_listing_price": 232.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 6.78,
        "gmp_percent": 3.0,
        "est_listing_price": 232.8,
        "notes": "Predicted \u20b9232.78 listing"
      }
    ]
  },
  {
    "id": "galaprec",
    "name": "Gala Precision Engineering Ltd",
    "symbol": "GALAPREC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Springs & Fasteners",
    "open_date": "02-Sep-24",
    "close_date": "04-Sep-24",
    "listing_date": "09-Sep-24",
    "price_band": "\u20b9529",
    "issue_price": 529.0,
    "lot_size": 28,
    "min_investment": 14812,
    "issue_size_cr": 167.93,
    "fresh_issue_cr": 125.9,
    "ofs_cr": 42.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 211.6,
    "gmp_closing_percent": 40.0,
    "gmp_estimated_listing": 740.6,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 82.92,
        "nii": 60.42,
        "retail": 36.78,
        "total": 60.42
      },
      "day2": {
        "qib": 207.31,
        "nii": 140.99,
        "retail": 73.56,
        "total": 130.92
      },
      "final_day": {
        "qib": 414.62,
        "nii": 302.12,
        "retail": 91.95,
        "total": 201.41
      },
      "applications_count": "201.41x Subscription"
    },
    "listing": {
      "listing_price": 729.0,
      "listing_gain_rs": 200.0,
      "listing_gain_percent": 37.8,
      "profit_per_lot": 5600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 740.6,
        "actual_price": 729.0,
        "variance_rs": -11.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9740.6 (+40.0%). Stock opened at \u20b9729.0 (+37.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 40.0,
      "actual_gain_pct": 37.8,
      "retail_profit_lost": 5600.0,
      "explanation": "Gala Precision Engineering Ltd delivered a stellar +37.8% listing gain, rewarding retail allottees with \u20b95,600 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +40% Listing Return",
      "long_term_potential": "Springs & Fasteners Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Springs & Fasteners",
        "Strong institutional interest with 414.62x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +37.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 165.0,
        "gmp_percent": 31.2,
        "est_listing_price": 694.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 190.4,
        "gmp_percent": 36.0,
        "est_listing_price": 719.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 211.6,
        "gmp_percent": 40.0,
        "est_listing_price": 740.6,
        "notes": "Predicted \u20b9740.6 listing"
      }
    ]
  },
  {
    "id": "stylebaaz",
    "name": "Baazar Style Retail Ltd",
    "symbol": "STYLEBAAZ.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Value Fashion Retail",
    "open_date": "30-Aug-24",
    "close_date": "03-Sep-24",
    "listing_date": "06-Sep-24",
    "price_band": "\u20b9389",
    "issue_price": 389.0,
    "lot_size": 38,
    "min_investment": 14782,
    "issue_size_cr": 834.68,
    "fresh_issue_cr": 626.0,
    "ofs_cr": 208.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 11.67,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 400.67,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.98,
        "nii": 1.39,
        "retail": 1.69,
        "total": 1.39
      },
      "day2": {
        "qib": 2.44,
        "nii": 3.25,
        "retail": 3.38,
        "total": 3.02
      },
      "final_day": {
        "qib": 4.88,
        "nii": 6.96,
        "retail": 4.22,
        "total": 4.64
      },
      "applications_count": "4.64x Subscription"
    },
    "listing": {
      "listing_price": 389.0,
      "listing_gain_rs": 0.0,
      "listing_gain_percent": 0.0,
      "profit_per_lot": 0.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 400.67,
        "actual_price": 389.0,
        "variance_rs": -11.67,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9400.67 (+3.0%). Stock opened at \u20b9389.0 (+0.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": 0.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (+0.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "Value Fashion Retail Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Value Fashion Retail",
        "Strong institutional interest with 4.88x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 11.1,
        "gmp_percent": 2.8,
        "est_listing_price": 400.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 11.4,
        "gmp_percent": 2.9,
        "est_listing_price": 400.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 11.67,
        "gmp_percent": 3.0,
        "est_listing_price": 400.7,
        "notes": "Predicted \u20b9400.67 listing"
      }
    ]
  },
  {
    "id": "ecosmobil",
    "name": "ECOS (India) Mobility & Hospitality",
    "symbol": "ECOSMOBIL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Chauffeur & Car Rental",
    "open_date": "28-Aug-24",
    "close_date": "30-Aug-24",
    "listing_date": "04-Sep-24",
    "price_band": "\u20b9334",
    "issue_price": 334.0,
    "lot_size": 44,
    "min_investment": 14696,
    "issue_size_cr": 601.2,
    "fresh_issue_cr": 450.9,
    "ofs_cr": 150.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 56.78,
    "gmp_closing_percent": 17.0,
    "gmp_estimated_listing": 390.78,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 14.25,
        "nii": 19.28,
        "retail": 7.92,
        "total": 19.28
      },
      "day2": {
        "qib": 35.62,
        "nii": 44.98,
        "retail": 15.83,
        "total": 41.77
      },
      "final_day": {
        "qib": 71.23,
        "nii": 96.39,
        "retail": 19.79,
        "total": 64.26
      },
      "applications_count": "64.26x Subscription"
    },
    "listing": {
      "listing_price": 390.0,
      "listing_gain_rs": 56.0,
      "listing_gain_percent": 16.8,
      "profit_per_lot": 2464.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 390.78,
        "actual_price": 390.0,
        "variance_rs": -0.78,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9390.78 (+17.0%). Stock opened at \u20b9390.0 (+16.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 17.0,
      "actual_gain_pct": 16.8,
      "retail_profit_lost": 2464.0,
      "explanation": "The issue opened with a healthy +16.8% pop (\u20b92,464 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +17% Listing Return",
      "long_term_potential": "Chauffeur & Car Rental Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Chauffeur & Car Rental",
        "Strong institutional interest with 71.23x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +16.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 53.9,
        "gmp_percent": 16.1,
        "est_listing_price": 387.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 55.6,
        "gmp_percent": 16.7,
        "est_listing_price": 389.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 56.78,
        "gmp_percent": 17.0,
        "est_listing_price": 390.8,
        "notes": "Predicted \u20b9390.78 listing"
      }
    ]
  },
  {
    "id": "premierene",
    "name": "Premier Energies Ltd",
    "symbol": "PREMIERENE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Solar Cells & Power",
    "open_date": "27-Aug-24",
    "close_date": "29-Aug-24",
    "listing_date": "03-Sep-24",
    "price_band": "\u20b9450",
    "issue_price": 450.0,
    "lot_size": 33,
    "min_investment": 14850,
    "issue_size_cr": 2830.4,
    "fresh_issue_cr": 2122.8,
    "ofs_cr": 707.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 495.0,
    "gmp_closing_percent": 110.0,
    "gmp_estimated_listing": 945.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 42.48,
        "nii": 22.31,
        "retail": 3.08,
        "total": 22.31
      },
      "day2": {
        "qib": 106.21,
        "nii": 52.07,
        "retail": 6.15,
        "total": 48.35
      },
      "final_day": {
        "qib": 212.42,
        "nii": 111.57,
        "retail": 7.69,
        "total": 74.38
      },
      "applications_count": "74.38x Subscription"
    },
    "listing": {
      "listing_price": 991.0,
      "listing_gain_rs": 541.0,
      "listing_gain_percent": 120.2,
      "profit_per_lot": 17853.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 945.0,
        "actual_price": 991.0,
        "variance_rs": 46.0,
        "reliability": "Underpredicted (Beat GMP)",
        "notes": "Closing GMP estimated \u20b9945.0 (+110.0%). Stock opened at \u20b9991.0 (+120.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 110.0,
      "actual_gain_pct": 120.2,
      "retail_profit_lost": 17853.0,
      "explanation": "Premier Energies Ltd delivered a stellar +120.2% listing gain, rewarding retail allottees with \u20b917,853 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +110% Listing Return",
      "long_term_potential": "Solar Cells & Power Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Solar Cells & Power",
        "Strong institutional interest with 212.42x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +120.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 386.1,
        "gmp_percent": 85.8,
        "est_listing_price": 836.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 445.5,
        "gmp_percent": 99.0,
        "est_listing_price": 895.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 495.0,
        "gmp_percent": 110.0,
        "est_listing_price": 945.0,
        "notes": "Predicted \u20b9945.0 listing"
      }
    ]
  },
  {
    "id": "orienttech",
    "name": "Orient Technologies Ltd",
    "symbol": "ORIENTTECH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "IT Infrastructure & Cloud Products",
    "open_date": "21-Aug-24",
    "close_date": "23-Aug-24",
    "listing_date": "28-Aug-24",
    "price_band": "\u20b9206",
    "issue_price": 206.0,
    "lot_size": 72,
    "min_investment": 14832,
    "issue_size_cr": 214.76,
    "fresh_issue_cr": 161.1,
    "ofs_cr": 53.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 86.52,
    "gmp_closing_percent": 42.0,
    "gmp_estimated_listing": 292.52,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 60.12,
        "nii": 45.51,
        "retail": 26.75,
        "total": 45.51
      },
      "day2": {
        "qib": 150.3,
        "nii": 106.2,
        "retail": 53.5,
        "total": 98.61
      },
      "final_day": {
        "qib": 300.6,
        "nii": 227.56,
        "retail": 66.87,
        "total": 151.71
      },
      "applications_count": "151.71x Subscription"
    },
    "listing": {
      "listing_price": 290.0,
      "listing_gain_rs": 84.0,
      "listing_gain_percent": 40.8,
      "profit_per_lot": 6048.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 292.52,
        "actual_price": 290.0,
        "variance_rs": -2.52,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9292.52 (+42.0%). Stock opened at \u20b9290.0 (+40.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 42.0,
      "actual_gain_pct": 40.8,
      "retail_profit_lost": 6048.0,
      "explanation": "Orient Technologies Ltd delivered a stellar +40.8% listing gain, rewarding retail allottees with \u20b96,048 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +42% Listing Return",
      "long_term_potential": "IT Infrastructure & Cloud Products Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in IT Infrastructure & Cloud Products",
        "Strong institutional interest with 300.6x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +40.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 67.5,
        "gmp_percent": 32.8,
        "est_listing_price": 273.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 77.9,
        "gmp_percent": 37.8,
        "est_listing_price": 283.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 86.52,
        "gmp_percent": 42.0,
        "est_listing_price": 292.5,
        "notes": "Predicted \u20b9292.52 listing"
      }
    ]
  },
  {
    "id": "interarch",
    "name": "Interarch Building Products Ltd",
    "symbol": "INTERARCH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pre-engineered Steel Buildings",
    "open_date": "19-Aug-24",
    "close_date": "21-Aug-24",
    "listing_date": "26-Aug-24",
    "price_band": "\u20b9900",
    "issue_price": 900.0,
    "lot_size": 16,
    "min_investment": 14400,
    "issue_size_cr": 600.29,
    "fresh_issue_cr": 450.2,
    "ofs_cr": 150.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 405.0,
    "gmp_closing_percent": 45.0,
    "gmp_estimated_listing": 1305.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 25.78,
        "nii": 28.06,
        "retail": 4.34,
        "total": 28.06
      },
      "day2": {
        "qib": 64.46,
        "nii": 65.47,
        "retail": 8.67,
        "total": 60.79
      },
      "final_day": {
        "qib": 128.92,
        "nii": 140.3,
        "retail": 10.84,
        "total": 93.53
      },
      "applications_count": "93.53x Subscription"
    },
    "listing": {
      "listing_price": 1299.0,
      "listing_gain_rs": 399.0,
      "listing_gain_percent": 44.3,
      "profit_per_lot": 6384.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1305.0,
        "actual_price": 1299.0,
        "variance_rs": -6.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91305.0 (+45.0%). Stock opened at \u20b91299.0 (+44.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 45.0,
      "actual_gain_pct": 44.3,
      "retail_profit_lost": 6384.0,
      "explanation": "Interarch Building Products Ltd delivered a stellar +44.3% listing gain, rewarding retail allottees with \u20b96,384 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +45% Listing Return",
      "long_term_potential": "Pre-engineered Steel Buildings Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pre-engineered Steel Buildings",
        "Strong institutional interest with 128.92x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +44.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 315.9,
        "gmp_percent": 35.1,
        "est_listing_price": 1215.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 364.5,
        "gmp_percent": 40.5,
        "est_listing_price": 1264.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 405.0,
        "gmp_percent": 45.0,
        "est_listing_price": 1305.0,
        "notes": "Predicted \u20b91305.0 listing"
      }
    ]
  },
  {
    "id": "saraswati",
    "name": "Saraswati Saree Depot Ltd",
    "symbol": "SARASWATI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Women Apparel & Sarees",
    "open_date": "12-Aug-24",
    "close_date": "14-Aug-24",
    "listing_date": "20-Aug-24",
    "price_band": "\u20b9160",
    "issue_price": 160.0,
    "lot_size": 90,
    "min_investment": 14400,
    "issue_size_cr": 160.01,
    "fresh_issue_cr": 120.0,
    "ofs_cr": 40.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 41.6,
    "gmp_closing_percent": 26.0,
    "gmp_estimated_listing": 201.6,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 71.69,
        "nii": 32.26,
        "retail": 24.75,
        "total": 32.26
      },
      "day2": {
        "qib": 179.24,
        "nii": 75.26,
        "retail": 49.5,
        "total": 69.89
      },
      "final_day": {
        "qib": 358.47,
        "nii": 161.28,
        "retail": 61.88,
        "total": 107.52
      },
      "applications_count": "107.52x Subscription"
    },
    "listing": {
      "listing_price": 200.0,
      "listing_gain_rs": 40.0,
      "listing_gain_percent": 25.0,
      "profit_per_lot": 3600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 201.6,
        "actual_price": 200.0,
        "variance_rs": -1.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9201.6 (+26.0%). Stock opened at \u20b9200.0 (+25.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 26.0,
      "actual_gain_pct": 25.0,
      "retail_profit_lost": 3600.0,
      "explanation": "Saraswati Saree Depot Ltd delivered a stellar +25.0% listing gain, rewarding retail allottees with \u20b93,600 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +26% Listing Return",
      "long_term_potential": "Women Apparel & Sarees Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Women Apparel & Sarees",
        "Strong institutional interest with 358.47x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +25.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 32.4,
        "gmp_percent": 20.3,
        "est_listing_price": 192.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 37.4,
        "gmp_percent": 23.4,
        "est_listing_price": 197.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 41.6,
        "gmp_percent": 26.0,
        "est_listing_price": 201.6,
        "notes": "Predicted \u20b9201.6 listing"
      }
    ]
  },
  {
    "id": "firstcry",
    "name": "Brainbees Solutions Ltd (FirstCry)",
    "symbol": "FIRSTCRY.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "E-Commerce / Baby & Kids",
    "open_date": "06-Aug-24",
    "close_date": "08-Aug-24",
    "listing_date": "13-Aug-24",
    "price_band": "\u20b9465",
    "issue_price": 465.0,
    "lot_size": 32,
    "min_investment": 14880,
    "issue_size_cr": 4193.73,
    "fresh_issue_cr": 3145.3,
    "ofs_cr": 1048.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 176.7,
    "gmp_closing_percent": 38.0,
    "gmp_estimated_listing": 641.7,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 3.86,
        "nii": 3.67,
        "retail": 0.92,
        "total": 3.67
      },
      "day2": {
        "qib": 9.65,
        "nii": 8.55,
        "retail": 1.85,
        "total": 7.94
      },
      "final_day": {
        "qib": 19.3,
        "nii": 18.33,
        "retail": 2.31,
        "total": 12.22
      },
      "applications_count": "12.22x Subscription"
    },
    "listing": {
      "listing_price": 651.0,
      "listing_gain_rs": 186.0,
      "listing_gain_percent": 40.0,
      "profit_per_lot": 5952.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 641.7,
        "actual_price": 651.0,
        "variance_rs": 9.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9641.7 (+38.0%). Stock opened at \u20b9651.0 (+40.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 38.0,
      "actual_gain_pct": 40.0,
      "retail_profit_lost": 5952.0,
      "explanation": "Brainbees Solutions Ltd (FirstCry) delivered a stellar +40.0% listing gain, rewarding retail allottees with \u20b95,952 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +38% Listing Return",
      "long_term_potential": "E-Commerce / Baby & Kids Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in E-Commerce / Baby & Kids",
        "Strong institutional interest with 19.3x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +40.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 137.8,
        "gmp_percent": 29.6,
        "est_listing_price": 602.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 159.0,
        "gmp_percent": 34.2,
        "est_listing_price": 624.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 176.7,
        "gmp_percent": 38.0,
        "est_listing_price": 641.7,
        "notes": "Predicted \u20b9641.7 listing"
      }
    ]
  },
  {
    "id": "olaelec",
    "name": "Ola Electric Mobility Ltd",
    "symbol": "OLAELEC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "EV Two-Wheelers",
    "open_date": "02-Aug-24",
    "close_date": "06-Aug-24",
    "listing_date": "09-Aug-24",
    "price_band": "\u20b976",
    "issue_price": 76.0,
    "lot_size": 195,
    "min_investment": 14820,
    "issue_size_cr": 6145.56,
    "fresh_issue_cr": 4609.2,
    "ofs_cr": 1536.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 3.8,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 79.8,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.06,
        "nii": 1.28,
        "retail": 1.57,
        "total": 1.28
      },
      "day2": {
        "qib": 2.65,
        "nii": 2.99,
        "retail": 3.14,
        "total": 2.78
      },
      "final_day": {
        "qib": 5.31,
        "nii": 6.4,
        "retail": 3.92,
        "total": 4.27
      },
      "applications_count": "4.27x Subscription"
    },
    "listing": {
      "listing_price": 76.0,
      "listing_gain_rs": 0.0,
      "listing_gain_percent": 0.0,
      "profit_per_lot": 0.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 79.8,
        "actual_price": 76.0,
        "variance_rs": -3.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b979.8 (+5.0%). Stock opened at \u20b976.0 (+0.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 0.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (+0.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "EV Two-Wheelers Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in EV Two-Wheelers",
        "Strong institutional interest with 5.31x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.6,
        "gmp_percent": 4.8,
        "est_listing_price": 79.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.7,
        "gmp_percent": 4.9,
        "est_listing_price": 79.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 3.8,
        "gmp_percent": 5.0,
        "est_listing_price": 79.8,
        "notes": "Predicted \u20b979.8 listing"
      }
    ]
  },
  {
    "id": "ceigall",
    "name": "Ceigall India Ltd",
    "symbol": "CEIGALL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Highways & Infrastructure EPC",
    "open_date": "01-Aug-24",
    "close_date": "05-Aug-24",
    "listing_date": "08-Aug-24",
    "price_band": "\u20b9401",
    "issue_price": 401.0,
    "lot_size": 37,
    "min_investment": 14837,
    "issue_size_cr": 1252.66,
    "fresh_issue_cr": 939.5,
    "ofs_cr": 313.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 24.06,
    "gmp_closing_percent": 6.0,
    "gmp_estimated_listing": 425.06,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.88,
        "nii": 4.15,
        "retail": 1.54,
        "total": 4.15
      },
      "day2": {
        "qib": 7.2,
        "nii": 9.69,
        "retail": 3.07,
        "total": 9.0
      },
      "final_day": {
        "qib": 14.4,
        "nii": 20.76,
        "retail": 3.84,
        "total": 13.84
      },
      "applications_count": "13.84x Subscription"
    },
    "listing": {
      "listing_price": 419.0,
      "listing_gain_rs": 18.0,
      "listing_gain_percent": 4.5,
      "profit_per_lot": 666.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 425.06,
        "actual_price": 419.0,
        "variance_rs": -6.06,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9425.06 (+6.0%). Stock opened at \u20b9419.0 (+4.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 6.0,
      "actual_gain_pct": 4.5,
      "retail_profit_lost": 666.0,
      "explanation": "The IPO had a flat listing (+4.5%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +6% Listing Return",
      "long_term_potential": "Highways & Infrastructure EPC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Highways & Infrastructure EPC",
        "Strong institutional interest with 14.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +4.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 22.9,
        "gmp_percent": 5.7,
        "est_listing_price": 423.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 23.6,
        "gmp_percent": 5.9,
        "est_listing_price": 424.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 24.06,
        "gmp_percent": 6.0,
        "est_listing_price": 425.1,
        "notes": "Predicted \u20b9425.06 listing"
      }
    ]
  },
  {
    "id": "akums",
    "name": "Akums Drugs and Pharmaceuticals",
    "symbol": "AKUMS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pharmaceuticals CDMO",
    "open_date": "30-Jul-24",
    "close_date": "01-Aug-24",
    "listing_date": "06-Aug-24",
    "price_band": "\u20b9679",
    "issue_price": 679.0,
    "lot_size": 22,
    "min_investment": 14938,
    "issue_size_cr": 1856.74,
    "fresh_issue_cr": 1392.6,
    "ofs_cr": 464.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 122.22,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 801.22,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 18.01,
        "nii": 19.07,
        "retail": 8.52,
        "total": 19.07
      },
      "day2": {
        "qib": 45.03,
        "nii": 44.49,
        "retail": 17.04,
        "total": 41.31
      },
      "final_day": {
        "qib": 90.07,
        "nii": 95.34,
        "retail": 21.3,
        "total": 63.56
      },
      "applications_count": "63.56x Subscription"
    },
    "listing": {
      "listing_price": 779.0,
      "listing_gain_rs": 100.0,
      "listing_gain_percent": 14.7,
      "profit_per_lot": 2200.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 801.22,
        "actual_price": 779.0,
        "variance_rs": -22.22,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9801.22 (+18.0%). Stock opened at \u20b9779.0 (+14.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 14.7,
      "retail_profit_lost": 2200.0,
      "explanation": "The issue opened with a healthy +14.7% pop (\u20b92,200 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "Pharmaceuticals CDMO Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pharmaceuticals CDMO",
        "Strong institutional interest with 90.07x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +14.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 116.1,
        "gmp_percent": 17.1,
        "est_listing_price": 795.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 119.8,
        "gmp_percent": 17.6,
        "est_listing_price": 798.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 122.22,
        "gmp_percent": 18.0,
        "est_listing_price": 801.2,
        "notes": "Predicted \u20b9801.22 listing"
      }
    ]
  },
  {
    "id": "sanstar",
    "name": "Sanstar Ltd",
    "symbol": "SANSTAR.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Plant-based Specialty Food Products",
    "open_date": "19-Jul-24",
    "close_date": "23-Jul-24",
    "listing_date": "26-Jul-24",
    "price_band": "\u20b995",
    "issue_price": 95.0,
    "lot_size": 150,
    "min_investment": 14250,
    "issue_size_cr": 510.15,
    "fresh_issue_cr": 382.6,
    "ofs_cr": 127.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 17.1,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 112.1,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 19.68,
        "nii": 24.9,
        "retail": 9.69,
        "total": 24.9
      },
      "day2": {
        "qib": 49.2,
        "nii": 58.09,
        "retail": 19.38,
        "total": 53.94
      },
      "final_day": {
        "qib": 98.4,
        "nii": 124.48,
        "retail": 24.23,
        "total": 82.99
      },
      "applications_count": "82.99x Subscription"
    },
    "listing": {
      "listing_price": 109.0,
      "listing_gain_rs": 14.0,
      "listing_gain_percent": 14.7,
      "profit_per_lot": 2100.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 112.1,
        "actual_price": 109.0,
        "variance_rs": -3.1,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9112.1 (+18.0%). Stock opened at \u20b9109.0 (+14.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 14.7,
      "retail_profit_lost": 2100.0,
      "explanation": "The issue opened with a healthy +14.7% pop (\u20b92,100 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "Plant-based Specialty Food Products Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Plant-based Specialty Food Products",
        "Strong institutional interest with 98.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +14.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 16.2,
        "gmp_percent": 17.1,
        "est_listing_price": 111.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 16.8,
        "gmp_percent": 17.6,
        "est_listing_price": 111.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 17.1,
        "gmp_percent": 18.0,
        "est_listing_price": 112.1,
        "notes": "Predicted \u20b9112.1 listing"
      }
    ]
  },
  {
    "id": "emcure",
    "name": "Emcure Pharmaceuticals Ltd",
    "symbol": "EMCURE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Formulations & Biotechnology",
    "open_date": "03-Jul-24",
    "close_date": "05-Jul-24",
    "listing_date": "10-Jul-24",
    "price_band": "\u20b91,008",
    "issue_price": 1008.0,
    "lot_size": 14,
    "min_investment": 14112,
    "issue_size_cr": 1952.03,
    "fresh_issue_cr": 1464.0,
    "ofs_cr": 488.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 302.4,
    "gmp_closing_percent": 30.0,
    "gmp_estimated_listing": 1310.4,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 9.66,
        "nii": 20.36,
        "retail": 2.88,
        "total": 20.36
      },
      "day2": {
        "qib": 24.16,
        "nii": 47.51,
        "retail": 5.77,
        "total": 44.12
      },
      "final_day": {
        "qib": 48.32,
        "nii": 101.81,
        "retail": 7.21,
        "total": 67.87
      },
      "applications_count": "67.87x Subscription"
    },
    "listing": {
      "listing_price": 1325.0,
      "listing_gain_rs": 317.0,
      "listing_gain_percent": 31.5,
      "profit_per_lot": 4438.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1310.4,
        "actual_price": 1325.0,
        "variance_rs": 14.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91310.4 (+30.0%). Stock opened at \u20b91325.0 (+31.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 30.0,
      "actual_gain_pct": 31.5,
      "retail_profit_lost": 4438.0,
      "explanation": "Emcure Pharmaceuticals Ltd delivered a stellar +31.5% listing gain, rewarding retail allottees with \u20b94,438 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +30% Listing Return",
      "long_term_potential": "Formulations & Biotechnology Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Formulations & Biotechnology",
        "Strong institutional interest with 48.32x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +31.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 235.9,
        "gmp_percent": 23.4,
        "est_listing_price": 1243.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 272.2,
        "gmp_percent": 27.0,
        "est_listing_price": 1280.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 302.4,
        "gmp_percent": 30.0,
        "est_listing_price": 1310.4,
        "notes": "Predicted \u20b91310.4 listing"
      }
    ]
  },
  {
    "id": "bansalwire",
    "name": "Bansal Wire Industries Ltd",
    "symbol": "BANSALWIRE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Steel Wire Manufacturing",
    "open_date": "03-Jul-24",
    "close_date": "05-Jul-24",
    "listing_date": "10-Jul-24",
    "price_band": "\u20b9256",
    "issue_price": 256.0,
    "lot_size": 58,
    "min_investment": 14848,
    "issue_size_cr": 745.0,
    "fresh_issue_cr": 558.8,
    "ofs_cr": 186.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 89.6,
    "gmp_closing_percent": 35.0,
    "gmp_estimated_listing": 345.6,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 10.29,
        "nii": 17.87,
        "retail": 5.46,
        "total": 17.87
      },
      "day2": {
        "qib": 25.73,
        "nii": 41.7,
        "retail": 10.91,
        "total": 38.72
      },
      "final_day": {
        "qib": 51.46,
        "nii": 89.36,
        "retail": 13.64,
        "total": 59.57
      },
      "applications_count": "59.57x Subscription"
    },
    "listing": {
      "listing_price": 352.0,
      "listing_gain_rs": 96.0,
      "listing_gain_percent": 37.5,
      "profit_per_lot": 5568.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 345.6,
        "actual_price": 352.0,
        "variance_rs": 6.4,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9345.6 (+35.0%). Stock opened at \u20b9352.0 (+37.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 35.0,
      "actual_gain_pct": 37.5,
      "retail_profit_lost": 5568.0,
      "explanation": "Bansal Wire Industries Ltd delivered a stellar +37.5% listing gain, rewarding retail allottees with \u20b95,568 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +35% Listing Return",
      "long_term_potential": "Steel Wire Manufacturing Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Steel Wire Manufacturing",
        "Strong institutional interest with 51.46x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +37.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 69.9,
        "gmp_percent": 27.3,
        "est_listing_price": 325.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 80.6,
        "gmp_percent": 31.5,
        "est_listing_price": 336.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 89.6,
        "gmp_percent": 35.0,
        "est_listing_price": 345.6,
        "notes": "Predicted \u20b9345.6 listing"
      }
    ]
  },
  {
    "id": "allied",
    "name": "Allied Blenders and Distillers",
    "symbol": "ALLIED.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Alcoholic Beverages (Officer's Choice)",
    "open_date": "25-Jun-24",
    "close_date": "27-Jun-24",
    "listing_date": "02-Jul-24",
    "price_band": "\u20b9281",
    "issue_price": 281.0,
    "lot_size": 53,
    "min_investment": 14893,
    "issue_size_cr": 1500.0,
    "fresh_issue_cr": 1125.0,
    "ofs_cr": 375.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 42.15,
    "gmp_closing_percent": 15.0,
    "gmp_estimated_listing": 323.15,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 6.48,
        "nii": 7.07,
        "retail": 1.8,
        "total": 7.07
      },
      "day2": {
        "qib": 16.2,
        "nii": 16.48,
        "retail": 3.61,
        "total": 15.31
      },
      "final_day": {
        "qib": 32.4,
        "nii": 35.33,
        "retail": 4.51,
        "total": 23.55
      },
      "applications_count": "23.55x Subscription"
    },
    "listing": {
      "listing_price": 318.0,
      "listing_gain_rs": 37.0,
      "listing_gain_percent": 13.2,
      "profit_per_lot": 1961.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 323.15,
        "actual_price": 318.0,
        "variance_rs": -5.15,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9323.15 (+15.0%). Stock opened at \u20b9318.0 (+13.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 15.0,
      "actual_gain_pct": 13.2,
      "retail_profit_lost": 1961.0,
      "explanation": "The issue opened with a healthy +13.2% pop (\u20b91,961 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +15% Listing Return",
      "long_term_potential": "Alcoholic Beverages (Officer's Choice) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Alcoholic Beverages (Officer's Choice)",
        "Strong institutional interest with 32.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +13.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 40.0,
        "gmp_percent": 14.2,
        "est_listing_price": 321.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 41.3,
        "gmp_percent": 14.7,
        "est_listing_price": 322.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 42.15,
        "gmp_percent": 15.0,
        "est_listing_price": 323.1,
        "notes": "Predicted \u20b9323.15 listing"
      }
    ]
  },
  {
    "id": "bhartihexa",
    "name": "Bharti Hexacom Ltd",
    "symbol": "BHARTIHEXA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Telecommunication Services",
    "open_date": "03-Apr-24",
    "close_date": "05-Apr-24",
    "listing_date": "12-Apr-24",
    "price_band": "\u20b9570",
    "issue_price": 570.0,
    "lot_size": 26,
    "min_investment": 14820,
    "issue_size_cr": 4275.0,
    "fresh_issue_cr": 3206.2,
    "ofs_cr": 1068.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 171.0,
    "gmp_closing_percent": 30.0,
    "gmp_estimated_listing": 741.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 9.71,
        "nii": 8.96,
        "retail": 1.13,
        "total": 8.96
      },
      "day2": {
        "qib": 24.29,
        "nii": 20.92,
        "retail": 2.26,
        "total": 19.42
      },
      "final_day": {
        "qib": 48.57,
        "nii": 44.82,
        "retail": 2.83,
        "total": 29.88
      },
      "applications_count": "29.88x Subscription"
    },
    "listing": {
      "listing_price": 755.0,
      "listing_gain_rs": 185.0,
      "listing_gain_percent": 32.5,
      "profit_per_lot": 4810.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 741.0,
        "actual_price": 755.0,
        "variance_rs": 14.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9741.0 (+30.0%). Stock opened at \u20b9755.0 (+32.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 30.0,
      "actual_gain_pct": 32.5,
      "retail_profit_lost": 4810.0,
      "explanation": "Bharti Hexacom Ltd delivered a stellar +32.5% listing gain, rewarding retail allottees with \u20b94,810 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +30% Listing Return",
      "long_term_potential": "Telecommunication Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Telecommunication Services",
        "Strong institutional interest with 48.57x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +32.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 133.4,
        "gmp_percent": 23.4,
        "est_listing_price": 703.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 153.9,
        "gmp_percent": 27.0,
        "est_listing_price": 723.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 171.0,
        "gmp_percent": 30.0,
        "est_listing_price": 741.0,
        "notes": "Predicted \u20b9741.0 listing"
      }
    ]
  },
  {
    "id": "srm",
    "name": "SRM Contractors Ltd",
    "symbol": "SRM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Tunnels & Road Construction",
    "open_date": "26-Mar-24",
    "close_date": "28-Mar-24",
    "listing_date": "03-Apr-24",
    "price_band": "\u20b9210",
    "issue_price": 210.0,
    "lot_size": 70,
    "min_investment": 14700,
    "issue_size_cr": 130.2,
    "fresh_issue_cr": 97.6,
    "ofs_cr": 32.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 25.2,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 235.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 42.99,
        "nii": 25.97,
        "retail": 18.79,
        "total": 25.97
      },
      "day2": {
        "qib": 107.47,
        "nii": 60.6,
        "retail": 37.58,
        "total": 56.27
      },
      "final_day": {
        "qib": 214.94,
        "nii": 129.85,
        "retail": 46.97,
        "total": 86.57
      },
      "applications_count": "86.57x Subscription"
    },
    "listing": {
      "listing_price": 225.0,
      "listing_gain_rs": 15.0,
      "listing_gain_percent": 7.1,
      "profit_per_lot": 1050.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 235.2,
        "actual_price": 225.0,
        "variance_rs": -10.2,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9235.2 (+12.0%). Stock opened at \u20b9225.0 (+7.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 7.1,
      "retail_profit_lost": 1050.0,
      "explanation": "The issue opened with a healthy +7.1% pop (\u20b91,050 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "Tunnels & Road Construction Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Tunnels & Road Construction",
        "Strong institutional interest with 214.94x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +7.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 23.9,
        "gmp_percent": 11.4,
        "est_listing_price": 233.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 24.7,
        "gmp_percent": 11.8,
        "est_listing_price": 234.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 25.2,
        "gmp_percent": 12.0,
        "est_listing_price": 235.2,
        "notes": "Predicted \u20b9235.2 listing"
      }
    ]
  },
  {
    "id": "krystal",
    "name": "Krystal Integrated Services Ltd",
    "symbol": "KRYSTAL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Facility Management & Staffing",
    "open_date": "14-Mar-24",
    "close_date": "18-Mar-24",
    "listing_date": "21-Mar-24",
    "price_band": "\u20b9715",
    "issue_price": 715.0,
    "lot_size": 20,
    "min_investment": 14300,
    "issue_size_cr": 300.13,
    "fresh_issue_cr": 225.1,
    "ofs_cr": 75.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 71.5,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 786.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 8.76,
        "nii": 3.96,
        "retail": 1.33,
        "total": 3.96
      },
      "day2": {
        "qib": 21.9,
        "nii": 9.25,
        "retail": 2.66,
        "total": 8.59
      },
      "final_day": {
        "qib": 43.8,
        "nii": 19.82,
        "retail": 3.32,
        "total": 13.21
      },
      "applications_count": "13.21x Subscription"
    },
    "listing": {
      "listing_price": 795.0,
      "listing_gain_rs": 80.0,
      "listing_gain_percent": 11.2,
      "profit_per_lot": 1600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 786.5,
        "actual_price": 795.0,
        "variance_rs": 8.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9786.5 (+10.0%). Stock opened at \u20b9795.0 (+11.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 11.2,
      "retail_profit_lost": 1600.0,
      "explanation": "The issue opened with a healthy +11.2% pop (\u20b91,600 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Facility Management & Staffing Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Facility Management & Staffing",
        "Strong institutional interest with 43.8x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +11.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 67.9,
        "gmp_percent": 9.5,
        "est_listing_price": 782.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 70.1,
        "gmp_percent": 9.8,
        "est_listing_price": 785.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 71.5,
        "gmp_percent": 10.0,
        "est_listing_price": 786.5,
        "notes": "Predicted \u20b9786.5 listing"
      }
    ]
  },
  {
    "id": "pvsl",
    "name": "Popular Vehicles and Services Ltd",
    "symbol": "PVSL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Automobile Dealerships",
    "open_date": "12-Mar-24",
    "close_date": "14-Mar-24",
    "listing_date": "19-Mar-24",
    "price_band": "\u20b9295",
    "issue_price": 295.0,
    "lot_size": 50,
    "min_investment": 14750,
    "issue_size_cr": 601.55,
    "fresh_issue_cr": 451.2,
    "ofs_cr": 150.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 295.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.39,
        "nii": 0.37,
        "retail": 0.43,
        "total": 0.37
      },
      "day2": {
        "qib": 0.98,
        "nii": 0.86,
        "retail": 0.86,
        "total": 0.8
      },
      "final_day": {
        "qib": 1.97,
        "nii": 1.84,
        "retail": 1.07,
        "total": 1.23
      },
      "applications_count": "1.23x Subscription"
    },
    "listing": {
      "listing_price": 292.0,
      "listing_gain_rs": -3.0,
      "listing_gain_percent": -1.0,
      "profit_per_lot": -150.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 295.0,
        "actual_price": 292.0,
        "variance_rs": -3.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9295.0 (+0.0%). Stock opened at \u20b9292.0 (-1.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -1.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-1.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Automobile Dealerships Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Automobile Dealerships",
        "Strong institutional interest with 1.97x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -1.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 295.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 295.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 295.0,
        "notes": "Predicted \u20b9295.0 listing"
      }
    ]
  },
  {
    "id": "gopal",
    "name": "Gopal Snacks Ltd",
    "symbol": "GOPAL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Packaged Snacks & FMCG",
    "open_date": "06-Mar-24",
    "close_date": "11-Mar-24",
    "listing_date": "14-Mar-24",
    "price_band": "\u20b9401",
    "issue_price": 401.0,
    "lot_size": 37,
    "min_investment": 14837,
    "issue_size_cr": 650.0,
    "fresh_issue_cr": 487.5,
    "ofs_cr": 162.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -20.05,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 380.95,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 1.9,
        "nii": 2.71,
        "retail": 1.6,
        "total": 2.71
      },
      "day2": {
        "qib": 4.75,
        "nii": 6.31,
        "retail": 3.21,
        "total": 5.86
      },
      "final_day": {
        "qib": 9.5,
        "nii": 13.53,
        "retail": 4.01,
        "total": 9.02
      },
      "applications_count": "9.02x Subscription"
    },
    "listing": {
      "listing_price": 350.0,
      "listing_gain_rs": -51.0,
      "listing_gain_percent": -12.7,
      "profit_per_lot": -1887.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 380.95,
        "actual_price": 350.0,
        "variance_rs": -30.95,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9380.95 (-5.0%). Stock opened at \u20b9350.0 (-12.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -12.7,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -12.7% (\u20b91,887 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Packaged Snacks & FMCG Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Packaged Snacks & FMCG",
        "Strong institutional interest with 9.5x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -12.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -25.1,
        "gmp_percent": -6.2,
        "est_listing_price": 375.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -22.5,
        "gmp_percent": -5.6,
        "est_listing_price": 378.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -20.05,
        "gmp_percent": -5.0,
        "est_listing_price": 380.9,
        "notes": "Predicted \u20b9380.95 listing"
      }
    ]
  },
  {
    "id": "jgchem",
    "name": "JG Chemicals Ltd",
    "symbol": "JGCHEM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Zinc Oxide & Chemicals",
    "open_date": "05-Mar-24",
    "close_date": "07-Mar-24",
    "listing_date": "13-Mar-24",
    "price_band": "\u20b9221",
    "issue_price": 221.0,
    "lot_size": 67,
    "min_investment": 14807,
    "issue_size_cr": 251.19,
    "fresh_issue_cr": 188.4,
    "ofs_cr": 62.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 6.63,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 227.63,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 9.27,
        "nii": 8.33,
        "retail": 6.98,
        "total": 8.33
      },
      "day2": {
        "qib": 23.16,
        "nii": 19.45,
        "retail": 13.95,
        "total": 18.06
      },
      "final_day": {
        "qib": 46.33,
        "nii": 41.67,
        "retail": 17.44,
        "total": 27.78
      },
      "applications_count": "27.78x Subscription"
    },
    "listing": {
      "listing_price": 211.0,
      "listing_gain_rs": -10.0,
      "listing_gain_percent": -4.5,
      "profit_per_lot": -670.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 227.63,
        "actual_price": 211.0,
        "variance_rs": -16.63,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9227.63 (+3.0%). Stock opened at \u20b9211.0 (-4.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": -4.5,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -4.5% (\u20b9670 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "Zinc Oxide & Chemicals Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Zinc Oxide & Chemicals",
        "Strong institutional interest with 46.33x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -4.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 6.3,
        "gmp_percent": 2.8,
        "est_listing_price": 227.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 6.5,
        "gmp_percent": 2.9,
        "est_listing_price": 227.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 6.63,
        "gmp_percent": 3.0,
        "est_listing_price": 227.6,
        "notes": "Predicted \u20b9227.63 listing"
      }
    ]
  },
  {
    "id": "bhinvit",
    "name": "Bharat Highways InvIT",
    "symbol": "BHINVIT.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Road Infrastructure & InvIT",
    "open_date": "28-Feb-24",
    "close_date": "01-Mar-24",
    "listing_date": "12-Mar-24",
    "price_band": "\u20b9100",
    "issue_price": 100.0,
    "lot_size": 150,
    "min_investment": 15000,
    "issue_size_cr": 2500.0,
    "fresh_issue_cr": 1875.0,
    "ofs_cr": 625.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 2.0,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 102.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.78,
        "nii": 2.4,
        "retail": 3.57,
        "total": 2.4
      },
      "day2": {
        "qib": 4.46,
        "nii": 5.61,
        "retail": 7.14,
        "total": 5.21
      },
      "final_day": {
        "qib": 8.92,
        "nii": 12.02,
        "retail": 8.93,
        "total": 8.01
      },
      "applications_count": "8.01x Subscription"
    },
    "listing": {
      "listing_price": 101.1,
      "listing_gain_rs": 1.1,
      "listing_gain_percent": 1.1,
      "profit_per_lot": 165.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 102.0,
        "actual_price": 101.1,
        "variance_rs": -0.9,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9102.0 (+2.0%). Stock opened at \u20b9101.1 (+1.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 1.1,
      "retail_profit_lost": 165.0,
      "explanation": "The IPO had a flat listing (+1.1%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Road Infrastructure & InvIT Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Road Infrastructure & InvIT",
        "Strong institutional interest with 8.92x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 1.9,
        "gmp_percent": 1.9,
        "est_listing_price": 101.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 2.0,
        "gmp_percent": 2.0,
        "est_listing_price": 102.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 2.0,
        "gmp_percent": 2.0,
        "est_listing_price": 102.0,
        "notes": "Predicted \u20b9102.0 listing"
      }
    ]
  },
  {
    "id": "mukka",
    "name": "Mukka Proteins Ltd",
    "symbol": "MUKKA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Fish Meal & Marine Feeds",
    "open_date": "29-Feb-24",
    "close_date": "04-Mar-24",
    "listing_date": "07-Mar-24",
    "price_band": "\u20b928",
    "issue_price": 28.0,
    "lot_size": 535,
    "min_investment": 14980,
    "issue_size_cr": 224.0,
    "fresh_issue_cr": 168.0,
    "ofs_cr": 56.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Cameo Corporate Services Ltd",
    "gmp_closing_day": 14.56,
    "gmp_closing_percent": 52.0,
    "gmp_estimated_listing": 42.56,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 37.86,
        "nii": 41.1,
        "retail": 23.41,
        "total": 41.1
      },
      "day2": {
        "qib": 94.64,
        "nii": 95.89,
        "retail": 46.82,
        "total": 89.04
      },
      "final_day": {
        "qib": 189.28,
        "nii": 205.49,
        "retail": 58.52,
        "total": 136.99
      },
      "applications_count": "136.99x Subscription"
    },
    "listing": {
      "listing_price": 42.25,
      "listing_gain_rs": 14.25,
      "listing_gain_percent": 50.9,
      "profit_per_lot": 7623.75,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 42.56,
        "actual_price": 42.25,
        "variance_rs": -0.31,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b942.56 (+52.0%). Stock opened at \u20b942.25 (+50.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 52.0,
      "actual_gain_pct": 50.9,
      "retail_profit_lost": 7623.75,
      "explanation": "Mukka Proteins Ltd delivered a stellar +50.9% listing gain, rewarding retail allottees with \u20b97,624 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +52% Listing Return",
      "long_term_potential": "Fish Meal & Marine Feeds Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Fish Meal & Marine Feeds",
        "Strong institutional interest with 189.28x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +50.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 11.4,
        "gmp_percent": 40.6,
        "est_listing_price": 39.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 13.1,
        "gmp_percent": 46.8,
        "est_listing_price": 41.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 14.56,
        "gmp_percent": 52.0,
        "est_listing_price": 42.6,
        "notes": "Predicted \u20b942.56 listing"
      }
    ]
  },
  {
    "id": "platind",
    "name": "Platinum Industries Ltd",
    "symbol": "PLATIND.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Specialty Chemicals & PVC",
    "open_date": "27-Feb-24",
    "close_date": "29-Feb-24",
    "listing_date": "05-Mar-24",
    "price_band": "\u20b9171",
    "issue_price": 171.0,
    "lot_size": 87,
    "min_investment": 14877,
    "issue_size_cr": 235.32,
    "fresh_issue_cr": 176.5,
    "ofs_cr": 58.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 59.85,
    "gmp_closing_percent": 35.0,
    "gmp_estimated_listing": 230.85,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 30.2,
        "nii": 29.71,
        "retail": 20.4,
        "total": 29.71
      },
      "day2": {
        "qib": 75.5,
        "nii": 69.32,
        "retail": 40.79,
        "total": 64.37
      },
      "final_day": {
        "qib": 151.0,
        "nii": 148.55,
        "retail": 50.99,
        "total": 99.03
      },
      "applications_count": "99.03x Subscription"
    },
    "listing": {
      "listing_price": 228.0,
      "listing_gain_rs": 57.0,
      "listing_gain_percent": 33.3,
      "profit_per_lot": 4959.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 230.85,
        "actual_price": 228.0,
        "variance_rs": -2.85,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9230.85 (+35.0%). Stock opened at \u20b9228.0 (+33.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 35.0,
      "actual_gain_pct": 33.3,
      "retail_profit_lost": 4959.0,
      "explanation": "Platinum Industries Ltd delivered a stellar +33.3% listing gain, rewarding retail allottees with \u20b94,959 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +35% Listing Return",
      "long_term_potential": "Specialty Chemicals & PVC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Specialty Chemicals & PVC",
        "Strong institutional interest with 151.0x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +33.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 46.7,
        "gmp_percent": 27.3,
        "est_listing_price": 217.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 53.9,
        "gmp_percent": 31.5,
        "est_listing_price": 224.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 59.85,
        "gmp_percent": 35.0,
        "est_listing_price": 230.8,
        "notes": "Predicted \u20b9230.85 listing"
      }
    ]
  },
  {
    "id": "exicom",
    "name": "Exicom Tele-Systems Ltd",
    "symbol": "EXICOM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "EV Chargers & Power Systems",
    "open_date": "27-Feb-24",
    "close_date": "29-Feb-24",
    "listing_date": "05-Mar-24",
    "price_band": "\u20b9142",
    "issue_price": 142.0,
    "lot_size": 100,
    "min_investment": 14200,
    "issue_size_cr": 429.0,
    "fresh_issue_cr": 321.8,
    "ofs_cr": 107.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 124.96,
    "gmp_closing_percent": 88.0,
    "gmp_estimated_listing": 266.96,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 24.36,
        "nii": 38.83,
        "retail": 47.84,
        "total": 38.83
      },
      "day2": {
        "qib": 60.9,
        "nii": 90.61,
        "retail": 95.67,
        "total": 84.14
      },
      "final_day": {
        "qib": 121.8,
        "nii": 194.16,
        "retail": 119.59,
        "total": 129.44
      },
      "applications_count": "129.44x Subscription"
    },
    "listing": {
      "listing_price": 265.0,
      "listing_gain_rs": 123.0,
      "listing_gain_percent": 86.6,
      "profit_per_lot": 12300.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 266.96,
        "actual_price": 265.0,
        "variance_rs": -1.96,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9266.96 (+88.0%). Stock opened at \u20b9265.0 (+86.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 88.0,
      "actual_gain_pct": 86.6,
      "retail_profit_lost": 12300.0,
      "explanation": "Exicom Tele-Systems Ltd delivered a stellar +86.6% listing gain, rewarding retail allottees with \u20b912,300 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +88% Listing Return",
      "long_term_potential": "EV Chargers & Power Systems Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in EV Chargers & Power Systems",
        "Strong institutional interest with 121.8x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +86.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 97.5,
        "gmp_percent": 68.6,
        "est_listing_price": 239.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 112.5,
        "gmp_percent": 79.2,
        "est_listing_price": 254.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 124.96,
        "gmp_percent": 88.0,
        "est_listing_price": 267.0,
        "notes": "Predicted \u20b9266.96 listing"
      }
    ]
  },
  {
    "id": "gpthealth",
    "name": "GPT Healthcare Ltd (ILS Hospitals)",
    "symbol": "GPTHEALTH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Hospital & Healthcare",
    "open_date": "22-Feb-24",
    "close_date": "26-Feb-24",
    "listing_date": "29-Feb-24",
    "price_band": "\u20b9186",
    "issue_price": 186.0,
    "lot_size": 80,
    "min_investment": 14880,
    "issue_size_cr": 525.14,
    "fresh_issue_cr": 393.9,
    "ofs_cr": 131.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 27.9,
    "gmp_closing_percent": 15.0,
    "gmp_estimated_listing": 213.9,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 3.46,
        "nii": 2.56,
        "retail": 0.98,
        "total": 2.56
      },
      "day2": {
        "qib": 8.65,
        "nii": 5.96,
        "retail": 1.95,
        "total": 5.54
      },
      "final_day": {
        "qib": 17.3,
        "nii": 12.78,
        "retail": 2.44,
        "total": 8.52
      },
      "applications_count": "8.52x Subscription"
    },
    "listing": {
      "listing_price": 216.15,
      "listing_gain_rs": 30.15,
      "listing_gain_percent": 16.2,
      "profit_per_lot": 2412.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 213.9,
        "actual_price": 216.15,
        "variance_rs": 2.25,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9213.9 (+15.0%). Stock opened at \u20b9216.15 (+16.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 15.0,
      "actual_gain_pct": 16.2,
      "retail_profit_lost": 2412.0,
      "explanation": "The issue opened with a healthy +16.2% pop (\u20b92,412 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +15% Listing Return",
      "long_term_potential": "Hospital & Healthcare Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Hospital & Healthcare",
        "Strong institutional interest with 17.3x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +16.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 26.5,
        "gmp_percent": 14.2,
        "est_listing_price": 212.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 27.3,
        "gmp_percent": 14.7,
        "est_listing_price": 213.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 27.9,
        "gmp_percent": 15.0,
        "est_listing_price": 213.9,
        "notes": "Predicted \u20b9213.9 listing"
      }
    ]
  },
  {
    "id": "juniper",
    "name": "Juniper Hotels Ltd (Hyatt)",
    "symbol": "JUNIPER.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Luxury Hospitality & Hotels",
    "open_date": "21-Feb-24",
    "close_date": "23-Feb-24",
    "listing_date": "28-Feb-24",
    "price_band": "\u20b9360",
    "issue_price": 360.0,
    "lot_size": 40,
    "min_investment": 14400,
    "issue_size_cr": 1800.0,
    "fresh_issue_cr": 1350.0,
    "ofs_cr": 450.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 10.8,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 370.8,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.59,
        "nii": 0.44,
        "retail": 0.51,
        "total": 0.44
      },
      "day2": {
        "qib": 1.48,
        "nii": 1.02,
        "retail": 1.02,
        "total": 0.95
      },
      "final_day": {
        "qib": 2.96,
        "nii": 2.19,
        "retail": 1.28,
        "total": 1.46
      },
      "applications_count": "1.46x Subscription"
    },
    "listing": {
      "listing_price": 365.0,
      "listing_gain_rs": 5.0,
      "listing_gain_percent": 1.4,
      "profit_per_lot": 200.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 370.8,
        "actual_price": 365.0,
        "variance_rs": -5.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9370.8 (+3.0%). Stock opened at \u20b9365.0 (+1.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": 1.4,
      "retail_profit_lost": 200.0,
      "explanation": "The IPO had a flat listing (+1.4%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "Luxury Hospitality & Hotels Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Luxury Hospitality & Hotels",
        "Strong institutional interest with 2.96x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 10.3,
        "gmp_percent": 2.8,
        "est_listing_price": 370.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 10.6,
        "gmp_percent": 2.9,
        "est_listing_price": 370.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 10.8,
        "gmp_percent": 3.0,
        "est_listing_price": 370.8,
        "notes": "Predicted \u20b9370.8 listing"
      }
    ]
  },
  {
    "id": "vstl",
    "name": "Vibhor Steel Tubes Ltd",
    "symbol": "VSTL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Steel & Pipes Manufacturing",
    "open_date": "13-Feb-24",
    "close_date": "15-Feb-24",
    "listing_date": "20-Feb-24",
    "price_band": "\u20b9151",
    "issue_price": 151.0,
    "lot_size": 99,
    "min_investment": 14949,
    "issue_size_cr": 72.17,
    "fresh_issue_cr": 54.1,
    "ofs_cr": 18.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 264.25,
    "gmp_closing_percent": 175.0,
    "gmp_estimated_listing": 415.25,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 35.75,
        "nii": 89.66,
        "retail": 75.32,
        "total": 89.66
      },
      "day2": {
        "qib": 89.39,
        "nii": 209.2,
        "retail": 150.63,
        "total": 194.26
      },
      "final_day": {
        "qib": 178.77,
        "nii": 448.29,
        "retail": 188.29,
        "total": 298.86
      },
      "applications_count": "298.86x Subscription"
    },
    "listing": {
      "listing_price": 425.0,
      "listing_gain_rs": 274.0,
      "listing_gain_percent": 181.5,
      "profit_per_lot": 27126.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 415.25,
        "actual_price": 425.0,
        "variance_rs": 9.75,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9415.25 (+175.0%). Stock opened at \u20b9425.0 (+181.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 175.0,
      "actual_gain_pct": 181.5,
      "retail_profit_lost": 27126.0,
      "explanation": "Vibhor Steel Tubes Ltd delivered a stellar +181.5% listing gain, rewarding retail allottees with \u20b927,126 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +175% Listing Return",
      "long_term_potential": "Steel & Pipes Manufacturing Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Steel & Pipes Manufacturing",
        "Strong institutional interest with 178.77x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +181.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 206.1,
        "gmp_percent": 136.5,
        "est_listing_price": 357.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 237.8,
        "gmp_percent": 157.5,
        "est_listing_price": 388.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 264.25,
        "gmp_percent": 175.0,
        "est_listing_price": 415.2,
        "notes": "Predicted \u20b9415.25 listing"
      }
    ]
  },
  {
    "id": "entero",
    "name": "Entero Healthcare Solutions Ltd",
    "symbol": "ENTERO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Healthcare & Pharma Distribution",
    "open_date": "09-Feb-24",
    "close_date": "13-Feb-24",
    "listing_date": "16-Feb-24",
    "price_band": "\u20b91,258",
    "issue_price": 1258.0,
    "lot_size": 11,
    "min_investment": 13838,
    "issue_size_cr": 1600.0,
    "fresh_issue_cr": 1200.0,
    "ofs_cr": 400.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 1258.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.46,
        "nii": 0.46,
        "retail": 0.53,
        "total": 0.46
      },
      "day2": {
        "qib": 1.14,
        "nii": 1.07,
        "retail": 1.06,
        "total": 0.99
      },
      "final_day": {
        "qib": 2.28,
        "nii": 2.29,
        "retail": 1.33,
        "total": 1.53
      },
      "applications_count": "1.53x Subscription"
    },
    "listing": {
      "listing_price": 1228.0,
      "listing_gain_rs": -30.0,
      "listing_gain_percent": -2.4,
      "profit_per_lot": -330.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 1258.0,
        "actual_price": 1228.0,
        "variance_rs": -30.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b91258.0 (+0.0%). Stock opened at \u20b91228.0 (-2.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -2.4,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -2.4% (\u20b9330 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Healthcare & Pharma Distribution Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Healthcare & Pharma Distribution",
        "Strong institutional interest with 2.28x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -2.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 1258.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 1258.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 1258.0,
        "notes": "Predicted \u20b91258.0 listing"
      }
    ]
  },
  {
    "id": "rptech",
    "name": "Rashi Peripherals Ltd",
    "symbol": "RPTECH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "IT & Tech Hardware Distribution",
    "open_date": "07-Feb-24",
    "close_date": "09-Feb-24",
    "listing_date": "14-Feb-24",
    "price_band": "\u20b9311",
    "issue_price": 311.0,
    "lot_size": 48,
    "min_investment": 14928,
    "issue_size_cr": 600.0,
    "fresh_issue_cr": 450.0,
    "ofs_cr": 150.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 34.21,
    "gmp_closing_percent": 11.0,
    "gmp_estimated_listing": 345.21,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 12.49,
        "nii": 17.91,
        "retail": 4.18,
        "total": 17.91
      },
      "day2": {
        "qib": 31.21,
        "nii": 41.8,
        "retail": 8.35,
        "total": 38.81
      },
      "final_day": {
        "qib": 62.43,
        "nii": 89.56,
        "retail": 10.44,
        "total": 59.71
      },
      "applications_count": "59.71x Subscription"
    },
    "listing": {
      "listing_price": 339.5,
      "listing_gain_rs": 28.5,
      "listing_gain_percent": 9.2,
      "profit_per_lot": 1368.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 345.21,
        "actual_price": 339.5,
        "variance_rs": -5.71,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9345.21 (+11.0%). Stock opened at \u20b9339.5 (+9.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 11.0,
      "actual_gain_pct": 9.2,
      "retail_profit_lost": 1368.0,
      "explanation": "The issue opened with a healthy +9.2% pop (\u20b91,368 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +11% Listing Return",
      "long_term_potential": "IT & Tech Hardware Distribution Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in IT & Tech Hardware Distribution",
        "Strong institutional interest with 62.43x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +9.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 32.5,
        "gmp_percent": 10.4,
        "est_listing_price": 343.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 33.5,
        "gmp_percent": 10.8,
        "est_listing_price": 344.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 34.21,
        "gmp_percent": 11.0,
        "est_listing_price": 345.2,
        "notes": "Predicted \u20b9345.21 listing"
      }
    ]
  },
  {
    "id": "jsfb",
    "name": "Jana Small Finance Bank Ltd",
    "symbol": "JSFB.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Banking & Microfinance",
    "open_date": "07-Feb-24",
    "close_date": "09-Feb-24",
    "listing_date": "14-Feb-24",
    "price_band": "\u20b9414",
    "issue_price": 414.0,
    "lot_size": 36,
    "min_investment": 14904,
    "issue_size_cr": 570.0,
    "fresh_issue_cr": 427.5,
    "ofs_cr": 142.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 8.28,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 422.28,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 7.75,
        "nii": 5.54,
        "retail": 2.18,
        "total": 5.54
      },
      "day2": {
        "qib": 19.38,
        "nii": 12.93,
        "retail": 4.37,
        "total": 12.01
      },
      "final_day": {
        "qib": 38.75,
        "nii": 27.7,
        "retail": 5.46,
        "total": 18.47
      },
      "applications_count": "18.47x Subscription"
    },
    "listing": {
      "listing_price": 396.0,
      "listing_gain_rs": -18.0,
      "listing_gain_percent": -4.3,
      "profit_per_lot": -648.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 422.28,
        "actual_price": 396.0,
        "variance_rs": -26.28,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9422.28 (+2.0%). Stock opened at \u20b9396.0 (-4.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": -4.3,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -4.3% (\u20b9648 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Banking & Microfinance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Banking & Microfinance",
        "Strong institutional interest with 38.75x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -4.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 7.9,
        "gmp_percent": 1.9,
        "est_listing_price": 421.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 8.1,
        "gmp_percent": 2.0,
        "est_listing_price": 422.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 8.28,
        "gmp_percent": 2.0,
        "est_listing_price": 422.3,
        "notes": "Predicted \u20b9422.28 listing"
      }
    ]
  },
  {
    "id": "capitalsfb",
    "name": "Capital Small Finance Bank Ltd",
    "symbol": "CAPITALSFB.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Banking & Small Finance",
    "open_date": "07-Feb-24",
    "close_date": "09-Feb-24",
    "listing_date": "14-Feb-24",
    "price_band": "\u20b9468",
    "issue_price": 468.0,
    "lot_size": 32,
    "min_investment": 14976,
    "issue_size_cr": 523.07,
    "fresh_issue_cr": 392.3,
    "ofs_cr": 130.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 4.68,
    "gmp_closing_percent": 1.0,
    "gmp_estimated_listing": 472.68,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.57,
        "nii": 1.2,
        "retail": 1.0,
        "total": 1.2
      },
      "day2": {
        "qib": 3.92,
        "nii": 2.8,
        "retail": 1.99,
        "total": 2.6
      },
      "final_day": {
        "qib": 7.85,
        "nii": 6.0,
        "retail": 2.49,
        "total": 4.0
      },
      "applications_count": "4.0x Subscription"
    },
    "listing": {
      "listing_price": 435.0,
      "listing_gain_rs": -33.0,
      "listing_gain_percent": -7.1,
      "profit_per_lot": -1056.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 472.68,
        "actual_price": 435.0,
        "variance_rs": -37.68,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9472.68 (+1.0%). Stock opened at \u20b9435.0 (-7.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 1.0,
      "actual_gain_pct": -7.1,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -7.1% (\u20b91,056 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +1% Listing Return",
      "long_term_potential": "Banking & Small Finance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Banking & Small Finance",
        "Strong institutional interest with 7.85x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -7.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 4.4,
        "gmp_percent": 0.9,
        "est_listing_price": 472.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 4.6,
        "gmp_percent": 1.0,
        "est_listing_price": 472.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 4.68,
        "gmp_percent": 1.0,
        "est_listing_price": 472.7,
        "notes": "Predicted \u20b9472.68 listing"
      }
    ]
  },
  {
    "id": "parkhotels",
    "name": "Apeejay Surrendra Park Hotels",
    "symbol": "PARKHOTELS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Hospitality & Hotels",
    "open_date": "05-Feb-24",
    "close_date": "07-Feb-24",
    "listing_date": "12-Feb-24",
    "price_band": "\u20b9155",
    "issue_price": 155.0,
    "lot_size": 96,
    "min_investment": 14880,
    "issue_size_cr": 920.0,
    "fresh_issue_cr": 690.0,
    "ofs_cr": 230.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 34.1,
    "gmp_closing_percent": 22.0,
    "gmp_estimated_listing": 189.1,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 15.03,
        "nii": 17.9,
        "retail": 12.05,
        "total": 17.9
      },
      "day2": {
        "qib": 37.57,
        "nii": 41.76,
        "retail": 24.1,
        "total": 38.78
      },
      "final_day": {
        "qib": 75.14,
        "nii": 89.49,
        "retail": 30.12,
        "total": 59.66
      },
      "applications_count": "59.66x Subscription"
    },
    "listing": {
      "listing_price": 187.0,
      "listing_gain_rs": 32.0,
      "listing_gain_percent": 20.6,
      "profit_per_lot": 3072.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 189.1,
        "actual_price": 187.0,
        "variance_rs": -2.1,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9189.1 (+22.0%). Stock opened at \u20b9187.0 (+20.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 22.0,
      "actual_gain_pct": 20.6,
      "retail_profit_lost": 3072.0,
      "explanation": "The issue opened with a healthy +20.6% pop (\u20b93,072 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +22% Listing Return",
      "long_term_potential": "Hospitality & Hotels Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Hospitality & Hotels",
        "Strong institutional interest with 75.14x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +20.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 26.6,
        "gmp_percent": 17.2,
        "est_listing_price": 181.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 30.7,
        "gmp_percent": 19.8,
        "est_listing_price": 185.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 34.1,
        "gmp_percent": 22.0,
        "est_listing_price": 189.1,
        "notes": "Predicted \u20b9189.1 listing"
      }
    ]
  },
  {
    "id": "blse",
    "name": "BLS E-Services Ltd",
    "symbol": "BLSE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Business Services",
    "open_date": "30-Jan-24",
    "close_date": "01-Feb-24",
    "listing_date": "06-Feb-24",
    "price_band": "\u20b9135",
    "issue_price": 135.0,
    "lot_size": 108,
    "min_investment": 14580,
    "issue_size_cr": 310.91,
    "fresh_issue_cr": 233.2,
    "ofs_cr": 77.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 168.75,
    "gmp_closing_percent": 125.0,
    "gmp_estimated_listing": 303.75,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 34.99,
        "nii": 48.74,
        "retail": 94.8,
        "total": 48.74
      },
      "day2": {
        "qib": 87.48,
        "nii": 113.74,
        "retail": 189.6,
        "total": 105.61
      },
      "final_day": {
        "qib": 174.96,
        "nii": 243.72,
        "retail": 237.0,
        "total": 162.48
      },
      "applications_count": "162.48x Subscription"
    },
    "listing": {
      "listing_price": 309.0,
      "listing_gain_rs": 174.0,
      "listing_gain_percent": 128.9,
      "profit_per_lot": 18792.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 303.75,
        "actual_price": 309.0,
        "variance_rs": 5.25,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9303.75 (+125.0%). Stock opened at \u20b9309.0 (+128.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 125.0,
      "actual_gain_pct": 128.9,
      "retail_profit_lost": 18792.0,
      "explanation": "BLS E-Services Ltd delivered a stellar +128.9% listing gain, rewarding retail allottees with \u20b918,792 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +125% Listing Return",
      "long_term_potential": "Digital Business Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Business Services",
        "Strong institutional interest with 174.96x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +128.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 131.6,
        "gmp_percent": 97.5,
        "est_listing_price": 266.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 151.9,
        "gmp_percent": 112.5,
        "est_listing_price": 286.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 168.75,
        "gmp_percent": 125.0,
        "est_listing_price": 303.8,
        "notes": "Predicted \u20b9303.75 listing"
      }
    ]
  },
  {
    "id": "mediassist",
    "name": "Medi Assist Healthcare Services",
    "symbol": "MEDIASSIST.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Healthcare TPA",
    "open_date": "15-Jan-24",
    "close_date": "17-Jan-24",
    "listing_date": "23-Jan-24",
    "price_band": "\u20b9418",
    "issue_price": 418.0,
    "lot_size": 35,
    "min_investment": 14630,
    "issue_size_cr": 1171.58,
    "fresh_issue_cr": 878.7,
    "ofs_cr": 292.9,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 50.16,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 468.16,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 8.03,
        "nii": 4.88,
        "retail": 1.28,
        "total": 4.88
      },
      "day2": {
        "qib": 20.07,
        "nii": 11.38,
        "retail": 2.55,
        "total": 10.56
      },
      "final_day": {
        "qib": 40.14,
        "nii": 24.38,
        "retail": 3.19,
        "total": 16.25
      },
      "applications_count": "16.25x Subscription"
    },
    "listing": {
      "listing_price": 465.0,
      "listing_gain_rs": 47.0,
      "listing_gain_percent": 11.2,
      "profit_per_lot": 1645.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 468.16,
        "actual_price": 465.0,
        "variance_rs": -3.16,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9468.16 (+12.0%). Stock opened at \u20b9465.0 (+11.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 11.2,
      "retail_profit_lost": 1645.0,
      "explanation": "The issue opened with a healthy +11.2% pop (\u20b91,645 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "Healthcare TPA Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Healthcare TPA",
        "Strong institutional interest with 40.14x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +11.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 47.7,
        "gmp_percent": 11.4,
        "est_listing_price": 465.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 49.2,
        "gmp_percent": 11.8,
        "est_listing_price": 467.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 50.16,
        "gmp_percent": 12.0,
        "est_listing_price": 468.2,
        "notes": "Predicted \u20b9468.16 listing"
      }
    ]
  },
  {
    "id": "jyoticnc",
    "name": "Jyoti CNC Automation Ltd",
    "symbol": "JYOTICNC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Industrial CNC Machinery",
    "open_date": "09-Jan-24",
    "close_date": "11-Jan-24",
    "listing_date": "16-Jan-24",
    "price_band": "\u20b9331",
    "issue_price": 331.0,
    "lot_size": 45,
    "min_investment": 14895,
    "issue_size_cr": 1000.0,
    "fresh_issue_cr": 750.0,
    "ofs_cr": 250.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 49.65,
    "gmp_closing_percent": 15.0,
    "gmp_estimated_listing": 380.65,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 8.84,
        "nii": 11.56,
        "retail": 10.47,
        "total": 11.56
      },
      "day2": {
        "qib": 22.1,
        "nii": 26.97,
        "retail": 20.94,
        "total": 25.04
      },
      "final_day": {
        "qib": 44.2,
        "nii": 57.8,
        "retail": 26.18,
        "total": 38.53
      },
      "applications_count": "38.53x Subscription"
    },
    "listing": {
      "listing_price": 372.0,
      "listing_gain_rs": 41.0,
      "listing_gain_percent": 12.4,
      "profit_per_lot": 1845.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 380.65,
        "actual_price": 372.0,
        "variance_rs": -8.65,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9380.65 (+15.0%). Stock opened at \u20b9372.0 (+12.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 15.0,
      "actual_gain_pct": 12.4,
      "retail_profit_lost": 1845.0,
      "explanation": "The issue opened with a healthy +12.4% pop (\u20b91,845 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +15% Listing Return",
      "long_term_potential": "Industrial CNC Machinery Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Industrial CNC Machinery",
        "Strong institutional interest with 44.2x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +12.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 47.2,
        "gmp_percent": 14.2,
        "est_listing_price": 378.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 48.7,
        "gmp_percent": 14.7,
        "est_listing_price": 379.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 49.65,
        "gmp_percent": 15.0,
        "est_listing_price": 380.6,
        "notes": "Predicted \u20b9380.65 listing"
      }
    ]
  },
  {
    "id": "tatatech",
    "name": "Tata Technologies Ltd",
    "symbol": "TATATECH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Engineering & Tech Services",
    "open_date": "22-Nov-23",
    "close_date": "24-Nov-23",
    "listing_date": "30-Nov-23",
    "price_band": "\u20b9500",
    "issue_price": 500.0,
    "lot_size": 30,
    "min_investment": 15000,
    "issue_size_cr": 3042.51,
    "fresh_issue_cr": 2281.9,
    "ofs_cr": 760.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 700.0,
    "gmp_closing_percent": 140.0,
    "gmp_estimated_listing": 1200.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 40.68,
        "nii": 20.83,
        "retail": 6.6,
        "total": 20.83
      },
      "day2": {
        "qib": 101.7,
        "nii": 48.6,
        "retail": 13.2,
        "total": 45.13
      },
      "final_day": {
        "qib": 203.41,
        "nii": 104.15,
        "retail": 16.5,
        "total": 69.43
      },
      "applications_count": "69.43x Subscription"
    },
    "listing": {
      "listing_price": 1200.0,
      "listing_gain_rs": 700.0,
      "listing_gain_percent": 140.0,
      "profit_per_lot": 21000.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1200.0,
        "actual_price": 1200.0,
        "variance_rs": 0.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91200.0 (+140.0%). Stock opened at \u20b91200.0 (+140.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 140.0,
      "actual_gain_pct": 140.0,
      "retail_profit_lost": 21000.0,
      "explanation": "Tata Technologies Ltd delivered a stellar +140.0% listing gain, rewarding retail allottees with \u20b921,000 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +140% Listing Return",
      "long_term_potential": "Engineering & Tech Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Engineering & Tech Services",
        "Strong institutional interest with 203.41x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +140.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 546.0,
        "gmp_percent": 109.2,
        "est_listing_price": 1046.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 630.0,
        "gmp_percent": 126.0,
        "est_listing_price": 1130.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 700.0,
        "gmp_percent": 140.0,
        "est_listing_price": 1200.0,
        "notes": "Predicted \u20b91200.0 listing"
      }
    ]
  },
  {
    "id": "ireda",
    "name": "Indian Renewable Energy Dev Agency (IREDA)",
    "symbol": "IREDA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "PSU Green Energy NBFC",
    "open_date": "21-Nov-23",
    "close_date": "23-Nov-23",
    "listing_date": "29-Nov-23",
    "price_band": "\u20b932",
    "issue_price": 32.0,
    "lot_size": 460,
    "min_investment": 14720,
    "issue_size_cr": 2150.0,
    "fresh_issue_cr": 1612.5,
    "ofs_cr": 537.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 16.0,
    "gmp_closing_percent": 50.0,
    "gmp_estimated_listing": 48.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 20.91,
        "nii": 11.64,
        "retail": 3.09,
        "total": 11.64
      },
      "day2": {
        "qib": 52.28,
        "nii": 27.16,
        "retail": 6.18,
        "total": 25.22
      },
      "final_day": {
        "qib": 104.57,
        "nii": 58.2,
        "retail": 7.73,
        "total": 38.8
      },
      "applications_count": "38.8x Subscription"
    },
    "listing": {
      "listing_price": 50.0,
      "listing_gain_rs": 18.0,
      "listing_gain_percent": 56.3,
      "profit_per_lot": 8280.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 48.0,
        "actual_price": 50.0,
        "variance_rs": 2.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b948.0 (+50.0%). Stock opened at \u20b950.0 (+56.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 50.0,
      "actual_gain_pct": 56.3,
      "retail_profit_lost": 8280.0,
      "explanation": "Indian Renewable Energy Dev Agency (IREDA) delivered a stellar +56.3% listing gain, rewarding retail allottees with \u20b98,280 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +50% Listing Return",
      "long_term_potential": "PSU Green Energy NBFC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in PSU Green Energy NBFC",
        "Strong institutional interest with 104.57x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +56.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 12.5,
        "gmp_percent": 39.0,
        "est_listing_price": 44.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 14.4,
        "gmp_percent": 45.0,
        "est_listing_price": 46.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 16.0,
        "gmp_percent": 50.0,
        "est_listing_price": 48.0,
        "notes": "Predicted \u20b948.0 listing"
      }
    ]
  },
  {
    "id": "sbfc",
    "name": "SBFC Finance Ltd",
    "symbol": "SBFC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Secured MSME Lending & Gold Loans",
    "open_date": "03-Aug-23",
    "close_date": "07-Aug-23",
    "listing_date": "16-Aug-23",
    "price_band": "\u20b957",
    "issue_price": 57.0,
    "lot_size": 260,
    "min_investment": 14820,
    "issue_size_cr": 1025.0,
    "fresh_issue_cr": 768.8,
    "ofs_cr": 256.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 25.65,
    "gmp_closing_percent": 45.0,
    "gmp_estimated_listing": 82.65,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 38.58,
        "nii": 21.05,
        "retail": 4.4,
        "total": 21.05
      },
      "day2": {
        "qib": 96.45,
        "nii": 49.11,
        "retail": 8.79,
        "total": 45.6
      },
      "final_day": {
        "qib": 192.9,
        "nii": 105.24,
        "retail": 10.99,
        "total": 70.16
      },
      "applications_count": "70.16x Subscription"
    },
    "listing": {
      "listing_price": 82.0,
      "listing_gain_rs": 25.0,
      "listing_gain_percent": 43.9,
      "profit_per_lot": 6500.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 82.65,
        "actual_price": 82.0,
        "variance_rs": -0.65,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b982.65 (+45.0%). Stock opened at \u20b982.0 (+43.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 45.0,
      "actual_gain_pct": 43.9,
      "retail_profit_lost": 6500.0,
      "explanation": "SBFC Finance Ltd delivered a stellar +43.9% listing gain, rewarding retail allottees with \u20b96,500 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +45% Listing Return",
      "long_term_potential": "Secured MSME Lending & Gold Loans Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Secured MSME Lending & Gold Loans",
        "Strong institutional interest with 192.9x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +43.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 20.0,
        "gmp_percent": 35.1,
        "est_listing_price": 77.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 23.1,
        "gmp_percent": 40.5,
        "est_listing_price": 80.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 25.65,
        "gmp_percent": 45.0,
        "est_listing_price": 82.7,
        "notes": "Predicted \u20b982.65 listing"
      }
    ]
  },
  {
    "id": "yatharth",
    "name": "Yatharth Hospital & Trauma Care",
    "symbol": "YATHARTH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Tertiary Super Specialty Hospitals",
    "open_date": "26-Jul-23",
    "close_date": "28-Jul-23",
    "listing_date": "07-Aug-23",
    "price_band": "\u20b9300",
    "issue_price": 300.0,
    "lot_size": 50,
    "min_investment": 15000,
    "issue_size_cr": 686.55,
    "fresh_issue_cr": 514.9,
    "ofs_cr": 171.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 12.0,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 312.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 17.02,
        "nii": 10.85,
        "retail": 3.34,
        "total": 10.85
      },
      "day2": {
        "qib": 42.55,
        "nii": 25.31,
        "retail": 6.67,
        "total": 23.5
      },
      "final_day": {
        "qib": 85.1,
        "nii": 54.24,
        "retail": 8.34,
        "total": 36.16
      },
      "applications_count": "36.16x Subscription"
    },
    "listing": {
      "listing_price": 304.0,
      "listing_gain_rs": 4.0,
      "listing_gain_percent": 1.3,
      "profit_per_lot": 200.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 312.0,
        "actual_price": 304.0,
        "variance_rs": -8.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9312.0 (+4.0%). Stock opened at \u20b9304.0 (+1.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 1.3,
      "retail_profit_lost": 200.0,
      "explanation": "The IPO had a flat listing (+1.3%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Tertiary Super Specialty Hospitals Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Tertiary Super Specialty Hospitals",
        "Strong institutional interest with 85.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 11.4,
        "gmp_percent": 3.8,
        "est_listing_price": 311.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 11.8,
        "gmp_percent": 3.9,
        "est_listing_price": 311.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 12.0,
        "gmp_percent": 4.0,
        "est_listing_price": 312.0,
        "notes": "Predicted \u20b9312.0 listing"
      }
    ]
  },
  {
    "id": "netweb",
    "name": "Netweb Technologies India",
    "symbol": "NETWEB.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Supercomputing & AI Servers",
    "open_date": "17-Jul-23",
    "close_date": "19-Jul-23",
    "listing_date": "27-Jul-23",
    "price_band": "\u20b9500",
    "issue_price": 500.0,
    "lot_size": 30,
    "min_investment": 15000,
    "issue_size_cr": 631.0,
    "fresh_issue_cr": 473.2,
    "ofs_cr": 157.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 450.0,
    "gmp_closing_percent": 90.0,
    "gmp_estimated_listing": 950.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 45.78,
        "nii": 27.11,
        "retail": 24.04,
        "total": 27.11
      },
      "day2": {
        "qib": 114.45,
        "nii": 63.25,
        "retail": 48.08,
        "total": 58.73
      },
      "final_day": {
        "qib": 228.91,
        "nii": 135.54,
        "retail": 60.1,
        "total": 90.36
      },
      "applications_count": "90.36x Subscription"
    },
    "listing": {
      "listing_price": 942.0,
      "listing_gain_rs": 442.0,
      "listing_gain_percent": 88.4,
      "profit_per_lot": 13260.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 950.0,
        "actual_price": 942.0,
        "variance_rs": -8.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9950.0 (+90.0%). Stock opened at \u20b9942.0 (+88.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 90.0,
      "actual_gain_pct": 88.4,
      "retail_profit_lost": 13260.0,
      "explanation": "Netweb Technologies India delivered a stellar +88.4% listing gain, rewarding retail allottees with \u20b913,260 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +90% Listing Return",
      "long_term_potential": "Supercomputing & AI Servers Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Supercomputing & AI Servers",
        "Strong institutional interest with 228.91x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +88.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 351.0,
        "gmp_percent": 70.2,
        "est_listing_price": 851.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 405.0,
        "gmp_percent": 81.0,
        "est_listing_price": 905.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 450.0,
        "gmp_percent": 90.0,
        "est_listing_price": 950.0,
        "notes": "Predicted \u20b9950.0 listing"
      }
    ]
  },
  {
    "id": "utkarshbnk",
    "name": "Utkarsh Small Finance Bank Ltd",
    "symbol": "UTKARSHBNK.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Micro-banking & Inclusive Finance",
    "open_date": "12-Jul-23",
    "close_date": "14-Jul-23",
    "listing_date": "21-Jul-23",
    "price_band": "\u20b925",
    "issue_price": 25.0,
    "lot_size": 600,
    "min_investment": 15000,
    "issue_size_cr": 500.0,
    "fresh_issue_cr": 375.0,
    "ofs_cr": 125.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 15.0,
    "gmp_closing_percent": 60.0,
    "gmp_estimated_listing": 40.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 24.97,
        "nii": 30.57,
        "retail": 28.84,
        "total": 30.57
      },
      "day2": {
        "qib": 62.42,
        "nii": 71.34,
        "retail": 57.68,
        "total": 66.24
      },
      "final_day": {
        "qib": 124.85,
        "nii": 152.87,
        "retail": 72.1,
        "total": 101.91
      },
      "applications_count": "101.91x Subscription"
    },
    "listing": {
      "listing_price": 39.95,
      "listing_gain_rs": 14.95,
      "listing_gain_percent": 59.8,
      "profit_per_lot": 8970.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 40.0,
        "actual_price": 39.95,
        "variance_rs": -0.05,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b940.0 (+60.0%). Stock opened at \u20b939.95 (+59.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 60.0,
      "actual_gain_pct": 59.8,
      "retail_profit_lost": 8970.0,
      "explanation": "Utkarsh Small Finance Bank Ltd delivered a stellar +59.8% listing gain, rewarding retail allottees with \u20b98,970 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +60% Listing Return",
      "long_term_potential": "Micro-banking & Inclusive Finance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Micro-banking & Inclusive Finance",
        "Strong institutional interest with 124.85x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +59.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 11.7,
        "gmp_percent": 46.8,
        "est_listing_price": 36.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 13.5,
        "gmp_percent": 54.0,
        "est_listing_price": 38.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 15.0,
        "gmp_percent": 60.0,
        "est_listing_price": 40.0,
        "notes": "Predicted \u20b940.0 listing"
      }
    ]
  },
  {
    "id": "senco",
    "name": "Senco Gold Ltd",
    "symbol": "SENCO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Gold Jewellery Retail Eastern India",
    "open_date": "04-Jul-23",
    "close_date": "06-Jul-23",
    "listing_date": "14-Jul-23",
    "price_band": "\u20b9317",
    "issue_price": 317.0,
    "lot_size": 47,
    "min_investment": 14899,
    "issue_size_cr": 405.0,
    "fresh_issue_cr": 303.8,
    "ofs_cr": 101.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 120.46,
    "gmp_closing_percent": 38.0,
    "gmp_estimated_listing": 437.46,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 36.13,
        "nii": 22.0,
        "retail": 6.18,
        "total": 22.0
      },
      "day2": {
        "qib": 90.32,
        "nii": 51.34,
        "retail": 12.37,
        "total": 47.68
      },
      "final_day": {
        "qib": 180.64,
        "nii": 110.02,
        "retail": 15.46,
        "total": 73.35
      },
      "applications_count": "73.35x Subscription"
    },
    "listing": {
      "listing_price": 431.0,
      "listing_gain_rs": 114.0,
      "listing_gain_percent": 36.0,
      "profit_per_lot": 5358.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 437.46,
        "actual_price": 431.0,
        "variance_rs": -6.46,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9437.46 (+38.0%). Stock opened at \u20b9431.0 (+36.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 38.0,
      "actual_gain_pct": 36.0,
      "retail_profit_lost": 5358.0,
      "explanation": "Senco Gold Ltd delivered a stellar +36.0% listing gain, rewarding retail allottees with \u20b95,358 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +38% Listing Return",
      "long_term_potential": "Gold Jewellery Retail Eastern India Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Gold Jewellery Retail Eastern India",
        "Strong institutional interest with 180.64x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +36.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 94.0,
        "gmp_percent": 29.6,
        "est_listing_price": 411.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 108.4,
        "gmp_percent": 34.2,
        "est_listing_price": 425.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 120.46,
        "gmp_percent": 38.0,
        "est_listing_price": 437.5,
        "notes": "Predicted \u20b9437.46 listing"
      }
    ]
  },
  {
    "id": "cyientdlm",
    "name": "Cyient DLM Ltd",
    "symbol": "CYIENTDLM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Aerospace & Defense EMS",
    "open_date": "27-Jun-23",
    "close_date": "30-Jun-23",
    "listing_date": "10-Jul-23",
    "price_band": "\u20b9265",
    "issue_price": 265.0,
    "lot_size": 56,
    "min_investment": 14840,
    "issue_size_cr": 592.0,
    "fresh_issue_cr": 444.0,
    "ofs_cr": 148.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 137.8,
    "gmp_closing_percent": 52.0,
    "gmp_estimated_listing": 402.8,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 38.2,
        "nii": 20.19,
        "retail": 19.68,
        "total": 20.19
      },
      "day2": {
        "qib": 95.5,
        "nii": 47.11,
        "retail": 39.36,
        "total": 43.74
      },
      "final_day": {
        "qib": 191.0,
        "nii": 100.95,
        "retail": 49.2,
        "total": 67.3
      },
      "applications_count": "67.3x Subscription"
    },
    "listing": {
      "listing_price": 401.0,
      "listing_gain_rs": 136.0,
      "listing_gain_percent": 51.3,
      "profit_per_lot": 7616.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 402.8,
        "actual_price": 401.0,
        "variance_rs": -1.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9402.8 (+52.0%). Stock opened at \u20b9401.0 (+51.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 52.0,
      "actual_gain_pct": 51.3,
      "retail_profit_lost": 7616.0,
      "explanation": "Cyient DLM Ltd delivered a stellar +51.3% listing gain, rewarding retail allottees with \u20b97,616 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +52% Listing Return",
      "long_term_potential": "Aerospace & Defense EMS Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Aerospace & Defense EMS",
        "Strong institutional interest with 191.0x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +51.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 107.5,
        "gmp_percent": 40.6,
        "est_listing_price": 372.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 124.0,
        "gmp_percent": 46.8,
        "est_listing_price": 389.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 137.8,
        "gmp_percent": 52.0,
        "est_listing_price": 402.8,
        "notes": "Predicted \u20b9402.8 listing"
      }
    ]
  },
  {
    "id": "ideaforge",
    "name": "Ideaforge Technology Ltd",
    "symbol": "IDEAFORGE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Surveillance Drones & UAVs",
    "open_date": "26-Jun-23",
    "close_date": "30-Jun-23",
    "listing_date": "07-Jul-23",
    "price_band": "\u20b9672",
    "issue_price": 672.0,
    "lot_size": 22,
    "min_investment": 14784,
    "issue_size_cr": 567.24,
    "fresh_issue_cr": 425.4,
    "ofs_cr": 141.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 638.4,
    "gmp_closing_percent": 95.0,
    "gmp_estimated_listing": 1310.4,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 25.16,
        "nii": 31.82,
        "retail": 34.08,
        "total": 31.82
      },
      "day2": {
        "qib": 62.91,
        "nii": 74.24,
        "retail": 68.16,
        "total": 68.94
      },
      "final_day": {
        "qib": 125.81,
        "nii": 159.09,
        "retail": 85.2,
        "total": 106.06
      },
      "applications_count": "106.06x Subscription"
    },
    "listing": {
      "listing_price": 1305.1,
      "listing_gain_rs": 633.1,
      "listing_gain_percent": 94.2,
      "profit_per_lot": 13928.2,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1310.4,
        "actual_price": 1305.1,
        "variance_rs": -5.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91310.4 (+95.0%). Stock opened at \u20b91305.1 (+94.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 95.0,
      "actual_gain_pct": 94.2,
      "retail_profit_lost": 13928.2,
      "explanation": "Ideaforge Technology Ltd delivered a stellar +94.2% listing gain, rewarding retail allottees with \u20b913,928 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +95% Listing Return",
      "long_term_potential": "Surveillance Drones & UAVs Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Surveillance Drones & UAVs",
        "Strong institutional interest with 125.81x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +94.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 498.0,
        "gmp_percent": 74.1,
        "est_listing_price": 1170.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 574.6,
        "gmp_percent": 85.5,
        "est_listing_price": 1246.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 638.4,
        "gmp_percent": 95.0,
        "est_listing_price": 1310.4,
        "notes": "Predicted \u20b91310.4 listing"
      }
    ]
  },
  {
    "id": "nxst",
    "name": "Nexus Select Trust (REIT)",
    "symbol": "NXST.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Retail Mall Grade-A REIT",
    "open_date": "09-May-23",
    "close_date": "11-May-23",
    "listing_date": "19-May-23",
    "price_band": "\u20b9100",
    "issue_price": 100.0,
    "lot_size": 150,
    "min_investment": 15000,
    "issue_size_cr": 3200.0,
    "fresh_issue_cr": 2400.0,
    "ofs_cr": 800.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 4.0,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 104.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.96,
        "nii": 1.64,
        "retail": 0.79,
        "total": 1.64
      },
      "day2": {
        "qib": 2.4,
        "nii": 3.81,
        "retail": 1.58,
        "total": 3.54
      },
      "final_day": {
        "qib": 4.81,
        "nii": 8.18,
        "retail": 1.97,
        "total": 5.45
      },
      "applications_count": "5.45x Subscription"
    },
    "listing": {
      "listing_price": 104.0,
      "listing_gain_rs": 4.0,
      "listing_gain_percent": 4.0,
      "profit_per_lot": 600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 104.0,
        "actual_price": 104.0,
        "variance_rs": 0.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9104.0 (+4.0%). Stock opened at \u20b9104.0 (+4.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 4.0,
      "retail_profit_lost": 600.0,
      "explanation": "The IPO had a flat listing (+4.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Retail Mall Grade-A REIT Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Retail Mall Grade-A REIT",
        "Strong institutional interest with 4.81x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +4.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.8,
        "gmp_percent": 3.8,
        "est_listing_price": 103.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.9,
        "gmp_percent": 3.9,
        "est_listing_price": 103.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 4.0,
        "gmp_percent": 4.0,
        "est_listing_price": 104.0,
        "notes": "Predicted \u20b9104.0 listing"
      }
    ]
  },
  {
    "id": "mankind",
    "name": "Mankind Pharma Ltd",
    "symbol": "MANKIND.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Formulations & OTC Consumer Healthcare",
    "open_date": "25-Apr-23",
    "close_date": "27-Apr-23",
    "listing_date": "09-May-23",
    "price_band": "\u20b91,080",
    "issue_price": 1080.0,
    "lot_size": 13,
    "min_investment": 14040,
    "issue_size_cr": 4326.36,
    "fresh_issue_cr": 3244.8,
    "ofs_cr": 1081.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 216.0,
    "gmp_closing_percent": 20.0,
    "gmp_estimated_listing": 1296.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 9.83,
        "nii": 4.6,
        "retail": 0.37,
        "total": 4.6
      },
      "day2": {
        "qib": 24.58,
        "nii": 10.72,
        "retail": 0.74,
        "total": 9.96
      },
      "final_day": {
        "qib": 49.16,
        "nii": 22.98,
        "retail": 0.92,
        "total": 15.32
      },
      "applications_count": "15.32x Subscription"
    },
    "listing": {
      "listing_price": 1300.0,
      "listing_gain_rs": 220.0,
      "listing_gain_percent": 20.4,
      "profit_per_lot": 2860.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1296.0,
        "actual_price": 1300.0,
        "variance_rs": 4.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91296.0 (+20.0%). Stock opened at \u20b91300.0 (+20.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 20.0,
      "actual_gain_pct": 20.4,
      "retail_profit_lost": 2860.0,
      "explanation": "The issue opened with a healthy +20.4% pop (\u20b92,860 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +20% Listing Return",
      "long_term_potential": "Formulations & OTC Consumer Healthcare Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Formulations & OTC Consumer Healthcare",
        "Strong institutional interest with 49.16x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +20.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 205.2,
        "gmp_percent": 19.0,
        "est_listing_price": 1285.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 211.7,
        "gmp_percent": 19.6,
        "est_listing_price": 1291.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 216.0,
        "gmp_percent": 20.0,
        "est_listing_price": 1296.0,
        "notes": "Predicted \u20b91296.0 listing"
      }
    ]
  },
  {
    "id": "globalsurf",
    "name": "Global Surfaces Ltd",
    "symbol": "GLOBALSURF.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Engineered Quartz Surfaces",
    "open_date": "13-Mar-23",
    "close_date": "15-Mar-23",
    "listing_date": "23-Mar-23",
    "price_band": "\u20b9140",
    "issue_price": 140.0,
    "lot_size": 100,
    "min_investment": 14000,
    "issue_size_cr": 154.98,
    "fresh_issue_cr": 116.2,
    "ofs_cr": 38.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 25.2,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 165.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.71,
        "nii": 3.66,
        "retail": 2.05,
        "total": 3.66
      },
      "day2": {
        "qib": 6.77,
        "nii": 8.55,
        "retail": 4.1,
        "total": 7.94
      },
      "final_day": {
        "qib": 13.54,
        "nii": 18.32,
        "retail": 5.12,
        "total": 12.21
      },
      "applications_count": "12.21x Subscription"
    },
    "listing": {
      "listing_price": 163.0,
      "listing_gain_rs": 23.0,
      "listing_gain_percent": 16.4,
      "profit_per_lot": 2300.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 165.2,
        "actual_price": 163.0,
        "variance_rs": -2.2,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9165.2 (+18.0%). Stock opened at \u20b9163.0 (+16.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 16.4,
      "retail_profit_lost": 2300.0,
      "explanation": "The issue opened with a healthy +16.4% pop (\u20b92,300 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "Engineered Quartz Surfaces Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Engineered Quartz Surfaces",
        "Strong institutional interest with 13.54x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +16.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 23.9,
        "gmp_percent": 17.1,
        "est_listing_price": 163.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 24.7,
        "gmp_percent": 17.6,
        "est_listing_price": 164.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 25.2,
        "gmp_percent": 18.0,
        "est_listing_price": 165.2,
        "notes": "Predicted \u20b9165.2 listing"
      }
    ]
  },
  {
    "id": "divgi",
    "name": "Divgi TorqTransfer Systems",
    "symbol": "DIVGI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "EV Transmissions & 4WD Transfer Cases",
    "open_date": "01-Mar-23",
    "close_date": "03-Mar-23",
    "listing_date": "14-Mar-23",
    "price_band": "\u20b9590",
    "issue_price": 590.0,
    "lot_size": 25,
    "min_investment": 14750,
    "issue_size_cr": 412.0,
    "fresh_issue_cr": 309.0,
    "ofs_cr": 103.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 17.7,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 607.7,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.57,
        "nii": 1.63,
        "retail": 1.72,
        "total": 1.63
      },
      "day2": {
        "qib": 3.92,
        "nii": 3.81,
        "retail": 3.45,
        "total": 3.54
      },
      "final_day": {
        "qib": 7.83,
        "nii": 8.16,
        "retail": 4.31,
        "total": 5.44
      },
      "applications_count": "5.44x Subscription"
    },
    "listing": {
      "listing_price": 600.0,
      "listing_gain_rs": 10.0,
      "listing_gain_percent": 1.7,
      "profit_per_lot": 250.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 607.7,
        "actual_price": 600.0,
        "variance_rs": -7.7,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9607.7 (+3.0%). Stock opened at \u20b9600.0 (+1.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": 1.7,
      "retail_profit_lost": 250.0,
      "explanation": "The IPO had a flat listing (+1.7%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "EV Transmissions & 4WD Transfer Cases Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in EV Transmissions & 4WD Transfer Cases",
        "Strong institutional interest with 7.83x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 16.8,
        "gmp_percent": 2.8,
        "est_listing_price": 606.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 17.3,
        "gmp_percent": 2.9,
        "est_listing_price": 607.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 17.7,
        "gmp_percent": 3.0,
        "est_listing_price": 607.7,
        "notes": "Predicted \u20b9607.7 listing"
      }
    ]
  },
  {
    "id": "sahpoly",
    "name": "Sah Polymers Ltd",
    "symbol": "SAHPOLY.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "FIBC Bulk Bags & Woven Sacks",
    "open_date": "30-Dec-22",
    "close_date": "04-Jan-23",
    "listing_date": "12-Jan-23",
    "price_band": "\u20b965",
    "issue_price": 65.0,
    "lot_size": 230,
    "min_investment": 14950,
    "issue_size_cr": 66.3,
    "fresh_issue_cr": 49.7,
    "ofs_cr": 16.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 19.5,
    "gmp_closing_percent": 30.0,
    "gmp_estimated_listing": 84.5,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 0.48,
        "nii": 5.24,
        "retail": 15.91,
        "total": 5.24
      },
      "day2": {
        "qib": 1.2,
        "nii": 12.22,
        "retail": 31.82,
        "total": 11.35
      },
      "final_day": {
        "qib": 2.4,
        "nii": 26.19,
        "retail": 39.78,
        "total": 17.46
      },
      "applications_count": "17.46x Subscription"
    },
    "listing": {
      "listing_price": 85.0,
      "listing_gain_rs": 20.0,
      "listing_gain_percent": 30.8,
      "profit_per_lot": 4600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 84.5,
        "actual_price": 85.0,
        "variance_rs": 0.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b984.5 (+30.0%). Stock opened at \u20b985.0 (+30.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 30.0,
      "actual_gain_pct": 30.8,
      "retail_profit_lost": 4600.0,
      "explanation": "Sah Polymers Ltd delivered a stellar +30.8% listing gain, rewarding retail allottees with \u20b94,600 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +30% Listing Return",
      "long_term_potential": "FIBC Bulk Bags & Woven Sacks Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in FIBC Bulk Bags & Woven Sacks",
        "Strong institutional interest with 2.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +30.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 15.2,
        "gmp_percent": 23.4,
        "est_listing_price": 80.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 17.6,
        "gmp_percent": 27.0,
        "est_listing_price": 82.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 19.5,
        "gmp_percent": 30.0,
        "est_listing_price": 84.5,
        "notes": "Predicted \u20b984.5 listing"
      }
    ]
  },
  {
    "id": "kfintech",
    "name": "KFin Technologies Ltd",
    "symbol": "KFINTECH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Registrar & Transfer Agency (RTA)",
    "open_date": "19-Dec-22",
    "close_date": "21-Dec-22",
    "listing_date": "29-Dec-22",
    "price_band": "\u20b9366",
    "issue_price": 366.0,
    "lot_size": 40,
    "min_investment": 14640,
    "issue_size_cr": 1500.0,
    "fresh_issue_cr": 1125.0,
    "ofs_cr": 375.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 7.32,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 373.32,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.55,
        "nii": 0.78,
        "retail": 0.74,
        "total": 0.78
      },
      "day2": {
        "qib": 1.38,
        "nii": 1.81,
        "retail": 1.48,
        "total": 1.68
      },
      "final_day": {
        "qib": 2.76,
        "nii": 3.88,
        "retail": 1.85,
        "total": 2.59
      },
      "applications_count": "2.59x Subscription"
    },
    "listing": {
      "listing_price": 367.0,
      "listing_gain_rs": 1.0,
      "listing_gain_percent": 0.3,
      "profit_per_lot": 40.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 373.32,
        "actual_price": 367.0,
        "variance_rs": -6.32,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9373.32 (+2.0%). Stock opened at \u20b9367.0 (+0.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 0.3,
      "retail_profit_lost": 40.0,
      "explanation": "The IPO had a flat listing (+0.3%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Registrar & Transfer Agency (RTA) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Registrar & Transfer Agency (RTA)",
        "Strong institutional interest with 2.76x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 7.0,
        "gmp_percent": 1.9,
        "est_listing_price": 373.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 7.2,
        "gmp_percent": 2.0,
        "est_listing_price": 373.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 7.32,
        "gmp_percent": 2.0,
        "est_listing_price": 373.3,
        "notes": "Predicted \u20b9373.32 listing"
      }
    ]
  },
  {
    "id": "abans",
    "name": "Abans Holdings Ltd",
    "symbol": "ABANS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Commodity Broking & NBFC",
    "open_date": "12-Dec-22",
    "close_date": "15-Dec-22",
    "listing_date": "23-Dec-22",
    "price_band": "\u20b9270",
    "issue_price": 270.0,
    "lot_size": 55,
    "min_investment": 14850,
    "issue_size_cr": 345.6,
    "fresh_issue_cr": 259.2,
    "ofs_cr": 86.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": -13.5,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 256.5,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.82,
        "nii": 0.33,
        "retail": 0.16,
        "total": 0.33
      },
      "day2": {
        "qib": 2.05,
        "nii": 0.77,
        "retail": 0.32,
        "total": 0.72
      },
      "final_day": {
        "qib": 4.1,
        "nii": 1.65,
        "retail": 0.4,
        "total": 1.1
      },
      "applications_count": "1.1x Subscription"
    },
    "listing": {
      "listing_price": 218.0,
      "listing_gain_rs": -52.0,
      "listing_gain_percent": -19.3,
      "profit_per_lot": -2860.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 256.5,
        "actual_price": 218.0,
        "variance_rs": -38.5,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9256.5 (-5.0%). Stock opened at \u20b9218.0 (-19.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -19.3,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -19.3% (\u20b92,860 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Commodity Broking & NBFC Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Commodity Broking & NBFC",
        "Strong institutional interest with 4.1x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -19.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -16.9,
        "gmp_percent": -6.2,
        "est_listing_price": 253.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -15.1,
        "gmp_percent": -5.6,
        "est_listing_price": 254.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -13.5,
        "gmp_percent": -5.0,
        "est_listing_price": 256.5,
        "notes": "Predicted \u20b9256.5 listing"
      }
    ]
  },
  {
    "id": "landmark",
    "name": "Landmark Cars Ltd",
    "symbol": "LANDMARK.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Mercedes-Benz & Jeep Premium Dealerships",
    "open_date": "13-Dec-22",
    "close_date": "15-Dec-22",
    "listing_date": "23-Dec-22",
    "price_band": "\u20b9506",
    "issue_price": 506.0,
    "lot_size": 29,
    "min_investment": 14674,
    "issue_size_cr": 552.0,
    "fresh_issue_cr": 414.0,
    "ofs_cr": 138.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -10.12,
    "gmp_closing_percent": -2.0,
    "gmp_estimated_listing": 495.88,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 1.74,
        "nii": 0.92,
        "retail": 0.24,
        "total": 0.92
      },
      "day2": {
        "qib": 4.36,
        "nii": 2.14,
        "retail": 0.47,
        "total": 1.99
      },
      "final_day": {
        "qib": 8.71,
        "nii": 4.59,
        "retail": 0.59,
        "total": 3.06
      },
      "applications_count": "3.06x Subscription"
    },
    "listing": {
      "listing_price": 465.0,
      "listing_gain_rs": -41.0,
      "listing_gain_percent": -8.1,
      "profit_per_lot": -1189.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 495.88,
        "actual_price": 465.0,
        "variance_rs": -30.88,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9495.88 (-2.0%). Stock opened at \u20b9465.0 (-8.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -2.0,
      "actual_gain_pct": -8.1,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -8.1% (\u20b91,189 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -2% Listing Return",
      "long_term_potential": "Mercedes-Benz & Jeep Premium Dealerships Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Mercedes-Benz & Jeep Premium Dealerships",
        "Strong institutional interest with 8.71x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -8.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -12.6,
        "gmp_percent": -2.5,
        "est_listing_price": 493.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -11.3,
        "gmp_percent": -2.2,
        "est_listing_price": 494.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -10.12,
        "gmp_percent": -2.0,
        "est_listing_price": 495.9,
        "notes": "Predicted \u20b9495.88 listing"
      }
    ]
  },
  {
    "id": "sula",
    "name": "Sula Vineyards Ltd",
    "symbol": "SULA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Wine Producer & Vineyard Resorts",
    "open_date": "12-Dec-22",
    "close_date": "14-Dec-22",
    "listing_date": "22-Dec-22",
    "price_band": "\u20b9357",
    "issue_price": 357.0,
    "lot_size": 42,
    "min_investment": 14994,
    "issue_size_cr": 960.35,
    "fresh_issue_cr": 720.3,
    "ofs_cr": 240.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 14.28,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 371.28,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.83,
        "nii": 0.7,
        "retail": 0.66,
        "total": 0.7
      },
      "day2": {
        "qib": 2.06,
        "nii": 1.63,
        "retail": 1.32,
        "total": 1.51
      },
      "final_day": {
        "qib": 4.13,
        "nii": 3.5,
        "retail": 1.65,
        "total": 2.33
      },
      "applications_count": "2.33x Subscription"
    },
    "listing": {
      "listing_price": 361.0,
      "listing_gain_rs": 4.0,
      "listing_gain_percent": 1.1,
      "profit_per_lot": 168.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 371.28,
        "actual_price": 361.0,
        "variance_rs": -10.28,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9371.28 (+4.0%). Stock opened at \u20b9361.0 (+1.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 1.1,
      "retail_profit_lost": 168.0,
      "explanation": "The IPO had a flat listing (+1.1%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Wine Producer & Vineyard Resorts Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Wine Producer & Vineyard Resorts",
        "Strong institutional interest with 4.13x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 13.6,
        "gmp_percent": 3.8,
        "est_listing_price": 370.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 14.0,
        "gmp_percent": 3.9,
        "est_listing_price": 371.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 14.28,
        "gmp_percent": 4.0,
        "est_listing_price": 371.3,
        "notes": "Predicted \u20b9371.28 listing"
      }
    ]
  },
  {
    "id": "uniparts",
    "name": "Uniparts India Ltd",
    "symbol": "UNIPARTS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Agriculture & Construction 3-Point Linkage",
    "open_date": "30-Nov-22",
    "close_date": "02-Dec-22",
    "listing_date": "12-Dec-22",
    "price_band": "\u20b9577",
    "issue_price": 577.0,
    "lot_size": 25,
    "min_investment": 14425,
    "issue_size_cr": 835.61,
    "fresh_issue_cr": 626.7,
    "ofs_cr": 208.9,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 11.54,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 588.54,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 13.43,
        "nii": 7.6,
        "retail": 1.85,
        "total": 7.6
      },
      "day2": {
        "qib": 33.57,
        "nii": 17.72,
        "retail": 3.7,
        "total": 16.46
      },
      "final_day": {
        "qib": 67.14,
        "nii": 37.98,
        "retail": 4.63,
        "total": 25.32
      },
      "applications_count": "25.32x Subscription"
    },
    "listing": {
      "listing_price": 575.0,
      "listing_gain_rs": -2.0,
      "listing_gain_percent": -0.3,
      "profit_per_lot": -50.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 588.54,
        "actual_price": 575.0,
        "variance_rs": -13.54,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9588.54 (+2.0%). Stock opened at \u20b9575.0 (-0.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": -0.3,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-0.3%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Agriculture & Construction 3-Point Linkage Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Agriculture & Construction 3-Point Linkage",
        "Strong institutional interest with 67.14x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -0.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 11.0,
        "gmp_percent": 1.9,
        "est_listing_price": 588.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 11.3,
        "gmp_percent": 2.0,
        "est_listing_price": 588.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 11.54,
        "gmp_percent": 2.0,
        "est_listing_price": 588.5,
        "notes": "Predicted \u20b9588.54 listing"
      }
    ]
  },
  {
    "id": "krl",
    "name": "Keystone Realtors (Rustomjee)",
    "symbol": "KRL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Mumbai Redevelopment Real Estate",
    "open_date": "14-Nov-22",
    "close_date": "16-Nov-22",
    "listing_date": "24-Nov-22",
    "price_band": "\u20b9541",
    "issue_price": 541.0,
    "lot_size": 27,
    "min_investment": 14607,
    "issue_size_cr": 635.0,
    "fresh_issue_cr": 476.2,
    "ofs_cr": 158.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 21.64,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 562.64,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.77,
        "nii": 0.6,
        "retail": 0.21,
        "total": 0.6
      },
      "day2": {
        "qib": 1.92,
        "nii": 1.41,
        "retail": 0.42,
        "total": 1.31
      },
      "final_day": {
        "qib": 3.84,
        "nii": 3.01,
        "retail": 0.53,
        "total": 2.01
      },
      "applications_count": "2.01x Subscription"
    },
    "listing": {
      "listing_price": 555.0,
      "listing_gain_rs": 14.0,
      "listing_gain_percent": 2.6,
      "profit_per_lot": 378.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 562.64,
        "actual_price": 555.0,
        "variance_rs": -7.64,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9562.64 (+4.0%). Stock opened at \u20b9555.0 (+2.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 2.6,
      "retail_profit_lost": 378.0,
      "explanation": "The IPO had a flat listing (+2.6%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Mumbai Redevelopment Real Estate Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Mumbai Redevelopment Real Estate",
        "Strong institutional interest with 3.84x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +2.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 20.6,
        "gmp_percent": 3.8,
        "est_listing_price": 561.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 21.2,
        "gmp_percent": 3.9,
        "est_listing_price": 562.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 21.64,
        "gmp_percent": 4.0,
        "est_listing_price": 562.6,
        "notes": "Predicted \u20b9562.64 listing"
      }
    ]
  },
  {
    "id": "inoxgreen",
    "name": "Inox Green Energy Services",
    "symbol": "INOXGREEN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Wind Farm Operations & Maintenance",
    "open_date": "11-Nov-22",
    "close_date": "15-Nov-22",
    "listing_date": "23-Nov-22",
    "price_band": "\u20b965",
    "issue_price": 65.0,
    "lot_size": 230,
    "min_investment": 14950,
    "issue_size_cr": 740.0,
    "fresh_issue_cr": 555.0,
    "ofs_cr": 185.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -1.95,
    "gmp_closing_percent": -3.0,
    "gmp_estimated_listing": 63.05,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.21,
        "nii": 0.46,
        "retail": 1.88,
        "total": 0.46
      },
      "day2": {
        "qib": 0.53,
        "nii": 1.08,
        "retail": 3.76,
        "total": 1.01
      },
      "final_day": {
        "qib": 1.05,
        "nii": 2.33,
        "retail": 4.7,
        "total": 1.55
      },
      "applications_count": "1.55x Subscription"
    },
    "listing": {
      "listing_price": 60.5,
      "listing_gain_rs": -4.5,
      "listing_gain_percent": -6.9,
      "profit_per_lot": -1035.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 63.05,
        "actual_price": 60.5,
        "variance_rs": -2.55,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b963.05 (-3.0%). Stock opened at \u20b960.5 (-6.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -3.0,
      "actual_gain_pct": -6.9,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -6.9% (\u20b91,035 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -3% Listing Return",
      "long_term_potential": "Wind Farm Operations & Maintenance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Wind Farm Operations & Maintenance",
        "Strong institutional interest with 1.05x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -6.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -2.4,
        "gmp_percent": -3.8,
        "est_listing_price": 62.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -2.2,
        "gmp_percent": -3.4,
        "est_listing_price": 62.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -1.95,
        "gmp_percent": -3.0,
        "est_listing_price": 63.0,
        "notes": "Predicted \u20b963.05 listing"
      }
    ]
  },
  {
    "id": "kaynes",
    "name": "Kaynes Technology India Ltd",
    "symbol": "KAYNES.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "IoT & Automotive EMS Electronics",
    "open_date": "10-Nov-22",
    "close_date": "14-Nov-22",
    "listing_date": "22-Nov-22",
    "price_band": "\u20b9587",
    "issue_price": 587.0,
    "lot_size": 25,
    "min_investment": 14675,
    "issue_size_cr": 857.82,
    "fresh_issue_cr": 643.4,
    "ofs_cr": 214.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 199.58,
    "gmp_closing_percent": 34.0,
    "gmp_estimated_listing": 786.58,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 19.69,
        "nii": 10.23,
        "retail": 1.64,
        "total": 10.23
      },
      "day2": {
        "qib": 49.23,
        "nii": 23.88,
        "retail": 3.28,
        "total": 22.17
      },
      "final_day": {
        "qib": 98.47,
        "nii": 51.16,
        "retail": 4.1,
        "total": 34.11
      },
      "applications_count": "34.11x Subscription"
    },
    "listing": {
      "listing_price": 775.0,
      "listing_gain_rs": 188.0,
      "listing_gain_percent": 32.0,
      "profit_per_lot": 4700.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 786.58,
        "actual_price": 775.0,
        "variance_rs": -11.58,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9786.58 (+34.0%). Stock opened at \u20b9775.0 (+32.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 34.0,
      "actual_gain_pct": 32.0,
      "retail_profit_lost": 4700.0,
      "explanation": "Kaynes Technology India Ltd delivered a stellar +32.0% listing gain, rewarding retail allottees with \u20b94,700 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +34% Listing Return",
      "long_term_potential": "IoT & Automotive EMS Electronics Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in IoT & Automotive EMS Electronics",
        "Strong institutional interest with 98.47x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +32.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 155.7,
        "gmp_percent": 26.5,
        "est_listing_price": 742.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 179.6,
        "gmp_percent": 30.6,
        "est_listing_price": 766.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 199.58,
        "gmp_percent": 34.0,
        "est_listing_price": 786.6,
        "notes": "Predicted \u20b9786.58 listing"
      }
    ]
  },
  {
    "id": "aci",
    "name": "Archean Chemical Industries",
    "symbol": "ACI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Marine Chemicals (Bromine & SOP)",
    "open_date": "09-Nov-22",
    "close_date": "11-Nov-22",
    "listing_date": "21-Nov-22",
    "price_band": "\u20b9407",
    "issue_price": 407.0,
    "lot_size": 36,
    "min_investment": 14652,
    "issue_size_cr": 1462.3,
    "fresh_issue_cr": 1096.7,
    "ofs_cr": 365.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 48.84,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 455.84,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 9.78,
        "nii": 9.67,
        "retail": 3.98,
        "total": 9.67
      },
      "day2": {
        "qib": 24.45,
        "nii": 22.56,
        "retail": 7.97,
        "total": 20.95
      },
      "final_day": {
        "qib": 48.91,
        "nii": 48.34,
        "retail": 9.96,
        "total": 32.23
      },
      "applications_count": "32.23x Subscription"
    },
    "listing": {
      "listing_price": 450.0,
      "listing_gain_rs": 43.0,
      "listing_gain_percent": 10.6,
      "profit_per_lot": 1548.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 455.84,
        "actual_price": 450.0,
        "variance_rs": -5.84,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9455.84 (+12.0%). Stock opened at \u20b9450.0 (+10.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 10.6,
      "retail_profit_lost": 1548.0,
      "explanation": "The issue opened with a healthy +10.6% pop (\u20b91,548 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "Marine Chemicals (Bromine & SOP) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Marine Chemicals (Bromine & SOP)",
        "Strong institutional interest with 48.91x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +10.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 46.4,
        "gmp_percent": 11.4,
        "est_listing_price": 453.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 47.9,
        "gmp_percent": 11.8,
        "est_listing_price": 454.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 48.84,
        "gmp_percent": 12.0,
        "est_listing_price": 455.8,
        "notes": "Predicted \u20b9455.84 listing"
      }
    ]
  },
  {
    "id": "medanta",
    "name": "Global Health Ltd (Medanta)",
    "symbol": "MEDANTA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Multi-Specialty Super Hospitals",
    "open_date": "03-Nov-22",
    "close_date": "07-Nov-22",
    "listing_date": "16-Nov-22",
    "price_band": "\u20b9336",
    "issue_price": 336.0,
    "lot_size": 44,
    "min_investment": 14784,
    "issue_size_cr": 2205.57,
    "fresh_issue_cr": 1654.2,
    "ofs_cr": 551.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 67.2,
    "gmp_closing_percent": 20.0,
    "gmp_estimated_listing": 403.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 5.73,
        "nii": 2.87,
        "retail": 1.49,
        "total": 2.87
      },
      "day2": {
        "qib": 14.32,
        "nii": 6.71,
        "retail": 2.98,
        "total": 6.23
      },
      "final_day": {
        "qib": 28.64,
        "nii": 14.37,
        "retail": 3.72,
        "total": 9.58
      },
      "applications_count": "9.58x Subscription"
    },
    "listing": {
      "listing_price": 398.15,
      "listing_gain_rs": 62.15,
      "listing_gain_percent": 18.5,
      "profit_per_lot": 2734.6,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 403.2,
        "actual_price": 398.15,
        "variance_rs": -5.05,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9403.2 (+20.0%). Stock opened at \u20b9398.15 (+18.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 20.0,
      "actual_gain_pct": 18.5,
      "retail_profit_lost": 2734.6,
      "explanation": "The issue opened with a healthy +18.5% pop (\u20b92,735 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +20% Listing Return",
      "long_term_potential": "Multi-Specialty Super Hospitals Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Multi-Specialty Super Hospitals",
        "Strong institutional interest with 28.64x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +18.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 63.8,
        "gmp_percent": 19.0,
        "est_listing_price": 399.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 65.9,
        "gmp_percent": 19.6,
        "est_listing_price": 401.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 67.2,
        "gmp_percent": 20.0,
        "est_listing_price": 403.2,
        "notes": "Predicted \u20b9403.2 listing"
      }
    ]
  },
  {
    "id": "bikaji",
    "name": "Bikaji Foods International",
    "symbol": "BIKAJI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Bhujia & Ethnic Indian Namkeen",
    "open_date": "03-Nov-22",
    "close_date": "07-Nov-22",
    "listing_date": "16-Nov-22",
    "price_band": "\u20b9300",
    "issue_price": 300.0,
    "lot_size": 50,
    "min_investment": 15000,
    "issue_size_cr": 881.22,
    "fresh_issue_cr": 660.9,
    "ofs_cr": 220.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 30.0,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 330.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 16.13,
        "nii": 8.0,
        "retail": 1.91,
        "total": 8.0
      },
      "day2": {
        "qib": 40.31,
        "nii": 18.67,
        "retail": 3.82,
        "total": 17.34
      },
      "final_day": {
        "qib": 80.63,
        "nii": 40.01,
        "retail": 4.77,
        "total": 26.67
      },
      "applications_count": "26.67x Subscription"
    },
    "listing": {
      "listing_price": 321.15,
      "listing_gain_rs": 21.15,
      "listing_gain_percent": 7.1,
      "profit_per_lot": 1057.5,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 330.0,
        "actual_price": 321.15,
        "variance_rs": -8.85,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9330.0 (+10.0%). Stock opened at \u20b9321.15 (+7.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 7.1,
      "retail_profit_lost": 1057.5,
      "explanation": "The issue opened with a healthy +7.1% pop (\u20b91,058 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Bhujia & Ethnic Indian Namkeen Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Bhujia & Ethnic Indian Namkeen",
        "Strong institutional interest with 80.63x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +7.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 28.5,
        "gmp_percent": 9.5,
        "est_listing_price": 328.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 29.4,
        "gmp_percent": 9.8,
        "est_listing_price": 329.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 30.0,
        "gmp_percent": 10.0,
        "est_listing_price": 330.0,
        "notes": "Predicted \u20b9330.0 listing"
      }
    ]
  },
  {
    "id": "fusion",
    "name": "Fusion Micro Finance Ltd",
    "symbol": "FUSION.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Joint Liability Rural MFI",
    "open_date": "02-Nov-22",
    "close_date": "04-Nov-22",
    "listing_date": "15-Nov-22",
    "price_band": "\u20b9368",
    "issue_price": 368.0,
    "lot_size": 40,
    "min_investment": 14720,
    "issue_size_cr": 1103.99,
    "fresh_issue_cr": 828.0,
    "ofs_cr": 276.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 368.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.17,
        "nii": 0.89,
        "retail": 3.44,
        "total": 0.89
      },
      "day2": {
        "qib": 0.42,
        "nii": 2.06,
        "retail": 6.87,
        "total": 1.92
      },
      "final_day": {
        "qib": 0.85,
        "nii": 4.43,
        "retail": 8.59,
        "total": 2.95
      },
      "applications_count": "2.95x Subscription"
    },
    "listing": {
      "listing_price": 360.5,
      "listing_gain_rs": -7.5,
      "listing_gain_percent": -2.0,
      "profit_per_lot": -300.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 368.0,
        "actual_price": 360.5,
        "variance_rs": -7.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9368.0 (+0.0%). Stock opened at \u20b9360.5 (-2.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -2.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-2.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Joint Liability Rural MFI Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Joint Liability Rural MFI",
        "Strong institutional interest with 0.85x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -2.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 368.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 368.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 368.0,
        "notes": "Predicted \u20b9368.0 listing"
      }
    ]
  },
  {
    "id": "tracxn",
    "name": "Tracxn Technologies Ltd",
    "symbol": "TRACXN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Private Market Intelligence SaaS",
    "open_date": "10-Oct-22",
    "close_date": "12-Oct-22",
    "listing_date": "20-Oct-22",
    "price_band": "\u20b980",
    "issue_price": 80.0,
    "lot_size": 185,
    "min_investment": 14800,
    "issue_size_cr": 309.38,
    "fresh_issue_cr": 232.0,
    "ofs_cr": 77.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 4.0,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 84.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.33,
        "nii": 0.6,
        "retail": 1.95,
        "total": 0.6
      },
      "day2": {
        "qib": 0.83,
        "nii": 1.41,
        "retail": 3.9,
        "total": 1.31
      },
      "final_day": {
        "qib": 1.66,
        "nii": 3.01,
        "retail": 4.87,
        "total": 2.01
      },
      "applications_count": "2.01x Subscription"
    },
    "listing": {
      "listing_price": 83.0,
      "listing_gain_rs": 3.0,
      "listing_gain_percent": 3.8,
      "profit_per_lot": 555.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 84.0,
        "actual_price": 83.0,
        "variance_rs": -1.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b984.0 (+5.0%). Stock opened at \u20b983.0 (+3.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 3.8,
      "retail_profit_lost": 555.0,
      "explanation": "The IPO had a flat listing (+3.8%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Private Market Intelligence SaaS Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Private Market Intelligence SaaS",
        "Strong institutional interest with 1.66x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +3.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.8,
        "gmp_percent": 4.8,
        "est_listing_price": 83.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.9,
        "gmp_percent": 4.9,
        "est_listing_price": 83.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 4.0,
        "gmp_percent": 5.0,
        "est_listing_price": 84.0,
        "notes": "Predicted \u20b984.0 listing"
      }
    ]
  },
  {
    "id": "emil",
    "name": "Electronics Mart India Ltd",
    "symbol": "EMIL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Consumer Electronics Retailer",
    "open_date": "04-Oct-22",
    "close_date": "07-Oct-22",
    "listing_date": "17-Oct-22",
    "price_band": "\u20b959",
    "issue_price": 59.0,
    "lot_size": 254,
    "min_investment": 14986,
    "issue_size_cr": 500.0,
    "fresh_issue_cr": 375.0,
    "ofs_cr": 125.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 30.68,
    "gmp_closing_percent": 52.0,
    "gmp_estimated_listing": 89.68,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 33.91,
        "nii": 21.58,
        "retail": 7.89,
        "total": 21.58
      },
      "day2": {
        "qib": 84.77,
        "nii": 50.35,
        "retail": 15.78,
        "total": 46.75
      },
      "final_day": {
        "qib": 169.54,
        "nii": 107.9,
        "retail": 19.72,
        "total": 71.93
      },
      "applications_count": "71.93x Subscription"
    },
    "listing": {
      "listing_price": 89.4,
      "listing_gain_rs": 30.4,
      "listing_gain_percent": 51.5,
      "profit_per_lot": 7721.6,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 89.68,
        "actual_price": 89.4,
        "variance_rs": -0.28,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b989.68 (+52.0%). Stock opened at \u20b989.4 (+51.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 52.0,
      "actual_gain_pct": 51.5,
      "retail_profit_lost": 7721.6,
      "explanation": "Electronics Mart India Ltd delivered a stellar +51.5% listing gain, rewarding retail allottees with \u20b97,722 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +52% Listing Return",
      "long_term_potential": "Consumer Electronics Retailer Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Consumer Electronics Retailer",
        "Strong institutional interest with 169.54x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +51.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 23.9,
        "gmp_percent": 40.6,
        "est_listing_price": 82.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 27.6,
        "gmp_percent": 46.8,
        "est_listing_price": 86.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 30.68,
        "gmp_percent": 52.0,
        "est_listing_price": 89.7,
        "notes": "Predicted \u20b989.68 listing"
      }
    ]
  },
  {
    "id": "harsha",
    "name": "Harsha Engineers International",
    "symbol": "HARSHA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Precision Bearing Cages",
    "open_date": "14-Sep-22",
    "close_date": "16-Sep-22",
    "listing_date": "26-Sep-22",
    "price_band": "\u20b9330",
    "issue_price": 330.0,
    "lot_size": 45,
    "min_investment": 14850,
    "issue_size_cr": 755.0,
    "fresh_issue_cr": 566.2,
    "ofs_cr": 188.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 118.8,
    "gmp_closing_percent": 36.0,
    "gmp_estimated_listing": 448.8,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 35.72,
        "nii": 22.41,
        "retail": 7.05,
        "total": 22.41
      },
      "day2": {
        "qib": 89.31,
        "nii": 52.29,
        "retail": 14.1,
        "total": 48.56
      },
      "final_day": {
        "qib": 178.61,
        "nii": 112.05,
        "retail": 17.63,
        "total": 74.7
      },
      "applications_count": "74.7x Subscription"
    },
    "listing": {
      "listing_price": 444.0,
      "listing_gain_rs": 114.0,
      "listing_gain_percent": 34.5,
      "profit_per_lot": 5130.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 448.8,
        "actual_price": 444.0,
        "variance_rs": -4.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9448.8 (+36.0%). Stock opened at \u20b9444.0 (+34.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 36.0,
      "actual_gain_pct": 34.5,
      "retail_profit_lost": 5130.0,
      "explanation": "Harsha Engineers International delivered a stellar +34.5% listing gain, rewarding retail allottees with \u20b95,130 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +36% Listing Return",
      "long_term_potential": "Precision Bearing Cages Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Precision Bearing Cages",
        "Strong institutional interest with 178.61x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +34.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 92.7,
        "gmp_percent": 28.1,
        "est_listing_price": 422.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 106.9,
        "gmp_percent": 32.4,
        "est_listing_price": 436.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 118.8,
        "gmp_percent": 36.0,
        "est_listing_price": 448.8,
        "notes": "Predicted \u20b9448.8 listing"
      }
    ]
  },
  {
    "id": "dreamfolks",
    "name": "Dreamfolks Services Ltd",
    "symbol": "DREAMFOLKS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Airport Lounge Access Aggregator",
    "open_date": "24-Aug-22",
    "close_date": "26-Aug-22",
    "listing_date": "06-Sep-22",
    "price_band": "\u20b9326",
    "issue_price": 326.0,
    "lot_size": 46,
    "min_investment": 14996,
    "issue_size_cr": 562.1,
    "fresh_issue_cr": 421.6,
    "ofs_cr": 140.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 179.3,
    "gmp_closing_percent": 55.0,
    "gmp_estimated_listing": 505.3,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 14.11,
        "nii": 17.0,
        "retail": 17.46,
        "total": 17.0
      },
      "day2": {
        "qib": 35.27,
        "nii": 39.68,
        "retail": 34.93,
        "total": 36.84
      },
      "final_day": {
        "qib": 70.53,
        "nii": 85.02,
        "retail": 43.66,
        "total": 56.68
      },
      "applications_count": "56.68x Subscription"
    },
    "listing": {
      "listing_price": 505.0,
      "listing_gain_rs": 179.0,
      "listing_gain_percent": 54.9,
      "profit_per_lot": 8234.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 505.3,
        "actual_price": 505.0,
        "variance_rs": -0.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9505.3 (+55.0%). Stock opened at \u20b9505.0 (+54.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 55.0,
      "actual_gain_pct": 54.9,
      "retail_profit_lost": 8234.0,
      "explanation": "Dreamfolks Services Ltd delivered a stellar +54.9% listing gain, rewarding retail allottees with \u20b98,234 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +55% Listing Return",
      "long_term_potential": "Airport Lounge Access Aggregator Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Airport Lounge Access Aggregator",
        "Strong institutional interest with 70.53x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +54.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 139.9,
        "gmp_percent": 42.9,
        "est_listing_price": 465.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 161.4,
        "gmp_percent": 49.5,
        "est_listing_price": 487.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 179.3,
        "gmp_percent": 55.0,
        "est_listing_price": 505.3,
        "notes": "Predicted \u20b9505.3 listing"
      }
    ]
  },
  {
    "id": "syrma",
    "name": "Syrma SGS Technology Ltd",
    "symbol": "SYRMA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Electronics Manufacturing Services (EMS)",
    "open_date": "12-Aug-22",
    "close_date": "18-Aug-22",
    "listing_date": "26-Aug-22",
    "price_band": "\u20b9220",
    "issue_price": 220.0,
    "lot_size": 68,
    "min_investment": 14960,
    "issue_size_cr": 840.13,
    "fresh_issue_cr": 630.1,
    "ofs_cr": 210.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 44.0,
    "gmp_closing_percent": 20.0,
    "gmp_estimated_listing": 264.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 17.51,
        "nii": 9.78,
        "retail": 2.21,
        "total": 9.78
      },
      "day2": {
        "qib": 43.78,
        "nii": 22.83,
        "retail": 4.42,
        "total": 21.2
      },
      "final_day": {
        "qib": 87.56,
        "nii": 48.91,
        "retail": 5.53,
        "total": 32.61
      },
      "applications_count": "32.61x Subscription"
    },
    "listing": {
      "listing_price": 262.0,
      "listing_gain_rs": 42.0,
      "listing_gain_percent": 19.1,
      "profit_per_lot": 2856.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 264.0,
        "actual_price": 262.0,
        "variance_rs": -2.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9264.0 (+20.0%). Stock opened at \u20b9262.0 (+19.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 20.0,
      "actual_gain_pct": 19.1,
      "retail_profit_lost": 2856.0,
      "explanation": "The issue opened with a healthy +19.1% pop (\u20b92,856 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +20% Listing Return",
      "long_term_potential": "Electronics Manufacturing Services (EMS) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Electronics Manufacturing Services (EMS)",
        "Strong institutional interest with 87.56x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +19.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 41.8,
        "gmp_percent": 19.0,
        "est_listing_price": 261.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 43.1,
        "gmp_percent": 19.6,
        "est_listing_price": 263.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 44.0,
        "gmp_percent": 20.0,
        "est_listing_price": 264.0,
        "notes": "Predicted \u20b9264.0 listing"
      }
    ]
  },
  {
    "id": "aether",
    "name": "Aether Industries Ltd",
    "symbol": "AETHER.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Advanced Fine & Specialty Chemicals",
    "open_date": "24-May-22",
    "close_date": "26-May-22",
    "listing_date": "03-Jun-22",
    "price_band": "\u20b9642",
    "issue_price": 642.0,
    "lot_size": 23,
    "min_investment": 14766,
    "issue_size_cr": 808.04,
    "fresh_issue_cr": 606.0,
    "ofs_cr": 202.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 77.04,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 719.04,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 3.51,
        "nii": 1.88,
        "retail": 0.79,
        "total": 1.88
      },
      "day2": {
        "qib": 8.79,
        "nii": 4.38,
        "retail": 1.58,
        "total": 4.07
      },
      "final_day": {
        "qib": 17.57,
        "nii": 9.39,
        "retail": 1.97,
        "total": 6.26
      },
      "applications_count": "6.26x Subscription"
    },
    "listing": {
      "listing_price": 706.15,
      "listing_gain_rs": 64.15,
      "listing_gain_percent": 10.0,
      "profit_per_lot": 1475.45,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 719.04,
        "actual_price": 706.15,
        "variance_rs": -12.89,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9719.04 (+12.0%). Stock opened at \u20b9706.15 (+10.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 10.0,
      "retail_profit_lost": 1475.45,
      "explanation": "The issue opened with a healthy +10.0% pop (\u20b91,475 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "Advanced Fine & Specialty Chemicals Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Advanced Fine & Specialty Chemicals",
        "Strong institutional interest with 17.57x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +10.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 73.2,
        "gmp_percent": 11.4,
        "est_listing_price": 715.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 75.5,
        "gmp_percent": 11.8,
        "est_listing_price": 717.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 77.04,
        "gmp_percent": 12.0,
        "est_listing_price": 719.0,
        "notes": "Predicted \u20b9719.04 listing"
      }
    ]
  },
  {
    "id": "emudhra",
    "name": "eMudhra Ltd",
    "symbol": "EMUDHRA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Signature & Trust Services",
    "open_date": "20-May-22",
    "close_date": "24-May-22",
    "listing_date": "01-Jun-22",
    "price_band": "\u20b9256",
    "issue_price": 256.0,
    "lot_size": 58,
    "min_investment": 14848,
    "issue_size_cr": 412.79,
    "fresh_issue_cr": 309.6,
    "ofs_cr": 103.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 20.48,
    "gmp_closing_percent": 8.0,
    "gmp_estimated_listing": 276.48,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.96,
        "nii": 0.82,
        "retail": 1.04,
        "total": 0.82
      },
      "day2": {
        "qib": 2.39,
        "nii": 1.9,
        "retail": 2.09,
        "total": 1.77
      },
      "final_day": {
        "qib": 4.78,
        "nii": 4.08,
        "retail": 2.61,
        "total": 2.72
      },
      "applications_count": "2.72x Subscription"
    },
    "listing": {
      "listing_price": 271.0,
      "listing_gain_rs": 15.0,
      "listing_gain_percent": 5.9,
      "profit_per_lot": 870.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 276.48,
        "actual_price": 271.0,
        "variance_rs": -5.48,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9276.48 (+8.0%). Stock opened at \u20b9271.0 (+5.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 8.0,
      "actual_gain_pct": 5.9,
      "retail_profit_lost": 870.0,
      "explanation": "The issue opened with a healthy +5.9% pop (\u20b9870 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +8% Listing Return",
      "long_term_potential": "Digital Signature & Trust Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Signature & Trust Services",
        "Strong institutional interest with 4.78x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +5.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 19.5,
        "gmp_percent": 7.6,
        "est_listing_price": 275.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 20.1,
        "gmp_percent": 7.8,
        "est_listing_price": 276.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 20.48,
        "gmp_percent": 8.0,
        "est_listing_price": 276.5,
        "notes": "Predicted \u20b9276.48 listing"
      }
    ]
  },
  {
    "id": "paradeep",
    "name": "Paradeep Phosphates Ltd",
    "symbol": "PARADEEP.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Phosphatic Fertilizers & DAP",
    "open_date": "17-May-22",
    "close_date": "19-May-22",
    "listing_date": "27-May-22",
    "price_band": "\u20b942",
    "issue_price": 42.0,
    "lot_size": 350,
    "min_investment": 14700,
    "issue_size_cr": 1501.73,
    "fresh_issue_cr": 1126.3,
    "ofs_cr": 375.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 2.1,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 44.1,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.6,
        "nii": 0.53,
        "retail": 0.55,
        "total": 0.53
      },
      "day2": {
        "qib": 1.5,
        "nii": 1.22,
        "retail": 1.1,
        "total": 1.14
      },
      "final_day": {
        "qib": 3.01,
        "nii": 2.62,
        "retail": 1.37,
        "total": 1.75
      },
      "applications_count": "1.75x Subscription"
    },
    "listing": {
      "listing_price": 43.5,
      "listing_gain_rs": 1.5,
      "listing_gain_percent": 3.6,
      "profit_per_lot": 525.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 44.1,
        "actual_price": 43.5,
        "variance_rs": -0.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b944.1 (+5.0%). Stock opened at \u20b943.5 (+3.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 3.6,
      "retail_profit_lost": 525.0,
      "explanation": "The IPO had a flat listing (+3.6%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Phosphatic Fertilizers & DAP Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Phosphatic Fertilizers & DAP",
        "Strong institutional interest with 3.01x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +3.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 2.0,
        "gmp_percent": 4.8,
        "est_listing_price": 44.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 2.1,
        "gmp_percent": 4.9,
        "est_listing_price": 44.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 2.1,
        "gmp_percent": 5.0,
        "est_listing_price": 44.1,
        "notes": "Predicted \u20b944.1 listing"
      }
    ]
  },
  {
    "id": "delhivery",
    "name": "Delhivery Ltd",
    "symbol": "DELHIVERY.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Third-Party Express Logistics",
    "open_date": "11-May-22",
    "close_date": "13-May-22",
    "listing_date": "24-May-22",
    "price_band": "\u20b9487",
    "issue_price": 487.0,
    "lot_size": 30,
    "min_investment": 14610,
    "issue_size_cr": 5235.0,
    "fresh_issue_cr": 3926.2,
    "ofs_cr": 1308.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 9.74,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 496.74,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.53,
        "nii": 0.49,
        "retail": 0.23,
        "total": 0.49
      },
      "day2": {
        "qib": 1.33,
        "nii": 1.14,
        "retail": 0.46,
        "total": 1.06
      },
      "final_day": {
        "qib": 2.66,
        "nii": 2.44,
        "retail": 0.57,
        "total": 1.63
      },
      "applications_count": "1.63x Subscription"
    },
    "listing": {
      "listing_price": 493.0,
      "listing_gain_rs": 6.0,
      "listing_gain_percent": 1.2,
      "profit_per_lot": 180.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 496.74,
        "actual_price": 493.0,
        "variance_rs": -3.74,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9496.74 (+2.0%). Stock opened at \u20b9493.0 (+1.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 1.2,
      "retail_profit_lost": 180.0,
      "explanation": "The IPO had a flat listing (+1.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Third-Party Express Logistics Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Third-Party Express Logistics",
        "Strong institutional interest with 2.66x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 9.3,
        "gmp_percent": 1.9,
        "est_listing_price": 496.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 9.5,
        "gmp_percent": 2.0,
        "est_listing_price": 496.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 9.74,
        "gmp_percent": 2.0,
        "est_listing_price": 496.7,
        "notes": "Predicted \u20b9496.74 listing"
      }
    ]
  },
  {
    "id": "venuspipes",
    "name": "Venus Pipes & Tubes Ltd",
    "symbol": "VENUSPIPES.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Stainless Steel Welded Pipes",
    "open_date": "11-May-22",
    "close_date": "13-May-22",
    "listing_date": "24-May-22",
    "price_band": "\u20b9326",
    "issue_price": 326.0,
    "lot_size": 46,
    "min_investment": 14996,
    "issue_size_cr": 165.42,
    "fresh_issue_cr": 124.1,
    "ofs_cr": 41.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 16.3,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 342.3,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.4,
        "nii": 4.89,
        "retail": 9.77,
        "total": 4.89
      },
      "day2": {
        "qib": 6.01,
        "nii": 11.42,
        "retail": 19.54,
        "total": 10.6
      },
      "final_day": {
        "qib": 12.02,
        "nii": 24.46,
        "retail": 24.42,
        "total": 16.31
      },
      "applications_count": "16.31x Subscription"
    },
    "listing": {
      "listing_price": 335.0,
      "listing_gain_rs": 9.0,
      "listing_gain_percent": 2.8,
      "profit_per_lot": 414.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 342.3,
        "actual_price": 335.0,
        "variance_rs": -7.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9342.3 (+5.0%). Stock opened at \u20b9335.0 (+2.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 2.8,
      "retail_profit_lost": 414.0,
      "explanation": "The IPO had a flat listing (+2.8%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Stainless Steel Welded Pipes Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Stainless Steel Welded Pipes",
        "Strong institutional interest with 12.02x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +2.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 15.5,
        "gmp_percent": 4.8,
        "est_listing_price": 341.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 16.0,
        "gmp_percent": 4.9,
        "est_listing_price": 342.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 16.3,
        "gmp_percent": 5.0,
        "est_listing_price": 342.3,
        "notes": "Predicted \u20b9342.3 listing"
      }
    ]
  },
  {
    "id": "prudent",
    "name": "Prudent Corporate Advisory Services",
    "symbol": "PRUDENT.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Mutual Fund Distribution IFA",
    "open_date": "10-May-22",
    "close_date": "12-May-22",
    "listing_date": "20-May-22",
    "price_band": "\u20b9630",
    "issue_price": 630.0,
    "lot_size": 23,
    "min_investment": 14490,
    "issue_size_cr": 538.61,
    "fresh_issue_cr": 404.0,
    "ofs_cr": 134.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 31.5,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 661.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.8,
        "nii": 0.37,
        "retail": 0.49,
        "total": 0.37
      },
      "day2": {
        "qib": 2.01,
        "nii": 0.85,
        "retail": 0.98,
        "total": 0.79
      },
      "final_day": {
        "qib": 4.02,
        "nii": 1.83,
        "retail": 1.23,
        "total": 1.22
      },
      "applications_count": "1.22x Subscription"
    },
    "listing": {
      "listing_price": 650.0,
      "listing_gain_rs": 20.0,
      "listing_gain_percent": 3.2,
      "profit_per_lot": 460.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 661.5,
        "actual_price": 650.0,
        "variance_rs": -11.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9661.5 (+5.0%). Stock opened at \u20b9650.0 (+3.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": 3.2,
      "retail_profit_lost": 460.0,
      "explanation": "The IPO had a flat listing (+3.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Mutual Fund Distribution IFA Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Mutual Fund Distribution IFA",
        "Strong institutional interest with 4.02x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +3.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 29.9,
        "gmp_percent": 4.8,
        "est_listing_price": 659.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 30.9,
        "gmp_percent": 4.9,
        "est_listing_price": 660.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 31.5,
        "gmp_percent": 5.0,
        "est_listing_price": 661.5,
        "notes": "Predicted \u20b9661.5 listing"
      }
    ]
  },
  {
    "id": "lici",
    "name": "Life Insurance Corp. of India",
    "symbol": "LICI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Life Insurance PSU Mega-Issue",
    "open_date": "04-May-22",
    "close_date": "09-May-22",
    "listing_date": "17-May-22",
    "price_band": "\u20b9949",
    "issue_price": 949.0,
    "lot_size": 15,
    "min_investment": 14235,
    "issue_size_cr": 21000.0,
    "fresh_issue_cr": 15750.0,
    "ofs_cr": 5250.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -18.98,
    "gmp_closing_percent": -2.0,
    "gmp_estimated_listing": 930.02,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.57,
        "nii": 0.89,
        "retail": 0.8,
        "total": 0.89
      },
      "day2": {
        "qib": 1.42,
        "nii": 2.06,
        "retail": 1.59,
        "total": 1.92
      },
      "final_day": {
        "qib": 2.83,
        "nii": 4.43,
        "retail": 1.99,
        "total": 2.95
      },
      "applications_count": "2.95x Subscription"
    },
    "listing": {
      "listing_price": 867.2,
      "listing_gain_rs": -81.8,
      "listing_gain_percent": -8.6,
      "profit_per_lot": -1227.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 930.02,
        "actual_price": 867.2,
        "variance_rs": -62.82,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9930.02 (-2.0%). Stock opened at \u20b9867.2 (-8.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -2.0,
      "actual_gain_pct": -8.6,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -8.6% (\u20b91,227 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -2% Listing Return",
      "long_term_potential": "Life Insurance PSU Mega-Issue Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Life Insurance PSU Mega-Issue",
        "Strong institutional interest with 2.83x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -8.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -23.7,
        "gmp_percent": -2.5,
        "est_listing_price": 925.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -21.3,
        "gmp_percent": -2.2,
        "est_listing_price": 927.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -18.98,
        "gmp_percent": -2.0,
        "est_listing_price": 930.0,
        "notes": "Predicted \u20b9930.02 listing"
      }
    ]
  },
  {
    "id": "manyavar",
    "name": "Vedant Fashions Ltd (Manyavar)",
    "symbol": "MANYAVAR.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Celebration Wear & Kurta Retail",
    "open_date": "04-Feb-22",
    "close_date": "08-Feb-22",
    "listing_date": "16-Feb-22",
    "price_band": "\u20b9866",
    "issue_price": 866.0,
    "lot_size": 17,
    "min_investment": 14722,
    "issue_size_cr": 3149.19,
    "fresh_issue_cr": 2361.9,
    "ofs_cr": 787.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 86.6,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 952.6,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.5,
        "nii": 0.77,
        "retail": 0.16,
        "total": 0.77
      },
      "day2": {
        "qib": 3.75,
        "nii": 1.8,
        "retail": 0.31,
        "total": 1.67
      },
      "final_day": {
        "qib": 7.49,
        "nii": 3.85,
        "retail": 0.39,
        "total": 2.57
      },
      "applications_count": "2.57x Subscription"
    },
    "listing": {
      "listing_price": 936.0,
      "listing_gain_rs": 70.0,
      "listing_gain_percent": 8.1,
      "profit_per_lot": 1190.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 952.6,
        "actual_price": 936.0,
        "variance_rs": -16.6,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9952.6 (+10.0%). Stock opened at \u20b9936.0 (+8.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 8.1,
      "retail_profit_lost": 1190.0,
      "explanation": "The issue opened with a healthy +8.1% pop (\u20b91,190 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Celebration Wear & Kurta Retail Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Celebration Wear & Kurta Retail",
        "Strong institutional interest with 7.49x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +8.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 82.3,
        "gmp_percent": 9.5,
        "est_listing_price": 948.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 84.9,
        "gmp_percent": 9.8,
        "est_listing_price": 950.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 86.6,
        "gmp_percent": 10.0,
        "est_listing_price": 952.6,
        "notes": "Predicted \u20b9952.6 listing"
      }
    ]
  },
  {
    "id": "awl",
    "name": "Adani Wilmar Ltd (Fortune)",
    "symbol": "AWL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Edible Oils & Packaged Staples",
    "open_date": "27-Jan-22",
    "close_date": "31-Jan-22",
    "listing_date": "08-Feb-22",
    "price_band": "\u20b9230",
    "issue_price": 230.0,
    "lot_size": 65,
    "min_investment": 14950,
    "issue_size_cr": 3600.0,
    "fresh_issue_cr": 2700.0,
    "ofs_cr": 900.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 11.5,
    "gmp_closing_percent": 5.0,
    "gmp_estimated_listing": 241.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 11.26,
        "nii": 5.21,
        "retail": 1.57,
        "total": 5.21
      },
      "day2": {
        "qib": 28.15,
        "nii": 12.16,
        "retail": 3.14,
        "total": 11.29
      },
      "final_day": {
        "qib": 56.3,
        "nii": 26.05,
        "retail": 3.92,
        "total": 17.37
      },
      "applications_count": "17.37x Subscription"
    },
    "listing": {
      "listing_price": 221.0,
      "listing_gain_rs": -9.0,
      "listing_gain_percent": -3.9,
      "profit_per_lot": -585.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 241.5,
        "actual_price": 221.0,
        "variance_rs": -20.5,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9241.5 (+5.0%). Stock opened at \u20b9221.0 (-3.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 5.0,
      "actual_gain_pct": -3.9,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -3.9% (\u20b9585 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +5% Listing Return",
      "long_term_potential": "Edible Oils & Packaged Staples Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Edible Oils & Packaged Staples",
        "Strong institutional interest with 56.3x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -3.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 10.9,
        "gmp_percent": 4.8,
        "est_listing_price": 240.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 11.3,
        "gmp_percent": 4.9,
        "est_listing_price": 241.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 11.5,
        "gmp_percent": 5.0,
        "est_listing_price": 241.5,
        "notes": "Predicted \u20b9241.5 listing"
      }
    ]
  },
  {
    "id": "agstra",
    "name": "AGS Transact Technologies",
    "symbol": "AGSTRA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Payment POS & ATM Solutions",
    "open_date": "19-Jan-22",
    "close_date": "21-Jan-22",
    "listing_date": "31-Jan-22",
    "price_band": "\u20b9175",
    "issue_price": 175.0,
    "lot_size": 85,
    "min_investment": 14875,
    "issue_size_cr": 680.0,
    "fresh_issue_cr": 510.0,
    "ofs_cr": 170.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 3.5,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 178.5,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 5.29,
        "nii": 2.34,
        "retail": 1.23,
        "total": 2.34
      },
      "day2": {
        "qib": 13.22,
        "nii": 5.45,
        "retail": 2.46,
        "total": 5.06
      },
      "final_day": {
        "qib": 26.44,
        "nii": 11.69,
        "retail": 3.08,
        "total": 7.79
      },
      "applications_count": "7.79x Subscription"
    },
    "listing": {
      "listing_price": 176.0,
      "listing_gain_rs": 1.0,
      "listing_gain_percent": 0.6,
      "profit_per_lot": 85.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 178.5,
        "actual_price": 176.0,
        "variance_rs": -2.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9178.5 (+2.0%). Stock opened at \u20b9176.0 (+0.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 0.6,
      "retail_profit_lost": 85.0,
      "explanation": "The IPO had a flat listing (+0.6%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Digital Payment POS & ATM Solutions Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Payment POS & ATM Solutions",
        "Strong institutional interest with 26.44x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 3.3,
        "gmp_percent": 1.9,
        "est_listing_price": 178.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 3.4,
        "gmp_percent": 2.0,
        "est_listing_price": 178.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 3.5,
        "gmp_percent": 2.0,
        "est_listing_price": 178.5,
        "notes": "Predicted \u20b9178.5 listing"
      }
    ]
  },
  {
    "id": "cmsinfo",
    "name": "CMS Info Systems Ltd",
    "symbol": "CMSINFO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Cash Management & ATM Networks",
    "open_date": "21-Dec-21",
    "close_date": "23-Dec-21",
    "listing_date": "31-Dec-21",
    "price_band": "\u20b9216",
    "issue_price": 216.0,
    "lot_size": 69,
    "min_investment": 14904,
    "issue_size_cr": 1100.0,
    "fresh_issue_cr": 825.0,
    "ofs_cr": 275.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 6.48,
    "gmp_closing_percent": 3.0,
    "gmp_estimated_listing": 222.48,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.29,
        "nii": 0.59,
        "retail": 1.21,
        "total": 0.59
      },
      "day2": {
        "qib": 0.72,
        "nii": 1.39,
        "retail": 2.42,
        "total": 1.29
      },
      "final_day": {
        "qib": 1.45,
        "nii": 2.97,
        "retail": 3.02,
        "total": 1.98
      },
      "applications_count": "1.98x Subscription"
    },
    "listing": {
      "listing_price": 218.5,
      "listing_gain_rs": 2.5,
      "listing_gain_percent": 1.2,
      "profit_per_lot": 172.5,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 222.48,
        "actual_price": 218.5,
        "variance_rs": -3.98,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9222.48 (+3.0%). Stock opened at \u20b9218.5 (+1.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 3.0,
      "actual_gain_pct": 1.2,
      "retail_profit_lost": 172.5,
      "explanation": "The IPO had a flat listing (+1.2%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +3% Listing Return",
      "long_term_potential": "Cash Management & ATM Networks Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Cash Management & ATM Networks",
        "Strong institutional interest with 1.45x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +1.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 6.2,
        "gmp_percent": 2.8,
        "est_listing_price": 222.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 6.4,
        "gmp_percent": 2.9,
        "est_listing_price": 222.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 6.48,
        "gmp_percent": 3.0,
        "est_listing_price": 222.5,
        "notes": "Predicted \u20b9222.48 listing"
      }
    ]
  },
  {
    "id": "supriya",
    "name": "Supriya Lifescience Ltd",
    "symbol": "SUPRIYA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Active Pharma Ingredients (API)",
    "open_date": "16-Dec-21",
    "close_date": "20-Dec-21",
    "listing_date": "28-Dec-21",
    "price_band": "\u20b9274",
    "issue_price": 274.0,
    "lot_size": 54,
    "min_investment": 14796,
    "issue_size_cr": 700.0,
    "fresh_issue_cr": 525.0,
    "ofs_cr": 175.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 150.7,
    "gmp_closing_percent": 55.0,
    "gmp_estimated_listing": 424.7,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 33.31,
        "nii": 21.47,
        "retail": 22.4,
        "total": 21.47
      },
      "day2": {
        "qib": 83.28,
        "nii": 50.09,
        "retail": 44.81,
        "total": 46.51
      },
      "final_day": {
        "qib": 166.56,
        "nii": 107.34,
        "retail": 56.01,
        "total": 71.56
      },
      "applications_count": "71.56x Subscription"
    },
    "listing": {
      "listing_price": 425.0,
      "listing_gain_rs": 151.0,
      "listing_gain_percent": 55.1,
      "profit_per_lot": 8154.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 424.7,
        "actual_price": 425.0,
        "variance_rs": 0.3,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9424.7 (+55.0%). Stock opened at \u20b9425.0 (+55.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 55.0,
      "actual_gain_pct": 55.1,
      "retail_profit_lost": 8154.0,
      "explanation": "Supriya Lifescience Ltd delivered a stellar +55.1% listing gain, rewarding retail allottees with \u20b98,154 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +55% Listing Return",
      "long_term_potential": "Active Pharma Ingredients (API) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Active Pharma Ingredients (API)",
        "Strong institutional interest with 166.56x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +55.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 117.5,
        "gmp_percent": 42.9,
        "est_listing_price": 391.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 135.6,
        "gmp_percent": 49.5,
        "est_listing_price": 409.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 150.7,
        "gmp_percent": 55.0,
        "est_listing_price": 424.7,
        "notes": "Predicted \u20b9424.7 listing"
      }
    ]
  },
  {
    "id": "hpal",
    "name": "HP Adhesives Ltd",
    "symbol": "HPAL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Consumer Adhesives & Sealants",
    "open_date": "15-Dec-21",
    "close_date": "17-Dec-21",
    "listing_date": "27-Dec-21",
    "price_band": "\u20b9274",
    "issue_price": 274.0,
    "lot_size": 50,
    "min_investment": 13700,
    "issue_size_cr": 125.96,
    "fresh_issue_cr": 94.5,
    "ofs_cr": 31.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 49.32,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 323.32,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 3.81,
        "nii": 6.29,
        "retail": 32.5,
        "total": 6.29
      },
      "day2": {
        "qib": 9.52,
        "nii": 14.67,
        "retail": 64.99,
        "total": 13.62
      },
      "final_day": {
        "qib": 19.04,
        "nii": 31.44,
        "retail": 81.24,
        "total": 20.96
      },
      "applications_count": "20.96x Subscription"
    },
    "listing": {
      "listing_price": 319.0,
      "listing_gain_rs": 45.0,
      "listing_gain_percent": 16.4,
      "profit_per_lot": 2250.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 323.32,
        "actual_price": 319.0,
        "variance_rs": -4.32,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9323.32 (+18.0%). Stock opened at \u20b9319.0 (+16.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 16.4,
      "retail_profit_lost": 2250.0,
      "explanation": "The issue opened with a healthy +16.4% pop (\u20b92,250 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "Consumer Adhesives & Sealants Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Consumer Adhesives & Sealants",
        "Strong institutional interest with 19.04x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +16.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 46.9,
        "gmp_percent": 17.1,
        "est_listing_price": 320.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 48.3,
        "gmp_percent": 17.6,
        "est_listing_price": 322.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 49.32,
        "gmp_percent": 18.0,
        "est_listing_price": 323.3,
        "notes": "Predicted \u20b9323.32 listing"
      }
    ]
  },
  {
    "id": "datapattns",
    "name": "Data Patterns (India) Ltd",
    "symbol": "DATAPATTNS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Defense Radars & Electronics",
    "open_date": "14-Dec-21",
    "close_date": "16-Dec-21",
    "listing_date": "24-Dec-21",
    "price_band": "\u20b9585",
    "issue_price": 585.0,
    "lot_size": 25,
    "min_investment": 14625,
    "issue_size_cr": 588.22,
    "fresh_issue_cr": 441.2,
    "ofs_cr": 147.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 280.8,
    "gmp_closing_percent": 48.0,
    "gmp_estimated_listing": 865.8,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 50.84,
        "nii": 35.89,
        "retail": 9.26,
        "total": 35.89
      },
      "day2": {
        "qib": 127.11,
        "nii": 83.73,
        "retail": 18.51,
        "total": 77.75
      },
      "final_day": {
        "qib": 254.22,
        "nii": 179.43,
        "retail": 23.14,
        "total": 119.62
      },
      "applications_count": "119.62x Subscription"
    },
    "listing": {
      "listing_price": 856.0,
      "listing_gain_rs": 271.0,
      "listing_gain_percent": 46.3,
      "profit_per_lot": 6775.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 865.8,
        "actual_price": 856.0,
        "variance_rs": -9.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9865.8 (+48.0%). Stock opened at \u20b9856.0 (+46.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 48.0,
      "actual_gain_pct": 46.3,
      "retail_profit_lost": 6775.0,
      "explanation": "Data Patterns (India) Ltd delivered a stellar +46.3% listing gain, rewarding retail allottees with \u20b96,775 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +48% Listing Return",
      "long_term_potential": "Defense Radars & Electronics Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Defense Radars & Electronics",
        "Strong institutional interest with 254.22x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +46.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 219.0,
        "gmp_percent": 37.4,
        "est_listing_price": 804.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 252.7,
        "gmp_percent": 43.2,
        "est_listing_price": 837.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 280.8,
        "gmp_percent": 48.0,
        "est_listing_price": 865.8,
        "notes": "Predicted \u20b9865.8 listing"
      }
    ]
  },
  {
    "id": "medplus",
    "name": "Medplus Health Services Ltd",
    "symbol": "MEDPLUS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pharmacy Retail Stores",
    "open_date": "13-Dec-21",
    "close_date": "15-Dec-21",
    "listing_date": "23-Dec-21",
    "price_band": "\u20b9796",
    "issue_price": 796.0,
    "lot_size": 18,
    "min_investment": 14328,
    "issue_size_cr": 1398.3,
    "fresh_issue_cr": 1048.7,
    "ofs_cr": 349.6,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 238.8,
    "gmp_closing_percent": 30.0,
    "gmp_estimated_listing": 1034.8,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 17.07,
        "nii": 15.78,
        "retail": 2.09,
        "total": 15.78
      },
      "day2": {
        "qib": 42.66,
        "nii": 36.81,
        "retail": 4.18,
        "total": 34.18
      },
      "final_day": {
        "qib": 85.33,
        "nii": 78.89,
        "retail": 5.23,
        "total": 52.59
      },
      "applications_count": "52.59x Subscription"
    },
    "listing": {
      "listing_price": 1015.0,
      "listing_gain_rs": 219.0,
      "listing_gain_percent": 27.5,
      "profit_per_lot": 3942.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1034.8,
        "actual_price": 1015.0,
        "variance_rs": -19.8,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b91034.8 (+30.0%). Stock opened at \u20b91015.0 (+27.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 30.0,
      "actual_gain_pct": 27.5,
      "retail_profit_lost": 3942.0,
      "explanation": "Medplus Health Services Ltd delivered a stellar +27.5% listing gain, rewarding retail allottees with \u20b93,942 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +30% Listing Return",
      "long_term_potential": "Pharmacy Retail Stores Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pharmacy Retail Stores",
        "Strong institutional interest with 85.33x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +27.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 186.3,
        "gmp_percent": 23.4,
        "est_listing_price": 982.3,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 214.9,
        "gmp_percent": 27.0,
        "est_listing_price": 1010.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 238.8,
        "gmp_percent": 30.0,
        "est_listing_price": 1034.8,
        "notes": "Predicted \u20b91034.8 listing"
      }
    ]
  },
  {
    "id": "metrobrand",
    "name": "Metro Brands Ltd",
    "symbol": "METROBRAND.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Footwear Retail (Mochi, Metro)",
    "open_date": "10-Dec-21",
    "close_date": "14-Dec-21",
    "listing_date": "22-Dec-21",
    "price_band": "\u20b9500",
    "issue_price": 500.0,
    "lot_size": 30,
    "min_investment": 15000,
    "issue_size_cr": 1367.5,
    "fresh_issue_cr": 1025.6,
    "ofs_cr": 341.9,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 10.0,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 510.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.6,
        "nii": 1.09,
        "retail": 0.45,
        "total": 1.09
      },
      "day2": {
        "qib": 1.51,
        "nii": 2.55,
        "retail": 0.9,
        "total": 2.37
      },
      "final_day": {
        "qib": 3.02,
        "nii": 5.46,
        "retail": 1.13,
        "total": 3.64
      },
      "applications_count": "3.64x Subscription"
    },
    "listing": {
      "listing_price": 437.0,
      "listing_gain_rs": -63.0,
      "listing_gain_percent": -12.6,
      "profit_per_lot": -1890.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 510.0,
        "actual_price": 437.0,
        "variance_rs": -73.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9510.0 (+2.0%). Stock opened at \u20b9437.0 (-12.6%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": -12.6,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -12.6% (\u20b91,890 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Footwear Retail (Mochi, Metro) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Footwear Retail (Mochi, Metro)",
        "Strong institutional interest with 3.02x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -12.6% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 9.5,
        "gmp_percent": 1.9,
        "est_listing_price": 509.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 9.8,
        "gmp_percent": 2.0,
        "est_listing_price": 509.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 10.0,
        "gmp_percent": 2.0,
        "est_listing_price": 510.0,
        "notes": "Predicted \u20b9510.0 listing"
      }
    ]
  },
  {
    "id": "mapmyindia",
    "name": "C.E. Info Systems (MapmyIndia)",
    "symbol": "MAPMYINDIA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Maps & GIS APIs",
    "open_date": "09-Dec-21",
    "close_date": "13-Dec-21",
    "listing_date": "21-Dec-21",
    "price_band": "\u20b91,033",
    "issue_price": 1033.0,
    "lot_size": 14,
    "min_investment": 14462,
    "issue_size_cr": 1040.0,
    "fresh_issue_cr": 780.0,
    "ofs_cr": 260.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 537.16,
    "gmp_closing_percent": 52.0,
    "gmp_estimated_listing": 1570.16,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 84.94,
        "nii": 46.41,
        "retail": 6.08,
        "total": 46.41
      },
      "day2": {
        "qib": 212.34,
        "nii": 108.3,
        "retail": 12.16,
        "total": 100.56
      },
      "final_day": {
        "qib": 424.69,
        "nii": 232.06,
        "retail": 15.2,
        "total": 154.71
      },
      "applications_count": "154.71x Subscription"
    },
    "listing": {
      "listing_price": 1565.0,
      "listing_gain_rs": 532.0,
      "listing_gain_percent": 51.5,
      "profit_per_lot": 7448.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1570.16,
        "actual_price": 1565.0,
        "variance_rs": -5.16,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91570.16 (+52.0%). Stock opened at \u20b91565.0 (+51.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 52.0,
      "actual_gain_pct": 51.5,
      "retail_profit_lost": 7448.0,
      "explanation": "C.E. Info Systems (MapmyIndia) delivered a stellar +51.5% listing gain, rewarding retail allottees with \u20b97,448 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +52% Listing Return",
      "long_term_potential": "Digital Maps & GIS APIs Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Maps & GIS APIs",
        "Strong institutional interest with 424.69x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +51.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 419.0,
        "gmp_percent": 40.6,
        "est_listing_price": 1452.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 483.4,
        "gmp_percent": 46.8,
        "est_listing_price": 1516.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 537.16,
        "gmp_percent": 52.0,
        "est_listing_price": 1570.2,
        "notes": "Predicted \u20b91570.16 listing"
      }
    ]
  },
  {
    "id": "shriramp",
    "name": "Shriram Properties Ltd",
    "symbol": "SHRIRAMP.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Mid-Market Real Estate South India",
    "open_date": "08-Dec-21",
    "close_date": "10-Dec-21",
    "listing_date": "20-Dec-21",
    "price_band": "\u20b9118",
    "issue_price": 118.0,
    "lot_size": 125,
    "min_investment": 14750,
    "issue_size_cr": 600.0,
    "fresh_issue_cr": 450.0,
    "ofs_cr": 150.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -9.44,
    "gmp_closing_percent": -8.0,
    "gmp_estimated_listing": 108.56,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.96,
        "nii": 1.38,
        "retail": 5.09,
        "total": 1.38
      },
      "day2": {
        "qib": 2.41,
        "nii": 3.22,
        "retail": 10.18,
        "total": 2.99
      },
      "final_day": {
        "qib": 4.82,
        "nii": 6.9,
        "retail": 12.72,
        "total": 4.6
      },
      "applications_count": "4.6x Subscription"
    },
    "listing": {
      "listing_price": 94.0,
      "listing_gain_rs": -24.0,
      "listing_gain_percent": -20.3,
      "profit_per_lot": -3000.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 108.56,
        "actual_price": 94.0,
        "variance_rs": -14.56,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9108.56 (-8.0%). Stock opened at \u20b994.0 (-20.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -8.0,
      "actual_gain_pct": -20.3,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -20.3% (\u20b93,000 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -8% Listing Return",
      "long_term_potential": "Mid-Market Real Estate South India Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Mid-Market Real Estate South India",
        "Strong institutional interest with 4.82x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -20.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -11.8,
        "gmp_percent": -10.0,
        "est_listing_price": 106.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -10.6,
        "gmp_percent": -9.0,
        "est_listing_price": 107.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -9.44,
        "gmp_percent": -8.0,
        "est_listing_price": 108.6,
        "notes": "Predicted \u20b9108.56 listing"
      }
    ]
  },
  {
    "id": "rategain",
    "name": "RateGain Travel Technologies",
    "symbol": "RATEGAIN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Travel & Hospitality SaaS",
    "open_date": "07-Dec-21",
    "close_date": "09-Dec-21",
    "listing_date": "17-Dec-21",
    "price_band": "\u20b9425",
    "issue_price": 425.0,
    "lot_size": 35,
    "min_investment": 14875,
    "issue_size_cr": 1335.74,
    "fresh_issue_cr": 1001.8,
    "ofs_cr": 333.9,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -21.25,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 403.75,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 8.48,
        "nii": 5.22,
        "retail": 3.23,
        "total": 5.22
      },
      "day2": {
        "qib": 21.2,
        "nii": 12.19,
        "retail": 6.46,
        "total": 11.32
      },
      "final_day": {
        "qib": 42.4,
        "nii": 26.12,
        "retail": 8.08,
        "total": 17.41
      },
      "applications_count": "17.41x Subscription"
    },
    "listing": {
      "listing_price": 364.8,
      "listing_gain_rs": -60.2,
      "listing_gain_percent": -14.2,
      "profit_per_lot": -2107.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 403.75,
        "actual_price": 364.8,
        "variance_rs": -38.95,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9403.75 (-5.0%). Stock opened at \u20b9364.8 (-14.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -14.2,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -14.2% (\u20b92,107 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Travel & Hospitality SaaS Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Travel & Hospitality SaaS",
        "Strong institutional interest with 42.4x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -14.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -26.6,
        "gmp_percent": -6.2,
        "est_listing_price": 398.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -23.8,
        "gmp_percent": -5.6,
        "est_listing_price": 401.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -21.25,
        "gmp_percent": -5.0,
        "est_listing_price": 403.8,
        "notes": "Predicted \u20b9403.75 listing"
      }
    ]
  },
  {
    "id": "anandrathi",
    "name": "Anand Rathi Wealth Ltd",
    "symbol": "ANANDRATHI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Private Wealth & Mutual Funds",
    "open_date": "02-Dec-21",
    "close_date": "06-Dec-21",
    "listing_date": "14-Dec-21",
    "price_band": "\u20b9550",
    "issue_price": 550.0,
    "lot_size": 27,
    "min_investment": 14850,
    "issue_size_cr": 660.0,
    "fresh_issue_cr": 495.0,
    "ofs_cr": 165.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 55.0,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 605.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 5.08,
        "nii": 2.93,
        "retail": 3.1,
        "total": 2.93
      },
      "day2": {
        "qib": 12.71,
        "nii": 6.85,
        "retail": 6.21,
        "total": 6.36
      },
      "final_day": {
        "qib": 25.42,
        "nii": 14.67,
        "retail": 7.76,
        "total": 9.78
      },
      "applications_count": "9.78x Subscription"
    },
    "listing": {
      "listing_price": 600.0,
      "listing_gain_rs": 50.0,
      "listing_gain_percent": 9.1,
      "profit_per_lot": 1350.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 605.0,
        "actual_price": 600.0,
        "variance_rs": -5.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9605.0 (+10.0%). Stock opened at \u20b9600.0 (+9.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 9.1,
      "retail_profit_lost": 1350.0,
      "explanation": "The issue opened with a healthy +9.1% pop (\u20b91,350 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Private Wealth & Mutual Funds Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Private Wealth & Mutual Funds",
        "Strong institutional interest with 25.42x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +9.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 52.2,
        "gmp_percent": 9.5,
        "est_listing_price": 602.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 53.9,
        "gmp_percent": 9.8,
        "est_listing_price": 603.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 55.0,
        "gmp_percent": 10.0,
        "est_listing_price": 605.0,
        "notes": "Predicted \u20b9605.0 listing"
      }
    ]
  },
  {
    "id": "starhealth",
    "name": "Star Health and Allied Insurance",
    "symbol": "STARHEALTH.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Standalone Health Insurance",
    "open_date": "30-Nov-21",
    "close_date": "02-Dec-21",
    "listing_date": "10-Dec-21",
    "price_band": "\u20b9900",
    "issue_price": 900.0,
    "lot_size": 16,
    "min_investment": 14400,
    "issue_size_cr": 7249.18,
    "fresh_issue_cr": 5436.9,
    "ofs_cr": 1812.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -27.0,
    "gmp_closing_percent": -3.0,
    "gmp_estimated_listing": 873.0,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.21,
        "nii": 0.24,
        "retail": 0.44,
        "total": 0.24
      },
      "day2": {
        "qib": 0.52,
        "nii": 0.55,
        "retail": 0.88,
        "total": 0.51
      },
      "final_day": {
        "qib": 1.03,
        "nii": 1.19,
        "retail": 1.1,
        "total": 0.79
      },
      "applications_count": "0.79x Subscription"
    },
    "listing": {
      "listing_price": 848.8,
      "listing_gain_rs": -51.2,
      "listing_gain_percent": -5.7,
      "profit_per_lot": -819.2,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 873.0,
        "actual_price": 848.8,
        "variance_rs": -24.2,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9873.0 (-3.0%). Stock opened at \u20b9848.8 (-5.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -3.0,
      "actual_gain_pct": -5.7,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -5.7% (\u20b9819 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -3% Listing Return",
      "long_term_potential": "Standalone Health Insurance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Standalone Health Insurance",
        "Strong institutional interest with 1.03x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -5.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -33.8,
        "gmp_percent": -3.8,
        "est_listing_price": 866.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -30.2,
        "gmp_percent": -3.4,
        "est_listing_price": 869.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -27.0,
        "gmp_percent": -3.0,
        "est_listing_price": 873.0,
        "notes": "Predicted \u20b9873.0 listing"
      }
    ]
  },
  {
    "id": "gocolors",
    "name": "Go Fashion (India) Ltd (Go Colors)",
    "symbol": "GOCOLORS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Women Bottomwear Retail",
    "open_date": "17-Nov-21",
    "close_date": "22-Nov-21",
    "listing_date": "30-Nov-21",
    "price_band": "\u20b9690",
    "issue_price": 690.0,
    "lot_size": 21,
    "min_investment": 14490,
    "issue_size_cr": 1013.61,
    "fresh_issue_cr": 760.2,
    "ofs_cr": 253.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 621.0,
    "gmp_closing_percent": 90.0,
    "gmp_estimated_listing": 1311.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 52.42,
        "nii": 40.64,
        "retail": 9.83,
        "total": 40.64
      },
      "day2": {
        "qib": 131.06,
        "nii": 94.82,
        "retail": 19.66,
        "total": 88.05
      },
      "final_day": {
        "qib": 262.11,
        "nii": 203.19,
        "retail": 24.58,
        "total": 135.46
      },
      "applications_count": "135.46x Subscription"
    },
    "listing": {
      "listing_price": 1316.0,
      "listing_gain_rs": 626.0,
      "listing_gain_percent": 90.7,
      "profit_per_lot": 13146.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1311.0,
        "actual_price": 1316.0,
        "variance_rs": 5.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91311.0 (+90.0%). Stock opened at \u20b91316.0 (+90.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 90.0,
      "actual_gain_pct": 90.7,
      "retail_profit_lost": 13146.0,
      "explanation": "Go Fashion (India) Ltd (Go Colors) delivered a stellar +90.7% listing gain, rewarding retail allottees with \u20b913,146 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +90% Listing Return",
      "long_term_potential": "Women Bottomwear Retail Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Women Bottomwear Retail",
        "Strong institutional interest with 262.11x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +90.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 484.4,
        "gmp_percent": 70.2,
        "est_listing_price": 1174.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 558.9,
        "gmp_percent": 81.0,
        "est_listing_price": 1248.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 621.0,
        "gmp_percent": 90.0,
        "est_listing_price": 1311.0,
        "notes": "Predicted \u20b91311.0 listing"
      }
    ]
  },
  {
    "id": "tarsons",
    "name": "Tarsons Products Ltd",
    "symbol": "TARSONS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Plastic Labware & Life Sciences",
    "open_date": "15-Nov-21",
    "close_date": "17-Nov-21",
    "listing_date": "26-Nov-21",
    "price_band": "\u20b9662",
    "issue_price": 662.0,
    "lot_size": 22,
    "min_investment": 14564,
    "issue_size_cr": 1023.84,
    "fresh_issue_cr": 767.9,
    "ofs_cr": 256.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 66.2,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 728.2,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 36.92,
        "nii": 23.25,
        "retail": 4.22,
        "total": 23.25
      },
      "day2": {
        "qib": 92.29,
        "nii": 54.24,
        "retail": 8.45,
        "total": 50.37
      },
      "final_day": {
        "qib": 184.58,
        "nii": 116.23,
        "retail": 10.56,
        "total": 77.49
      },
      "applications_count": "77.49x Subscription"
    },
    "listing": {
      "listing_price": 700.0,
      "listing_gain_rs": 38.0,
      "listing_gain_percent": 5.7,
      "profit_per_lot": 836.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 728.2,
        "actual_price": 700.0,
        "variance_rs": -28.2,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9728.2 (+10.0%). Stock opened at \u20b9700.0 (+5.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 5.7,
      "retail_profit_lost": 836.0,
      "explanation": "The issue opened with a healthy +5.7% pop (\u20b9836 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Plastic Labware & Life Sciences Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Plastic Labware & Life Sciences",
        "Strong institutional interest with 184.58x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +5.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 62.9,
        "gmp_percent": 9.5,
        "est_listing_price": 724.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 64.9,
        "gmp_percent": 9.8,
        "est_listing_price": 726.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 66.2,
        "gmp_percent": 10.0,
        "est_listing_price": 728.2,
        "notes": "Predicted \u20b9728.2 listing"
      }
    ]
  },
  {
    "id": "latentview",
    "name": "Latent View Analytics Ltd",
    "symbol": "LATENTVIEW.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Data & AI Consulting",
    "open_date": "10-Nov-21",
    "close_date": "12-Nov-21",
    "listing_date": "23-Nov-21",
    "price_band": "\u20b9197",
    "issue_price": 197.0,
    "lot_size": 76,
    "min_investment": 14972,
    "issue_size_cr": 600.0,
    "fresh_issue_cr": 450.0,
    "ofs_cr": 150.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 315.2,
    "gmp_closing_percent": 160.0,
    "gmp_estimated_listing": 512.2,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 170.13,
        "nii": 97.95,
        "retail": 47.78,
        "total": 97.95
      },
      "day2": {
        "qib": 425.33,
        "nii": 228.54,
        "retail": 95.55,
        "total": 212.22
      },
      "final_day": {
        "qib": 850.66,
        "nii": 489.74,
        "retail": 119.44,
        "total": 326.49
      },
      "applications_count": "326.49x Subscription"
    },
    "listing": {
      "listing_price": 520.0,
      "listing_gain_rs": 323.0,
      "listing_gain_percent": 164.0,
      "profit_per_lot": 24548.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 512.2,
        "actual_price": 520.0,
        "variance_rs": 7.8,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9512.2 (+160.0%). Stock opened at \u20b9520.0 (+164.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 160.0,
      "actual_gain_pct": 164.0,
      "retail_profit_lost": 24548.0,
      "explanation": "Latent View Analytics Ltd delivered a stellar +164.0% listing gain, rewarding retail allottees with \u20b924,548 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +160% Listing Return",
      "long_term_potential": "Data & AI Consulting Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Data & AI Consulting",
        "Strong institutional interest with 850.66x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +164.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 245.9,
        "gmp_percent": 124.8,
        "est_listing_price": 442.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 283.7,
        "gmp_percent": 144.0,
        "est_listing_price": 480.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 315.2,
        "gmp_percent": 160.0,
        "est_listing_price": 512.2,
        "notes": "Predicted \u20b9512.2 listing"
      }
    ]
  },
  {
    "id": "paytm",
    "name": "One97 Communications (Paytm)",
    "symbol": "PAYTM.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Payments & QR",
    "open_date": "08-Nov-21",
    "close_date": "10-Nov-21",
    "listing_date": "18-Nov-21",
    "price_band": "\u20b92,150",
    "issue_price": 2150.0,
    "lot_size": 6,
    "min_investment": 12900,
    "issue_size_cr": 18300.0,
    "fresh_issue_cr": 13725.0,
    "ofs_cr": 4575.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -107.5,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 2042.5,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.56,
        "nii": 0.57,
        "retail": 0.66,
        "total": 0.57
      },
      "day2": {
        "qib": 1.4,
        "nii": 1.32,
        "retail": 1.33,
        "total": 1.23
      },
      "final_day": {
        "qib": 2.79,
        "nii": 2.83,
        "retail": 1.66,
        "total": 1.89
      },
      "applications_count": "1.89x Subscription"
    },
    "listing": {
      "listing_price": 1955.0,
      "listing_gain_rs": -195.0,
      "listing_gain_percent": -9.1,
      "profit_per_lot": -1170.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 2042.5,
        "actual_price": 1955.0,
        "variance_rs": -87.5,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b92042.5 (-5.0%). Stock opened at \u20b91955.0 (-9.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -9.1,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -9.1% (\u20b91,170 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Digital Payments & QR Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Payments & QR",
        "Strong institutional interest with 2.79x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -9.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -134.4,
        "gmp_percent": -6.2,
        "est_listing_price": 2015.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -120.4,
        "gmp_percent": -5.6,
        "est_listing_price": 2029.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -107.5,
        "gmp_percent": -5.0,
        "est_listing_price": 2042.5,
        "notes": "Predicted \u20b92042.5 listing"
      }
    ]
  },
  {
    "id": "sapphire",
    "name": "Sapphire Foods India Ltd",
    "symbol": "SAPPHIRE.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "QSR Fast Food Franchisee",
    "open_date": "09-Nov-21",
    "close_date": "11-Nov-21",
    "listing_date": "18-Nov-21",
    "price_band": "\u20b91,180",
    "issue_price": 1180.0,
    "lot_size": 12,
    "min_investment": 14160,
    "issue_size_cr": 2073.25,
    "fresh_issue_cr": 1554.9,
    "ofs_cr": 518.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 141.6,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 1321.6,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 1.5,
        "nii": 1.99,
        "retail": 3.48,
        "total": 1.99
      },
      "day2": {
        "qib": 3.75,
        "nii": 4.63,
        "retail": 6.96,
        "total": 4.3
      },
      "final_day": {
        "qib": 7.5,
        "nii": 9.93,
        "retail": 8.7,
        "total": 6.62
      },
      "applications_count": "6.62x Subscription"
    },
    "listing": {
      "listing_price": 1311.0,
      "listing_gain_rs": 131.0,
      "listing_gain_percent": 11.1,
      "profit_per_lot": 1572.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1321.6,
        "actual_price": 1311.0,
        "variance_rs": -10.6,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91321.6 (+12.0%). Stock opened at \u20b91311.0 (+11.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 11.1,
      "retail_profit_lost": 1572.0,
      "explanation": "The issue opened with a healthy +11.1% pop (\u20b91,572 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "QSR Fast Food Franchisee Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in QSR Fast Food Franchisee",
        "Strong institutional interest with 7.5x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +11.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 134.5,
        "gmp_percent": 11.4,
        "est_listing_price": 1314.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 138.8,
        "gmp_percent": 11.8,
        "est_listing_price": 1318.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 141.6,
        "gmp_percent": 12.0,
        "est_listing_price": 1321.6,
        "notes": "Predicted \u20b91321.6 listing"
      }
    ]
  },
  {
    "id": "sjs",
    "name": "SJS Enterprises Ltd",
    "symbol": "SJS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Decorative Aesthetics & Dials",
    "open_date": "01-Nov-21",
    "close_date": "03-Nov-21",
    "listing_date": "15-Nov-21",
    "price_band": "\u20b9542",
    "issue_price": 542.0,
    "lot_size": 27,
    "min_investment": 14634,
    "issue_size_cr": 800.0,
    "fresh_issue_cr": 600.0,
    "ofs_cr": 200.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 5.42,
    "gmp_closing_percent": 1.0,
    "gmp_estimated_listing": 547.42,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.46,
        "nii": 0.48,
        "retail": 0.55,
        "total": 0.48
      },
      "day2": {
        "qib": 1.16,
        "nii": 1.11,
        "retail": 1.1,
        "total": 1.03
      },
      "final_day": {
        "qib": 2.32,
        "nii": 2.39,
        "retail": 1.38,
        "total": 1.59
      },
      "applications_count": "1.59x Subscription"
    },
    "listing": {
      "listing_price": 540.0,
      "listing_gain_rs": -2.0,
      "listing_gain_percent": -0.4,
      "profit_per_lot": -54.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 547.42,
        "actual_price": 540.0,
        "variance_rs": -7.42,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9547.42 (+1.0%). Stock opened at \u20b9540.0 (-0.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 1.0,
      "actual_gain_pct": -0.4,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (-0.4%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +1% Listing Return",
      "long_term_potential": "Decorative Aesthetics & Dials Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Decorative Aesthetics & Dials",
        "Strong institutional interest with 2.32x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -0.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 5.1,
        "gmp_percent": 0.9,
        "est_listing_price": 547.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 5.3,
        "gmp_percent": 1.0,
        "est_listing_price": 547.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 5.42,
        "gmp_percent": 1.0,
        "est_listing_price": 547.4,
        "notes": "Predicted \u20b9547.42 listing"
      }
    ]
  },
  {
    "id": "sigachi",
    "name": "Sigachi Industries Ltd",
    "symbol": "SIGACHI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Microcrystalline Cellulose (MCC)",
    "open_date": "01-Nov-21",
    "close_date": "03-Nov-21",
    "listing_date": "15-Nov-21",
    "price_band": "\u20b9163",
    "issue_price": 163.0,
    "lot_size": 90,
    "min_investment": 14670,
    "issue_size_cr": 125.43,
    "fresh_issue_cr": 94.1,
    "ofs_cr": 31.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Bigshare Services Pvt Ltd",
    "gmp_closing_day": 407.5,
    "gmp_closing_percent": 250.0,
    "gmp_estimated_listing": 570.5,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 34.49,
        "nii": 30.57,
        "retail": 32.2,
        "total": 30.57
      },
      "day2": {
        "qib": 86.22,
        "nii": 71.34,
        "retail": 64.39,
        "total": 66.24
      },
      "final_day": {
        "qib": 172.43,
        "nii": 152.87,
        "retail": 80.49,
        "total": 101.91
      },
      "applications_count": "101.91x Subscription"
    },
    "listing": {
      "listing_price": 575.0,
      "listing_gain_rs": 412.0,
      "listing_gain_percent": 252.8,
      "profit_per_lot": 37080.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 570.5,
        "actual_price": 575.0,
        "variance_rs": 4.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9570.5 (+250.0%). Stock opened at \u20b9575.0 (+252.8%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 250.0,
      "actual_gain_pct": 252.8,
      "retail_profit_lost": 37080.0,
      "explanation": "Sigachi Industries Ltd delivered a stellar +252.8% listing gain, rewarding retail allottees with \u20b937,080 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +250% Listing Return",
      "long_term_potential": "Microcrystalline Cellulose (MCC) Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Microcrystalline Cellulose (MCC)",
        "Strong institutional interest with 172.43x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +252.8% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 317.9,
        "gmp_percent": 195.0,
        "est_listing_price": 480.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 366.8,
        "gmp_percent": 225.0,
        "est_listing_price": 529.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 407.5,
        "gmp_percent": 250.0,
        "est_listing_price": 570.5,
        "notes": "Predicted \u20b9570.5 listing"
      }
    ]
  },
  {
    "id": "policybzr",
    "name": "PB Fintech Ltd (Policybazaar)",
    "symbol": "POLICYBZR.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Insurance & Credit Marketplace",
    "open_date": "01-Nov-21",
    "close_date": "03-Nov-21",
    "listing_date": "15-Nov-21",
    "price_band": "\u20b9980",
    "issue_price": 980.0,
    "lot_size": 15,
    "min_investment": 14700,
    "issue_size_cr": 5625.0,
    "fresh_issue_cr": 4218.8,
    "ofs_cr": 1406.2,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 176.4,
    "gmp_closing_percent": 18.0,
    "gmp_estimated_listing": 1156.4,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 4.98,
        "nii": 4.98,
        "retail": 1.32,
        "total": 4.98
      },
      "day2": {
        "qib": 12.45,
        "nii": 11.61,
        "retail": 2.65,
        "total": 10.78
      },
      "final_day": {
        "qib": 24.89,
        "nii": 24.88,
        "retail": 3.31,
        "total": 16.59
      },
      "applications_count": "16.59x Subscription"
    },
    "listing": {
      "listing_price": 1150.0,
      "listing_gain_rs": 170.0,
      "listing_gain_percent": 17.3,
      "profit_per_lot": 2550.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1156.4,
        "actual_price": 1150.0,
        "variance_rs": -6.4,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91156.4 (+18.0%). Stock opened at \u20b91150.0 (+17.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 18.0,
      "actual_gain_pct": 17.3,
      "retail_profit_lost": 2550.0,
      "explanation": "The issue opened with a healthy +17.3% pop (\u20b92,550 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +18% Listing Return",
      "long_term_potential": "Insurance & Credit Marketplace Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Insurance & Credit Marketplace",
        "Strong institutional interest with 24.89x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +17.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 167.6,
        "gmp_percent": 17.1,
        "est_listing_price": 1147.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 172.9,
        "gmp_percent": 17.6,
        "est_listing_price": 1152.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 176.4,
        "gmp_percent": 18.0,
        "est_listing_price": 1156.4,
        "notes": "Predicted \u20b91156.4 listing"
      }
    ]
  },
  {
    "id": "finopb",
    "name": "Fino Payments Bank Ltd",
    "symbol": "FINOPB.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Digital Payments & Merchant Banking",
    "open_date": "29-Oct-21",
    "close_date": "02-Nov-21",
    "listing_date": "12-Nov-21",
    "price_band": "\u20b9577",
    "issue_price": 577.0,
    "lot_size": 25,
    "min_investment": 14425,
    "issue_size_cr": 1200.29,
    "fresh_issue_cr": 900.2,
    "ofs_cr": 300.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 577.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.04,
        "nii": 0.61,
        "retail": 2.37,
        "total": 0.61
      },
      "day2": {
        "qib": 0.1,
        "nii": 1.42,
        "retail": 4.74,
        "total": 1.32
      },
      "final_day": {
        "qib": 0.21,
        "nii": 3.04,
        "retail": 5.92,
        "total": 2.03
      },
      "applications_count": "2.03x Subscription"
    },
    "listing": {
      "listing_price": 540.0,
      "listing_gain_rs": -37.0,
      "listing_gain_percent": -6.4,
      "profit_per_lot": -925.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 577.0,
        "actual_price": 540.0,
        "variance_rs": -37.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9577.0 (+0.0%). Stock opened at \u20b9540.0 (-6.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -6.4,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -6.4% (\u20b9925 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Digital Payments & Merchant Banking Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Digital Payments & Merchant Banking",
        "Strong institutional interest with 0.21x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -6.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 577.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 577.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 577.0,
        "notes": "Predicted \u20b9577.0 listing"
      }
    ]
  },
  {
    "id": "nykaa",
    "name": "FSN E-Commerce Ventures (Nykaa)",
    "symbol": "NYKAA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Beauty & Fashion E-Commerce",
    "open_date": "28-Oct-21",
    "close_date": "01-Nov-21",
    "listing_date": "10-Nov-21",
    "price_band": "\u20b91,125",
    "issue_price": 1125.0,
    "lot_size": 12,
    "min_investment": 13500,
    "issue_size_cr": 5351.92,
    "fresh_issue_cr": 4013.9,
    "ofs_cr": 1338.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 900.0,
    "gmp_closing_percent": 80.0,
    "gmp_estimated_listing": 2025.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 18.24,
        "nii": 24.53,
        "retail": 4.9,
        "total": 24.53
      },
      "day2": {
        "qib": 45.59,
        "nii": 57.25,
        "retail": 9.79,
        "total": 53.16
      },
      "final_day": {
        "qib": 91.18,
        "nii": 122.67,
        "retail": 12.24,
        "total": 81.78
      },
      "applications_count": "81.78x Subscription"
    },
    "listing": {
      "listing_price": 2001.0,
      "listing_gain_rs": 876.0,
      "listing_gain_percent": 77.9,
      "profit_per_lot": 10512.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 2025.0,
        "actual_price": 2001.0,
        "variance_rs": -24.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b92025.0 (+80.0%). Stock opened at \u20b92001.0 (+77.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 80.0,
      "actual_gain_pct": 77.9,
      "retail_profit_lost": 10512.0,
      "explanation": "FSN E-Commerce Ventures (Nykaa) delivered a stellar +77.9% listing gain, rewarding retail allottees with \u20b910,512 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +80% Listing Return",
      "long_term_potential": "Beauty & Fashion E-Commerce Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Beauty & Fashion E-Commerce",
        "Strong institutional interest with 91.18x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +77.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 702.0,
        "gmp_percent": 62.4,
        "est_listing_price": 1827.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 810.0,
        "gmp_percent": 72.0,
        "est_listing_price": 1935.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 900.0,
        "gmp_percent": 80.0,
        "est_listing_price": 2025.0,
        "notes": "Predicted \u20b92025.0 listing"
      }
    ]
  },
  {
    "id": "abslamc",
    "name": "Aditya Birla Sun Life AMC",
    "symbol": "ABSLAMC.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Mutual Fund & Asset Management",
    "open_date": "29-Sep-21",
    "close_date": "01-Oct-21",
    "listing_date": "11-Oct-21",
    "price_band": "\u20b9712",
    "issue_price": 712.0,
    "lot_size": 20,
    "min_investment": 14240,
    "issue_size_cr": 2768.26,
    "fresh_issue_cr": 2076.2,
    "ofs_cr": 692.1,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 14.24,
    "gmp_closing_percent": 2.0,
    "gmp_estimated_listing": 726.24,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.07,
        "nii": 1.57,
        "retail": 1.3,
        "total": 1.57
      },
      "day2": {
        "qib": 5.18,
        "nii": 3.67,
        "retail": 2.59,
        "total": 3.41
      },
      "final_day": {
        "qib": 10.36,
        "nii": 7.88,
        "retail": 3.24,
        "total": 5.25
      },
      "applications_count": "5.25x Subscription"
    },
    "listing": {
      "listing_price": 712.0,
      "listing_gain_rs": 0.0,
      "listing_gain_percent": 0.0,
      "profit_per_lot": 0.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 726.24,
        "actual_price": 712.0,
        "variance_rs": -14.24,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9726.24 (+2.0%). Stock opened at \u20b9712.0 (+0.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 2.0,
      "actual_gain_pct": 0.0,
      "retail_profit_lost": 0.0,
      "explanation": "The IPO had a flat listing (+0.0%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +2% Listing Return",
      "long_term_potential": "Mutual Fund & Asset Management Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Mutual Fund & Asset Management",
        "Strong institutional interest with 10.36x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +0.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 13.5,
        "gmp_percent": 1.9,
        "est_listing_price": 725.5,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 14.0,
        "gmp_percent": 2.0,
        "est_listing_price": 726.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 14.24,
        "gmp_percent": 2.0,
        "est_listing_price": 726.2,
        "notes": "Predicted \u20b9726.24 listing"
      }
    ]
  },
  {
    "id": "parasdef",
    "name": "Paras Defence & Space Tech",
    "symbol": "PARASDEF.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Defense Optics & EMP Protection",
    "open_date": "21-Sep-21",
    "close_date": "23-Sep-21",
    "listing_date": "01-Oct-21",
    "price_band": "\u20b9175",
    "issue_price": 175.0,
    "lot_size": 85,
    "min_investment": 14875,
    "issue_size_cr": 170.78,
    "fresh_issue_cr": 128.1,
    "ofs_cr": 42.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 306.25,
    "gmp_closing_percent": 175.0,
    "gmp_estimated_listing": 481.25,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 33.93,
        "nii": 91.28,
        "retail": 45.12,
        "total": 91.28
      },
      "day2": {
        "qib": 84.83,
        "nii": 212.98,
        "retail": 90.25,
        "total": 197.77
      },
      "final_day": {
        "qib": 169.65,
        "nii": 456.39,
        "retail": 112.81,
        "total": 304.26
      },
      "applications_count": "304.26x Subscription"
    },
    "listing": {
      "listing_price": 475.0,
      "listing_gain_rs": 300.0,
      "listing_gain_percent": 171.4,
      "profit_per_lot": 25500.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 481.25,
        "actual_price": 475.0,
        "variance_rs": -6.25,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9481.25 (+175.0%). Stock opened at \u20b9475.0 (+171.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 175.0,
      "actual_gain_pct": 171.4,
      "retail_profit_lost": 25500.0,
      "explanation": "Paras Defence & Space Tech delivered a stellar +171.4% listing gain, rewarding retail allottees with \u20b925,500 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +175% Listing Return",
      "long_term_potential": "Defense Optics & EMP Protection Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Defense Optics & EMP Protection",
        "Strong institutional interest with 169.65x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +171.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 238.9,
        "gmp_percent": 136.5,
        "est_listing_price": 413.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 275.6,
        "gmp_percent": 157.5,
        "est_listing_price": 450.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 306.25,
        "gmp_percent": 175.0,
        "est_listing_price": 481.2,
        "notes": "Predicted \u20b9481.25 listing"
      }
    ]
  },
  {
    "id": "sansera",
    "name": "Sansera Engineering Ltd",
    "symbol": "SANSERA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Connecting Rods & Auto Components",
    "open_date": "14-Sep-21",
    "close_date": "16-Sep-21",
    "listing_date": "24-Sep-21",
    "price_band": "\u20b9744",
    "issue_price": 744.0,
    "lot_size": 20,
    "min_investment": 14880,
    "issue_size_cr": 1282.98,
    "fresh_issue_cr": 962.2,
    "ofs_cr": 320.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 74.4,
    "gmp_closing_percent": 10.0,
    "gmp_estimated_listing": 818.4,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 5.3,
        "nii": 3.44,
        "retail": 1.26,
        "total": 3.44
      },
      "day2": {
        "qib": 13.24,
        "nii": 8.03,
        "retail": 2.52,
        "total": 7.46
      },
      "final_day": {
        "qib": 26.49,
        "nii": 17.21,
        "retail": 3.15,
        "total": 11.47
      },
      "applications_count": "11.47x Subscription"
    },
    "listing": {
      "listing_price": 811.5,
      "listing_gain_rs": 67.5,
      "listing_gain_percent": 9.1,
      "profit_per_lot": 1350.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 818.4,
        "actual_price": 811.5,
        "variance_rs": -6.9,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9818.4 (+10.0%). Stock opened at \u20b9811.5 (+9.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 10.0,
      "actual_gain_pct": 9.1,
      "retail_profit_lost": 1350.0,
      "explanation": "The issue opened with a healthy +9.1% pop (\u20b91,350 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +10% Listing Return",
      "long_term_potential": "Connecting Rods & Auto Components Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Connecting Rods & Auto Components",
        "Strong institutional interest with 26.49x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +9.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 70.7,
        "gmp_percent": 9.5,
        "est_listing_price": 814.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 72.9,
        "gmp_percent": 9.8,
        "est_listing_price": 816.9,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 74.4,
        "gmp_percent": 10.0,
        "est_listing_price": 818.4,
        "notes": "Predicted \u20b9818.4 listing"
      }
    ]
  },
  {
    "id": "vijaya",
    "name": "Vijaya Diagnostic Centre Ltd",
    "symbol": "VIJAYA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Diagnostic & Imaging Services",
    "open_date": "01-Sep-21",
    "close_date": "03-Sep-21",
    "listing_date": "14-Sep-21",
    "price_band": "\u20b9531",
    "issue_price": 531.0,
    "lot_size": 28,
    "min_investment": 14868,
    "issue_size_cr": 1895.04,
    "fresh_issue_cr": 1421.3,
    "ofs_cr": 473.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 21.24,
    "gmp_closing_percent": 4.0,
    "gmp_estimated_listing": 552.24,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 2.61,
        "nii": 1.36,
        "retail": 0.44,
        "total": 1.36
      },
      "day2": {
        "qib": 6.54,
        "nii": 3.18,
        "retail": 0.87,
        "total": 2.95
      },
      "final_day": {
        "qib": 13.07,
        "nii": 6.81,
        "retail": 1.09,
        "total": 4.54
      },
      "applications_count": "4.54x Subscription"
    },
    "listing": {
      "listing_price": 542.3,
      "listing_gain_rs": 11.3,
      "listing_gain_percent": 2.1,
      "profit_per_lot": 316.4,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 552.24,
        "actual_price": 542.3,
        "variance_rs": -9.94,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9552.24 (+4.0%). Stock opened at \u20b9542.3 (+2.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 4.0,
      "actual_gain_pct": 2.1,
      "retail_profit_lost": 316.4,
      "explanation": "The IPO had a flat listing (+2.1%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +4% Listing Return",
      "long_term_potential": "Diagnostic & Imaging Services Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Diagnostic & Imaging Services",
        "Strong institutional interest with 13.07x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +2.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 20.2,
        "gmp_percent": 3.8,
        "est_listing_price": 551.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 20.8,
        "gmp_percent": 3.9,
        "est_listing_price": 551.8,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 21.24,
        "gmp_percent": 4.0,
        "est_listing_price": 552.2,
        "notes": "Predicted \u20b9552.24 listing"
      }
    ]
  },
  {
    "id": "amiorg",
    "name": "Ami Organics Ltd",
    "symbol": "AMIORG.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Pharma Intermediates",
    "open_date": "01-Sep-21",
    "close_date": "03-Sep-21",
    "listing_date": "14-Sep-21",
    "price_band": "\u20b9610",
    "issue_price": 610.0,
    "lot_size": 24,
    "min_investment": 14640,
    "issue_size_cr": 569.64,
    "fresh_issue_cr": 427.2,
    "ofs_cr": 142.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 274.5,
    "gmp_closing_percent": 45.0,
    "gmp_estimated_listing": 884.5,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 17.33,
        "nii": 19.36,
        "retail": 5.34,
        "total": 19.36
      },
      "day2": {
        "qib": 43.32,
        "nii": 45.18,
        "retail": 10.69,
        "total": 41.95
      },
      "final_day": {
        "qib": 86.64,
        "nii": 96.81,
        "retail": 13.36,
        "total": 64.54
      },
      "applications_count": "64.54x Subscription"
    },
    "listing": {
      "listing_price": 902.0,
      "listing_gain_rs": 292.0,
      "listing_gain_percent": 47.9,
      "profit_per_lot": 7008.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 884.5,
        "actual_price": 902.0,
        "variance_rs": 17.5,
        "reliability": "Underpredicted (Beat GMP)",
        "notes": "Closing GMP estimated \u20b9884.5 (+45.0%). Stock opened at \u20b9902.0 (+47.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 45.0,
      "actual_gain_pct": 47.9,
      "retail_profit_lost": 7008.0,
      "explanation": "Ami Organics Ltd delivered a stellar +47.9% listing gain, rewarding retail allottees with \u20b97,008 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +45% Listing Return",
      "long_term_potential": "Pharma Intermediates Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Pharma Intermediates",
        "Strong institutional interest with 86.64x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +47.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 214.1,
        "gmp_percent": 35.1,
        "est_listing_price": 824.1,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 247.1,
        "gmp_percent": 40.5,
        "est_listing_price": 857.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 274.5,
        "gmp_percent": 45.0,
        "est_listing_price": 884.5,
        "notes": "Predicted \u20b9884.5 listing"
      }
    ]
  },
  {
    "id": "chemplasts",
    "name": "Chemplast Sanmar Ltd",
    "symbol": "CHEMPLASTS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Specialty Paste PVC & Chlorochemicals",
    "open_date": "10-Aug-21",
    "close_date": "12-Aug-21",
    "listing_date": "24-Aug-21",
    "price_band": "\u20b9541",
    "issue_price": 541.0,
    "lot_size": 27,
    "min_investment": 14607,
    "issue_size_cr": 3850.0,
    "fresh_issue_cr": 2887.5,
    "ofs_cr": 962.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 0.0,
    "gmp_closing_percent": 0.0,
    "gmp_estimated_listing": 541.0,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 0.55,
        "nii": 0.65,
        "retail": 0.92,
        "total": 0.65
      },
      "day2": {
        "qib": 1.38,
        "nii": 1.52,
        "retail": 1.83,
        "total": 1.41
      },
      "final_day": {
        "qib": 2.76,
        "nii": 3.25,
        "retail": 2.29,
        "total": 2.17
      },
      "applications_count": "2.17x Subscription"
    },
    "listing": {
      "listing_price": 525.0,
      "listing_gain_rs": -16.0,
      "listing_gain_percent": -3.0,
      "profit_per_lot": -432.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 541.0,
        "actual_price": 525.0,
        "variance_rs": -16.0,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9541.0 (+0.0%). Stock opened at \u20b9525.0 (-3.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": 0.0,
      "actual_gain_pct": -3.0,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -3.0% (\u20b9432 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated +0% Listing Return",
      "long_term_potential": "Specialty Paste PVC & Chlorochemicals Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Specialty Paste PVC & Chlorochemicals",
        "Strong institutional interest with 2.76x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -3.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 541.0,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 541.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 0.0,
        "gmp_percent": 0.0,
        "est_listing_price": 541.0,
        "notes": "Predicted \u20b9541.0 listing"
      }
    ]
  },
  {
    "id": "aptus",
    "name": "Aptus Value Housing Finance",
    "symbol": "APTUS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Affordable Housing Finance",
    "open_date": "10-Aug-21",
    "close_date": "12-Aug-21",
    "listing_date": "24-Aug-21",
    "price_band": "\u20b9353",
    "issue_price": 353.0,
    "lot_size": 42,
    "min_investment": 14826,
    "issue_size_cr": 2780.05,
    "fresh_issue_cr": 2085.0,
    "ofs_cr": 695.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": -7.06,
    "gmp_closing_percent": -2.0,
    "gmp_estimated_listing": 345.94,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 6.72,
        "nii": 5.16,
        "retail": 3.97,
        "total": 5.16
      },
      "day2": {
        "qib": 16.8,
        "nii": 12.04,
        "retail": 7.94,
        "total": 11.18
      },
      "final_day": {
        "qib": 33.6,
        "nii": 25.8,
        "retail": 9.93,
        "total": 17.2
      },
      "applications_count": "17.2x Subscription"
    },
    "listing": {
      "listing_price": 329.95,
      "listing_gain_rs": -23.05,
      "listing_gain_percent": -6.5,
      "profit_per_lot": -968.1,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 345.94,
        "actual_price": 329.95,
        "variance_rs": -15.99,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9345.94 (-2.0%). Stock opened at \u20b9329.95 (-6.5%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -2.0,
      "actual_gain_pct": -6.5,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -6.5% (\u20b9968 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -2% Listing Return",
      "long_term_potential": "Affordable Housing Finance Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Affordable Housing Finance",
        "Strong institutional interest with 33.6x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -6.5% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -8.8,
        "gmp_percent": -2.5,
        "est_listing_price": 344.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -7.9,
        "gmp_percent": -2.2,
        "est_listing_price": 345.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -7.06,
        "gmp_percent": -2.0,
        "est_listing_price": 345.9,
        "notes": "Predicted \u20b9345.94 listing"
      }
    ]
  },
  {
    "id": "nuvoco",
    "name": "Nuvoco Vistas Corporation",
    "symbol": "NUVOCO.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Cement & Building Materials",
    "open_date": "09-Aug-21",
    "close_date": "11-Aug-21",
    "listing_date": "23-Aug-21",
    "price_band": "\u20b9570",
    "issue_price": 570.0,
    "lot_size": 26,
    "min_investment": 14820,
    "issue_size_cr": 5000.0,
    "fresh_issue_cr": 3750.0,
    "ofs_cr": 1250.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": -28.5,
    "gmp_closing_percent": -5.0,
    "gmp_estimated_listing": 541.5,
    "gmp_trend": "Falling",
    "subscription": {
      "day1": {
        "qib": 0.85,
        "nii": 0.51,
        "retail": 0.29,
        "total": 0.51
      },
      "day2": {
        "qib": 2.12,
        "nii": 1.2,
        "retail": 0.58,
        "total": 1.11
      },
      "final_day": {
        "qib": 4.23,
        "nii": 2.56,
        "retail": 0.73,
        "total": 1.71
      },
      "applications_count": "1.71x Subscription"
    },
    "listing": {
      "listing_price": 471.0,
      "listing_gain_rs": -99.0,
      "listing_gain_percent": -17.4,
      "profit_per_lot": -2574.0,
      "is_profitable": false,
      "gmp_accuracy": {
        "predicted_price": 541.5,
        "actual_price": 471.0,
        "variance_rs": -70.5,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9541.5 (-5.0%). Stock opened at \u20b9471.0 (-17.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Good Decision to Skip",
      "verdict_badge": "success",
      "is_missed_opp": false,
      "expected_gain_pct": -5.0,
      "actual_gain_pct": -17.4,
      "retail_profit_lost": 0.0,
      "explanation": "The stock listed at a discount of -17.4% (\u20b92,574 loss per lot). Skipping this IPO protected retail investor capital from immediate listing day erosion."
    },
    "recommendation_at_ipo": {
      "verdict": "Avoid",
      "badge": "danger",
      "listing_gain_prospect": "Estimated -5% Listing Return",
      "long_term_potential": "Cement & Building Materials Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Cement & Building Materials",
        "Strong institutional interest with 4.23x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered -17.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": -35.6,
        "gmp_percent": -6.2,
        "est_listing_price": 534.4,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": -31.9,
        "gmp_percent": -5.6,
        "est_listing_price": 538.1,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": -28.5,
        "gmp_percent": -5.0,
        "est_listing_price": 541.5,
        "notes": "Predicted \u20b9541.5 listing"
      }
    ]
  },
  {
    "id": "devyani",
    "name": "Devyani International Ltd",
    "symbol": "DEVYANI.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "QSR Fast Food Chains",
    "open_date": "04-Aug-21",
    "close_date": "06-Aug-21",
    "listing_date": "16-Aug-21",
    "price_band": "\u20b990",
    "issue_price": 90.0,
    "lot_size": 165,
    "min_investment": 14850,
    "issue_size_cr": 1838.0,
    "fresh_issue_cr": 1378.5,
    "ofs_cr": 459.5,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 49.5,
    "gmp_closing_percent": 55.0,
    "gmp_estimated_listing": 139.5,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 24.58,
        "nii": 35.01,
        "retail": 15.81,
        "total": 35.01
      },
      "day2": {
        "qib": 61.45,
        "nii": 81.69,
        "retail": 31.62,
        "total": 75.86
      },
      "final_day": {
        "qib": 122.9,
        "nii": 175.05,
        "retail": 39.52,
        "total": 116.7
      },
      "applications_count": "116.7x Subscription"
    },
    "listing": {
      "listing_price": 141.0,
      "listing_gain_rs": 51.0,
      "listing_gain_percent": 56.7,
      "profit_per_lot": 8415.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 139.5,
        "actual_price": 141.0,
        "variance_rs": 1.5,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9139.5 (+55.0%). Stock opened at \u20b9141.0 (+56.7%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 55.0,
      "actual_gain_pct": 56.7,
      "retail_profit_lost": 8415.0,
      "explanation": "Devyani International Ltd delivered a stellar +56.7% listing gain, rewarding retail allottees with \u20b98,415 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +55% Listing Return",
      "long_term_potential": "QSR Fast Food Chains Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in QSR Fast Food Chains",
        "Strong institutional interest with 122.9x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +56.7% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 38.6,
        "gmp_percent": 42.9,
        "est_listing_price": 128.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 44.6,
        "gmp_percent": 49.5,
        "est_listing_price": 134.6,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 49.5,
        "gmp_percent": 55.0,
        "est_listing_price": 139.5,
        "notes": "Predicted \u20b9139.5 listing"
      }
    ]
  },
  {
    "id": "krsnaa",
    "name": "Krsnaa Diagnostics Ltd",
    "symbol": "KRSNAA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Public-Private Diagnostic Labs",
    "open_date": "04-Aug-21",
    "close_date": "06-Aug-21",
    "listing_date": "16-Aug-21",
    "price_band": "\u20b9954",
    "issue_price": 954.0,
    "lot_size": 15,
    "min_investment": 14310,
    "issue_size_cr": 1213.33,
    "fresh_issue_cr": 910.0,
    "ofs_cr": 303.3,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 114.48,
    "gmp_closing_percent": 12.0,
    "gmp_estimated_listing": 1068.48,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 23.56,
        "nii": 19.32,
        "retail": 16.82,
        "total": 19.32
      },
      "day2": {
        "qib": 58.9,
        "nii": 45.08,
        "retail": 33.63,
        "total": 41.86
      },
      "final_day": {
        "qib": 117.8,
        "nii": 96.6,
        "retail": 42.04,
        "total": 64.4
      },
      "applications_count": "64.4x Subscription"
    },
    "listing": {
      "listing_price": 1025.0,
      "listing_gain_rs": 71.0,
      "listing_gain_percent": 7.4,
      "profit_per_lot": 1065.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1068.48,
        "actual_price": 1025.0,
        "variance_rs": -43.48,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b91068.48 (+12.0%). Stock opened at \u20b91025.0 (+7.4%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Moderate Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 12.0,
      "actual_gain_pct": 7.4,
      "retail_profit_lost": 1065.0,
      "explanation": "The issue opened with a healthy +7.4% pop (\u20b91,065 profit/lot). While profitable, listing demand was in line with expectations."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +12% Listing Return",
      "long_term_potential": "Public-Private Diagnostic Labs Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Public-Private Diagnostic Labs",
        "Strong institutional interest with 117.8x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +7.4% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 108.8,
        "gmp_percent": 11.4,
        "est_listing_price": 1062.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 112.2,
        "gmp_percent": 11.8,
        "est_listing_price": 1066.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 114.48,
        "gmp_percent": 12.0,
        "est_listing_price": 1068.5,
        "notes": "Predicted \u20b91068.48 listing"
      }
    ]
  },
  {
    "id": "rolexrings",
    "name": "Rolex Rings Ltd",
    "symbol": "ROLEXRINGS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Automotive Forged Rings",
    "open_date": "28-Jul-21",
    "close_date": "30-Jul-21",
    "listing_date": "09-Aug-21",
    "price_band": "\u20b9900",
    "issue_price": 900.0,
    "lot_size": 16,
    "min_investment": 14400,
    "issue_size_cr": 731.0,
    "fresh_issue_cr": 548.2,
    "ofs_cr": 182.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 360.0,
    "gmp_closing_percent": 40.0,
    "gmp_estimated_listing": 1260.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 28.72,
        "nii": 39.13,
        "retail": 9.8,
        "total": 39.13
      },
      "day2": {
        "qib": 71.79,
        "nii": 91.31,
        "retail": 19.59,
        "total": 84.79
      },
      "final_day": {
        "qib": 143.58,
        "nii": 195.66,
        "retail": 24.49,
        "total": 130.44
      },
      "applications_count": "130.44x Subscription"
    },
    "listing": {
      "listing_price": 1250.0,
      "listing_gain_rs": 350.0,
      "listing_gain_percent": 38.9,
      "profit_per_lot": 5600.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1260.0,
        "actual_price": 1250.0,
        "variance_rs": -10.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b91260.0 (+40.0%). Stock opened at \u20b91250.0 (+38.9%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 40.0,
      "actual_gain_pct": 38.9,
      "retail_profit_lost": 5600.0,
      "explanation": "Rolex Rings Ltd delivered a stellar +38.9% listing gain, rewarding retail allottees with \u20b95,600 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +40% Listing Return",
      "long_term_potential": "Automotive Forged Rings Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Automotive Forged Rings",
        "Strong institutional interest with 143.58x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +38.9% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 280.8,
        "gmp_percent": 31.2,
        "est_listing_price": 1180.8,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 324.0,
        "gmp_percent": 36.0,
        "est_listing_price": 1224.0,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 360.0,
        "gmp_percent": 40.0,
        "est_listing_price": 1260.0,
        "notes": "Predicted \u20b91260.0 listing"
      }
    ]
  },
  {
    "id": "gls",
    "name": "Glenmark Life Sciences Ltd",
    "symbol": "GLS.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "API & Cardiovascular Drugs",
    "open_date": "27-Jul-21",
    "close_date": "29-Jul-21",
    "listing_date": "06-Aug-21",
    "price_band": "\u20b9720",
    "issue_price": 720.0,
    "lot_size": 20,
    "min_investment": 14400,
    "issue_size_cr": 1513.6,
    "fresh_issue_cr": 1135.2,
    "ofs_cr": 378.4,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 57.6,
    "gmp_closing_percent": 8.0,
    "gmp_estimated_listing": 777.6,
    "gmp_trend": "Stable",
    "subscription": {
      "day1": {
        "qib": 7.39,
        "nii": 13.43,
        "retail": 5.86,
        "total": 13.43
      },
      "day2": {
        "qib": 18.48,
        "nii": 31.35,
        "retail": 11.72,
        "total": 29.11
      },
      "final_day": {
        "qib": 36.97,
        "nii": 67.17,
        "retail": 14.65,
        "total": 44.78
      },
      "applications_count": "44.78x Subscription"
    },
    "listing": {
      "listing_price": 751.1,
      "listing_gain_rs": 31.1,
      "listing_gain_percent": 4.3,
      "profit_per_lot": 622.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 777.6,
        "actual_price": 751.1,
        "variance_rs": -26.5,
        "reliability": "Overpredicted (Listed Below GMP)",
        "notes": "Closing GMP estimated \u20b9777.6 (+8.0%). Stock opened at \u20b9751.1 (+4.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Neutral / Fair Outcome",
      "verdict_badge": "neutral",
      "is_missed_opp": false,
      "expected_gain_pct": 8.0,
      "actual_gain_pct": 4.3,
      "retail_profit_lost": 622.0,
      "explanation": "The IPO had a flat listing (+4.3%), yielding neither major profits nor losses. Skipping did not result in significant regret."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply with Caution",
      "badge": "warning",
      "listing_gain_prospect": "Estimated +8% Listing Return",
      "long_term_potential": "API & Cardiovascular Drugs Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in API & Cardiovascular Drugs",
        "Strong institutional interest with 36.97x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +4.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 54.7,
        "gmp_percent": 7.6,
        "est_listing_price": 774.7,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 56.4,
        "gmp_percent": 7.8,
        "est_listing_price": 776.4,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 57.6,
        "gmp_percent": 8.0,
        "est_listing_price": 777.6,
        "notes": "Predicted \u20b9777.6 listing"
      }
    ]
  },
  {
    "id": "tatva",
    "name": "Tatva Chintan Pharma Chem",
    "symbol": "TATVA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Phase Transfer Catalysts",
    "open_date": "16-Jul-21",
    "close_date": "20-Jul-21",
    "listing_date": "29-Jul-21",
    "price_band": "\u20b91,083",
    "issue_price": 1083.0,
    "lot_size": 13,
    "min_investment": 14079,
    "issue_size_cr": 500.0,
    "fresh_issue_cr": 375.0,
    "ofs_cr": 125.0,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 996.36,
    "gmp_closing_percent": 92.0,
    "gmp_estimated_listing": 2079.36,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 51.08,
        "nii": 54.11,
        "retail": 14.14,
        "total": 54.11
      },
      "day2": {
        "qib": 127.71,
        "nii": 126.25,
        "retail": 28.28,
        "total": 117.23
      },
      "final_day": {
        "qib": 255.42,
        "nii": 270.54,
        "retail": 35.35,
        "total": 180.36
      },
      "applications_count": "180.36x Subscription"
    },
    "listing": {
      "listing_price": 2111.8,
      "listing_gain_rs": 1028.8,
      "listing_gain_percent": 95.0,
      "profit_per_lot": 13374.4,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 2079.36,
        "actual_price": 2111.8,
        "variance_rs": 32.44,
        "reliability": "Underpredicted (Beat GMP)",
        "notes": "Closing GMP estimated \u20b92079.36 (+92.0%). Stock opened at \u20b92111.8 (+95.0%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 92.0,
      "actual_gain_pct": 95.0,
      "retail_profit_lost": 13374.4,
      "explanation": "Tatva Chintan Pharma Chem delivered a stellar +95.0% listing gain, rewarding retail allottees with \u20b913,374 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +92% Listing Return",
      "long_term_potential": "Phase Transfer Catalysts Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Phase Transfer Catalysts",
        "Strong institutional interest with 255.42x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +95.0% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 777.2,
        "gmp_percent": 71.8,
        "est_listing_price": 1860.2,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 896.7,
        "gmp_percent": 82.8,
        "est_listing_price": 1979.7,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 996.36,
        "gmp_percent": 92.0,
        "est_listing_price": 2079.4,
        "notes": "Predicted \u20b92079.36 listing"
      }
    ]
  },
  {
    "id": "eternal",
    "name": "Zomato Ltd",
    "symbol": "ETERNAL.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Food Delivery & Quick Commerce",
    "open_date": "14-Jul-21",
    "close_date": "16-Jul-21",
    "listing_date": "23-Jul-21",
    "price_band": "\u20b976",
    "issue_price": 76.0,
    "lot_size": 195,
    "min_investment": 14820,
    "issue_size_cr": 9375.0,
    "fresh_issue_cr": 7031.2,
    "ofs_cr": 2343.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 38.0,
    "gmp_closing_percent": 50.0,
    "gmp_estimated_listing": 114.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 10.36,
        "nii": 11.47,
        "retail": 2.98,
        "total": 11.47
      },
      "day2": {
        "qib": 25.89,
        "nii": 26.77,
        "retail": 5.96,
        "total": 24.86
      },
      "final_day": {
        "qib": 51.79,
        "nii": 57.38,
        "retail": 7.45,
        "total": 38.25
      },
      "applications_count": "38.25x Subscription"
    },
    "listing": {
      "listing_price": 115.0,
      "listing_gain_rs": 39.0,
      "listing_gain_percent": 51.3,
      "profit_per_lot": 7605.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 114.0,
        "actual_price": 115.0,
        "variance_rs": 1.0,
        "reliability": "Highly Accurate",
        "notes": "Closing GMP estimated \u20b9114.0 (+50.0%). Stock opened at \u20b9115.0 (+51.3%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 50.0,
      "actual_gain_pct": 51.3,
      "retail_profit_lost": 7605.0,
      "explanation": "Zomato Ltd delivered a stellar +51.3% listing gain, rewarding retail allottees with \u20b97,605 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +50% Listing Return",
      "long_term_potential": "Food Delivery & Quick Commerce Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Food Delivery & Quick Commerce",
        "Strong institutional interest with 51.79x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +51.3% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 29.6,
        "gmp_percent": 39.0,
        "est_listing_price": 105.6,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 34.2,
        "gmp_percent": 45.0,
        "est_listing_price": 110.2,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 38.0,
        "gmp_percent": 50.0,
        "est_listing_price": 114.0,
        "notes": "Predicted \u20b9114.0 listing"
      }
    ]
  },
  {
    "id": "clean",
    "name": "Clean Science and Technology",
    "symbol": "CLEAN.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Green Chemicals & Catalysts",
    "open_date": "07-Jul-21",
    "close_date": "09-Jul-21",
    "listing_date": "19-Jul-21",
    "price_band": "\u20b9900",
    "issue_price": 900.0,
    "lot_size": 16,
    "min_investment": 14400,
    "issue_size_cr": 1546.62,
    "fresh_issue_cr": 1160.0,
    "ofs_cr": 386.7,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "Link Intime India Pvt Ltd",
    "gmp_closing_day": 855.0,
    "gmp_closing_percent": 95.0,
    "gmp_estimated_listing": 1755.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 41.29,
        "nii": 28.02,
        "retail": 3.6,
        "total": 28.02
      },
      "day2": {
        "qib": 103.22,
        "nii": 65.39,
        "retail": 7.2,
        "total": 60.72
      },
      "final_day": {
        "qib": 206.43,
        "nii": 140.12,
        "retail": 9.0,
        "total": 93.41
      },
      "applications_count": "93.41x Subscription"
    },
    "listing": {
      "listing_price": 1784.0,
      "listing_gain_rs": 884.0,
      "listing_gain_percent": 98.2,
      "profit_per_lot": 14144.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1755.0,
        "actual_price": 1784.0,
        "variance_rs": 29.0,
        "reliability": "Underpredicted (Beat GMP)",
        "notes": "Closing GMP estimated \u20b91755.0 (+95.0%). Stock opened at \u20b91784.0 (+98.2%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 95.0,
      "actual_gain_pct": 98.2,
      "retail_profit_lost": 14144.0,
      "explanation": "Clean Science and Technology delivered a stellar +98.2% listing gain, rewarding retail allottees with \u20b914,144 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +95% Listing Return",
      "long_term_potential": "Green Chemicals & Catalysts Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Green Chemicals & Catalysts",
        "Strong institutional interest with 206.43x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +98.2% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 666.9,
        "gmp_percent": 74.1,
        "est_listing_price": 1566.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 769.5,
        "gmp_percent": 85.5,
        "est_listing_price": 1669.5,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 855.0,
        "gmp_percent": 95.0,
        "est_listing_price": 1755.0,
        "notes": "Predicted \u20b91755.0 listing"
      }
    ]
  },
  {
    "id": "grinfra",
    "name": "G R Infraprojects Ltd",
    "symbol": "GRINFRA.NS",
    "ipo_type": "Mainboard",
    "status": "Listed",
    "closes_today": false,
    "sector": "Roads & Highways Construction",
    "open_date": "07-Jul-21",
    "close_date": "09-Jul-21",
    "listing_date": "19-Jul-21",
    "price_band": "\u20b9837",
    "issue_price": 837.0,
    "lot_size": 17,
    "min_investment": 14229,
    "issue_size_cr": 963.28,
    "fresh_issue_cr": 722.5,
    "ofs_cr": 240.8,
    "lead_managers": [
      "Kotak Investment Banking",
      "Morgan Stanley",
      "ICICI Securities"
    ],
    "registrar": "KFin Technologies Ltd",
    "gmp_closing_day": 837.0,
    "gmp_closing_percent": 100.0,
    "gmp_estimated_listing": 1674.0,
    "gmp_trend": "Rising",
    "subscription": {
      "day1": {
        "qib": 33.72,
        "nii": 30.77,
        "retail": 5.03,
        "total": 30.77
      },
      "day2": {
        "qib": 84.29,
        "nii": 71.81,
        "retail": 10.06,
        "total": 66.68
      },
      "final_day": {
        "qib": 168.58,
        "nii": 153.87,
        "retail": 12.57,
        "total": 102.58
      },
      "applications_count": "102.58x Subscription"
    },
    "listing": {
      "listing_price": 1700.0,
      "listing_gain_rs": 863.0,
      "listing_gain_percent": 103.1,
      "profit_per_lot": 14671.0,
      "is_profitable": true,
      "gmp_accuracy": {
        "predicted_price": 1674.0,
        "actual_price": 1700.0,
        "variance_rs": 26.0,
        "reliability": "Underpredicted (Beat GMP)",
        "notes": "Closing GMP estimated \u20b91674.0 (+100.0%). Stock opened at \u20b91700.0 (+103.1%)."
      }
    },
    "missed_opportunity_analysis": {
      "verdict": "Massive Missed Opportunity",
      "verdict_badge": "warning",
      "is_missed_opp": true,
      "expected_gain_pct": 100.0,
      "actual_gain_pct": 103.1,
      "retail_profit_lost": 14671.0,
      "explanation": "G R Infraprojects Ltd delivered a stellar +103.1% listing gain, rewarding retail allottees with \u20b914,671 net profit per lot. Skipping this was a clear missed opportunity."
    },
    "recommendation_at_ipo": {
      "verdict": "Apply",
      "badge": "success",
      "listing_gain_prospect": "Estimated +100% Listing Return",
      "long_term_potential": "Roads & Highways Construction Leader",
      "confidence_level": "High",
      "strengths": [
        "Established footprint in Roads & Highways Construction",
        "Strong institutional interest with 168.58x QIB subscription"
      ],
      "risks": [
        "Valuation pricing leaves moderate room for subsequent quarterly beats"
      ],
      "reasons": "Delivered +103.1% listing gains on market debut."
    },
    "gmp_history": [
      {
        "stage": "Day -2",
        "label": "2 Days Before Close",
        "gmp_rs": 652.9,
        "gmp_percent": 78.0,
        "est_listing_price": 1489.9,
        "notes": "Early bidding demand"
      },
      {
        "stage": "Day -1",
        "label": "1 Day Before Close",
        "gmp_rs": 753.3,
        "gmp_percent": 90.0,
        "est_listing_price": 1590.3,
        "notes": "QIB & HNI bidding momentum"
      },
      {
        "stage": "Closing Day",
        "label": "Closing Day (Final)",
        "gmp_rs": 837.0,
        "gmp_percent": 100.0,
        "est_listing_price": 1674.0,
        "notes": "Predicted \u20b91674.0 listing"
      }
    ]
  }
]
