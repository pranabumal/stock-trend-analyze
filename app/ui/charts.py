from __future__ import annotations

import plotly.graph_objects as go
from plotly.subplots import make_subplots


def correlation_strength(corr: float) -> str:
    a = abs(corr)
    if a >= 0.7:
        return "Strong"
    if a >= 0.4:
        return "Moderate"
    if a >= 0.2:
        return "Weak"
    return "Very Weak"


def make_dual_axis_figure(df, symbol: str, keyword: str, corr: float):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["price"],
            name=f"{symbol} Price",
            line=dict(color="#1f77b4", width=3),
            hovertemplate=f"{symbol} Price: $%{{y:.2f}}<extra></extra>",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["interest"],
            name=f"'{keyword}' Searches",
            line=dict(color="#ff7f0e", width=2),
            hovertemplate="Search Interest: %{y:.0f}<extra></extra>",
        ),
        secondary_y=True,
    )

    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text=f"{symbol} Stock Price ($)", secondary_y=False, tickprefix="$")
    fig.update_yaxes(title_text="Search Interest (0-100)", secondary_y=True, range=[0, 100])

    color = "green" if corr > 0.3 else "red" if corr < -0.3 else "orange"
    fig.update_layout(
        title=dict(
            text=(
                f"{symbol} vs '{keyword}'<br><span style='font-size:0.8em; color: {color}'>"
                f"Correlation: {corr:.3f} ({correlation_strength(corr)})</span>"
            ),
            x=0.5,
            xanchor="center",
        ),
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=500,
    )
    return fig
