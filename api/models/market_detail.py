from enum import Enum
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AmmType(Enum):
    STRING = "<string>"


class Category(BaseModel):
    id: Optional[AmmType] = None
    label: Optional[AmmType] = None
    parent_category: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    published_at: Optional[AmmType] = None
    created_by: Optional[AmmType] = None
    updated_by: Optional[AmmType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Chat(BaseModel):
    id: Optional[AmmType] = None
    channel_id: Optional[AmmType] = None
    channel_name: Optional[AmmType] = None
    channel_image: Optional[AmmType] = None
    live: Optional[bool] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class Optimized(BaseModel):
    id: Optional[AmmType] = None
    image_url_source: Optional[AmmType] = None
    image_url_optimized: Optional[AmmType] = None
    image_size_kb_source: Optional[int] = None
    image_size_kb_optimized: Optional[int] = None
    image_optimized_complete: Optional[bool] = None
    image_optimized_last_updated: Optional[AmmType] = None
    rel_id: Optional[int] = None
    field: Optional[AmmType] = None
    relname: Optional[AmmType] = None


class Collection(BaseModel):
    id: Optional[AmmType] = None
    ticker: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    title: Optional[AmmType] = None
    subtitle: Optional[AmmType] = None
    collection_type: Optional[AmmType] = None
    description: Optional[AmmType] = None
    tags: Optional[AmmType] = None
    image: Optional[AmmType] = None
    icon: Optional[AmmType] = None
    header_image: Optional[AmmType] = None
    layout: Optional[AmmType] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    is_template: Optional[bool] = None
    template_variables: Optional[AmmType] = None
    published_at: Optional[AmmType] = None
    created_by: Optional[AmmType] = None
    updated_by: Optional[AmmType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    comments_enabled: Optional[bool] = None
    image_optimized: Optional[Optimized] = None
    icon_optimized: Optional[Optimized] = None
    header_image_optimized: Optional[Optimized] = None


class EventCreator(BaseModel):
    id: Optional[AmmType] = None
    creator_name: Optional[AmmType] = None
    creator_handle: Optional[AmmType] = None
    creator_url: Optional[AmmType] = None
    creator_image: Optional[AmmType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Market(BaseModel):
    pass


class Tag(BaseModel):
    id: Optional[AmmType] = None
    label: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    force_show: Optional[bool] = None
    published_at: Optional[AmmType] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    force_hide: Optional[bool] = None
    is_carousel: Optional[bool] = None


class Series(BaseModel):
    id: Optional[AmmType] = None
    ticker: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    title: Optional[AmmType] = None
    subtitle: Optional[AmmType] = None
    series_type: Optional[AmmType] = None
    recurrence: Optional[AmmType] = None
    description: Optional[AmmType] = None
    image: Optional[AmmType] = None
    icon: Optional[AmmType] = None
    layout: Optional[AmmType] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    is_template: Optional[bool] = None
    template_variables: Optional[bool] = None
    published_at: Optional[AmmType] = None
    created_by: Optional[AmmType] = None
    updated_by: Optional[AmmType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    comments_enabled: Optional[bool] = None
    competitive: Optional[AmmType] = None
    volume24_hr: Optional[int] = None
    volume: Optional[int] = None
    liquidity: Optional[int] = None
    start_date: Optional[datetime] = None
    pyth_token_id: Optional[AmmType] = None
    cg_asset_name: Optional[AmmType] = None
    score: Optional[int] = None
    events: Optional[List[Market]] = None
    collections: Optional[List[Collection]] = None
    categories: Optional[List[Category]] = None
    tags: Optional[List[Tag]] = None
    comment_count: Optional[int] = None
    chats: Optional[List[Chat]] = None


class Template(BaseModel):
    id: Optional[AmmType] = None
    event_title: Optional[AmmType] = None
    event_slug: Optional[AmmType] = None
    event_image: Optional[AmmType] = None
    market_title: Optional[AmmType] = None
    description: Optional[AmmType] = None
    resolution_source: Optional[AmmType] = None
    neg_risk: Optional[bool] = None
    sort_by: Optional[AmmType] = None
    show_market_images: Optional[bool] = None
    series_slug: Optional[AmmType] = None
    outcomes: Optional[AmmType] = None


class Event(BaseModel):
    id: Optional[AmmType] = None
    ticker: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    title: Optional[AmmType] = None
    subtitle: Optional[AmmType] = None
    description: Optional[AmmType] = None
    resolution_source: Optional[AmmType] = None
    start_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    image: Optional[AmmType] = None
    icon: Optional[AmmType] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    liquidity: Optional[int] = None
    volume: Optional[int] = None
    open_interest: Optional[int] = None
    sort_by: Optional[AmmType] = None
    category: Optional[AmmType] = None
    subcategory: Optional[AmmType] = None
    is_template: Optional[bool] = None
    template_variables: Optional[AmmType] = None
    published_at: Optional[AmmType] = None
    created_by: Optional[AmmType] = None
    updated_by: Optional[AmmType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    comments_enabled: Optional[bool] = None
    competitive: Optional[int] = None
    volume24_hr: Optional[int] = None
    volume1_wk: Optional[int] = None
    volume1_mo: Optional[int] = None
    volume1_yr: Optional[int] = None
    featured_image: Optional[AmmType] = None
    disqus_thread: Optional[AmmType] = None
    parent_event: Optional[AmmType] = None
    enable_order_book: Optional[bool] = None
    liquidity_amm: Optional[int] = None
    liquidity_clob: Optional[int] = None
    neg_risk: Optional[bool] = None
    neg_risk_market_id: Optional[AmmType] = None
    neg_risk_fee_bips: Optional[int] = None
    comment_count: Optional[int] = None
    image_optimized: Optional[Optimized] = None
    icon_optimized: Optional[Optimized] = None
    featured_image_optimized: Optional[Optimized] = None
    sub_events: Optional[List[AmmType]] = None
    markets: Optional[List[Market]] = None
    series: Optional[List[Series]] = None
    categories: Optional[List[Category]] = None
    collections: Optional[List[Collection]] = None
    tags: Optional[List[Tag]] = None
    cyom: Optional[bool] = None
    closed_time: Optional[datetime] = None
    show_all_outcomes: Optional[bool] = None
    show_market_images: Optional[bool] = None
    automatically_resolved: Optional[bool] = None
    enable_neg_risk: Optional[bool] = None
    automatically_active: Optional[bool] = None
    event_date: Optional[AmmType] = None
    start_time: Optional[datetime] = None
    event_week: Optional[int] = None
    series_slug: Optional[AmmType] = None
    score: Optional[AmmType] = None
    elapsed: Optional[AmmType] = None
    period: Optional[AmmType] = None
    live: Optional[bool] = None
    ended: Optional[bool] = None
    finished_timestamp: Optional[datetime] = None
    gmp_chart_mode: Optional[AmmType] = None
    event_creators: Optional[List[EventCreator]] = None
    tweet_count: Optional[int] = None
    chats: Optional[List[Chat]] = None
    featured_order: Optional[int] = None
    estimate_value: Optional[bool] = None
    cant_estimate: Optional[bool] = None
    estimated_value: Optional[AmmType] = None
    templates: Optional[List[Template]] = None
    spreads_main_line: Optional[int] = None
    totals_main_line: Optional[int] = None
    carousel_map: Optional[AmmType] = None
    pending_deployment: Optional[bool] = None
    deploying: Optional[bool] = None
    deploying_timestamp: Optional[datetime] = None
    scheduled_deployment_timestamp: Optional[datetime] = None
    game_status: Optional[AmmType] = None


class MarketDetail(BaseModel):
    id: Optional[AmmType] = None
    question: Optional[AmmType] = None
    condition_id: Optional[AmmType] = None
    slug: Optional[AmmType] = None
    twitter_card_image: Optional[AmmType] = None
    resolution_source: Optional[AmmType] = None
    end_date: Optional[datetime] = None
    category: Optional[AmmType] = None
    amm_type: Optional[AmmType] = None
    liquidity: Optional[AmmType] = None
    sponsor_name: Optional[AmmType] = None
    sponsor_image: Optional[AmmType] = None
    start_date: Optional[datetime] = None
    x_axis_value: Optional[AmmType] = None
    y_axis_value: Optional[AmmType] = None
    denomination_token: Optional[AmmType] = None
    fee: Optional[AmmType] = None
    image: Optional[AmmType] = None
    icon: Optional[AmmType] = None
    lower_bound: Optional[AmmType] = None
    upper_bound: Optional[AmmType] = None
    description: Optional[AmmType] = None
    outcomes: Optional[AmmType] = None
    outcome_prices: Optional[AmmType] = None
    volume: Optional[AmmType] = None
    active: Optional[bool] = None
    market_type: Optional[AmmType] = None
    format_type: Optional[AmmType] = None
    lower_bound_date: Optional[AmmType] = None
    upper_bound_date: Optional[AmmType] = None
    closed: Optional[bool] = None
    market_maker_address: Optional[AmmType] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_time: Optional[AmmType] = None
    wide_format: Optional[bool] = None
    new: Optional[bool] = None
    mailchimp_tag: Optional[AmmType] = None
    featured: Optional[bool] = None
    archived: Optional[bool] = None
    resolved_by: Optional[AmmType] = None
    restricted: Optional[bool] = None
    market_group: Optional[int] = None
    group_item_title: Optional[AmmType] = None
    group_item_threshold: Optional[AmmType] = None
    question_id: Optional[AmmType] = None
    uma_end_date: Optional[AmmType] = None
    enable_order_book: Optional[bool] = None
    order_price_min_tick_size: Optional[int] = None
    order_min_size: Optional[int] = None
    uma_resolution_status: Optional[AmmType] = None
    curation_order: Optional[int] = None
    volume_num: Optional[int] = None
    liquidity_num: Optional[int] = None
    end_date_iso: Optional[AmmType] = None
    start_date_iso: Optional[AmmType] = None
    uma_end_date_iso: Optional[AmmType] = None
    has_reviewed_dates: Optional[bool] = None
    ready_for_cron: Optional[bool] = None
    comments_enabled: Optional[bool] = None
    volume24_hr: Optional[int] = None
    volume1_wk: Optional[int] = None
    volume1_mo: Optional[int] = None
    volume1_yr: Optional[int] = None
    game_start_time: Optional[AmmType] = None
    seconds_delay: Optional[int] = None
    clob_token_ids: Optional[AmmType] = None
    disqus_thread: Optional[AmmType] = None
    short_outcomes: Optional[AmmType] = None
    team_aid: Optional[AmmType] = None
    team_bid: Optional[AmmType] = None
    uma_bond: Optional[AmmType] = None
    uma_reward: Optional[AmmType] = None
    fpmm_live: Optional[bool] = None
    volume24_hr_amm: Optional[int] = None
    volume1_wk_amm: Optional[int] = None
    volume1_mo_amm: Optional[int] = None
    volume1_yr_amm: Optional[int] = None
    volume24_hr_clob: Optional[int] = None
    volume1_wk_clob: Optional[int] = None
    volume1_mo_clob: Optional[int] = None
    volume1_yr_clob: Optional[int] = None
    volume_amm: Optional[int] = None
    volume_clob: Optional[int] = None
    liquidity_amm: Optional[int] = None
    liquidity_clob: Optional[int] = None
    maker_base_fee: Optional[int] = None
    taker_base_fee: Optional[int] = None
    custom_liveness: Optional[int] = None
    accepting_orders: Optional[bool] = None
    notifications_enabled: Optional[bool] = None
    score: Optional[int] = None
    image_optimized: Optional[Optimized] = None
    icon_optimized: Optional[Optimized] = None
    events: Optional[List[Event]] = None
    categories: Optional[List[Category]] = None
    tags: Optional[List[Tag]] = None
    creator: Optional[AmmType] = None
    ready: Optional[bool] = None
    funded: Optional[bool] = None
    past_slugs: Optional[AmmType] = None
    ready_timestamp: Optional[datetime] = None
    funded_timestamp: Optional[datetime] = None
    accepting_orders_timestamp: Optional[datetime] = None
    competitive: Optional[int] = None
    rewards_min_size: Optional[int] = None
    rewards_max_spread: Optional[int] = None
    spread: Optional[int] = None
    automatically_resolved: Optional[bool] = None
    one_day_price_change: Optional[int] = None
    one_hour_price_change: Optional[int] = None
    one_week_price_change: Optional[int] = None
    one_month_price_change: Optional[int] = None
    one_year_price_change: Optional[int] = None
    last_trade_price: Optional[int] = None
    best_bid: Optional[int] = None
    best_ask: Optional[int] = None
    automatically_active: Optional[bool] = None
    clear_book_on_start: Optional[bool] = None
    chart_color: Optional[AmmType] = None
    series_color: Optional[AmmType] = None
    show_gmp_series: Optional[bool] = None
    show_gmp_outcome: Optional[bool] = None
    manual_activation: Optional[bool] = None
    neg_risk_other: Optional[bool] = None
    game_id: Optional[AmmType] = None
    group_item_range: Optional[AmmType] = None
    sports_market_type: Optional[AmmType] = None
    line: Optional[int] = None
    uma_resolution_statuses: Optional[AmmType] = None
    pending_deployment: Optional[bool] = None
    deploying: Optional[bool] = None
    deploying_timestamp: Optional[datetime] = None
    scheduled_deployment_timestamp: Optional[datetime] = None
    rfq_enabled: Optional[bool] = None
    event_start_time: Optional[datetime] = None
