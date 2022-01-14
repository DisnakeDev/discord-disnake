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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from disnake.utils import (
        _IS_ASCII,
        _MARKDOWN_ESCAPE_COMMON,
        _MARKDOWN_ESCAPE_REGEX,
        _MARKDOWN_ESCAPE_SUBREGEX,
        _MARKDOWN_STOCK_REGEX,
        _URL_REGEX,
        DISCORD_EPOCH,
        HAS_ORJSON,
        MISSING,
        PY_310,
        CachedSlotProperty,
        InvalidArgument,
        SequenceProxy,
        SnowflakeList,
        T,
        T_co,
        _achunk,
        _bytes_to_base64_data,
        _cached_property,
        _chunk,
        _count_left_spaces,
        _get_and_cast,
        _get_as_snowflake,
        _get_description,
        _get_header_line,
        _get_mime_type_for_image,
        _get_next_header_line,
        _get_option_desc,
        _MissingSentinel,
        _parse_ratelimit_header,
        _string_width,
        _to_json,
        _unique,
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

__all__ = (
    "oauth_url",
    "parse_token",
    "snowflake_time",
    "time_snowflake",
    "find",
    "get",
    "sleep_until",
    "utcnow",
    "remove_markdown",
    "escape_markdown",
    "escape_mentions",
    "as_chunks",
    "format_dt",
)

# isort: split
from disnake.utils import __dict__ as __original_dict__

locals().update(__original_dict__)
