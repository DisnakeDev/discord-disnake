"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Disnake Development

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
__all__ = (
    "as_chunks",
    "escape_markdown",
    "escape_mentions",
    "find",
    "format_dt",
    "get",
    "oauth_url",
    "parse_token",
    "remove_markdown",
    "sleep_until",
    "snowflake_time",
    "time_snowflake",
    "utcnow",
)

from disnake.utils import (
    MISSING,
    CachedSlotProperty,
    SequenceProxy,
    SnowflakeList,
    T,
    T_co,
    as_chunks,
    async_all,
    cached_property,
    cached_slot_property,
    classproperty,
    compute_timedelta,
    copy_doc,
    deprecated,
    escape_markdown,
    escape_mentions,
    evaluate_annotation,
    find,
    flatten_literal_params,
    format_dt,
    get,
    get_slots,
    maybe_coroutine,
    normalise_optional_params,
    oauth_url,
    parse_docstring,
    parse_time,
    parse_token,
    remove_markdown,
    resolve_annotation,
    resolve_invite,
    resolve_template,
    sane_wait_for,
    sleep_until,
    snowflake_time,
    time_snowflake,
    utcnow,
    valid_icon_size,
    warn_deprecated,
)
