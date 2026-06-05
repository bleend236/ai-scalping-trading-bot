#!/usr/bin/env python3
"""
Helper Functions for Trading Bot
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

def calculate_kelly_fraction(win_rate: float, avg_win: float, avg_loss: float) -> float:
    """Calculate Kelly Criterion for position sizing"""
    if avg_loss == 0:
        return 0
    loss_rate = 1 - win_rate
    kelly = (win_rate * avg_win - loss_rate * avg_loss) / avg_loss
    kelly = np.clip(kelly, -1, 1) * 0.25
    return kelly

def calculate_position_size(
    capital: float,
    risk_per_trade: float,
    entry_price: float,
    stop_loss_price: float,
    pip_value: float = 1.0
) -> float:
    """Calculate position size based on risk management"""
    if entry_price == stop_loss_price:
        return 0
    risk_amount = capital * risk_per_trade
    price_diff = abs(entry_price - stop_loss_price)
    position_size = risk_amount / (price_diff * pip_value)
    return position_size

def calculate_atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    """Calculate Average True Range"""
    tr1 = high - low
    tr2 = np.abs(high - np.roll(close, 1))
    tr3 = np.abs(low - np.roll(close, 1))
    tr = np.maximum(np.maximum(tr1, tr2), tr3)
    atr = pd.Series(tr).rolling(window=period).mean().values
    return atr

def calculate_sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.02) -> float:
    """Calculate Sharpe Ratio"""
    if len(returns) < 2:
        return 0
    excess_returns = returns - risk_free_rate / 252
    std_dev = np.std(excess_returns)
    return np.mean(excess_returns) / std_dev if std_dev > 0 else 0

def calculate_max_drawdown(returns: np.ndarray) -> float:
    """Calculate maximum drawdown"""
    cumulative = np.cumprod(1 + returns)
    running_max = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - running_max) / running_max
    return np.min(drawdown) if len(drawdown) > 0 else 0

def calculate_win_rate(trades: List[Dict]) -> float:
    """Calculate win rate from trades"""
    if not trades:
        return 0
    winning_trades = sum(1 for t in trades if t.get('pnl', 0) > 0)
    return winning_trades / len(trades)

def normalize_array(arr: np.ndarray, axis: Optional[int] = None) -> np.ndarray:
    """Normalize array to 0-1 range"""
    min_val = np.min(arr, axis=axis, keepdims=True)
    max_val = np.max(arr, axis=axis, keepdims=True)
    return (arr - min_val) / (max_val - min_val + 1e-8)
