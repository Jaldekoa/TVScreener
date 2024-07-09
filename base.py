import pandas as pd
import requests

__base_url = 'https://scanner.tradingview.com/global/scan'
__all_cols = ['name', 'description', 'logoid', 'update_mode', 'type', 'typespecs', 'Perf.6M', 'Perf.W', 'cash_n_short_term_invest_fq', 'return_on_assets_fq', 'Perf.YTD', 'Candle.Doji.Dragonfly', 'relative_volume_10d_calc', 'free_cash_flow_ttm', 'dividends_yield_current', 'net_debt_fq', 'close', 'capital_expenditures_ttm', 'net_income_ttm', 'Candle.3WhiteSoldiers', 'Recommend.Other', 'Candle.EveningStar', 'enterprise_value_to_ebit_ttm', 'industry.tr', 'minmov', 'Volatility.W', 'total_equity_fq', 'recommendation_mark', 'Candle.LongShadow.Lower', 'continuous_dividend_payout', 'cash_f_financing_activities_ttm', 'continuous_dividend_growth', 'Candle.3BlackCrows', 'Candle.Engulfing.Bullish', 'RSI', 'Candle.ShootingStar', 'Candle.TriStar.Bearish', 'total_current_assets_fq', 'minmove2', 'total_revenue_yoy_growth_ttm', 'total_debt_fq', 'free_cash_flow_margin_ttm', 'sell_gen_admin_exp_other_ratio_ttm', 'sector', 'current_ratio_fq', 'price_sales_current', 'Candle.InvertedHammer', 'dps_common_stock_prim_issue_fq', 'dps_common_stock_prim_issue_fy', 'industry', 'total_revenue_ttm', 'currency', 'AO', 'cash_n_short_term_invest_to_total_debt_fq', 'price_to_cash_ratio', 'dividends_yield', 'operating_margin_ttm', 'market', 'Candle.Kicking.Bearish', 'Candle.Engulfing.Bearish', 'total_liabilities_fq', 'Candle.LongShadow.Upper', 'Candle.Doji', 'enterprise_value_current', 'Candle.MorningStar', 'dps_common_stock_prim_issue_yoy_growth_fy', 'Perf.Y', 'Perf.5Y', 'Candle.Kicking.Bullish', 'Candle.SpinningTop.White', 'Perf.10Y', 'return_on_invested_capital_fq', 'Candle.Doji.Gravestone', 'Candle.AbandonedBaby.Bearish', 'Volatility.M', 'Mom', 'volume', 'oper_income_ttm', 'pricescale', 'Perf.1M', 'total_assets_fq', 'Perf.3M', 'Stoch.K', 'enterprise_value_ebitda_ttm', 'Recommend.MA', 'Recommend.All', 'Candle.TriStar.Bullish', 'price_earnings_ttm', 'fundamental_currency_code', 'sector.tr', 'enterprise_value_to_revenue_ttm', 'Candle.Harami.Bullish', 'research_and_dev_ratio_ttm', 'price_to_cash_f_operating_activities_ttm', 'Stoch.D', 'price_book_fq', 'net_margin_ttm', 'Candle.SpinningTop.Black', 'fractional', 'price_free_cash_flow_ttm', 'gross_profit_ttm', 'market_cap_basic', 'Perf.All', 'Candle.HangingMan', 'Candle.AbandonedBaby.Bullish', 'price_earnings_growth_ttm', 'gross_margin_ttm', 'change', 'Candle.Hammer', 'dividend_payout_ratio_ttm', 'earnings_per_share_diluted_ttm', 'quick_ratio_fq', 'CCI20', 'pre_tax_margin_ttm', 'Candle.Marubozu.Black', 'earnings_per_share_diluted_yoy_growth_ttm', 'Candle.Harami.Bearish', 'Perf.1Y.MarketCap', 'Candle.Marubozu.White', 'exchange', 'ebitda_ttm', 'cash_f_operating_activities_ttm', 'return_on_equity_fq', 'cash_f_investing_activities_ttm', 'debt_to_equity_fq']
__all_markets = ["america", "argentina", "australia", "austria", "bahrain", "bangladesh", "belgium", "brazil", "canada", "chile", "china", "colombia", "cyprus", "czech", "denmark", "egypt", "estonia", "finland", "france", "germany", "greece", "hongkong", "hungary", "iceland", "india", "indonesia", "israel", "italy", "japan", "kenya", "kuwait", "latvia", "lithuania", "luxembourg", "malaysia", "mexico", "morocco", "netherlands", "newzealand", "nigeria", "norway", "pakistan", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "ksa", "serbia", "singapore", "slovakia", "rsa", "korea", "spain", "srilanka", "sweden", "switzerland", "taiwan", "thailand", "tunisia", "turkey", "uae", "uk", "venezuela", "vietnam"]


def get_data(cols: list, max_range: int, markets: list):

    cols = [c for c in cols if c in __all_cols]
    markets = [m for m in markets if m in __all_markets]
    data = {"columns": cols, "range": [0, max_range], "markets": markets}

    res = requests.post(__base_url, headers={}, json=data).json()['data']
    df = pd.DataFrame(res)

    df_s = pd.DataFrame(df['s'].str.split(':').tolist(), columns=["exchange", "ticker"])
    df_d = pd.DataFrame(df['d'].tolist(), columns=cols)
    print(df_s)
    print(df_d)

    df_res = pd.concat([df_s, df_d], axis=1, ignore_index=True)
    df_res = pd.concat([df_s.reset_index(drop=True), df_d.reset_index(drop=True)], axis=1)
    return df_res.reset_index(drop=True)


df = get_data(cols=__all_cols, max_range=100, markets=__all_markets)
print(df)
