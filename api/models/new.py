from typing import Optional, List, Union, Any
from datetime import datetime
from enum import Enum

from utils import CamelModel


class UserEnrolledBy(CamelModel):
    type: Optional[str] = None
    percent: Optional[int] = None
    allowlist_addresses: Optional[List[str]] = None


class Datum(CamelModel):
    slug: Optional[str] = None
    label: Optional[str] = None
    id: Optional[int] = None
    force_show: Optional[bool] = None
    updated_at: Optional[datetime] = None
    published_at: Optional[str] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    force_hide: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    user_enrolled_by: Optional[UserEnrolledBy] = None
    version: Optional[str] = None


class ClobReward(CamelModel):
    id: Optional[int] = None
    condition_id: Optional[str] = None
    asset_address: Optional[str] = None
    rewards_amount: Optional[int] = None
    rewards_daily_rate: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class PurpleSeries(CamelModel):
    id: Optional[int] = None


class MarketEvent(CamelModel):
    id: Optional[int] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    ticker: Optional[str] = None
    series: Optional[List[PurpleSeries]] = None


class Market(CamelModel):
    id: Optional[int] = None
    question: Optional[str] = None
    condition_id: Optional[str] = None
    slug: Optional[str] = None
    end_date: Optional[datetime] = None
    liquidity: Optional[str] = None
    start_date: Optional[datetime] = None
    image: Optional[str] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    outcomes: Optional[List[str]] = None
    outcome_prices: Optional[List[str]] = None
    volume: Optional[str] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    market_maker_address: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    submitted_by: Optional[str] = None
    archived: Optional[bool] = None
    resolved_by: Optional[str] = None
    restricted: Optional[bool] = None
    group_item_title: Optional[str] = None
    group_item_threshold: Optional[int] = None
    question_id: Optional[str] = None
    enable_order_book: Optional[bool] = None
    order_price_min_tick_size: Optional[float] = None
    order_min_size: Optional[int] = None
    volume_num: Optional[float] = None
    liquidity_num: Optional[float] = None
    end_date_iso: Optional[datetime] = None
    start_date_iso: Optional[datetime] = None
    has_reviewed_dates: Optional[bool] = None
    volume24_hr: Optional[float] = None
    volume1_wk: Optional[float] = None
    volume1_mo: Optional[float] = None
    volume1_yr: Optional[float] = None
    clob_token_ids: Optional[List[str]] = None
    uma_bond: Optional[int] = None
    uma_reward: Optional[int] = None
    volume24_hr_clob: Optional[float] = None
    volume1_wk_clob: Optional[float] = None
    volume1_mo_clob: Optional[float] = None
    volume1_yr_clob: Optional[float] = None
    volume_clob: Optional[float] = None
    liquidity_clob: Optional[float] = None
    custom_liveness: Optional[int] = None
    accepting_orders: Optional[bool] = None
    neg_risk: Optional[bool] = None
    neg_risk_request_id: Optional[str] = None
    ready: Optional[bool] = None
    funded: Optional[bool] = None
    accepting_orders_timestamp: Optional[datetime] = None
    cyom: Optional[bool] = None
    competitive: Optional[float] = None
    pager_duty_notification_enabled: Optional[bool] = None
    approved: Optional[bool] = None
    rewards_min_size: Optional[int] = None
    rewards_max_spread: Optional[float] = None
    spread: Optional[float] = None
    last_trade_price: Optional[float] = None
    best_bid: Optional[float] = None
    best_ask: Optional[float] = None
    automatically_active: Optional[bool] = None
    clear_book_on_start: Optional[bool] = None
    show_gmp_series: Optional[bool] = None
    show_gmp_outcome: Optional[bool] = None
    manual_activation: Optional[bool] = None
    neg_risk_other: Optional[bool] = None
    uma_resolution_statuses: Optional[str] = None
    pending_deployment: Optional[bool] = None
    deploying: Optional[bool] = None
    deploying_timestamp: Optional[datetime] = None
    rfq_enabled: Optional[bool] = None
    holding_rewards_enabled: Optional[bool] = None
    fees_enabled: Optional[bool] = None
    lower_bound_date: None
    upper_bound_date: None
    market_type: None
    market_resolution_source: Optional[str] = None
    market_end_date: Optional[datetime] = None
    event_start_time: None
    amm_type: None
    x_axis_value: None
    y_axis_value: None
    denomination_token: None
    market_resolved_by: Optional[str] = None
    upper_bound: None
    lower_bound: None
    market_created_at: Optional[datetime] = None
    market_updated_at: Optional[datetime] = None
    closed_time: None
    wide_format: None
    market_volume_num: Optional[float] = None
    market_liquidity_num: Optional[float] = None
    image_raw: Optional[str] = None
    events: Optional[List[MarketEvent]] = None
    one_hour_price_change: Optional[float] = None
    resolution_source: Optional[str] = None
    neg_risk_market_id: Optional[str] = None
    one_day_price_change: Optional[float] = None
    sports_market_type: Optional[str] = None
    clob_rewards: Optional[List[ClobReward]] = None


