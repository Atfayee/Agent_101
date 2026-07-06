class ToolInputError(ValueError):
    pass


class ToolTemporaryError(RuntimeError):
    pass


class ToolFataError(RuntimeError):
    pass


def format_tool_error(error: Exception) -> str:

    if isinstance(error, ToolInputError):
        return (
            "TOOL_INPUT_ERROR: Invalid tool arguments."
            f"Reason: {str(error)}. Correct the arguments and try again."
        )
    
    if isinstance(error, ToolTemporaryError):
        return (
            "TOOL_TEMPORARY_ERROR: Temporary provider failure."
            f"Reason: {str(error)}. Retry later may help"
        )
    
    if isinstance(error, ToolFataError):
        return (
            "TOOL_FATA_ERROR: Tool cannot continue because of system configuration issue."
            "Do not retry this exact call."
        )
    
    return (
        "TOOL_UNKNOWN_ERROR: Tool failed unexpectedly. Do not invent results."
    )