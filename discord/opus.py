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

from disnake.opus import (
    APPLICATION_AUDIO,
    APPLICATION_LOWDELAY,
    APPLICATION_VOIP,
    BAD_ARG,
    CTL_LAST_PACKET_DURATION,
    CTL_SET_BANDWIDTH,
    CTL_SET_BITRATE,
    CTL_SET_FEC,
    CTL_SET_GAIN,
    CTL_SET_PLP,
    CTL_SET_SIGNAL,
    OK,
    BandCtl,
    Decoder,
    DecoderStruct,
    DecoderStructPtr,
    DiscordException,
    Encoder,
    EncoderStruct,
    EncoderStructPtr,
    InvalidArgument,
    OpusError,
    OpusNotLoaded,
    SignalCtl,
    __dict__ as __original_dict__,
    _err_lt,
    _err_ne,
    _lib,
    _load_default,
    _OpusStruct,
    band_ctl,
    c_float_ptr,
    c_int16_ptr,
    c_int_ptr,
    exported_functions,
    is_loaded,
    libopus_loader,
    load_opus,
    signal_ctl,
)

__all__ = ("Encoder", "OpusError", "OpusNotLoaded")

locals().update(__original_dict__)

del __original_dict__