class FluffySeries(CamelModel):
    id: Optional[int] = None
    ticker: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    series_type: Optional[str] = None
    recurrence: Optional[str] = None
    image: Optional[str] = None
    icon: Optional[str] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    published_at: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    comments_enabled: Optional[bool] = None
    competitive: Optional[int] = None
    volume24_hr: Optional[int] = None
    volume: Optional[float] = None
    liquidity: Optional[float] = None
    start_date: Optional[datetime] = None
    comment_count: Optional[int] = None


class SortBy(Enum):
    PRICE = "price"


class Tag(CamelModel):
    id: Optional[int] = None
    label: Optional[str] = None
    slug: Optional[str] = None
    force_show: Optional[bool] = None
    published_at: Optional[str] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_carousel: Optional[bool] = None
    force_hide: Optional[bool] = None


class PageEvent(CamelModel):
    id: Optional[int] = None
    ticker: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    resolution_source: Optional[str] = None
    start_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    image: Optional[str] = None
    icon: Optional[str] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    liquidity: Optional[float] = None
    volume: Optional[float] = None
    open_interest: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    competitive: Optional[float] = None
    volume24_hr: Optional[float] = None
    volume1_wk: Optional[float] = None
    volume1_mo: Optional[float] = None
    volume1_yr: Optional[float] = None
    enable_order_book: Optional[bool] = None
    liquidity_clob: Optional[float] = None
    neg_risk: Optional[bool] = None
    comment_count: Optional[int] = None
    markets: Optional[List[Market]] = None
    tags: Optional[List[Tag]] = None
    cyom: Optional[bool] = None
    show_all_outcomes: Optional[bool] = None
    show_market_images: Optional[bool] = None
    enable_neg_risk: Optional[bool] = None
    automatically_active: Optional[bool] = None
    gmp_chart_mode: Optional[str] = None
    neg_risk_augmented: Optional[bool] = None
    pending_deployment: Optional[bool] = None
    deploying: Optional[bool] = None
    image_raw: Optional[str] = None
    neg_risk_market_id: Optional[str] = None
    series: Optional[List[FluffySeries]] = None
    start_time: Optional[datetime] = None
    series_slug: Optional[str] = None
    deploying_timestamp: Optional[datetime] = None
    featured_order: Optional[int] = None
    sort_by: Optional[SortBy] = None


class Page(CamelModel):
    events: Optional[List[PageEvent]] = None
    total_results: Optional[int] = None
    has_more: Optional[bool] = None


class DataSate(CamelModel):
    pages: Optional[List[Page]] = None
    page_params: Optional[List[int]] = None


class State(CamelModel):
    data: Optional[Union[DataSate, int, List[Datum]]] = None
    data_update_count: Optional[int] = None
    data_updated_at: Optional[int] = None
    error: None
    error_update_count: Optional[int] = None
    error_updated_at: Optional[int] = None
    fetch_failure_count: Optional[int] = None
    fetch_failure_reason: None
    fetch_meta: None
    is_invalidated: Optional[bool] = None
    status: Optional[str] = None
    fetch_status: Optional[str] = None


class Query(CamelModel):
    dehydrated_at: Optional[int] = None
    state: Optional[State] = None
    query_key: Optional[List[Optional[Union[bool, str]]]] = None
    query_hash: Optional[str] = None


class DehydratedState(CamelModel):
    mutations: Optional[List[Any]] = None
    queries: Optional[List[Query]] = None


class PageProps(CamelModel):
    category: Optional[str] = None
    dehydrated_state: Optional[DehydratedState] = None


class PolymarketNewResponse(CamelModel):
    page_props: Optional[PageProps] = None
    n_ssg: Optional[bool] = None
