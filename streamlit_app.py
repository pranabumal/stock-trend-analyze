from __future__ import annotations

import os
from datetime import datetime
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from app.config.di import get_analyzer_service
from app.ui.charts import make_dual_axis_figure, correlation_strength

st.set_page_config(
    page_title="Stock vs Trends Analyzer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

AVAILABLE_STOCKS = {
    "Technology": ["AAPL", "MSFT", "GOOGL", "META", "NVDA", "TSLA", "AMD", "INTC"],
    "Finance": ["JPM", "BAC", "GS", "MS", "V", "MA"],
    "Healthcare": ["JNJ", "PFE", "MRK", "ABT", "UNH"],
    "Consumer": ["AMZN", "WMT", "TGT", "NKE", "SBUX"],
}


def main():
    st.title("📈 Stock Price vs Search Trends Analyzer")
    st.markdown("Analyze correlations between stock performance and public interest")

    # Load environment from .env once at app start
    load_dotenv(override=False)

    st.sidebar.header("Configuration")

    # Environment toggle
    use_mock = st.sidebar.toggle("Use Mock Data", value=os.getenv("USE_MOCK", "false").lower() == "true")
    os.environ["USE_MOCK"] = "true" if use_mock else "false"

    # API Key input (used when USE_MOCK=false)
    api_key = st.sidebar.text_input(
        "Alpha Vantage API Key (optional)", value=os.getenv("ALPHAVANTAGE_API_KEY", ""), help="Get free key from: https://www.alphavantage.co/support/#api-key"
    )
    if api_key:
        os.environ["ALPHAVANTAGE_API_KEY"] = api_key

    st.sidebar.subheader("Select Stocks to Analyze")

    selected = []
    for cat, symbols in AVAILABLE_STOCKS.items():
        with st.sidebar.expander(f"{cat} Stocks"):
            for s in symbols:
                if st.checkbox(s, key=f"stock_{s}"):
                    selected.append(s)

    custom = st.sidebar.text_input("Or add custom stock symbol", "").strip().upper()
    if custom and custom not in selected:
        selected.append(custom)

    st.sidebar.subheader("Analysis Parameters")
    days = st.sidebar.slider("Analysis Period (days)", 30, 365, 90)
    term_mode = st.sidebar.radio("Trends Keyword", ["Auto-generate", "Custom"])

    custom_terms = {}
    if term_mode == "Custom":
        st.sidebar.info("Enter custom search terms for each stock")
        for s in selected:
            custom_terms[s] = st.sidebar.text_input(f"Search term for {s}", f"{s} stock", key=f"kw_{s}")

    if not selected:
        st.info("👈 Select stocks from the sidebar to begin analysis")
        st.markdown(
            """
            ### How to use:
            - Select stocks from the categories in the sidebar
            - Adjust analysis period as needed
            - Choose auto-generated or custom search terms
            - View correlation analysis and interactive charts
            """
        )
        return

    if st.button("Run Analysis", type="primary"):
        svc = get_analyzer_service()
        progress = st.progress(0)
        status = st.empty()
        results = []
        figs = []

        for i, s in enumerate(selected):
            status.text(f"Analyzing {s}...")
            progress.progress(i / max(1, len(selected)))
            kw = f"{s} stock" if term_mode == "Auto-generate" else custom_terms.get(s, f"{s} stock")
            df, corr = svc.analyze(s, kw, days)
            if df is None or df.empty:
                st.warning(f"No overlapping data returned for {s} and '{kw}' in the selected period.")
                continue
            results.append({"stock": s, "keyword": kw, "correlation": corr, "data": df})
            figs.append(make_dual_axis_figure(df, s, kw, corr))

        progress.progress(1.0)
        status.text("Analysis complete!")

        if not results:
            st.warning("No results to display. Try a different period, stock symbol, or keyword, or enable Mock Data.")
            return

        st.header("Analysis Results")
        st.subheader("Correlation Summary")
        summary = [
            {
                "Stock": r["stock"],
                "Search Term": r["keyword"],
                "Correlation": f"{r['correlation']:.3f}",
                "Strength": correlation_strength(r["correlation"]),
            }
            for r in results
        ]
        st.dataframe(pd.DataFrame(summary), use_container_width=True)

        st.subheader("Interactive Charts")
        for i, (r, fig) in enumerate(zip(results, figs)):
            st.plotly_chart(fig, use_container_width=True)
            with st.expander(f"View raw data for {r['stock']}"):
                st.dataframe(r["data"].tail(20))
            if i < len(results) - 1:
                st.markdown("---")

        st.subheader("Download Results")
        if st.button("Export All Data to CSV"):
            all_df = pd.concat([r["data"].rename(columns={"price": f"{r['stock']}_Price", "interest": f"{r['keyword']}_Trend"}) for r in results], axis=1)
            st.download_button(
                label="Download CSV",
                data=all_df.to_csv(),
                file_name=f"stock_trends_analysis_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )


if __name__ == "__main__":
    main()
