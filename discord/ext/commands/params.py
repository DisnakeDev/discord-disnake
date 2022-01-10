"""
Repsonsible for handling Params for slash commands
"""

from disnake.ext.commands.params import (
    CONVERTER_MAPPING,
    CallableT,
    ChannelType,
    CommandInteraction,
    ConverterMethod,
    Injection,
    Option,
    OptionChoice,
    OptionType,
    Param,
    ParamInfo,
    T,
    TChoice,
    TypeT,
    __dict__ as __original_dict__,
    _channel_type_factory,
    _xt_to_xe,
    call_param_func,
    collect_nested_params,
    collect_params,
    commands,
    converter_method,
    errors,
    expand_params,
    format_kwargs,
    inject,
    isolate_self,
    issubclass_,
    maybe_coroutine,
    option_enum,
    param,
    register_injection,
    remove_optionals,
    run_injections,
    safe_call,
    signature,
    try_enum_to_int,
)

__all__ = (
    "ParamInfo", "Param", "param", "inject", "option_enum", "register_injection", "converter_method"
)

locals().update(__original_dict__)

del __original_dict__
