class ToolInputError(ValueError):
    """
    用户或 LLM 输入错误参数。
    这类错误通常 LLM 可以自我修复。
    """
    pass

class ToolTemporaryError(RuntimeError):
    """
    系统暂时性错误。
    例如 timeout、rate limit。
    LLM 可以稍后retry 或 使用 backoff
    """
    pass

class ToolFataError(RuntimeError):
    """
    系统不可恢复错误。
    例如 API key 缺失、权限错误等系统配置问题。
    """
    pass

def format_tool_error(error: Exception) -> str:
    """
    将 Python error 转化为 LLM 可以理解的 tool error message。
    注意：
    不要暴露敏感信息，例如 API key、数据库连接串、文件路径等。    
    """
    
    if isinstance(error, ToolInputError):
        return (
            "TOOL_INPUT_ERROR: Invalid arguments. "
            f"Reason: {str(error)}"
            "Please correct the invalid arguments and call the tool again."
        )
    
    if isinstance(error, ToolTemporaryError):
        return (
            "TOOL_TEMPORARY_ERROR: The tool failed because of a temproray system issue.",
            f"Reason: {str(error)}"
            "LLM may retry later or use an alternative."
        )
    
    if isinstance(error, ToolFataError):
        return (
            "TOOL_FATA_ERROR: The tool failed because of a system configuration error."
            f"Reason: {str(error)}"
            "Do not retry. Explain the error to user."
        )
    
    return (
        "TOOL_UNKNOWN_ERROR: The tool failed unexpectedly."
        "Do not invent results. Explain the error to user."
    )