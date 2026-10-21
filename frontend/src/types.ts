export interface StockSearchResult {
  symbol: string;
  name: string;
  sector: string;
  exchange: string;
  bse_code?: string;
  index?: string;
}

export interface ValuationData {
  verdict: "BEST BUY" | "AT FAIR PRICE" | "CURRENTLY EXPENSIVE";
  verdict_badge: "success" | "warning" | "danger";
  verdict_desc: string;
  action_call: string;
  composite_score: number;
  fundamental_score: number;
  technical_score: number;
  current_price: number;
  fair_value: number;
  margin_of_safety_percent: number;
  graham_number?: number | null;
  dcf_intrinsic_value?: number | null;
  rsi?: number | null;
  dma_50?: number | null;
  dma_200?: number | null;
  high_52?: number | null;
  low_52?: number | null;
  pros: string[];
  cons: string[];
  valuation_status: string;
}

export interface StockRatios {
  pe_ratio?: number | null;
  pb_ratio?: number | null;
  peg_ratio?: number | null;
  eps?: number | null;
  book_value?: number | null;
  dividend_yield?: number | null;
  roe?: number | null;
  profit_margin?: number | null;
  debt_to_equity?: number | null;
  beta?: number | null;
}

export interface ChartPoint {
  date: string;
  open?: number | null;
  high?: number | null;
  low?: number | null;
  close: number;
  volume: number;
  sma_50?: number | null;
  sma_200?: number | null;
}

export interface StockAnalysisResponse {
  symbol: string;
  display_symbol: string;
  exchange: "NSE" | "BSE";
  name: string;
  sector: string;
  industry: string;
  description: string;
  current_price: number;
  previous_close: number;
  change: number;
  change_percent: number;
  currency: string;
  market_cap?: number | null;
  market_cap_formatted: string;
  volume?: number | null;
  high_52?: number | null;
  low_52?: number | null;
  valuation: ValuationData;
  ratios: StockRatios;
  chart: ChartPoint[];
}

export interface ScreenerItem {
  symbol: string;
  display_symbol: string;
  name: string;
  exchange: string;
  sector: string;
  current_price: number;
  change_percent: number;
  fair_value: number;
  margin_of_safety: number;
  composite_score: number;
  verdict: string;
  verdict_badge: "success" | "warning" | "danger";
  pe_ratio?: number | null;
  roe?: number | null;
  rsi?: number | null;
}

export interface MarketIndex {
  symbol: string;
  name: string;
  price: number;
  change: number;
  change_percent: number;
}

export interface IPOSubscriptionCategory {
  qib: number;
  nii: number;
  retail: number;
  total: number;
}

export interface IPOSubscription {
  day1?: IPOSubscriptionCategory | null;
  day2?: IPOSubscriptionCategory | null;
  final_day?: IPOSubscriptionCategory | null;
  applications_count?: string;
}

export interface IPOListing {
  listing_price: number;
  listing_gain_rs: number;
  listing_gain_percent: number;
  profit_per_lot: number;
  is_profitable: boolean;
  closing_price_day1?: number;
  gmp_accuracy?: {
    predicted_price: number;
    actual_price: number;
    variance_rs: number;
    reliability: string;
    notes: string;
  };
}

export interface IPOMissedOpportunity {
  verdict: string;
  verdict_badge: "success" | "warning" | "danger" | "neutral";
  is_missed_opp: boolean;
  expected_gain_pct: number;
  actual_gain_pct: number;
  retail_profit_lost: number;
  explanation: string;
}

export interface IPOFinancials {
  pe_ratio?: number | null;
  peer_pe?: number | null;
  revenue_growth_yoy?: number | null;
  pat_margin?: number | null;
  debt_to_equity?: number | null;
}

export interface IPORecommendation {
  verdict: "Apply" | "Apply with Caution" | "Avoid";
  badge: "success" | "warning" | "danger";
  listing_gain_prospect: string;
  long_term_potential: string;
  confidence_level: "High" | "Medium" | "Low";
  strengths: string[];
  risks: string[];
  reasons: string;
  financials?: IPOFinancials;
}

export interface IPOData {
  id: string;
  name: string;
  symbol: string;
  ipo_type: "Mainboard" | "SME";
  status: "Upcoming" | "Open" | "Closed" | "Listed";
  closes_today?: boolean;
  sector: string;
  open_date: string;
  close_date: string;
  allotment_date?: string;
  listing_date?: string;
  price_band: string;
  issue_price: number;
  lot_size: number;
  min_investment: number;
  issue_size_cr: number;
  fresh_issue_cr?: number;
  ofs_cr?: number;
  lead_managers?: string[];
  registrar?: string;
  gmp_closing_day: number;
  gmp_closing_percent: number;
  gmp_estimated_listing: number;
  gmp_trend: "Rising" | "Falling" | "Stable";
  gmp_history?: Array<{
    stage: string;
    label: string;
    gmp_rs: number;
    gmp_percent: number;
    est_listing_price?: number;
    notes?: string;
  }>;
  subscription: IPOSubscription;
  listing?: IPOListing | null;
  missed_opportunity_analysis?: IPOMissedOpportunity | null;
  recommendation_at_ipo?: IPORecommendation | null;
}

export interface IPOSummaryMetrics {
  open_count: number;
  closes_today_count?: number;
  upcoming_count: number;
  closed_count?: number;
  total_listed_tracked: number;
  average_listing_gain_percent: number;
  best_performer?: {
    name: string;
    gain_percent: number;
    profit_per_lot: number;
  } | null;
  worst_performer?: {
    name: string;
    gain_percent: number;
    profit_per_lot: number;
  } | null;
  total_1_lot_profit_sum: number;
  last_updated: string;
}

export interface MostTradedStock {
  symbol: string;
  name: string;
  exchange: string;
  current_price: number;
  change: number;
  change_percent: number;
  volume: number;
  volume_formatted: string;
  sparkline: number[];
}

export interface TopMoverStock {
  symbol: string;
  name: string;
  exchange: string;
  current_price: number;
  change: number;
  change_percent: number;
  volume: number;
  volume_formatted: string;
  sparkline: number[];
}

export interface TrendingSector {
  id: string;
  name: string;
  icon?: string;
  gainers: number;
  losers: number;
  change_percent: number;
}

export interface SectorStockItem {
  symbol: string;
  name: string;
  exchange: string;
  current_price: number;
  change: number;
  change_percent: number;
  volume: number;
  volume_formatted: string;
  vol_diff_percent?: number;
  low_52?: number;
  high_52?: number;
  position_52w_percent?: number;
  rsi?: number;
  macd?: string;
  in_news?: boolean;
  sparkline: number[];
}

export interface MarketExploreData {
  most_traded: MostTradedStock[];
  top_movers: {
    gainers: TopMoverStock[];
    losers: TopMoverStock[];
    volume_shockers: TopMoverStock[];
  };
  trending_sectors: TrendingSector[];
}

